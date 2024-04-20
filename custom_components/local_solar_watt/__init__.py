"""The LocalSolarWatt integration."""

import asyncio
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api_data import ApiData
from .const import (
    COORDINATOR,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    ENERGY_MANAGER_DATA,
    ENERGY_MANAGER_NAME,
    ENERGY_MANAGER_UNIQUE_ID,
    PLATFORMS,
    UNDO_UPDATE_LISTENER,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up LocalSolarWatt from a config entry."""
    config = entry.data
    host = config[CONF_HOST]

    alias = config.get(CONF_ALIAS)
    scan_interval = config.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    data = ApiData(host, alias)

    async def async_update_data():
        """Fetch data from api."""
        async with asyncio.timeout(10):
            await hass.async_add_executor_job(data.update)
            if not data.status:
                raise UpdateFailed("Error fetching energy manager api")

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="LocalSolarWatt",
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

    hass.data.setdefault(DOMAIN, {})
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


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
