class DevicePool:
    def __init__(self):
        self.devices = {}

    def add(self, device):
        self.devices[device.id] = device
