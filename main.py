import os

from fastapi import FastAPI
from azure.iot.hub import IoTHubRegistryManager

from src.device_pool import DevicePool
from src.device_wrangler import DeviceWrangler
from src.toaster import Toaster

app = FastAPI()
# Use this for Azure
# connection_string = os.environ['IOT_HUB_CONNECTION']
# registry_manager = IoTHubRegistryManager(connection_string)

# Use this for local in-mem
registry_manager = DevicePool()
device_wrangler = DeviceWrangler(registry_manager)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/toaster/status/{device_id}")
async def device_status(device_id: str):
    return device_wrangler.send(device_id, Toaster.STATUS)

