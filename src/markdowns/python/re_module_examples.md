```python
In [1]: import re

In [2]: sentence = "One of my fav language is python and it is great!"

In [3]: re.sub(r"is", "was", sentence)
Out[3]: 'One of my fav language was python and it was great!'
```

```python
In [5]: print(sentence)
One of my fav language is python and it is great!

In [6]: sentence
Out[6]: 'One of my fav language is python and it is great!'

In [7]: re.split(r"\s", sentence)
Out[7]: 
['One',
 'of',
 'my',
 'fav',
 'language',
 'is',
 'python',
 'and',
 'it',
 'is',
 'great!']

In [8]: sentence2 = "One  of my fav language  is python  and it is     great!"

In [9]: sentence2
Out[9]: 'One  of my fav language  is python  and it is     great!'

In [10]: re.split(r"\s", sentence2)
Out[10]: 
['One',
 '',
 'of',
 'my',
 'fav',
 'language',
 '',
 'is',
 'python',
 '',
 'and',
 'it',
 'is',
 '',
 '',
 '',
 '',
 'great!']

In [11]: re.split(r"\s+", sentence2)
Out[11]: 
['One',
 'of',
 'my',
 'fav',
 'language',
 'is',
 'python',
 'and',
 'it',
 'is',
 'great!']
 ```

 ```python
 In [12]: sentence3 = "Here1goes2the417usage987examples1789related76to123python!"

In [13]: words = re.split(r"\d+", sentence3)

In [14]: print(words)
['Here', 'goes', 'the', 'usage', 'examples', 'related', 'to', 'python!']
```

```python
In [15]: words = re.split(r"^\d+$", sentence3)

In [16]: print(words)
['Here1goes2the417usage987examples1789related76to123python!']
```

```python

In [17]: str_numbers = re.split(r"[a-z]+", sentence3)

In [18]: print(str_numbers)
['H', '1', '2', '417', '987', '1789', '76', '123', '!']

In [19]: str_numbers = re.split(r"[a-zA-Z!]+", sentence3)

In [20]: print(str_numbers)
['', '1', '2', '417', '987', '1789', '76', '123', '']

In [21]: str_numbers = [int(str_number) for str_number in str_numbers if str_number]

In [22]: print(str_numbers)
[1, 2, 417, 987, 1789, 76, 123]
```

```python
In [1]: import re

In [2]: sentence = "Rishikesh is 32 years old!"

In [3]: match = re.match(r"(\w+) (\w+) (\d+) (.*)", sentence)

In [4]: match.group(0) # The entire match
Out[4]: 'Rishikesh is 32 years old!'

In [5]: match.group(1) # The 1st parenthesized group
Out[5]: 'Rishikesh'

In [6]: match.group(2) # The 2nd parenthesized group
Out[6]: 'is'

In [7]: match.group(3) # The 3rd parenthesized group
Out[7]: '32'

In [8]: match.group(4) # The 4th parenthesized group
Out[8]: 'years old!'
```

```python
In [9]: match.group(5)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[9], line 1
----> 1 match.group(5)

IndexError: no such group
```

```python
In [1]: import re

In [2]: sentence = "Rishikesh is 32 years old!"

In [3]: match = re.match(r"\d+", sentence)

In [4]: match

In [5]: print(match)
None

In [6]: search = re.search(r"\d+", sentence)

In [7]: search
Out[7]: <re.Match object; span=(13, 15), match='32'>

In [8]: search.group(0)
Out[8]: '32'

In [9]: search.group()
Out[9]: '32'

In [10]: search = re.search(r"\d+ \w+", sentence)

In [11]: search
Out[11]: <re.Match object; span=(13, 21), match='32 years'>

In [12]: search.group()
Out[12]: '32 years'

In [13]: search.group(0)
Out[13]: '32 years'
```

```python
In [16]: sentence = "Rishikesh is a dev. RISHIKESH likes coding in the weekend!"

In [17]: re.findall(r"rishikesh", sentence)
Out[17]: []

In [18]: re.findall(r"Rishikesh", sentence)
Out[18]: ['Rishikesh']

In [19]: re.findall(r"RISHIKESH", sentence)
Out[19]: ['RISHIKESH']

In [20]: re.findall(r"RISHIKESH", sentence, re.IGNORECASE)
Out[20]: ['Rishikesh', 'RISHIKESH']
```

```python
In [1]: import re

In [2]: sentence = "Rishikesh is 32 years old, and his birth year is 1992 and this is year 2025."

In [3]: numbers = re.findall(r"\d+", sentence)

In [4]: numbers
Out[4]: ['32', '1992', '2025']

In [5]: numbers = [number for number in numbers]

In [6]: numbers
Out[6]: ['32', '1992', '2025']

In [7]: numbers = [int(number) for number in numbers]

In [8]: numbers
Out[8]: [32, 1992, 2025]

In [9]: numbers = [float(number) for number in numbers]

In [10]: numbers
Out[10]: [32.0, 1992.0, 2025.0]

In [11]: numbers = [bool(number) for number in numbers]

In [12]: numbers
Out[12]: [True, True, True]

In [13]: sum(numbers)
Out[13]: 3
```

