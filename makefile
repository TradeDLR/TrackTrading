all:
	#@PYTHONPATH=$(shell pwd) python3 src/AssetSocket.py
	#@PYTHONPATH=$(shell pwd) python3 src/MarketInfoSocket.py
	#@PYTHONPATH=$(shell pwd) python3 src/SelfInfoSocket.py
	@PYTHONPATH=$(shell pwd) python3 trade/SpotApi.py