# Trading_Track 
## Getting Started
TrackTrading is a trading analysis tool that helps users keep track of various crypto assets, get real-time price updates, 
and calculate the total value of their assets in USDT (or any other reference currency).

### TrackTrading Setup
Your workspace should have the following structure:
```
[path_to_your_workspace]
.
└── TrackTrading
```

### TrackTrading installation
1. Create a config.py under TrackTrading: /../TrackTrading/config.py
2. Add your API_KEY and SECRET_KEY in config.py
3. Build the TrackTrading:
```shell
make makefile
make -j$(nproc)
```
