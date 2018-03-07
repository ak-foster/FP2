.. Lesson Plan documentation master file, created by
   sphinx-quickstart on Sun Jan 28 19:33:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========================
Functional Programming 2
========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


************
Introduction
************

In this second lesson on functional programming we look at the lambda special form, which can be used in conjunction with `map` and `filter` and also in comprehensions.  We will consider the debates as to lambda's effectiveness by looking at its history and the comments of Python's creator Guido van Rossum.

Where we had been avoiding the topic up until now, at long last we investigate iterators and iterables, core constructs in Python 3.  Both terms are sprinkled throughout the Python programming literature and the distinction between them can be subtle.

Finally we look at generators, powerful programming constructs that are lazy by nature (in the functional programming sense of lazy) and thus can produce infinite sequences without exhausting the resources of real-world computers.

Recommended Text
================

For the functional programming modules,  we recommend the text Functional Python Programming by Steven Lott.

| Publisher: Packt Publishing
| Pub. Date: January 31, 2015
| Web ISBN-13: 978-1-78439-761-6
| Print ISBN-13: 978-1-78439-699-2
| http://bit.ly/2azI62S

Each lesson's optional readings will draw from this text.


Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

* use the lambda special form to define an anonymous function.
* use lambda expressions with `map` and `filter` and in comprehensions.
* articulate the difference between an iterator and an iterable.
* use `yield` to create a generator.


New Words or Concepts
=====================

* Anonymous function
* Lambda
* Iterator
* iterable
* Generator
* yield


Required Reading
================

* Small functions and the lambda expression

  | https://docs.python.org/dev/howto/functional.html?highlight=lambda#small-functions-and-the-lambda-expression

* Iterators

  | https://docs.python.org/3/glossary.html#term-iterator
  | https://docs.python.org/3/library/stdtypes.html#iterator-types
  | https://docs.python.org/dev/howto/functional.html#iterators

* Itertools

  | https://docs.python.org/3/library/itertools.html
  | https://pymotw.com/3/itertools/index.html

* What exactly are Python's iterator, iterable, and iteration protocols?

  | https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols

* Generators

  | https://wiki.python.org/moin/Generators


Optional Reading
================

* Lott, S. (2015) Chapter 5. Higher-order Functions. Using Python lambda forms. In Functional Python Programming.

* Lott, S. (2015) Chapter 3. Functions, Iterators, and Generators. In Functional Python Programming.

* Ramalho, L (2015) Chapter 14: Iterables, Iterators, and Generators. In Fluent Python

* The Iterator Protocol: How For Loops Work in Python

  | http://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/

* Chapter 14 in Fluent Python by Luciano Ramalho

  | http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/

* PEP 255 --- Simple Generators

  | https://www.python.org/dev/peps/pep-0255/


*******
Content
*******


Lambda
======

The Lambda special form is Python's syntax for creating an unnamed function --- a function without a name.  This is its general form:

.. code-block:: python

    lambda arguments: expression

The function evaluates to the result of the expression.  Here is a lambda that adds one to its argument:

.. code-block:: python3

    lambda x: x + 1

Here is a lambda that adds its two arguments together:

.. code-block:: python3

    lambda x, y: x + y

Compare this syntax to that of a standard function definition:

.. code-block:: python3

    def my_sum(x, y):
        return x + y

This simple function does nothing more than return the value of the expression in the ``return``, so it is viable written on a single line.

.. code-block:: python3

    def my_sum(x, y): return x + y

Notice how this named function maps directly to its unnamed, lambda equivalent:

.. code-block:: python3

    lambda x, y: x + y

Now, unlike most code snippets, if you were to type these examples into your favorite python interpreter by themselves they would not accomplish much.

Ipython:

.. code-block:: ipython3

    In []: lambda x, y: x + y
    Out[]: <function __main__.<lambda>>

The reference cpython interpreter:

.. code-block:: python3

    >>> lambda x, y: x + y
    <function <lambda> at 0x104f61e18>