```python
In [29]: import re

In [30]: uuids = (
    ...:     "18d3ad19-e4b2-4f78-a79b-077072588328",
    ...:     "8f0f1bdd-0729-429f-baf6-0b18d495649b",
    ...:     "c816456b-6268-4a79-b548-5364bf89b9cf",
    ...:     "bf0d0eca-cafa-4bf8-a3e7-3f550f865447",
    ...:     "259ef702-1a46-4228-b2b8-da3ef6058456",
    ...:     "387dbe1b-1fe9-4520-9321-07cd8d66d368",
    ...:     "cc6faa47-92cc-4c4a-9c40-eb808de1f156",
    ...:     "607e171a-c1ad-4c9a-8dec-67d06da9afe1",
    ...:     "93641658-a9a3-4f0e-8708-80eeda4f0c3b",
    ...:     "9047d021-071a-4e24-b6aa-55cb816b7c07",
    ...:     "abeab76f-e9d5-441d-813e-cc2ec1348a40",
    ...:     "ecea968a-d6da-43f5-9dc2-255e7dbf9cb5",
    ...:     "edf2c83a-deb6-4b4b-a729-836a6e9cd12e",
    ...:     "038bd9d0-a638-4b16-a84f-710f9e2c2c51",
    ...:     "448a55a8-06f4-4642-93eb-9ae1ec9988e0",
    ...: )

In [31]: for uuid in uuids:
    ...:     print(uuid, ' -> ', re.sub(r"[abcd]", "9", uuid))
    ...: 
18d3ad19-e4b2-4f78-a79b-077072588328  ->  18939919-e492-4f78-9799-077072588328
8f0f1bdd-0729-429f-baf6-0b18d495649b  ->  8f0f1999-0729-429f-99f6-091894956499
c816456b-6268-4a79-b548-5364bf89b9cf  ->  98164569-6268-4979-9548-53649f89999f
bf0d0eca-cafa-4bf8-a3e7-3f550f865447  ->  9f090e99-99f9-49f8-93e7-3f550f865447
259ef702-1a46-4228-b2b8-da3ef6058456  ->  259ef702-1946-4228-9298-993ef6058456
387dbe1b-1fe9-4520-9321-07cd8d66d368  ->  38799e19-1fe9-4520-9321-079989669368
cc6faa47-92cc-4c4a-9c40-eb808de1f156  ->  996f9947-9299-4949-9940-e98089e1f156
607e171a-c1ad-4c9a-8dec-67d06da9afe1  ->  607e1719-9199-4999-89e9-679069999fe1
93641658-a9a3-4f0e-8708-80eeda4f0c3b  ->  93641658-9993-4f0e-8708-80ee994f0939
9047d021-071a-4e24-b6aa-55cb816b7c07  ->  90479021-0719-4e24-9699-559981697907
abeab76f-e9d5-441d-813e-cc2ec1348a40  ->  99e9976f-e995-4419-813e-992e91348940
ecea968a-d6da-43f5-9dc2-255e7dbf9cb5  ->  e9e99689-9699-43f5-9992-255e799f9995
edf2c83a-deb6-4b4b-a729-836a6e9cd12e  ->  e9f29839-9e96-4949-9729-83696e99912e
038bd9d0-a638-4b16-a84f-710f9e2c2c51  ->  03899990-9638-4916-984f-710f9e292951
448a55a8-06f4-4642-93eb-9ae1ec9988e0  ->  44895598-06f4-4642-93e9-99e1e99988e0
```

```python
In [32]: print(','.join(uuids))
18d3ad19-e4b2-4f78-a79b-077072588328,8f0f1bdd-0729-429f-baf6-0b18d495649b,c816456b-6268-4a79-b548-5364bf89b9cf,bf0d0eca-cafa-4bf8-a3e7-3f550f865447,259ef702-1a46-4228-b2b8-da3ef6058456,387dbe1b-1fe9-4520-9321-07cd8d66d368,cc6faa47-92cc-4c4a-9c40-eb808de1f156,607e171a-c1ad-4c9a-8dec-67d06da9afe1,93641658-a9a3-4f0e-8708-80eeda4f0c3b,9047d021-071a-4e24-b6aa-55cb816b7c07,abeab76f-e9d5-441d-813e-cc2ec1348a40,ecea968a-d6da-43f5-9dc2-255e7dbf9cb5,edf2c83a-deb6-4b4b-a729-836a6e9cd12e,038bd9d0-a638-4b16-a84f-710f9e2c2c51,448a55a8-06f4-4642-93eb-9ae1ec9988e0
```

#### Wrong

```python

In [34]: print(','.join("'{uuid}'" for uuid in uuids))
'{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}','{uuid}'
```

```python

In [35]: print(','.join(f"'{uuid}'" for uuid in uuids))
'18d3ad19-e4b2-4f78-a79b-077072588328','8f0f1bdd-0729-429f-baf6-0b18d495649b','c816456b-6268-4a79-b548-5364bf89b9cf','bf0d0eca-cafa-4bf8-a3e7-3f550f865447','259ef702-1a46-4228-b2b8-da3ef6058456','387dbe1b-1fe9-4520-9321-07cd8d66d368','cc6faa47-92cc-4c4a-9c40-eb808de1f156','607e171a-c1ad-4c9a-8dec-67d06da9afe1','93641658-a9a3-4f0e-8708-80eeda4f0c3b','9047d021-071a-4e24-b6aa-55cb816b7c07','abeab76f-e9d5-441d-813e-cc2ec1348a40','ecea968a-d6da-43f5-9dc2-255e7dbf9cb5','edf2c83a-deb6-4b4b-a729-836a6e9cd12e','038bd9d0-a638-4b16-a84f-710f9e2c2c51','448a55a8-06f4-4642-93eb-9ae1ec9988e0'
```