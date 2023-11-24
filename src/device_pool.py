class DevicePool:
    def __init__(self):
        self.devices = {}

    def add(self, device):
        self.devices[device.id] = device

    def invoke_device_method(self, device_id, method):
        obj = lambda: None
        obj.payload = 'somevalue'
        return obj
