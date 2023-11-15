all:

	#@PYTHONPATH=$(shell pwd) python3 backend/src/AssetSocket.py
	@PYTHONPATH=$(shell pwd) python3 backend/src/MarketInfoSocket.py
	#@PYTHONPATH=$(shell pwd) python3 backend/src/SelfInfoSocket.py
	#@PYTHONPATH=$(shell pwd) python3 backend/trade/spot.py

