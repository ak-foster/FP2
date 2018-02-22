# Lambda tutorial
# rriehle February 2018

def add_two(x):
    return x + 2

add_two(3)

lambda x: x + 2

map(add_two, [x for x in range(10)])
list(map(add_two, [x for x in range(10)]))
list(map(lambda x: x+2, [x for x in range(10)]))

def mod_two(x):
    return x % 2

list(map(mod_two, [x for x in range(10)]))
list(map(lambda x: x % 2, [x for x in range(10)]))

# Do NOT do this at home

mod_two = lambda x: x % 2

list(map(mod_two, [x for x in range(10)]))

import this

# There should be one obvious way to do it, but now we have two.

# The secret behind lambda: there is no secret.
# Can't stress this enough, there is nothing a lambda can do
# that a standard function def can't do.

# Guido wanted to drop it from the language.

# Great in Lisp, Scheme, Closure.  It's terrible in Python.
