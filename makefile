all:
	@PYTHONPATH=$(shell pwd) python3 src/AssetSocket.py
	@PYTHONPATH=$(shell pwd) python3 src/MarketInfoSocket.py
