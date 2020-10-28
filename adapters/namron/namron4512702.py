from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch

class Namron4512702(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.switch = SelectorSwitch(devices, 'switch', 'action')
        self.switch.add_level('Off', 'off')
        self.switch.add_level('On', 'on')
        self.switch.add_level('Up', 'brightness_step_up')
        self.switch.add_level('Down', 'brightness_step_down')
        self.switch.add_level('Move up', 'brightness_move_up')
        self.switch.add_level('Move down', 'brightness_move_down')
        self.switch.add_level('Stop', 'brightness_stop')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
        
# Possible messages:
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_step_down"}
# {"linkquality":42,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_step_up"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_stop"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_move_up"}
# {"linkquality":47,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"brightness_move_down"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"on"}
# {"linkquality":44,"battery":37.5,"action_step_size":32,"action_rate":50,"action":"off"}
