# note

use get method to get values using keys. get method can config if the key is not in the dict.

### setdefault()

```python
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

```pyhton
message = 'It was a bright cold day in April, and the clocks were striking
thirteen.'
count = {}

for character in message:
➊ count.setdefault(character, 0)
➋ count[character] = count[character] + 1

print(count)

## this kind of things can happen.
```
