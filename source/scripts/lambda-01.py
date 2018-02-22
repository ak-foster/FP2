# Lambda tutorial
# rriehle February 2018

def times_two(x):
    return x * 2

times_two(3)

lambda x: x * 2

# Lambda originated in lisp where it is mostly used with map
# First, let's try it with the standard function.
map(times_two, [x for x in range(10)])

# Map returns an iterator, so let's force it to be iterated over via list.
list(map(times_two, [x for x in range(10)]))

# Now let's use a lamdda.
list(map(lambda x: x*2, [x for x in range(10)]))

# Let's look at this in a comprehension.null=True
[x for x in range(10)]
[times_two(x) for x in range(10)]

# Now the lambda in a coprehension
[lambda x: x * 2 for x in range(10)]

# Ugh.
[(labda x: x * 2)(x) for x in range(10)]

# Or, forget them both, you need neither the function nor the lambda.
[x * 2 for x in range(10)]


# Do NOT do this at home

times_two = lambda x: x * 2


import this

# There should be one obvious way to do it, but now we have two.

# The secret behind lambda: there is no secret.
# Can't stress this enough, there is nothing a lambda can do
# that a standard function def can't do.

# Guido wanted to drop it from the language.

# Great in Lisp, Scheme, Closure.  It's terrible in Python.
