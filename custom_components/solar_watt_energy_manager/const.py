"""Constants for the SolarWattEnergyManager integration."""

from homeassistant.components.sensor import STATE_CLASS_TOTAL_INCREASING
from homeassistant.const import (
    FREQUENCY_HERTZ,
    PERCENTAGE,
    POWER_WATT,
    TEMP_CELSIUS,
    CURRENCY_EURO,
    ENERGY_KILO_WATT_HOUR,
    DEVICE_CLASS_MONETARY,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_TEMPERATURE,
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
        DEVICE_CLASS_BATTERY,
        None,
    ],
    "energymanager.pv.power_produced": [
        "pv power",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.sens.power_consumed": [
        "power consumed sum",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.sens.power_consumed_grid": [
        "power consumed grid",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.sens.power_consumed_storage": [
        "power consumed storage",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.sens.power_consumed_producer": [
        "power consumed pv",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None
    ],
    "energymanager.sens.power_to_grid": [
        "power to grid",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None
    ],
    "energymanager.myreserve.power_out": [
        "power storage out",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.myreserve.power_in": [
        "power storage in",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.myreserve.power_self": [
        "myReserve power self supplied",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None
    ],
    "energymanager.sens.power_self_consumed": [
        "power self consumed",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.myreserve.power_in_grid": [
        "power buffered grid",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
        None,
    ],
    "energymanager.myreserve.power_in_producers": [
        "power buffered pv",
        POWER_WATT,
        "mdi:flash",
        DEVICE_CLASS_POWER,
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
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
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
        DEVICE_CLASS_MONETARY,
        None,
    ],
    "energymanager.price.price_work_in": [
        "cost kWh from grid",
        "EUR /kWh",
        None,
        DEVICE_CLASS_MONETARY,
        None,
    ],
    "energymanager.work.self_consumed": [
        "energy self consumed",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.self_supplied": [
        "energy self supplied",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.consumed": [
        "energy consumed",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.in": [
        "energy net in",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.consumed_from_grid": [
        "energy consumed grid",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.buffered_from_grid": [
        "energy grid into storage",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.buffered_from_producers": [
        "energy from pv into storage",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.consumed_from_storage": [
        "energy consumed storage",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.out_from_storage": [
        "energy to grid from storage",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.produced": [
        "energy produced",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.buffered": [
        "energy bufferd",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.released": [
        "energy released",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.out_from_producers": [
        "energy to grid from pv",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.consumed_from_producers": [
        "energy consumed pv",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],
    "energymanager.work.out": [
        "energy net out",
        ENERGY_KILO_WATT_HOUR,
        "mdi:chart-histogram",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
    ],

}

SENSOR_NAME = 0
SENSOR_UNIT = 1
SENSOR_ICON = 2
SENSOR_DEVICE_CLASS = 3
SENSOR_STATE_CLASS = 4
