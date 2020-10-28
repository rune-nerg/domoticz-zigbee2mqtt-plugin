from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch

class Namron4512703(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        
        self.sel1 = SelectorSwitch(devices, 'l1', 'action', ' (Dimmer1)')
        self.sel1.add_level('Off', 'off')
        self.sel1.add_level('On', 'on')
        self.sel1.add_level('Up', 'brightness_move_up')
        self.sel1.add_level('Down', 'brightness_move_down')
        self.sel1.add_level('Stop', 'brightness_stop')
        self.sel1.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.sel1.disable_value_check_on_update()
        self.devices.append(self.sel1)
        self.sel2 = SelectorSwitch(devices, 'l2', 'action', ' (Dimmer2)')
        self.sel2.add_level('Off', 'off')
        self.sel2.add_level('On', 'on')
        self.sel2.add_level('Up', 'brightness_move_up')
        self.sel2.add_level('Down', 'brightness_move_down')
        self.sel2.add_level('Stop', 'brightness_stop')
        self.sel2.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.sel2.disable_value_check_on_update()
        self.devices.append(self.sel2)
        self.sel3 = SelectorSwitch(devices, 'sel3', 'action', ' (Dimmer3)')
        self.sel3.add_level('Off', 'off')
        self.sel3.add_level('On', 'on')
        self.sel3.add_level('Up', 'brightness_move_up')
        self.sel3.add_level('Down', 'brightness_move_down')
        self.sel3.add_level('Stop', 'brightness_stop')
        self.sel3.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.sel3.disable_value_check_on_update()
        self.devices.append(self.sel3)
        self.sel4 = SelectorSwitch(devices, 'sel4', 'action', ' (Dimmer4)')
        self.sel4.add_level('Off', 'off')
        self.sel4.add_level('On', 'on')
        self.sel4.add_level('Up', 'brightness_move_up')
        self.sel4.add_level('Down', 'brightness_move_down')
        self.sel4.add_level('Stop', 'brightness_stop')
        self.sel4.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.sel4.disable_value_check_on_update()
        self.devices.append(self.sel4)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'action' in message.raw:
            # Remove switch designator
            message.raw['action'] = message.raw['action'].split('_')[0,-1]
        return message

    def handleMqttMessage(self, device_data, message):
        if 'action' not in message.raw:
            return
        actions = message.raw['action'].split('_')
        if len(actions) == 0:
            return

        converted_message = self.convert_message(message)

        alias = actions[-1]
        device = self.get_device_by_alias(alias)
        if device != None:
            device.handle_message(device_data, converted_message)
        
        self.update_battery_status(device_data, converted_message)
        self.update_link_quality(device_data, converted_message)

    def handleCommand(self, alias, device, device_data, command, level, color):
        device = self.get_device_by_alias(alias)
        if device != None:
            device.handle_command(device_data, command, level, color)

# {'action': 'on_l1', 'action_group': 9217, 'battery': 37.5, 'linkquality': 13}
# {'action': 'off_l1', 'action_group': 9217, 'battery': 37.5, 'linkquality': 15}
# {'action': 'brightness_move_down_l1', 'action_group': 9217, 'action_rate': 50, 'battery': 37.5, 'linkquality': 15}
# {'action': 'brightness_move_up_l1', 'action_group': 9217, 'action_rate': 50, 'battery': 37.5, 'linkquality': 13}
# {'action': 'brightness_stop_l1', 'action_group': 9217, 'battery': 37.5, 'linkquality': 15}
# etc with l2, l3 and l4
