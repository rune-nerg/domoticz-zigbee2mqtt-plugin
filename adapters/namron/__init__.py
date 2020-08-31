from adapters.namron.namron4512702 import Namron4512702
from adapters.namron.namron4512703 import Namron4512703
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter

namron_adapters = {
    '4512702': Namron4512702,           # Namron ZigBee 1 channel switch K4
    '4512703': Namron4512703,           # Namron ZigBee 4 channel switch K8
    'Eco-Dim.07': DimmableBulbAdapter,  # Namron/EcoDim push/turn ZigBee dimmer
    # Namron sells this as a pure ZigBee dimmer. It also exists from other Vendors (EcoDim among others) as combined ZigBee/Z-Wave dimmer
}
