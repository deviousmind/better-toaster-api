import json

from azure.iot.hub.models import CloudToDeviceMethod, CloudToDeviceMethodResult, Twin


class DeviceWrangler:

    def __init__(self, registry_manager):
        self.registry_manager = registry_manager

    def send(self, device_id, command, **kwargs):
        device_method = CloudToDeviceMethod(method_name=command, payload=json.dumps(kwargs))
        response = self.registry_manager.invoke_device_method(device_id, device_method)
        return response.payload
