# README
We have a Python 3.10 application.
We do not want to roll out 3.10 however on our production system

# build via
```python3 setup.py bdist_wheel```

# problem
We can install this application now by going into dist and run `pip3 install currency_converter-0.1-py3-none-any.whl`

Unless we have Python3.10 installed, we will have an issue
