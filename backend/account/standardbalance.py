from backend.utils.apiUtils import BingxAPI

class StandardBalance:
    def __init__(self):
        self.bingxAPI = BingxAPI()

    def getStdBalance(self):
        margin, unrealizedProfit = self.getOpenOrder()
        if margin is not None and unrealizedProfit is not None:
            assetBalance = margin + unrealizedProfit
            return assetBalance
        else:
            print("Failed to fetch standard balance.")
            return 0

    def getStdUP(self):
        _, unrealizedProfit = self.getOpenOrder()
        if unrealizedProfit is not None:
            # print(unrealizedProfit)
            return unrealizedProfit
        else:
            print("Failed to fetch standard unrealized profit.")
            return 0

    def getStdTotal(self):
        margin, unrealizedProfit = self.getOpenOrder()
        if margin is not None and unrealizedProfit is not None:
            total = margin + unrealizedProfit
            # print(total)
            return total
        else:
            print("Failed to fetch standard total balance.")
            return 0

    def getOpenOrder(self):
        path = '/openApi/contract/v1/allPosition'
        method = "GET"
        paramsMap = {
            "recvWindow": 0
        }
        paramsStr = self.bingxAPI.parseParams(paramsMap)
        responseDict = self.bingxAPI.sendRequest(method, path, paramsStr, {})
        # print(responseDict)

        dataExist = responseDict.get('data', [])
        if dataExist:
            margin, unrealizedProfit = self.getMarginUnrealizedProfit(responseDict)
            return margin, unrealizedProfit
        return 0, 0

    @staticmethod
    def getMarginUnrealizedProfit(dataDict):
        orders = dataDict.get('data', [])
        totalMargin = 0
        totalUnrealizedProfit = 0

        for order in orders:
            margin = float(order.get('initialMargin', 0))
            unrealizedProfit = float(order.get('unrealized_pro', 0))

            order["margin"] = margin
            order["unrealizedProfit"] = unrealizedProfit

            totalMargin += margin
            totalUnrealizedProfit += unrealizedProfit

        return float(totalMargin), float(totalUnrealizedProfit)
