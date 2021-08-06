"""Constants for the SolarWattEnergyManager integration."""

from homeassistant.components.sensor import DEVICE_CLASS_BATTERY, DEVICE_CLASS_POWER, DEVICE_CLASS_TEMPERATURE
from homeassistant.const import (
    FREQUENCY_HERTZ,
    PERCENTAGE,
    POWER_WATT,
    VOLT,
    TEMP_CELSIUS
)

DOMAIN = "solar_watt_energy_manager"

PLATFORMS = ["sensor"]

COORDINATOR = "coordinator"
ENERGY_MANAGER_DATA = "data"
ENERGY_MANAGER_NAME = "name"
ENERGY_MANAGER_UNIQUE_ID = "unique_id"

DEFAULT_SCAN_INTERVAL = 60
DEFAULT_NAME = "EnergyManager"

CONNECTION_STATUS = "connected"

UNDO_UPDATE_LISTENER = "undo_update_listener"

SENSOR_TYPES = {
    "energymanager.myreserve.charge": [
        "MyReserve Charge",
        PERCENTAGE,
        "mdi:battery",
        DEVICE_CLASS_BATTERY,
    ],
    "energymanager.pv.power_produced": [
        "PV Power",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.sens.power_consumed": [
        "Power Consumed",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.sens.power_consumed_grid": [
        "Power Consumed From Grid",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.sens.power_consumed_storage": [
        "Power Consumed From Storage",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.sens.power_consumed_producer": [
        "Power Consumed From Producers",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.sens.power_to_grid": [
        "Power Export to Grid",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.myreserve.power_out": [
        "Power Storage Out",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.myreserve.power_in": [
        "Power Storage In",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.myreserve.power_self": [
        "MyReserve Power Self Supplied",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.sens.power_self_consumed": [
        "Power Self Consumed",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.myreserve.power_in_grid": [
        "MyReserve Power in from Grid",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.myreserve.power_in_producers": [
        "MyReserve Power in from Producers",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
    ],
    "energymanager.device.mode": [
        "EnergyManager Mode",
        None,
        "mdi:cog",
        None,
    ],
    "energymanager.myreserve.health": [
        "MyReserve Battery Health",
        PERCENTAGE,
        "mdi:battery-alert",
        None,
    ],
    "energymanager.myreserve.temperature": [
        "MyReserve Battery Temperature",
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
    ],
    "energymanager.device.load": [
        "EnergyManager CPU Load",
        PERCENTAGE,
        "mdi:cpu-32-bit",
        None,
    ],
}

SENSOR_NAME = 0
SENSOR_UNIT = 1
SENSOR_ICON = 2
SENSOR_DEVICE_CLASS = 3
