import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from AssetSocket import getAssetSocket
from MarketInfoSocket import getMarketInfoSocket
from SelfInfoSocket import getSelfInfoSocket
from TradeSpotSocket import getTradeSpotSocket
from backend.utils.utilities import PrintCommand

class UserInterface(PrintCommand):
    def __init__(self):
        commands = {
            ("asset proof", "asset", "ap"): self.assetProof,
            ("user info", "user", "ui"): self.userInfo,
            ("market info", "market", "mi"): self.marketInfo,
            ("spot trading", "spot", "st"): self.spotTrading,
            ("quit", "Q", "q"): self.quit
        }

        descriptions = {
            "asset proof (asset or ap)": "Get user's asset overview, including asset.csv and asset.xlsx",
            "user info (user or ui)": "Get user's specific information",
            "market info (market or mi)": "Get market information",
            "spot trading (spot or st)": "For spot trading",
            "quit (Q or q)": "Quit"
        }
        super().__init__(commands, descriptions)

    def assetProof(self):
        getAssetSocket().run()

    def userInfo(self):
        getSelfInfoSocket().userInput()

    def marketInfo(self):
        getMarketInfoSocket().userInput()

    def spotTrading(self):
        getTradeSpotSocket().userInput()

    def quit(self):
        print("Goodbye") 
        exit()

if __name__ == "__main__":
    user = UserInterface()
    user.userInput()