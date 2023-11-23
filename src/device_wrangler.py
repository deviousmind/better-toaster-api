class DeviceWrangler:

    def __init__(self, pool):
        self.pool = pool

    def send(self, device_id, **kwargs):
        pass

    def get_status(self, device_id):
        device = self.pool.devices[device_id]
        return device.status
