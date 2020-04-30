# List Selected GPU(s)
from tensorflow.python.client import device_lib
for dev in device_lib.list_local_devices():
    if dev.__getattribute__('device_type') == 'GPU':
        print(">>>>>>>>>>>>>>>",dev.__getattribute__('device_type'),dev.__getattribute__('physical_device_desc'))