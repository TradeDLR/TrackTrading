## Getting Started
TrackTrading is a trading analysis tool that helps users keep track of various crypto assets, get real-time price updates, 
and calculate the total value of their assets in USDT (or any other reference currency).

### Features

- Real-time Asset Tracking: Get the most recent prices of your crypto assets.
- Export to CSV: Conveniently export your asset details and values to a CSV file.
- Supports Multiple Cryptocurrencies: Track and manage a wide range of cryptocurrencies.
- [Any Other Feature]: Brief description of the feature.


### Installation
1. Clone the repository:
```shell
git clone https://github.com/TradeDLR/TrackTrading.git
```
2. Navigate to the project directory:
``` shell
cd TrackTrading
```
3. Create a config.py under TrackTrading and add your API_KEY and SECRET_KEY in config.py
``` shell
nano config.py
```
``` config.py
API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"
```

### Usage
Run AccountBal.py to fetch the latest balances:
```shell
make makefile
make -j$(nproc)
```
or
```shell
python3 backend/src/UserInterface.py
```

