"""Config flow for LocalSolarWatt integration."""

import logging

from local_solar_watt import EnergyManagerVersion
import voluptuous as vol

from homeassistant import config_entries, exceptions
from homeassistant.config_entries import ConfigFlowResult
from homeassistant.const import (
    CONF_ALIAS,
    CONF_API_VERSION,
    CONF_HOST,
    CONF_SCAN_INTERVAL,
)

from .client_wrapper import ClientWrapper
from .const import DEFAULT_NAME, DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ALIAS, default=DEFAULT_NAME): str,
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_API_VERSION): vol.In(
            [member.value for member in EnergyManagerVersion]
        ),
        vol.Required(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
    },
    extra=vol.ALLOW_EXTRA,
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for LocalSolarWatt."""

    VERSION = 2
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None) -> ConfigFlowResult:
        """Handle the initial step."""
        if user_input is not None:
            host = user_input[CONF_HOST]
            api_version = EnergyManagerVersion(user_input[CONF_API_VERSION])
            alias = user_input.get(CONF_ALIAS)
            api = ClientWrapper(host, api_version)
            await self.hass.async_add_executor_job(api.test_connection)
            if not api.connected:
                return self.async_abort(reason="cannot_connect")
            title = user_input[CONF_HOST]
            return self.async_create_entry(
                title=title,
                data={
                    CONF_HOST: host,
                    CONF_ALIAS: alias,
                    CONF_API_VERSION: user_input[CONF_API_VERSION],
                    CONF_SCAN_INTERVAL: user_input[CONF_SCAN_INTERVAL],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=CONFIG_SCHEMA,
            errors="Error fetching data, please see logs for details.",
        )


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""