You can't call those, because they have no name.  For all intents and purposes the anonymous functions were defined, recognized by the python interpreter as valid, syntactically correct python code, and then discarded, never to be seen or used again.  You could, however, use the function immediately by calling it with its required arguments:

.. code-block:: python3

    >>> (lambda x, y: x + y)(2, 3)
    5

In this case python defines the anonymous function, calls it with the supplied arguments and prints the result, but this feels like we're using the python interpreter as little more than a calculator; we are not writing useful code.  Indeed simply entering ``2 + 3`` in the interpreter provides the same result with a lot less typing.  So what's the point?  Where are lambdas useful?

Lambdas are only useful within larger code constructs --- specifically when defined inline --- and generally as an argument to a function or method which is expecting a function.

[Video: Lambda]


What is so special about Lambda?
--------------------------------

Here is the secret about Lambda: there is no secret to lambda.  There is nothing it can do that a standard named function cannot do.  It has no special powers aside from its ability to be defined inline.  Wherever you can use a Lambda you could instead choose to use a standard named function.


What use is Lambda?
-------------------

According to Python's creator, not much.

"About 12 years ago, Python aquired lambda, reduce(), filter() and map(), courtesy of (I believe) a Lisp hacker who missed them and submitted working patches. But, despite of the PR value, I think these features should be cut from Python 3000.

Why drop lambda? Most Python users are unfamiliar with Lisp or Scheme, so the name is confusing; also, there is a widespread misunderstanding that lambda can do things that a nested function can't -- I still recall Laura Creighton's Aha!-erlebnis after I showed her there was no difference! Even with a better name, I think having the two choices side-by-side just requires programmers to think about making a choice that's irrelevant for their program; not having the choice streamlines the thought process. Also, once map(), filter() and reduce() are gone, there aren't a whole lot of places where you really need to write very short local functions; Tkinter callbacks come to mind, but I find that more often than not the callbacks should be methods of some state-carrying object anyway (the exception being toy programs).

Update: lambda, filter and map will stay (the latter two with small changes, returning iterators instead of lists). Only reduce will be removed from the 3.0 standard library. You can import it from functools. "

 -- Guido van Rossum
 | http://www.artima.com/weblogs/viewpost.jsp?thread=98196

Why would we teach the Lambda special form if even if Python's creator has a low opinion of it?

You need to understand it, because you are going to see it in the wild.

As to whether you decide to propagate its use, we leave that to you.


Iterators and Iterables
=======================

Python 2
--------

Python used to be all about sequences --- a good chunk of anything you did was stored in a sequence or involved manipulating a sequence.

* lists
* tuples
* strings
* dict.keys()
* dict.values()
* dict.items()
* zip()


In python2 those are all sequences.  It turns out, however, that the most common operation for sequences is to iterate through them:

.. code-block:: python

    for item in a_sequence:
        do_something_with_item

So fairly early in Python2, Python introduced the idea of the "iterable".  An iterable is something you can, well, iterate over in a for loop, but often does not keep the whole sequence in memory at once.  After all, why make a copy of something just to look at all its items?

For example, in python2: ``dict.keys()`` returns a list of all the keys in the dict.  But why make a full copy of all the keys, when all you want to do is:

.. code-block:: python

    for key in dict.keys():
        do_something_with(key)

Even worse ``dict.items()`` created a full list of ``(key,value)`` tuples --- a complete copy of all the data in the dict.  Yet worse ``enumerate(dict.items())`` created a whole list of
``(index, (key, value))`` tuples --- lots of copies of everything.

Python2 then introduced "iterable" versions of a number of functions and methods:

| ``itertools.izip``
| ``dict.iteritems()``
| ``dict.iterkeys()``
| ``dict.itervalues()``

So you could now iterate through that stuff without copying anything.

Python3
-------

Python3 embraces iterables --- now everything that could be an iterator is already an iterator --- no unnecessary copies.  An iterator is an iterable that has been made more efficient by removing as much from memory as possible.  You have to make a list out of them explicitly if you really want it:

``list(dict.keys())``

Then there is an entire module: ``itertools`` that provides nifty ways to iterate through stuff.  So while we used to think in terms of sequences we now think in terms of iterables.

