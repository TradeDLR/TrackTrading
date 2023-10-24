from apiUtils import BingxAPI


class PerpetualBalance(BingxAPI):

    @staticmethod
    def getPerpBalance():
        payload = {}
        path = '/openApi/swap/v2/user/balance'
        method = "GET"
        paramsMap = {
            "recvWindow": 0
        }
        paramsStr = PerpetualBalance.parseParams(paramsMap)
        responseDict = PerpetualBalance.sendRequest(method, path, paramsStr, payload)

        asset = float(responseDict.get('data', {}).get('balance', {}).get('balance', '0'))
        unrealizedProfit = float(responseDict.get('data', {}).get('balance', {}).get('unrealizedProfit', '0'))
        realizedProfit = float(responseDict.get('data', {}).get('balance', {}).get('realizedProfit', '0'))

        return asset, unrealizedProfit, realizedProfit
