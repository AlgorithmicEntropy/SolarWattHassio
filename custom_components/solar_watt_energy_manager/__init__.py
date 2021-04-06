"""The SolarWattEnergyManager integration."""

import asyncio
from datetime import timedelta
import ipaddress
import logging

from SolarWattEnergyManagerAPI.SolarWatt import EnergyManagerAPI
import async_timeout
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_SCAN_INTERVAL, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    COORDINATOR,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_NAME,
    DOMAIN,
    ENERGY_MANAGER_DATA,
    ENERGY_MANAGER_NAME,
    ENERGY_MANAGER_UNIQUE_ID,
    PLATFORMS,
    UNDO_UPDATE_LISTENER,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict):
    """Setup the solar watt energy manager component."""
    hass.data.setdefault(DOMAIN, {})

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up SolarWattEnergyManager from a config entry."""
    # TODO Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    config = entry.data
    host = config[CONF_HOST]

    alias = config.get(CONF_ALIAS)
    scan_interval = config.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    data = EnergyManagerData(host, alias)

    async def async_update_data():
        """Fetch data from api"""
        async with async_timeout.timeout(10):
            await hass.async_add_executor_job(data.update)
            if not data.status:
                raise UpdateFailed("Error fetching energy manager api")

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="solarWattEnergyManager",
        update_method=async_update_data,
        update_interval=timedelta(seconds=scan_interval),
    )

    # Fetch initial data so we have data when entities subscribe
    await coordinator.async_refresh()
    status = data.status

    if not status:
        _LOGGER.error("EnergyManager Sensor has no data, unable to set up")
        raise ConfigEntryNotReady

    _LOGGER.debug("EnergyManager Sensors Available: %s", status)

    undo_listener = entry.add_update_listener(_async_update_listener)

    unique_id = _unique_id_from_status(status)

    if unique_id is None:
        unique_id = entry.entry_id

    hass.data[DOMAIN][entry.entry_id] = {
        COORDINATOR: coordinator,
        ENERGY_MANAGER_DATA: data,
        ENERGY_MANAGER_NAME: data.name,
        ENERGY_MANAGER_UNIQUE_ID: unique_id,
        UNDO_UPDATE_LISTENER: undo_listener,
    }

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)


def _unique_id_from_status(status):
    """Find the best unique id value from the status."""
    serial = status.get("Serial")
    if not serial:
        return None
    return serial


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )

    hass.data[DOMAIN][entry.entry_id][UNDO_UPDATE_LISTENER]()

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class EnergyManagerData:
    """Stores retrieved data"""

    def __init__(self, host, alias):
        self.host = host
        self._alias = alias
        api = EnergyManagerAPI()
        # api.set_logger(_LOGGER.cl)
        api.set_host(host)
        self._api = api
        self._status = None
        self._connection_status = False

    @property
    def status(self):
        """Get latest update if throttle allows. Return status."""
        return self._status

    @property
    def name(self):
        """Return the name of the device"""
        return self._alias

    @property
    def connected(self):
        """Last known state of the connection"""
        return self._connection_status

    def test_connection(self):
        "Test connection to the energy manager api"
        self._connection_status = self._api.test_connection()
        if self._connection_status:
            self.update()

    def _get_status(self):
        """Get the status from the energy manager api"""
        return self._api.pull_data()

    def update(self, **kwargs):
        """Fetch the latest status"""
        self._status = self._get_status()
