"""Build sensor enteties frim api data."""

import logging

from local_solar_watt import Api
import voluptuous as vol

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_NAME, CONF_RESOURCES
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    COORDINATOR,
    DEFAULT_NAME,
    DEVICE_MAPPER,
    DEVICE_NAME_MAPPER,
    DOMAIN,
    ENERGY_MANAGER_DATA,
    SENSOR_DEVICE_CLASS,
    SENSOR_ICON,
    SENSOR_NAME,
    SENSOR_STATE_CLASS,
    SENSOR_UNIT,
)

_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_HOST): cv.string,
        vol.Optional(CONF_ALIAS): cv.string,
        vol.Required(CONF_RESOURCES): vol.All(
            cv.ensure_list, [vol.In(list(DEVICE_MAPPER.values()))]
        ),
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Import the platform into a config entry."""

    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": SOURCE_IMPORT}, data=config
        )
    )


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Add the solar watt energy manager sensors."""
    # Add the needed sensors to hass
    energy_manager_data = hass.data[DOMAIN][entry.entry_id]
    coordinator = energy_manager_data[COORDINATOR]
    data = energy_manager_data[ENERGY_MANAGER_DATA]
    status = data.status

    entities = []

    for device_class in status:
        sensor_type_class = DEVICE_MAPPER[device_class]
        entities += [
            EnergyManagerSensor(
                coordinator,
                data,
                DEVICE_NAME_MAPPER[device_class],
                sensor_type_class[id],
                device_class,
                data.host,
                id,
            )
            for id in sensor_type_class
        ]

    async_add_entities(entities)


class EnergyManagerSensor(CoordinatorEntity, SensorEntity):
    """Representation of a sensor entity for energy manager status values."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator,
        data,
        device_name,
        sensor_conf,
        sensor_class,
        host,
        sensor_id,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._type_class = sensor_class
        self._data_id = sensor_id
        self._name = sensor_conf[SENSOR_NAME]
        self._unit = sensor_conf[SENSOR_UNIT]
        self._device_class = sensor_conf[SENSOR_DEVICE_CLASS]
        self._state_class = sensor_conf[SENSOR_STATE_CLASS]
        self._icon = sensor_conf[SENSOR_ICON]
        self._data = data
        self._unique_id = f"{host}_{device_name}_{sensor_id}"
        self._device_info = DeviceInfo(
            identifiers={(DOMAIN, f"{host.replace(".", "_")}_{device_name}")},
            name=device_name,
            manufacturer="Solar Watt",  # TODO set manufacturer and device ids from API info
            configuration_url=f"http://{host}",
        )
        # set precision for numeric data
        if isinstance(self.native_value, float):
            self._attr_suggested_display_precision = 2

    @property
    def device_info(self) -> DeviceInfo | None:
        """Device info for the ups."""
        return self._device_info

    @property
    def unique_id(self) -> str | None:
        """Sensor Unique id."""
        return self._unique_id

    @property
    def icon(self) -> str | None:
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def device_class(self) -> SensorDeviceClass | None:
        """Device class of the sensor."""
        return self._device_class

    @property
    def native_value(self) -> str | None:
        """Return entity state from ups."""
        if not self._data.status:
            return None
        return self._data.status.get(self._type_class).get(self._data_id)

    @property
    def state_class(self) -> SensorStateClass | None:
        """State class of the sensor."""
        return self._state_class

    @property
    def native_unit_of_measurement(self) -> str | None:
        """Return the unit of measurement of this entity, if any."""
        return self._unit

    @property
    def name(self) -> str | None:
        """Name of the enity."""
        return self._name
