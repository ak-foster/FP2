.. Lesson Plan documentation master file, created by
   sphinx-quickstart on Sun Jan 28 19:33:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========================
Functional Programming 2
========================

.. toctree::
   :maxdepth: 3
   :caption: Contents:


************
Introduction
************

[1-3 paragraphs introducing topic(s)]


Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

* Use the lambda special form to define and anonymous function.
*


New Words or Concepts
=====================

* Comprehension
* Anonymous function
* Lambda
* Iterator
* iterable
* Generator


Required Reading
================



Optional Reading
================

* Lott, S. (2015) Chapter 5. Higher-order Functions. Using Python lambda forms. In Functional Python Programming.
* Lott, S. (2015) Chapter 3. Functions, Iterators, and Generators. In Functional Python Programming.


*******
Content
*******


Comprehensions
==============



Lambda
======

The Lambda special form is Python's syntax for creating an unnamed function, i.e., a function without a name.  This is its general form:

```
    lambda arguments: expression

```

For example, here is a lambda form which adds one to its argument:

.. .. code-block:: python3

    lambda x: x + 1

Here is a lambda that adds its two arguments together:

.. .. code-block:: python3

    lambda x, y: x + y

Now unlike most code snippets, if you were to type these examples into your favorite python interpreter by themselves they would not accomplish much.

.. .. code-block:: ipython3

    In [1]: lambda x, y: x + y
    Out[1]: <function __main__.<lambda>>

.. .. code-block:: python3

    >>> lambda x, y: x + y
    <function <lambda> at 0x104f61e18>




What use is Lambda?
-------------------

According to Python's creator, not much.

"About 12 years ago, Python aquired lambda, reduce(), filter() and map(), courtesy of (I believe) a Lisp hacker who missed them and submitted working patches. But, despite of the PR value, I think these features should be cut from Python 3000.

Why drop lambda? Most Python users are unfamiliar with Lisp or Scheme, so the name is confusing; also, there is a widespread misunderstanding that lambda can do things that a nested function can't -- I still recall Laura Creighton's Aha!-erlebnis after I showed her there was no difference! Even with a better name, I think having the two choices side-by-side just requires programmers to think about making a choice that's irrelevant for their program; not having the choice streamlines the thought process. Also, once map(), filter() and reduce() are gone, there aren't a whole lot of places where you really need to write very short local functions; Tkinter callbacks come to mind, but I find that more often than not the callbacks should be methods of some state-carrying object anyway (the exception being toy programs).

Update: lambda, filter and map will stay (the latter two with small changes, returning iterators instead of lists). Only reduce will be removed from the 3.0 standard library. You can import it from functools. "

 -- Guido van Rossum
 -- http://www.artima.com/weblogs/viewpost.jsp?thread=98196

Why would we teach the Lambda special form if even if Python's creator has a low opinion of it?

You need to understand it, because you are going to see it in the wild.

As to whether you decide to propogate its use, we leave that to you.


Iterators and Iterables
=======================



Generators
==========



****
Quiz
****



********
Activity
********

Comprehensions and Lambdas
==========================


Iterators & Iteratables
=======================

Write an Iterable that

Generators
==========



**********
Assignment
**********



******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
