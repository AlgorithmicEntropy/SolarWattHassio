"""Class to retrive data from the api."""

import asyncio

from local_solar_watt import EnergyManagerApi, EnergyManagerVersion


class ClientWrapper:
    """Stores retrieved data."""

    def __init__(self, host, api_version: EnergyManagerVersion) -> None:
        """Initialize the data object."""
        self.host = host
        api = EnergyManagerApi(api_version, host)
        self._api = api
        self._data = None
        self._connection_status = False

    @property
    def data(self):
        """Get latest update if throttle allows. Return status."""
        return self._data

    @property
    def connected(self):
        """Last known state of the connection."""
        return self._connection_status

    def test_connection(self):
        """Test connection to the energy manager api."""
        status = self._api.test_connection()
        self._connection_status = status

    async def update(self, **kwargs):
        """Fetch the latest status."""
        loop = asyncio.get_running_loop()
        parsed = await loop.run_in_executor(None, self._api.fetch_data)
        self._connection_status = parsed is not None
        self._data = parsed
        self._connection_status = parsed is not None
        self._data = parsed
