all:
	@PYTHONPATH=$(shell pwd) python3 accountinfo/Asset.py
	@PYTHONPATH=$(shell pwd) python3 marketinterface/marketinfo.py
