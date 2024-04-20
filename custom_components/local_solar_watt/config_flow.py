"""Config flow for LocalSolarWatt integration."""

import logging

import voluptuous as vol

from homeassistant import config_entries, core, exceptions
from homeassistant.config_entries import ConfigFlowResult
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_SCAN_INTERVAL

from .const import DEFAULT_NAME, DEFAULT_SCAN_INTERVAL, DOMAIN
from .api_data import ApiData

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ALIAS, default=DEFAULT_NAME): str,
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
    },
    extra=vol.ALLOW_EXTRA,
)


async def validate_input(hass: core.HomeAssistant, data):
    """Validate the user input allows us to connect."""

    host = data[CONF_HOST]
    alias = data.get(CONF_ALIAS)

    data = ApiData(host, alias)
    await hass.async_add_executor_job(data.test_connection)
    if not data.connected:
        raise CannotConnect(data.connection_error)

    return {"available_resources": data.status}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for LocalSolarWatt."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self) -> None:
        """Initialize the config flow."""
        self.available_resources = {}
        self.energy_manager_config = {}

    async def async_step_user(self, user_input=None) -> ConfigFlowResult:
        """Handle the initial step."""
        error = None
        if user_input is not None:
            info, error = await self._async_validate_or_error(user_input)
            if error:
                return self.async_abort(reason="cannot_connect")
            self.energy_manager_config.update(user_input)
            self.available_resources.update(info["available_resources"])
            title = user_input[CONF_HOST]
            return self.async_create_entry(title=title, data=self.energy_manager_config)

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=error
        )

    async def _async_validate_or_error(self, config):
        error = None
        info = {}
        try:
            info = await validate_input(self.hass, config)
        except CannotConnect as e:
            error = e.args[0]
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            error = "Unknown error occured"
        return info, error


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""
