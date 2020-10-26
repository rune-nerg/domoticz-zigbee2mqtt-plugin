from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.dimmer_switch import DimmerSwitch

class Namron4512702(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.dimmer = DimmerSwitch(devices, 'dimmer', 'value')
        self.devices.append(self.dimmer)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'action' in message.raw:
            actions = message.raw['action'].split('_')
            if len(actions) > 0:
                if (actions[0] == 'on' or actions[0] == 'off'):
                    message.raw['value'] = actions[0]
                elif actions[0] == 'brightness':
                    device = self.dimmer
                    if len(actions) > 1:
                        if actions[1] == 'move':
                            rate = message.raw['action_rate']
                            value = int(device.sValue)*255/100 + (rate if actions[2] == 'up' else -rate)
                            value = value * 100 / 255
                            message.raw['value'] = value
                        elif actions[1] == 'step':
                            step = message.raw['action_step_size']
                            value = int(device.sValue)*255/100 + (step if actions[2] == 'up' else -step)
                            value = value * 100 / 255
                            message.raw['value'] = value
                        elif actions[1] == 'stop':
                            none
        return message

# Possible messages:
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_step_down"}
# {"linkquality":42,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_step_up"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_stop"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_move_up"}
# {"linkquality":47,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_move_down"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"on"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"off"}
