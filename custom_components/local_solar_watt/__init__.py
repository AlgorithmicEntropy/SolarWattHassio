"""The LocalSolarWatt integration."""

import asyncio
import logging
from datetime import timedelta
from .coordinator import UpdateCoordinator
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant
from .client_wrapper import ClientWrapper
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
    # Add the needed sensors to hass
    host = entry.data[CONF_HOST]
    update_interval = entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    client = ClientWrapper(host)
    coordinator = UpdateCoordinator(
        hass,
        config_entry=entry,
        client=client,
        update_interval=timedelta(seconds=update_interval),
        always_update=True,
    )
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        CONF_HOST: host,
        CONF_ALIAS: entry.data[CONF_ALIAS],
        COORDINATOR: coordinator,
        ENERGY_MANAGER_NAME: entry.data[CONF_ALIAS],
        ENERGY_MANAGER_UNIQUE_ID: entry.unique_id,
        UNDO_UPDATE_LISTENER: None,
    }

    entry.add_update_listener(_async_update_listener)
    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )
    return True


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)


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
