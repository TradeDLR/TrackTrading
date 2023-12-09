import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from AssetSocket import getAssetSocket
from PerpMarketSocket import getPerpMarketSocket
from SelfInfoSocket import getSelfInfoSocket
from TradeSpotSocket import getTradeSpotSocket
from SpotMarketSocket import getSpotMarketSocket
from backend.utils.utilities import PrintCommand
from TradePerpSocket import getTradePerpSocket

class UserInterface(PrintCommand):
    def __init__(self):
        commands = {
            ("asset proof", "asset", "ap"): self.assetProof,
            ("user info", "user", "ui"): self.userInfo,
            ("perp market info", "p market", "pmi"): self.perpMarketInfo,
            ("spot market info", "s market", "smi"): self.spotMarketInfo,
            ("spot trading", "spot", "st"): self.spotTrading,
            ("perp trading", "perp", "pt"): self.perpTrading,
            ("quit", "Q", "q"): self.quit
        }

        descriptions = {
            "asset proof (asset or ap)": "Get user's asset overview, including asset.csv and asset.xlsx",
            "user info (user or ui)": "Get user's specific information",
            "perpetual market info (p market or pmi)": "Get perp market information",
            "spot market info (s market or smi)": "Get spot market information",
            "spot trading (spot or st)": "For spot trading",
            "perp trading (perp or pt)": "For perpetual trading",
            "quit (Q or q)": "Quit"
        }
        super().__init__(commands, descriptions)

    def assetProof(self):
        getAssetSocket().run()

    def userInfo(self):
        getSelfInfoSocket().userInput()

    def perpMarketInfo(self):
        getPerpMarketSocket().userInput()

    def spotMarketInfo(self):
        getSpotMarketSocket().userInput()

    def spotTrading(self):
        getTradeSpotSocket().userInput()

    def perpTrading(self):
        getTradePerpSocket().userInput()

    def quit(self):
        print("Goodbye") 
        exit()

if __name__ == "__main__":
    user = UserInterface()
    user.userInput()