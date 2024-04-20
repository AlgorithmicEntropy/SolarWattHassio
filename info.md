# Local SolarWatt Integration for HA
Home Assistant custom component for SolarWatt PV systems.

#### Description
This integration will read data from your solarwatt energy manager device via the local kiwi-grid api.  
It provides data from all devices connected to the energy manager, namely inverter, battery, grid-meter data.  
Lifetime statistics are also provided, like total energy produced, self-consumed, fed into the grid, etc. (also conveniently provided by the energy manager).

#### Installation

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

The easiest way to install it is through [HACS (Home Assistant Community Store)](https://hacs.xyz/), add this repository as a custom one in the HACS settings and download the integration.

If you want to install it manually,  
Download the `custom_components/solar_watt_energy_manager` folder and place into your `HOMEASSISTANT_CONFIG_DIR/custom_components` directory.

Once downloaded restart your Home Assistant installation.
After the restart you should be able to add it from the integrations screen.

#### Configuration

The integration provides a config flow, in which you need to enter the IP address (host) of your energy manager device.  
No further changes are required.

But you can optionally change its name and the update (pull) delay.  
I advise to not change the update time below one minute, otherwise it could overload the device  
(Further testing required)

#### Supported devices
The reference system, which I use for testing this integration uses an AC Battery and Fronius inverter.
Your setup might differ, and the energy manager API also has multiple versions with different data formats.
If you want to help me to integrate support for your setup see the "Supported devices" section of the underlying [python library.](https://github.com/AlgorithmicEntropy/SolarWattEnergyManagerAPI)
