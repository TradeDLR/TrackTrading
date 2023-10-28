all:
	@PYTHONPATH=$(shell pwd) python3 GUI/Asset.py
	@PYTHONPATH=$(shell pwd) python3 GUI/Call.py
