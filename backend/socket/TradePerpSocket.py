from backend.market.perpetual import Perpetual
from backend.market.perpinfo import getPerpInfo
from backend.utils.utilities import PrintCommand
import time

class TradePerpSocket(Perpetual, PrintCommand):
    def __init__(self):
        Perpetual.__init__(self)
        self.perpinfo = getPerpInfo()
