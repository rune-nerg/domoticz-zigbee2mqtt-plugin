from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.dimmer_switch import DimmerSwitch

class Namron4512702(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        selv.dim1 = DimmerSwitch(devices, 'dimmer', 'value')
        self.devices.append(self.dim1)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'key' in message.raw:
            valuekey = 'value' + str(message.raw['key'])
            if 'click' in message.raw and message.raw['click'].lower() == 'off':
                message.raw[valuekey] = 0
            elif 'brightness' in message.raw:
                message.raw[valuekey] = message.raw['brightness']
        return message
