"""Support for SolarWatt EnergyManager API."""

import logging

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_NAME, CONF_RESOURCES
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    COORDINATOR,
    DEFAULT_NAME,
    DOMAIN,
    ENERGY_MANAGER_DATA,
    ENERGY_MANAGER_NAME,
    ENERGY_MANAGER_UNIQUE_ID,
    SENSOR_DEVICE_CLASS,
    SENSOR_STATE_CLASS,
    SENSOR_ICON,
    SENSOR_NAME,
    SENSOR_TYPES,
    SENSOR_UNIT,
)

_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_HOST): cv.string,
        vol.Optional(CONF_ALIAS): cv.string,
        vol.Required(CONF_RESOURCES): vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)]),
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Import the platform into a config entry."""

    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": SOURCE_IMPORT}, data=config
        )
    )


async def async_setup_entry(hass, entry, async_add_entities):
    """Add the solar watt energy manager sensors."""
    # Add the needed sensors to hass
    energy_manager_data = hass.data[DOMAIN][entry.entry_id]
    name = energy_manager_data[ENERGY_MANAGER_NAME]
    unique_id = energy_manager_data[ENERGY_MANAGER_UNIQUE_ID]
    coordinator = energy_manager_data[COORDINATOR]
    data = energy_manager_data[ENERGY_MANAGER_DATA]
    status = data.status

    _LOGGER.debug("adding sensors")

    entities = []

    for sensor_type in status:
        entities.append(
            EnergyManagerSensor(
                coordinator,
                data,
                name,
                sensor_type,
                unique_id,
            )
        )

    async_add_entities(entities)

    _LOGGER.debug("added sensors for energy manager")


class EnergyManagerSensor(CoordinatorEntity, SensorEntity):
    """Representation of a sensor entity for energy manager status values."""

    def __init__(
        self,
        coordinator,
        data,
        name,
        sensor_type,
        unique_id,
    ):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._type = sensor_type
        self._device_name = name
        self._name = f"{SENSOR_TYPES[sensor_type][SENSOR_NAME]}"
        self._unit = SENSOR_TYPES[sensor_type][SENSOR_UNIT]
        self._data = data
        self._unique_id = unique_id

    @property
    def device_info(self):
        """Device info."""
        if not self._unique_id:
            return None
        device_info = {
            "identifiers": {(DOMAIN, self._unique_id)},
            "name": self._device_name,
        }
        return device_info

    @property
    def unique_id(self):
        """Sensor Unique id."""
        if not self._unique_id:
            return None
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return SENSOR_TYPES[self._type][SENSOR_ICON]

    @property
    def device_class(self):
        """Device class of the sensor."""
        return SENSOR_TYPES[self._type][SENSOR_DEVICE_CLASS]

    @property
    def state_class(self):
        """State class of the sensor"""
        return SENSOR_TYPES[self._type][SENSOR_STATE_CLASS]

    @property
    def native_value(self):
        """Current value of the sensor"""
        if not self._data.status:
            return None
        return self._data.status.get(self._type)

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return self._unit

    @property
    def name(self):
        """Name of the enity."""
        return self._name
