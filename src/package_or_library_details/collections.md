## Help on package collections:

### NAME
collections

### MODULE REFERENCE
https://docs.python.org/3.6/library/collections

The following documentation is automatically generated from the Python
source files.  It may be incomplete, incorrect or include features that
are considered implementation detail and may vary between Python
implementations.  When in doubt, consult the module reference at the
location listed above.

### DESCRIPTION
This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing


### `namedtuple`
Help on function namedtuple in module collections:

```shell
namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
    Returns a new subclass of tuple with named fields.
```

```shell
>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)
```


### `deque`
```shell
Help on class deque in module collections:

class deque(builtins.object)
 |  deque([iterable[, maxlen]]) --> deque object
 |  
 |  A list-like sequence optimized for data accesses near its endpoints.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __copy__(...)
 |      Return a shallow copy of a deque.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      D.__reversed__() -- return a reverse iterator over the deque
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -- size of D in memory, in bytes
 |  
 |  append(...)
 |      Add an element to the right side of the deque.
 |  
 |  appendleft(...)
 |      Add an element to the left side of the deque.
 |  
 |  clear(...)
 |      Remove all elements from the deque.
 |  
 |  copy(...)
 |      Return a shallow copy of a deque.
 |  
 |  count(...)
 |      D.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      Extend the right side of the deque with elements from the iterable
 |  
 |  extendleft(...)
 |      Extend the left side of the deque with elements from the iterable
 |  
 |  index(...)
 |      D.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      D.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      Remove and return the rightmost element.
 |  
 |  popleft(...)
 |      Remove and return the leftmost element.
 |  
 |  remove(...)
 |      D.remove(value) -- remove first occurrence of value.
 |  
 |  reverse(...)
 |      D.reverse() -- reverse *IN PLACE*
 |  
 |  rotate(...)
 |      Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  maxlen
 |      maximum size of a deque or None if unbounded
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
```