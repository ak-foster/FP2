# Generator Tutorial
# rriehle February 2018

# By now you're well familiar with range()
range(10)

# Let's iterate over it in a list comprehension.
[x for x in range(10)]

# Or, let's subtly alter the syntax... what to we get?
(x for x in range(10))

# Cool, a generator. What's a generator?
# Let's name it so that we can play with it.
my_first_generator = (x for x in range(10))

my_first_generator?

for i in my_first_generator: print(i)

# Cool, let's try it again.
for i in my_first_generator: print(i)

# Uh oh.  It looks to be spent.  What's up?
# Let's spin up another couple generators.
my_second_generator = (x for x in range(10))
my_third_generator = (x for x in range(10))

dir(my_second_generator)

# What's the __next__ dunder?
my_second_generator.__next__?

# Look at the docstring. Implement next() on self.

# Let's call it anyway once or twice just for kicks.
my_second_generator.__next__()

# That's a bit awkward, so let's use the next() builtin instead.
next?

next(my_second_generator)
next(my_second_generator)
next(my_second_generator)
next(my_second_generator)

# Alright, so it is remembering its state
# and upon each call to next() it is giving
# us its next value

# We've been ignoring the other generator
# Let's next() it.
next(my_third_generator)
next(my_third_generator)

# Cool, so the two generators are each remembering
# their own state and operating independently of each other.

# Let's spin them out until they're empty.
next(my_second_generator)
next(my_second_generator)
next(my_second_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)
next(my_third_generator)

