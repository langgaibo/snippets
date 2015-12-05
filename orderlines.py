# coding: utf8
# 朗盖博 2015

# todo - make a class for this

from sys import exit, argv

# take args and open the file
this_script, filename = argv

# file to string, close file
the_file = open(filename, 'r')
block = the_file.read()
the_file.close()

# split dat
to_sort = block.splitlines()

# sort dat, ignoring case
to_sort.sort(key=lambda s: s.lower())

# output
for item in to_sort:
    print item

exit(0)
