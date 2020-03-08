from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.dimmer_switch import DimmerSwitch

class Namron4512702(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.dimmer = DimmerSwitch(devices, 'dimmer', 'value')
        self.devices.append(self.dimmer)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'click' in message.raw and message.raw['click'].lower() == 'off':
            message.raw['value'] = 0
        elif 'brightness' in message.raw:
            message.raw['value'] = message.raw['brightness']
        return message
