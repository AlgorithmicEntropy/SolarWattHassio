"""Config flow for SolarWattEnergyManager integration."""
import ipaddress
import logging

import voluptuous as vol

from homeassistant import config_entries, core, exceptions
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_SCAN_INTERVAL
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from . import EnergyManagerData
from .const import (
    CONNECTION_STATUS,
    DEFAULT_NAME,
    DEFAULT_SCAN_INTERVAL,
)
from .const import DOMAIN  # pylint:disable=unused-import

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_ALIAS, default=DEFAULT_NAME): str,
        vol.Required(CONF_HOST): str,
        vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
    },
    extra=vol.ALLOW_EXTRA,
)


async def validate_input(hass: core.HomeAssistant, data):
    """Validate the user input allows us to connect."""

    host = data[CONF_HOST]
    alias = data.get(CONF_ALIAS)

    data = EnergyManagerData(host, alias)
    await hass.async_add_executor_job(data.test_connection)
    if not data.connected:
        raise CannotConnect

    return {"available_resources": data.status}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SolarWattEnergyManager."""

    VERSION = 1
    # TODO pick one of the available connection classes in homeassistant/config_entries.py
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self) -> None:
        """Initialize the config flow."""
        self.available_resources = {}
        self.energy_manager_config = {}

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            info, errors = await self._async_validate_or_error(user_input)

            if not errors:
                self.energy_manager_config.update(user_input)
                self.available_resources.update(info["available_resources"])
                title = user_input[CONF_HOST]
                return self.async_create_entry(
                    title=title, data=self.energy_manager_config
                )

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )

    async def _async_validate_or_error(self, config):
        errors = {}
        info = {}
        try:
            info = await validate_input(self.hass, config)
        except CannotConnect:
            errors["base"] = "cannot_connect"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        return info, errors


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""
