"""Constants for the SolarWattEnergyManager integration."""

from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.const import (
    UnitOfFrequency,
    PERCENTAGE,
    UnitOfPower,
    UnitOfTemperature,
    CURRENCY_EURO,
    UnitOfEnergy,
)

DOMAIN = "solar_watt_energy_manager"

PLATFORMS = ["sensor"]

COORDINATOR = "coordinator"
ENERGY_MANAGER_DATA = "data"
ENERGY_MANAGER_NAME = "name"
ENERGY_MANAGER_UNIQUE_ID = "unique_id"

DEFAULT_SCAN_INTERVAL = 60
DEFAULT_NAME = "em"

CONNECTION_STATUS = "connected"

UNDO_UPDATE_LISTENER = "undo_update_listener"

SENSOR_TYPES = {
    "energymanager.myreserve.charge": [
        "myReserve charge",
        PERCENTAGE,
        "mdi:battery",
        SensorDeviceClass.BATTERY,
        None,
    ],
    "energymanager.pv.power_produced": [
        "pv power",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.sens.power_consumed": [
        "power consumed sum",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.sens.power_consumed_grid": [
        "power consumed grid",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.sens.power_consumed_storage": [
        "power consumed storage",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.sens.power_consumed_producer": [
        "power consumed pv",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.sens.power_to_grid": [
        "power to grid",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.myreserve.power_out": [
        "power storage out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.myreserve.power_in": [
        "power storage in",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.myreserve.power_self": [
        "myReserve power self supplied",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.sens.power_self_consumed": [
        "power self consumed",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.myreserve.power_in_grid": [
        "power buffered grid",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.myreserve.power_in_producers": [
        "power buffered pv",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        None,
    ],
    "energymanager.device.mode": [
        "energyManager mode",
        None,
        "mdi:cog",
        None,
        None,
    ],
    "energymanager.myreserve.health": [
        "myReserve battery health",
        PERCENTAGE,
        "mdi:battery-alert",
        None,
        None,
    ],
    "energymanager.myreserve.temperature": [
        "myReserve battery temperature",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        None,
    ],
    "energymanager.device.load": [
        "energyManager CPU Load",
        PERCENTAGE,
        "mdi:cpu-32-bit",
        None,
        None,
    ],
    "energymanager.price.profit_feed": [
        "profit kWh to grid",
        "EUR /kWh",
        None,
        SensorDeviceClass.MONETARY,
        None,
    ],
    "energymanager.price.price_work_in": [
        "cost kWh from grid",
        "EUR /kWh",
        None,
        SensorDeviceClass.MONETARY,
        None,
    ],
    "energymanager.work.self_consumed": [
        "energy self consumed",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.self_supplied": [
        "energy self supplied",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.consumed": [
        "energy consumed",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.in": [
        "energy net in",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.consumed_from_grid": [
        "energy consumed from grid",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.buffered_from_grid": [
        "energy from grid into storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.buffered_from_producers": [
        "energy from pv into storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.consumed_from_storage": [
        "energy consumed from storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.out_from_storage": [
        "energy to grid from storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.produced": [
        "energy produced pv",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.buffered": [
        "energy bufferd",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.released": [
        "energy released",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.out_from_producers": [
        "energy to grid from pv",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.consumed_from_producers": [
        "energy consumed from pv",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energymanager.work.out": [
        "energy net out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:chart-histogram",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
}

SENSOR_NAME = 0
SENSOR_UNIT = 1
SENSOR_ICON = 2
SENSOR_DEVICE_CLASS = 3
SENSOR_STATE_CLASS = 4
