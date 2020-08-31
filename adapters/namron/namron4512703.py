from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.dimmer_switch import DimmerSwitch
from devices.switch.selector_switch import SelectorSwitch

class Namron4512703(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        
        self.dim1 = DimmerSwitch(devices, 'dim1', 'l1', ' (Dimmer1)')
        self.dim2 = DimmerSwitch(devices, 'dim2', 'l2', ' (Dimmer2)')
        self.dim3 = DimmerSwitch(devices, 'dim3', 'l3', ' (Dimmer3)')
        self.dim4 = DimmerSwitch(devices, 'dim4', 'l4', ' (Dimmer4)')
        self.devices.append(self.dim1)
        self.devices.append(self.dim2)
        self.devices.append(self.dim3)
        self.devices.append(self.dim4)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'action' in message.raw:
            actions = message.raw['action'].Split('_')
            valuekey = actions[-1]
            if len(actions) > 0:
                if (actions[0] == 'on' or actions[0] == 'off') and len(actions) > 1:
                    message.raw[valuekey] = actions[0]
                elif actions[0] == 'brightness':
                    device = self.get_device_by_value_key(valuekey)
                    if len(actions) > 1:
                        if actions[1] == 'move':
                            rate = message.raw['action_rate']
                            value = int(device.sValue)*255/100 + (rate if actions[2] == 'up' else -rate)
                            value = str(value * 100 / 255)
                            message.raw[valuekey] = value
                        elif actions[1] == 'stop':
                            none
        return message

    def handleMqttMessage(self, device_data, message):
        if 'action' not in message.raw:
            return

        actions = message.raw['action'].Split('_')
        if len(actions) == 0:
            return;

        converted_message = self.convert_message(message)

        valuekey = actions[-1]
        if (actions[0] == 'on' or actions[0] == 'off') and len(actions) > 1:
            device = self.get_device_by_value_key(valuekey)
            if device != None:
                device.handle_message(device_data, converted_message)
        
        self.update_battery_status(device_data, converted_message)
        self.update_link_quality(device_data, converted_message)

    def get_device_by_value_key(self, value_key):
        for device in self.devices:
            if device.value_key == value_key:
                return device
        return None