Iterators and Iterables
-----------------------

Iteration is one of the main reasons Python code is so readable:

.. code-block:: python

    for x in just_about_anything:
        do_stuff(x)

An iterable is anything that can be looped over sequentially, so it does not have to be a "sequence": list, tuple, etc.  For example, a string is iterable. So is a set.

An iterator is an iterable that remembers state. All sequences are iterable, but not all sequences are iterators. To make a sequence an iterator, you can call it with iter:

.. code-block:: python

   my_iter = iter(my_sequence)

Iterables
---------

To make an object iterable, you simply have to implement the __getitem__ method.

.. code-block:: python

    class T:
        def __getitem__(self, position):
            if position > 5:
                raise IndexError
            return position


iter()
------

How do you get the iterator object from an "iterable"?  The iter() function will make any iterable an iterator.  It first looks for the __iter__() method, and if none is found, uses get_item to create the iterator.  The ``iter()`` function:

.. code-block:: ipython

    In []: iter([2,3,4])
    Out[]: <listiterator at 0x101e01350>

    In []: iter("a string")
    Out[]: <iterator at 0x101e01090>

    In []: iter( ('a', 'tuple') )
    Out[]: <tupleiterator at 0x101e01710>


List as an Iterator
-------------------

.. code-block:: ipython

    In []: a_list = [1,2,3]

    In []: list_iter = iter(a_list)

    In []: next(list_iter)
    Out[]: 1

    In []: next(list_iter)
    Out[]: 2

    In []: next(list_iter)
    Out[]: 3

    In []: next(list_iter)
    --------------------------------------------------
    StopIteration     Traceback (most recent call last)
    <ipython-input-15-1a7db9b70878> in <module>()
    ----> 1 next(list_iter)
    StopIteration:

Use iterators when you can
--------------------------

Consider the example from the trigrams problem:

(http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/)

You have a list of words and you want to go through it, three at a time, and match up pairs with the following word.

The *non-pythonic* way to do that is to loop through the indices:

.. code-block:: python

    for i in range(len(words)-2):
        triple = words[i:i+3]

It works, and is fairly efficient, but what about:

.. code-block:: python

    for triple in zip(words[:-2], words[1:-1], words[2:-2]):

zip() returns an iterable --- it does not build up the whole list, so this is quite efficient.  However, we are still slicing: ([1:]), which produces a copy --- so we are creating three copies of the list --- not so good if memory is tight.  Note that they are shallow copies, so this is not terribly bad.  Nevertheless, we can do better.

The ``itertools`` module has a ``islice()`` (iterable slice) function.  It returns an iterator over a slice of a sequence --- so no more copies:

.. code-block:: python

    from itertools import islice

    triplets = zip(words, islice(words, 1, None), islice(words, 2, None))

    for triplet in triplets:
        print(triplet)

    ('this', 'that', 'the')
    ('that', 'the', 'other')
    ('the', 'other', 'and')
    ('other', 'and', 'one')
    ('and', 'one', 'more')

The Iterator Protocol
----------------------

The main thing that differentiates an iterator from an iterable (sequence) is that an iterator saves state.  An iterable must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

Usually returns the iterator object itself.

.. code-block:: python

    an_iterator.__next__()

Returns the next item from the container. If there are no further items it raises the ``StopIteration`` exception.

Making an Iterator
-------------------

A simple version of ``range()``

.. code-block:: python

    class IterateMe_1:
        def __init__(self, stop=5):
            self.current = 0
            self.stop = stop
        def __iter__(self):
            return self
        def __next__(self):
            if self.current < self.stop:
                self.current += 1
                return self.current
            else:
                raise StopIteration

What does for do?
-----------------

Now that we know the iterator protocol, we can write something like a for loop:

:download:`my_for.py <../examples/iterators_generators/my_for.py>`

.. code-block:: python

    def my_for(an_iterable, func):
        """
        Emulation of a for loop.

        func() will be called with each item in an_iterable
        """
        # equiv of "for i in l:"
        iterator = iter(an_iterable)
        while True:
            try:
                i = next(iterator)
            except StopIteration:
                break
            func(i)

