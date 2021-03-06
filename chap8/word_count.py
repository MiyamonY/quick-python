# /usr/bin/env python
# -*- coding:utf-8 -*-
"""Reads a file and returns the number of line, words, and characters -
similar to the UNIX wc utility"""

infile = open('word_count.tst')

lines = infile.read().split('\n')

line_count = len(lines)

word_count, char_count = 0, 0

for line in lines:
    words = line.split()
    word_count += len(words)
    char_count += len(line)


print("File has {0} lines, {1} words,"
      "{2} characters".format(line_count, word_count, char_count) )
