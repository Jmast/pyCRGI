
test:
	PYIGRF_DEBUG=1 pytest
	python verification/verify.py
