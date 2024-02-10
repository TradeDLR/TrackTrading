all:

	@PYTHONPATH=$(shell pwd) python3 backend/socket/UserInterface.py
	#@PYTHONPATH=$(shell pwd) python3 backend/socket/PriceNotify.py
