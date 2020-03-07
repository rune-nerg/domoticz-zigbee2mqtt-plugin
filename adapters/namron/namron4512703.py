from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.dimmer_switch import DimmerSwitch

class Namron4512703(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        selv.dim1 = DimmerSwitch(devices, 'dimmer1', 'value1')
        selv.dim2 = DimmerSwitch(devices, 'dimmer2', 'value2')
        selv.dim3 = DimmerSwitch(devices, 'dimmer3', 'value3')
        selv.dim4 = DimmerSwitch(devices, 'dimmer4', 'value4')
        self.devices.append(self.dim1)
        self.devices.append(self.dim2)
        self.devices.append(self.dim3)
        self.devices.append(self.dim4)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'key' in message.raw:
            valuekey = 'value' + str(message.raw['key'])
            if 'click' in message.raw and message.raw['click'].lower() == 'off':
                message.raw[valuekey] = 0
            elif 'brightness' in message.raw:
                message.raw[valuekey] = message.raw['brightness']
        return message
