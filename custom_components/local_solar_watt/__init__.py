"""The LocalSolarWatt integration."""

from datetime import timedelta
import logging

from local_solar_watt import EnergyManagerVersion

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_ALIAS,
    CONF_API_VERSION,
    CONF_HOST,
    CONF_SCAN_INTERVAL,
)
from homeassistant.core import HomeAssistant

from .client_wrapper import ClientWrapper
from .const import (
    COORDINATOR,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    ENERGY_MANAGER_NAME,
    ENERGY_MANAGER_UNIQUE_ID,
    PLATFORMS,
    UNDO_UPDATE_LISTENER,
)
from .coordinator import UpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up LocalSolarWatt from a config entry."""
    # Add the needed sensors to hass
    host = entry.data[CONF_HOST]
    api_version = EnergyManagerVersion(entry.data[CONF_API_VERSION])
    update_interval = entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    client = ClientWrapper(host, api_version)
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
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    )
    return True


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Migrate config entry."""
    _LOGGER.debug(
        "Migrating configuration from version %s.%s",
        config_entry.version,
        config_entry.minor_version,
    )

    if config_entry.version > 1:
        # This means the user has downgraded from a future version
        return False

    if config_entry.version == 1:
        new_data = {**config_entry.data}
        new_data[CONF_API_VERSION] = EnergyManagerVersion.CLASSIC.value

        hass.config_entries.async_update_entry(
            config_entry, data=new_data, minor_version=3, version=1
        )

    _LOGGER.debug(
        "Migration to configuration version %s.%s successful",
        config_entry.version,
        config_entry.minor_version,
    )

    return True
