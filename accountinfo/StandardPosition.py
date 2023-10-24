import sys
sys.path.append('../')
from apiUtils import BingxAPI
class StandardPosition(BingxAPI):

    @staticmethod
    def getOpenOrder():
        path = '/openApi/contract/v1/allPosition'
        method = "GET"
        paramsMap = {
            "recvWindow": 0
        }
        paramsStr = StandardPosition.parseParams(paramsMap)
        responseDict = StandardPosition.sendRequest(method, path, paramsStr, {})

        dataExist = responseDict.get('data', [])
        if dataExist:
            margin, unrealizedProfit = StandardPosition.getMarginUnrealizedProfit(responseDict)
            return margin, unrealizedProfit
        return 0, 0

    @staticmethod
    def getMarginUnrealizedProfit(data_dict):
        orders = data_dict.get('data', [])
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
