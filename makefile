all:
	@PYTHONPATH=$(shell pwd) python3 TrackTradingBackend/src/AssetSocket.py
	@PYTHONPATH=$(shell pwd) python3 TrackTradingBackend/src/MarketInfoSocket.py
	@PYTHONPATH=$(shell pwd) python3 TrackTradingBackend/src/SelfInfoSocket.py
