from bingX import BingX
from bingX.perpetual.v2.types import HistoryOrder
import config

bingx_client = BingX(api_key=config.API_KEY,
                     secret_key=config.SECRET_KEY)
# Example
my_order = HistoryOrder(symbol=None)

print(bingx_client.standard.get_orders_history(order=my_order))


