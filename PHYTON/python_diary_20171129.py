Python 2.7.3 (default, Jan  2 2013, 16:53:07) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print "Teksts"
Teksts
>>> __bultina__.
SyntaxError: invalid syntax
>>> __bultina__.
SyntaxError: invalid syntax
>>> __bultina__.
SyntaxError: invalid syntax
>>> vars.__doc__
'vars([object]) -> dictionary\n\nWithout arguments, equivalent to locals().\nWith an argument, equivalent to object.__dict__.'
>>> print vars.__doc__
vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__.
>>> x = 5
>>> x. __doc__
'int(x[, base]) -> integer\n\nConvert a string or number to an integer, if possible.  A floating point\nargument will be truncated towards zero (this does not include a string\nrepresentation of a floating point number!)  When converting a string, use\nthe optional base.  It is an error to supply a base when converting a\nnon-string.  If base is zero, the proper base is guessed based on the\nstring content.  If the argument is outside the integer range a\nlong object will be returned instead.'
>>> print x.__doc__
int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead.
>>> print input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> input ("Vadi skaitli: ")
Vadi skaitli: 6
6
>>> from math import sin
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 5, '__name__': '__main__', 'sin': <built-in function sin>, '__doc__': None}
>>> sin(0.56)
0.5311861979208834
>>> print sin.__doc__
sin(x)

Return the sine of x (measured in radians).
>>> 
>>> from math import sin as sinuss
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 5, '__name__': '__main__', 'sinuss': <built-in function sin>, 'sin': <built-in function sin>, '__doc__': None}
>>> sin(0.56)
0.5311861979208834
>>> sinuss(0.56)
0.5311861979208834
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 5, '__name__': '__main__', 'sinuss': <built-in function sin>, 'sin': <built-in function sin>, '__doc__': None}
>>> math.cos(0.56)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    math.cos(0.56)
NameError: name 'math' is not defined
>>> import math
>>> math.cos(0.56)
0.8472551110134161
>>> math.tan(0.56)
0.6269495350526982
>>> from mats import *

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    from mats import *
ImportError: No module named mats
>>> from math import *
>>> vars()
{'exp': <built-in function exp>, 'pow': <built-in function pow>, 'fsum': <built-in function fsum>, 'cosh': <built-in function cosh>, 'ldexp': <built-in function ldexp>, 'hypot': <built-in function hypot>, 'acosh': <built-in function acosh>, 'tan': <built-in function tan>, 'asin': <built-in function asin>, 'isnan': <built-in function isnan>, 'log': <built-in function log>, 'fabs': <built-in function fabs>, 'floor': <built-in function floor>, 'atanh': <built-in function atanh>, 'sqrt': <built-in function sqrt>, '__package__': None, 'frexp': <built-in function frexp>, 'factorial': <built-in function factorial>, 'degrees': <built-in function degrees>, 'pi': 3.141592653589793, 'log10': <built-in function log10>, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>, 'asinh': <built-in function asinh>, 'fmod': <built-in function fmod>, 'atan': <built-in function atan>, '__builtins__': <module '__builtin__' (built-in)>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'ceil': <built-in function ceil>, 'atan2': <built-in function atan2>, 'isinf': <built-in function isinf>, '__doc__': None, 'sinh': <built-in function sinh>, '__name__': '__main__', 'trunc': <built-in function trunc>, 'expm1': <built-in function expm1>, 'e': 2.718281828459045, 'tanh': <built-in function tanh>, 'radians': <built-in function radians>, 'sinuss': <built-in function sin>, 'lgamma': <built-in function lgamma>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'modf': <built-in function modf>, 'x': 5, 'acos': <built-in function acos>, 'log1p': <built-in function log1p>, 'gamma': <built-in function gamma>}
>>> import math as abc
>>> vars()
{'exp': <built-in function exp>, 'pow': <built-in function pow>, 'fsum': <built-in function fsum>, 'cosh': <built-in function cosh>, 'ldexp': <built-in function ldexp>, 'hypot': <built-in function hypot>, 'acosh': <built-in function acosh>, 'tan': <built-in function tan>, 'asin': <built-in function asin>, 'isnan': <built-in function isnan>, 'abc': <module 'math' (built-in)>, 'log': <built-in function log>, 'fabs': <built-in function fabs>, 'floor': <built-in function floor>, 'atanh': <built-in function atanh>, 'sqrt': <built-in function sqrt>, '__package__': None, 'frexp': <built-in function frexp>, 'factorial': <built-in function factorial>, 'degrees': <built-in function degrees>, 'pi': 3.141592653589793, 'log10': <built-in function log10>, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>, 'asinh': <built-in function asinh>, 'fmod': <built-in function fmod>, 'atan': <built-in function atan>, '__builtins__': <module '__builtin__' (built-in)>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'ceil': <built-in function ceil>, 'atan2': <built-in function atan2>, 'isinf': <built-in function isinf>, '__doc__': None, 'sinh': <built-in function sinh>, '__name__': '__main__', 'trunc': <built-in function trunc>, 'expm1': <built-in function expm1>, 'e': 2.718281828459045, 'tanh': <built-in function tanh>, 'radians': <built-in function radians>, 'sinuss': <built-in function sin>, 'lgamma': <built-in function lgamma>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'modf': <built-in function modf>, 'x': 5, 'acos': <built-in function acos>, 'log1p': <built-in function log1p>, 'gamma': <built-in function gamma>}
>>> 
