"""Class to retrive data from the api."""

from local_solar_watt import Api


class ApiData:
    """Stores retrieved data."""

    def __init__(self, host, alias) -> None:
        """Initialize the data object."""
        self.host = host
        self._alias = alias
        api = Api(host)
        self._api = api
        self._status = None
        self._connection_error = None
        self._connection_status = False

    @property
    def status(self):
        """Get latest update if throttle allows. Return status."""
        return self._status

    @property
    def name(self):
        """Return the name of the device."""
        return self._alias

    @property
    def connected(self):
        """Last known state of the connection."""
        return self._connection_status

    @property
    def connection_error(self):
        """Current error of the connection."""
        return self._connection_error

    def test_connection(self):
        """Test connection to the energy manager api."""
        self._connection_status, self._connection_error = self._api.test_connection()
        if self._connection_status:
            self.update()

    def update(self, **kwargs):
        """Fetch the latest status."""
        self._status = self._api.pull_data()