Itertools
---------

``itertools``  is a collection of utilities that make it easy to build an iterator that iterates over sequences in common ways.

NOTE: iteratables are not *only* for ``for``.  They can be used with anything that expects an iterable:

``sum``, ``tuple``, ``sorted``, ``list``, ...

Is an iterator a type?
----------------------

Iterators are not a type. An "iterable" is anything that has an ``__iter__``
method that returns an iterator and/or has a ``__getitem__`` method that takes 0-based indexes.

An "iterator" is anything that conforms to the "iterator protocol":

 * Has a ``__next__()`` method that returns objects.
 * Raises ``StopIteration`` when their are no more objects to be returned.
 * Has a ``__iter__()`` method that returns an iterator --- usually itself.

Lots of common iterators are different types:

.. code-block:: ipython

    In []: type(iter(range(5)))
    Out[]: range_iterator

    In []: iter(list())
    Out[]: <list_iterator at 0x104437fd0>

    In []: type(iter(zip([],[])))
    Out[]: zip


Generators
==========

Generators give you an iterator object with no access to the underlying data ... if it even exists.

Conceptually iterators are about various ways to loop over data.  They can generate data on the fly.

Practically you can use either an iterator or a generator --- and a generator is a type of iterator.

Generators do some of the book-keeping for you and therefore involve simpler syntax.

yield
------

The ``yield`` keyword is a way to make a quickie generator with a function:

.. code-block:: python

    def a_generator_function(params):
        some_stuff
        yield something

Generator functions "yield" a value, rather than returning a value.  It *does* 'return' a value, but rather than ending execution of the function it preserves function state so that it can pick up where it left off.  In other words, state is preserved between yields.

A function with ``yield``  in it is a factory for a generator.  Each time you call it, you get a new generator:

.. code-block:: python

    gen_a = a_generator()
    gen_b = a_generator()

Each instance keeps its own state.

Really just a shorthand for an iterator class that does the book keeping for you.

To master yield, you must understand that when you call the function, the code you have written in the function body does not run.  The function
only returns the generator object.  The actual code in the function is run when next() is called on the generator itself.

An example: like ``range()``

.. code-block:: python

    def y_range(start, stop, step=1):
        i = start
        while i < stop:
            yield i
            i += step

Note:

.. code-block:: ipython

    In []: gen = y_range(2,6)
    In []: type(gen)
    Out[]: generator
    In []: dir(gen)
    Out[]:
    ...
     '__iter__',
    ...
     '__next__',


So a generator **is** an iterator.

:download:`yield_example.py <../examples/iterators_generators/yield_example.py>`

Generator Comprehensions
------------------------

yet another way to make a generator:

.. code-block:: python

    >>> [x * 2 for x in [1, 2, 3]]
    [2, 4, 6]
    >>> (x * 2 for x in [1, 2, 3])
    <generator object <genexpr> at 0x10911bf50>
    >>> for n in (x * 2 for x in [1, 2, 3]):
    ...   print n
    ... 2 4 6


More interesting if [1, 2, 3] is also a generator

Note that ``map`` and ``filter`` produce iterators.

Keep in mind --- if all you need to do with the results is loop over it -- use a generator expression rather than a list comprehension.

[Video: Generators]


****
Quiz
****

1. Lambda can do things that standard, named functions cannot.

   | True
   | False

2. Iterators and generators are more memory efficient than instantiated sequences such as lists.

   | True
   | False

3. Iterators and generators raise the StopIteration exception when they have no more values to emit.

   | True
   | False

4. Between subsequent calls generators pick up from where they left off by using this special keyword.

   | return
   | yield

5. Generators can create infinite series without using infinite computer memory.

   | True
   | False



*********************
Activity & Assignment
*********************


Comprehensions
==============

Ever since the anthem rockers started sweeping the Grammy Awards (circa 2013) popular music has been a frightening place for many of us.  Thus, each year, after the hoopla has died down, some of us cautiously venture out looking for new music.  The trouble is that actually listening to any of it could cause irreparable damage.  What are we to do?

