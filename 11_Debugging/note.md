# note

```python
# raise exception
raise Exception("blah blah")

a = 10
b = 5

# assert
assert a < b, f"Assertion failed: a = {a}, b = {b}"


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# logging to file.
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s -  %(levelname)s -  %(message)s')

```
