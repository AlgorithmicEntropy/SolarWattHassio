"""DataUpdateCoordinator for LocalSolarWatt."""

import asyncio
import logging

from homeassistant.components.sensor import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .client_wrapper import ClientWrapper

_LOGGER = logging.getLogger(__name__)


class UpdateCoordinator(DataUpdateCoordinator):
    """Custom DataUpdateCoordinator for LocalSolarWatt."""

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry,
        client: ClientWrapper,
        update_interval: timedelta,
        always_update: bool,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="EnergyManager",
            config_entry=config_entry,
            update_interval=update_interval,
            always_update=always_update,
        )
        self.client = client

    async def _async_update_data(self):
        """Fetch data from api."""
        async with asyncio.timeout(10):
            await self.client.update()
            if not self.client.connected:
                raise UpdateFailed("Error fetching energy manager api")
            return self.client.data
