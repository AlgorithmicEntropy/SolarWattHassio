"""Constants for the LocalSolarWatt integration."""

from local_solar_watt import DeviceClass as DC

from homeassistant.components.sensor import SensorDeviceClass
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
        SensorDeviceClass.BATTERY,
    ],
    "power_out": [
        "Power Storage Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_in": [
        "Power Storage In",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "work_out": [
        "Work Storage Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_in": [
        "Work Storage In",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
}

# this will be also part of the storage entity, but it is a different device in the API so keep it separate
BATTERY_METER_TYPES = {
    "ac_power": [
        "AC Power",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "backup_state_of_charge": [
        "Backup State of Charge",
        PERCENTAGE,
        "mdi:battery",
        SensorDeviceClass.BATTERY,
    ],
    "battery_error": [
        "Battery Error",
        None,
        "mdi:alert-circle",
        None,
    ],
    "count_battery_modules": [
        "Count of Battery Modules",
        None,
        "mdi:counter",
        None,
    ],
    "current_battery_in": [
        "Current Battery In",
        UnitOfElectricCurrent.AMPERE,
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
    ],
    "current_battery_out": [
        "Current Battery Out",
        UnitOfElectricCurrent.AMPERE,
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
    ],
    "factor_forecast": [
        "Factor Forecast",
        None,
        "mdi:chart-line",
        None,
    ],
    "mode_converter": [
        "Mode Converter",
        None,
        "mdi:swap-horizontal",
        None,
    ],
    "power_ac_in": [
        "Power AC In",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_ac_out": [
        "Power AC Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_request_wanted": [
        "Power Request Wanted",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_yield_sum": [
        "Power Yield Sum",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "state_of_charge": [
        "State of Charge",
        PERCENTAGE,
        "mdi:battery-charging-100",
        SensorDeviceClass.BATTERY,
    ],
    "state_of_health": [
        "State of Health",
        PERCENTAGE,
        "mdi:heart",
        None,
    ],
    "system_error": [
        "System Error",
        None,
        "mdi:alert",
        None,
    ],
    "system_status": [
        "System Status",
        None,
        "mdi:information",
        None,
    ],
    "temp_packs": [
        "Temperature Packs",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
    ],
    "temp_base": [
        "Temperature Base",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
    ],
    "temp_battery": [
        "Temperature Battery",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
    ],
    "temp_grm": [
        "Temperature GRM",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
    ],
    "work_ac_in": [
        "Work AC In",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_ac_out": [
        "Work AC Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_capacity": [
        "Work Capacity",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_charge": [
        "Work Charge",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-positive",
        SensorDeviceClass.ENERGY,
    ],
    "work_charged": [
        "Work Charged",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-positive",
        SensorDeviceClass.ENERGY,
    ],
    "work_discharged": [
        "Work Discharged",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-negative",
        SensorDeviceClass.ENERGY,
    ],
}

INVERTER_TYPES = {
    "device_state": [
        "Device State",
        None,
        "mdi:information-variant",
        None,
    ],
    "state_error_list": [
        "State Error List",
        None,
        "mdi:alert-box",
        None,
    ],
    "ac_power": [
        "AC Power",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_ac_out": [
        "Power AC Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_string_dc_in": [
        "Power String DC In",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
    ],
    "power_yield_sum": [
        "Power Yield Sum",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "work_ac_out": [
        "Work AC Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
}

LOCATION_TYPES = {
    "device_state": [
        "Device State",
        None,
        "mdi:information-variant",
        None,
    ],
    "power_buffered": [
        "Power Buffered",
        UnitOfPower.WATT,
        "mdi:battery-arrow-up",
        SensorDeviceClass.POWER,
    ],
    "power_buffered_from_grid": [
        "Power Buffered From Grid",
        UnitOfPower.WATT,
        "mdi:transmission-tower",
        SensorDeviceClass.POWER,
    ],
    "power_buffered_from_producers": [
        "Power Buffered From Producers",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
    ],
    "power_consumed": [
        "Power Consumed",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_consumed_from_grid": [
        "Power Consumed From Grid",
        UnitOfPower.WATT,
        "mdi:transmission-tower",
        SensorDeviceClass.POWER,
    ],
    "power_consumed_from_producers": [
        "Power Consumed From Producers",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
    ],
    "power_consumed_from_storage": [
        "Power Consumed From Storage",
        UnitOfPower.WATT,
        "mdi:battery",
        SensorDeviceClass.POWER,
    ],
    "power_in": [
        "Power In",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_out": [
        "Power Out",
        UnitOfPower.WATT,
        "mdi:flash",
        SensorDeviceClass.POWER,
    ],
    "power_out_from_producers": [
        "Power Out From Producers",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
    ],
    "power_out_from_storage": [
        "Power Out From Storage",
        UnitOfPower.WATT,
        "mdi:battery",
        SensorDeviceClass.POWER,
    ],
    "power_produced": [
        "Power Produced",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
    ],
    "power_released": [
        "Power Released",
        UnitOfPower.WATT,
        "mdi:battery-arrow-down",
        SensorDeviceClass.POWER,
    ],
    "power_self_supplied": [
        "Power Self Supplied",
        UnitOfPower.WATT,
        "mdi:home-import-outline",
        SensorDeviceClass.POWER,
    ],
    "power_self_consumed": [
        "Power Self Consumed",
        UnitOfPower.WATT,
        "mdi:home",
        SensorDeviceClass.POWER,
    ],
    "work_buffered": [
        "Work Buffered",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery-arrow-up",
        SensorDeviceClass.ENERGY,
    ],
    "work_buffered_from_grid": [
        "Work Buffered From Grid",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:transmission-tower",
        SensorDeviceClass.ENERGY,
    ],
    "work_buffered_from_producers": [
        "Work Buffered From Producers",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
    ],
    "work_consumed": [
        "Work Consumed",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_consumed_from_grid": [
        "Work Consumed From Grid",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:transmission-tower",
        SensorDeviceClass.ENERGY,
    ],
    "work_consumed_from_producers": [
        "Work Consumed From Producers",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
    ],
    "work_consumed_from_storage": [
        "Work Consumed From Storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery",
        SensorDeviceClass.ENERGY,
    ],
    "work_in": [
        "Work In",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_out": [
        "Work Out",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
    ],
    "work_out_from_producers": [
        "Work Out From Producers",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
    ],
    "work_out_from_storage": [
        "Work Out From Storage",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:battery",
        SensorDeviceClass.ENERGY,
    ],
    "work_produced": [
        "Work Produced",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:solar-power",
        SensorDeviceClass.ENERGY,
    ],
    "work_released": [
        "Work Released",
        UnitOfEnergy.KILO_WATT_HOUR,
        None,
        SensorDeviceClass.ENERGY,
    ],
    "work_self_supplied": [
        "Work Self Supplied",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:home-import-outline",
        SensorDeviceClass.ENERGY,
    ],
    "work_self_consumed": [
        "Work Self Consumed",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:home",
        SensorDeviceClass.ENERGY,
    ],
    "price_work_in": [
        "Price Work In",
        CURRENCY_EURO,
        "mdi:currency-eur",
        None,
    ],
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
