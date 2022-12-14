"""A Practical introduction to python descriptors.

Descriptors come in a few flavours in python and underpin most of the core concepts.
Typically, they come in two flavours, both outlined below. (data vs non data descriptors).

The Object model dunder methods for dealing with descriptors are:

__set_name__ (tho not specific to descriptors only - Optional)
__get__
__set__
__delete__

Data descriptors implement __get__ and either (or both) __set__ / __delete__
Non data descriptors

Descriptors are only used as class variables, inside instances they have no effect.

Descriptors allow a hook for objects stored in class variables to control what happens
to them during attribute lookup, typically the calling class decides, however descriptors
invert that relationship and allow the data being retried to have a say.

Some common places in the standard library that use descriptors are:
 * classmethod()
 * staticmethod()
 * property()
 * functools.cached_property()
 * many more...
"""

class ReturnsOneHundred:
    """A Completely pointless descriptor instance."""

    def __get__(self, obj, objtype=None):
        return 100


class DescriptorUser:

    one_hundred = ReturnsOneHundred()



def main():
    """Tests:
    >>> DescriptorUser().one_hundred == 100
    True
    >>> DescriptorUser().one_hundred == 101
    False
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()