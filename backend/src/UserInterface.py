from AssetSocket import getAssetSocket
from MarketInfoSocket import getMarketInfoSocket
from SelfInfoSocket import getSelfInfoSocket
from TradeSpotSocket import getTradeSpotSocket
from backend.utils.utilities import PrintCommand

class UserInterface(PrintCommand):
    def __init__(self):
        commands = {
            "asset proof": self.assetProof,
            "user info": self.userInfo,
            "market info": self.marketInfo,
            "spot trading": self.spotTrading,
            "quit": self.quit
        }

        descriptions = {
            "asset proof": "Get user's asset overview, including asset.csv and asset.xlsx",
            "user info": "Get user's specific information",
            "market info": "Get market information",
            "spot trading": "For spot trading",
            "quit": "Quit"
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

if __name__ == "__main__":
    user = UserInterface()
    user.userInput()