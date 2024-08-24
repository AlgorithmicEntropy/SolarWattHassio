"""Constants for the LocalSolarWatt integration."""

from local_solar_watt import DeviceClass as DC

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    CURRENCY_EURO,
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
)

DOMAIN = "local_solar_watt"

PLATFORMS = ["sensor"]

COORDINATOR = "coordinator"
ENERGY_MANAGER_DATA = "data"
ENERGY_MANAGER_NAME = "name"
ENERGY_MANAGER_UNIQUE_ID = "unique_id"

DEFAULT_SCAN_INTERVAL = 60
DEFAULT_NAME = "SolarWatt"

CONNECTION_STATUS = "connected"

UNDO_UPDATE_LISTENER = "undo_update_listener"

BATTERY_TYPES = {
    "device_state": [
        None,  # "Storage Device State" main entity of battery device
        None,
        "mdi:battery",
        None,
        None,
    ],
    "power_out": [
        "Power Storage Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_in": [
        "Power Storage In",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "work_out": [
        "Work Storage Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_in": [
        "Work Storage In",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
}

# this will be also part of the storage entity, but it is a different device in the API so keep it separate
BATTERY_METER_TYPES = {
    "id_firmware": [
        "Firmware Version",
        None,
        "mdi:information-variant",
        None,
        None,
    ],
    "ac_power": [
        "AC Power",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "backup_state_of_charge": [
        "Backup State of Charge",
        PERCENTAGE,
        "mdi:battery",
        SensorDeviceClass.BATTERY,
        SensorStateClass.MEASUREMENT,
    ],
    "battery_error": ["Battery Error", None, "mdi:alert-circle", None, None],
    "count_battery_modules": [
        "Count of Battery Modules",
        None,
        "mdi:counter",
        None,
        None,
    ],
    "current_battery_in": [
        "Current Battery In",
        UnitOfElectricCurrent.AMPERE,
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "current_battery_out": [
        "Current Battery Out",
        UnitOfElectricCurrent.AMPERE,
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "factor_forecast": [
        "Factor Forecast",
        None,
        "mdi:chart-line",
        None,
        None,
    ],
    "mode_converter": [
        "Mode Converter",
        None,
        "mdi:swap-horizontal",
        None,
        None,
    ],
    "power_ac_in": [
        "Power AC In",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_ac_out": [
        "Power AC Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_yield_sum": [
        "Power Yield Sum",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "state_of_charge": [
        "State of Charge",
        PERCENTAGE,
        "mdi:battery-charging-100",
        SensorDeviceClass.BATTERY,
        SensorStateClass.MEASUREMENT,
    ],
    "state_of_health": [
        "State of Health",
        PERCENTAGE,
        "mdi:heart",
        None,
        SensorStateClass.MEASUREMENT,
    ],
    "system_error": [
        "System Error",
        None,
        "mdi:alert",
        None,
        None,
    ],
    "system_status": [
        "System Status",
        None,
        "mdi:information",
        None,
        None,
    ],
    "temp_packs": [
        "Temperature Packs",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ],
    "temp_base": [
        "Temperature Base",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ],
    "temp_battery": [
        "Temperature Battery",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ],
    "temp_grm": [
        "Temperature GRM",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ],
    "work_ac_in": [
        "Work AC In",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        None,
    ],
    "work_ac_out": [
        "Work AC Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        None,
    ],
    "work_capacity": [
        "Work Capacity",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        None,
    ],
    "work_charge": [
        "Work Charge",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery",
        SensorDeviceClass.ENERGY,
        None,
    ],
    "work_charged": [
        "Work Charged",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-positive",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_discharged": [
        "Work Discharged",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-negative",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
}

INVERTER_TYPES = {
    "id_firmware": [
        "Firmware Version",
        None,
        "mdi:information-variant",
        None,
        None,
    ],
    "device_state": [
        "Device State",
        None,
        "mdi:information-variant",
        None,
        None,
    ],
    "state_error_list": [
        "State Error List",
        None,
        "mdi:alert-box",
        None,
        None,
    ],
    "ac_power": [
        "AC Power",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_ac_out": [
        "Power AC Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_string_dc_in": [
        "Power String DC In",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_yield_sum": [
        "Power Yield Sum",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "work_ac_out": [
        "Work AC Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
}

LOCATION_TYPES = {
    "device_state": [
        "Device State",
        None,
        "mdi:information-variant",
        None,
        None,
    ],
    "power_buffered": [
        "Power Buffered",
        UnitOfPower.WATT,
        "mdi:battery-arrow-up",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_buffered_from_grid": [
        "Power Buffered From Grid",
        UnitOfPower.WATT,
        "mdi:transmission-tower",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_buffered_from_producers": [
        "Power Buffered From Producers",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_consumed": [
        "Power Consumed",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_consumed_from_grid": [
        "Power Consumed From Grid",
        UnitOfPower.WATT,
        "mdi:transmission-tower",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_consumed_from_producers": [
        "Power Consumed From Producers",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_consumed_from_storage": [
        "Power Consumed From Storage",
        UnitOfPower.WATT,
        "mdi:battery",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_in": [
        "Power In",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_out": [
        "Power Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_out_from_producers": [
        "Power Out From Producers",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_out_from_storage": [
        "Power Out From Storage",
        UnitOfPower.WATT,
        "mdi:battery",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_produced": [
        "Power Produced",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_released": [
        "Power Released",
        UnitOfPower.WATT,
        "mdi:battery-arrow-down",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_self_supplied": [
        "Power Self Supplied",
        UnitOfPower.WATT,
        "mdi:home-import-outline",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "power_self_consumed": [
        "Power Self Consumed",
        UnitOfPower.WATT,
        "mdi:home",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "work_buffered": [
        "Work Buffered",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-arrow-up",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_buffered_from_grid": [
        "Work Buffered From Grid",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:transmission-tower",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_buffered_from_producers": [
        "Work Buffered From Producers",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_consumed": [
        "Work Consumed",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_consumed_from_grid": [
        "Work Consumed From Grid",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:transmission-tower",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_consumed_from_producers": [
        "Work Consumed From Producers",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_consumed_from_storage": [
        "Work Consumed From Storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_in": [
        "Work In",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_out": [
        "Work Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_out_from_producers": [
        "Work Out From Producers",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_out_from_storage": [
        "Work Out From Storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_produced": [
        "Work Produced",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_released": [
        "Work Released",
        UnitOfEnergy.KILO_WATT_HOUR,
        None,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_self_supplied": [
        "Work Self Supplied",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:home-import-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "work_self_consumed": [
        "Work Self Consumed",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:home",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "price_work_in": ["Price Work In", CURRENCY_EURO, "mdi:currency-eur", None, None],
}

DEVICE_MAPPER = {
    DC.BATTERY: BATTERY_TYPES,
    DC.BATTERY_METER: BATTERY_METER_TYPES,
    DC.INVERTER: INVERTER_TYPES,
    DC.LOCATION: LOCATION_TYPES,
}

# TODO translation strings
DEVICE_NAME_MAPPER = {
    DC.BATTERY: "PV Battery",
    DC.BATTERY_METER: "PV Battery Converter",
    DC.INVERTER: "PV Inverter",
    DC.LOCATION: "PV Installation",
}

SENSOR_NAME = 0
SENSOR_UNIT = 1
SENSOR_ICON = 2
SENSOR_DEVICE_CLASS = 3
SENSOR_STATE_CLASS = 4
