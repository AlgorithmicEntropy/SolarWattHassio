"""Build sensor enteties frim api data."""

from datetime import timedelta
import logging

import voluptuous as vol

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA as SENSOR_PLATFORM_SCHEMA,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry
from homeassistant.const import CONF_ALIAS, CONF_HOST, CONF_NAME, CONF_RESOURCES
from homeassistant.core import HomeAssistant, callback
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import (
    AddConfigEntryEntitiesCallback,
    AddEntitiesCallback,
)
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import (
    COORDINATOR,
    DEFAULT_NAME,
    DEVICE_MAPPER,
    DEVICE_NAME_MAPPER,
    DOMAIN,
    SENSOR_DEVICE_CLASS,
    SENSOR_ICON,
    SENSOR_NAME,
    SENSOR_STATE_CLASS,
    SENSOR_UNIT,
)

_LOGGER = logging.getLogger(__name__)


SENSOR_PLATFORM_SCHEMA = SENSOR_PLATFORM_SCHEMA.extend(
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
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Add the solar watt energy manager sensors."""
    config = hass.data[DOMAIN][entry.entry_id]
    host = config[CONF_HOST]
    coordinator: DataUpdateCoordinator = config[COORDINATOR]
    sensor_data = coordinator.data
    entities = []

    for device_class in sensor_data:
        class_items = DEVICE_MAPPER[device_class]
        # Get number of discovered instances of this type, e.g. 2 inverters
        num_devices = len(sensor_data[device_class])
        for i in range(num_devices):
            entities += [
                EnergyManagerSensor(
                    coordinator,
                    i,
                    DEVICE_NAME_MAPPER[device_class] + str(i),
                    class_items[sensor_id],
                    device_class,
                    host,
                    sensor_id,
                )
                for sensor_id in class_items
            ]
    async_add_entities(entities)
    coordinator.async_update_listeners()


class EnergyManagerSensor(CoordinatorEntity, SensorEntity):
    """Representation of a sensor entity for energy manager status values."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator,
        device_idx,
        device_name,
        sensor_conf,
        sensor_class,
        host,
        sensor_id,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._type_class = sensor_class
        self._sensor_id = sensor_id
        self._device_idx = device_idx
        self._attr_name = sensor_conf[SENSOR_NAME]
        self._unit_of_measurement = sensor_conf[SENSOR_UNIT]
        self._device_class = sensor_conf[SENSOR_DEVICE_CLASS]
        self._state_class = sensor_conf[SENSOR_STATE_CLASS]
        self._attr_icon = sensor_conf[SENSOR_ICON]
        self._attr_unique_id = f"{host}_{device_name}_{sensor_id}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"{host.replace('.', '_')}_{device_name}")},
            name=device_name,
            manufacturer="Solar Watt",  # TODO set manufacturer and device ids from API info
            configuration_url=f"http://{host}",
        )
        # set precision for numeric data, mybe there is a better way to do this
        if self._state_class == SensorStateClass.TOTAL_INCREASING:
            self._attr_suggested_display_precision = 2

    @property
    def native_unit_of_measurement(self) -> str | None:
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def native_value(self) -> str | None:
        """Return the state of the sensor."""
        return self._attr_native_value

    @property
    def device_class(self) -> SensorDeviceClass | None:
        """Return the device class of the sensor."""
        return self._device_class

    @property
    def state_class(self) -> SensorStateClass | None:
        """Return the state class of the sensor."""
        return self._state_class

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data
        val = data.get(self._type_class)[self._device_idx].get(self._sensor_id)
        self._attr_native_value = val
        self.async_write_ha_state()
