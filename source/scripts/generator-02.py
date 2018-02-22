# Generator Tutorial
# rriehle February 2018

def my_first_generator(a):
    for i in a:
        yield i

my_super_generagor = my_first_generator("supercalifragilisticexpalidiocious")

# Let's spin this out a little.
next(my_super_generagor)
next(my_super_generagor)
next(my_super_generagor)
next(my_super_generagor)
next(my_super_generagor)


# Notice that we've almost accidently made a general purpose generator factory.

my_number_generator = my_first_generator([55, 44, 33, 22, 11])
next(my_number_generator)
next(my_number_generator)
next(my_number_generator)
next(my_number_generator)
next(my_number_generator)
next(my_number_generator)


# Let's use a generator in a way that lets it shine: infinite series.

def odd_forever(i=0):
    while True:
        if i % 2:
            yield i
        i += 1

my_odds = odd_forever(999999)
next(my_odds)
next(my_odds)
next(my_odds)
next(my_odds)
next(my_odds)
next(my_odds)
next(my_odds)

# Note that we need not put the yield at the end of the function; it could go anywhere.
# When the function is called again it picks up immediately after the yield.
