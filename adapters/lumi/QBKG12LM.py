import Domoticz
import json
from adapters.lumi.QBKG03LM import QBKG03LM
from devices.sensor.kwh import KwhSensor


class QBKG12LM(QBKG03LM):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(KwhSensor(devices, 'kwh', ['power']))
