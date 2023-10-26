from bingX import BingX
from bingX.perpetual.v2.types import HistoryOrder
import config

bingxClient = BingX(api_key=config.API_KEY,
                    secret_key=config.SECRET_KEY)
# Example
myOrder = HistoryOrder(symbol=None)

print(bingxClient.standard.get_orders_history(order=myOrder))


