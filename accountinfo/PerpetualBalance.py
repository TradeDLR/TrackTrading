from .apiUtils import BingxAPI

class PerpetualBalance:
    def __init__(self):
        self.bingxAPI = BingxAPI()
        self.responseData = {}

    def fetchPerpBalance(self):
        """
        Fetch perpetual balance data from the API and return the result as a dictionary.
        """
        path = '/openApi/swap/v2/user/balance'
        method = "GET"
        paramsMap = {"recvWindow": 0}
        paramsStr = self.bingxAPI.parseParams(paramsMap)
        responseDict = self.bingxAPI.sendRequest(method, path, paramsStr, {})
        return responseDict

    def updatePerpBalance(self):
        """
        Update the perpetual balance data.
        Returns True if the update was successful, False otherwise.
        """
        try:
            responseDict = self.fetchPerpBalance()
            if "data" in responseDict and "balance" in responseDict["data"]:
                self.responseData = responseDict["data"]["balance"]
                return True
            else:
                print("Failed to fetch balance data. Please check the API response.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def getPerpAsset(self):
        """
        Get the perpetual asset balance.
        """
        return float(self.responseData.get('balance', '0'))

    def getPerpUP(self):
        """
        Get the perpetual unrealized profit.
        """
        return float(self.responseData.get('unrealizedProfit', '0'))

    def getPerpRP(self):
        """
        Get the perpetual realized profit.
        """
        return float(self.responseData.get('realizedProfit', '0'))

    def getPerpTotal(self):
        """
        Calculate the total perpetual balance.
        """
        asset = self.getPerpAsset()
        unrealizedProfit = self.getPerpUP()
        realizedProfit = self.getPerpRP()
        return asset + unrealizedProfit + realizedProfit
