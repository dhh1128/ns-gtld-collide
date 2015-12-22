#! /usr/bin/python

import os, sys


def uniquify(items):
    d = {}
    for x in items:
        d[x] = 1
    return d.keys()


def expand(possibly_dotted):
    return possibly_dotted.split('.')


def expand_all(items):
    expanded = []
    for item in items:
        x = expand(item)
        for xx in x:
            expanded.append(xx)
    return expanded


def xref(fname1, fname2):
    with open(fname1, 'r') as f:
        set1 = uniquify(expand_all([x.strip().lower() for x in f.readlines()]))
    with open(fname2, 'r') as f:
        set2 = uniquify(expand_all([x.strip().lower() for x in f.readlines()]))
    for item in set1:
        if item in set2:
            print(item)
    

if __name__ == '__main__':
    xref(sys.argv[1], sys.argv[2])
