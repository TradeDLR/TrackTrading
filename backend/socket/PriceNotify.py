import time
import smtplib
from email.message import EmailMessage
from collections import deque
from datetime import datetime
from backend.market.spotinfo import SpotInfo

class Notify(SpotInfo):

    def pricesNotify(self, check_interval=15):
        coin_thresholds = self.priceInput()
        notified_coins = set()
        while True:

            for coin, threshold in coin_thresholds.items():
                current_price = self.getLastprice(coin)
                print(f"{coin} Price: {current_price}")

                if current_price and current_price >= threshold and coin not in notified_coins:
                    self.send_notification(coin, current_price)
                    notified_coins.add(coin)

            time.sleep(check_interval)

    def checkPrices(self, check_interval=10, price_change_interval=30):

        coins = self.coinInput()
        price_history = {coin: deque(maxlen=price_change_interval // check_interval) for coin in coins}
        max_coin_name_length = max(len(coin) for coin in coins)
        max_price_length = 0
        while True:
            for coin in coins:
                current_price = self.getLastprice(coin)
                current_time = datetime.now()
                price_str = f"{current_price:.10g}"  # Convert the price to string with general format
                max_price_length = max(max_price_length, len(price_str))

                # Maintain a rolling record of the last 3 minutes of prices
                price_history[coin].append((current_price, current_time))

                if len(price_history[coin]) == price_history[coin].maxlen:
                    # Compare current price to the price from 3 minutes ago
                    initial_price, initial_time = price_history[coin][0]

                    if initial_price:

                        change = (current_price - initial_price) / initial_price
                        price_str = f"{current_price:.10g}"
                        interval_min = price_change_interval/60
                        #print(f"{coin} Price Change Rate: {change * 100:.2f}%")
                        print(f"{coin.ljust(max_coin_name_length)} Price: {price_str.rjust(max_price_length)} | {interval_min} min Change Rate: {change * 100:>6.2f}%")

            print(f"--------------{current_time.strftime('%Y-%m-%d %H:%M:%S')}--------------")
            time.sleep(check_interval)


    def send_notification(self, coin, price):
        sender_email = "ericericxx@gmail.com"
        password = "xkhekpbmdnisfors"
        receiver_email = "linspiringhh@gmail.com"

        # Email content
        subject = f"Alert: {coin} has reached the price of {price}"
        body = f"The price of {coin} is now {price}."

        # Create EmailMessage object and set its content
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)


    def coinInput(self):
        while True:
            input_string = input("Enter coins (separated by space): ")
            if input_string:
                coins = input_string.upper().split()
                valid_coins = [coin for coin in coins if self.getQuerySymbols(coin) is not None]

                if valid_coins:
                    return valid_coins
                else:
                    print(f"Please try again. Invalid coins: {', '.join(coins)}")
            else:
                print("No coins entered. Please try again.")

    def priceInput(self):
        coins = self.coinInput()
        targetPrices={}
        while True:
            for coin in coins:
                current_price = self.getLastprice(coin)
                print(f"{coin} price : {current_price}")
                target_price = float(input(f"Enter target price for {coin}: "))
                targetPrices[coin] = target_price

            print("Target prices:", targetPrices)
            return targetPrices

# Example usage
class_instance = Notify()
#coin_thresholds = {'BTC': 40000}
#coin_list = (['BTC','ETH','MUBI','APE','WLD','ENS'])
class_instance.pricesNotify()
#class_instance.checkPrices()