Functional programming thrives in this environment.  First we'll need to find a dataset of current, popular music.  Then we'll need to analyze it.  Data sets of these types can be enormous; many times the size of the drives in professional-grade laptops.  Let's use Spotify's top 100 tracks from 2017 to get started.

Let's say we like music that you can dance too, but that isn't too loud.  Tricky to come by, perhaps.  Nonetheless, let's see what we can find.

For this research we are going to use a library that has become a cornerstone in Python's analytics stack, Pandas.  It is a powerful library, but we need touch only a few of its features to get started.  First, install Pandas into your virtualenvironment.

.. code-block:: bash

    $ pip install pandas

Bring up an interpreter and load the data.

.. code-block:: python3

    import pandas as pd
    music = pd.read_csv("featuresdf.csv")

Take a look around to get a sense of the general shape of the data.

.. code-block:: python3

    music.head()
    music.describe()

Now we are ready for the analytics.  This first one is a gimme.  We will use a comprehension to get danceability scores over 0.8.

.. code-block:: python3

    [x for x in music.danceability if x > 0.8]

Your job, now, is to get artists and song names for for tracks with danceability scores over 0.8 and loudness scores below -5.0.  In other words, quiet yet danceable tracks.  Also, these tracks should be sorted in descending order by danceability so that the most danceable tracks are up top.  You should be able to work your way there starting with the comprehension above.  And while you could use Pandas features along the way, you don't need to.  To accomplish the objective you do not need to know anything more about Pandas than what you can infer from the material herein.  Standard library functions that could come in handy include zip() and sorted().

Submit your code and the top five tracks to complete the assignment.

Then, put on your dancing shoes, get out to Spotify or Youtube, and let's get this party started.  Stay safe.  It's a scary pop world out there.


Iterators & Iteratables
=======================

:download:`iterator_1.py <../examples/iterators_generators/iterator_1.py>`

* Extend (``iterator_1.py`` ) to be more like ``range()`` -- add three input parameters: ``iterator_2(start, stop, step=1)``

* What happens if you break from a loop and try to pick it up again:

.. code-block:: python

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)

.. code-block:: python

    for i in it:
        print(i)

* Does ``range()``  behave the same?

  - make yours match ``range()``

  - is range an iterator or an iteratable?


Generators
==========

Write a few generators:

* Sum of integers
* Doubler
* Fibonacci sequence
* Prime numbers

Test code in:

:download:`test_generator.py <../examples/iterators_generators/test_generator.py>`

Descriptions:

Sum of the integers:
  keep adding the next integer

  0 + 1 + 2 + 3 + 4 + 5 + ...

  so the sequence is:

  0, 1, 3, 6, 10, 15 .....

Doubler:
  Each value is double the previous value:

  1, 2, 4, 8, 16, 32,

Fibonacci sequence:
  The Fibonacci sequence as a generator:

  f(n) = f(n-1) + f(n-2)

  1, 1, 2, 3, 5, 8, 13, 21, 34...

Prime numbers:
  Generate the prime numbers (numbers only divisible by them self and 1):

  2, 3, 5, 7, 11, 13, 17, 19, 23...

Others to try:
  Try x^2, x^3, counting by threes, x^e, counting by minus seven, ...


**********
Assignment
**********

Generators
==========

Write some generators:

(test code in ``test_generator.py``)

Sum of integers
---------------

keep adding the next integer

0 + 1 + 2 + 3 + 4 + 5 + ...

so the sequence is:

0, 1, 3, 6, 10, 15 .....

Doubler
-------

Each value is double the previous value:

1, 2, 4, 8, 16, 32,

Fibonacci sequence
------------------

The Fibonacci sequence as a generator:

f(n) = f(n-1) + f(n-2)

1, 1, 2, 3, 5, 8, 13, 21, 34...

Prime numbers
-------------

Generate the prime numbers (numbers only divisible by them self and 1):

2, 3, 5, 7, 11, 13, 17, 19, 23...

Others to try:
--------------

Try x^2, x^3, counting by threes, x^e, counting by minus seven, ...


******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
