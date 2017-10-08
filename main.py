#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naive import Naive
from RabinKarp import RabinKarp
import pyhash

def main():
    T = "abcxaabcdy"
    P = ["a", "c", "y"]
    rabinKarp = RabinKarp()
    hasher = pyhash.murmur1_32()
    rabinKarp.setHasher(hasher)
    rabinKarp.set_n_patterns(P)
    rabinKarp.set_text(T)
    matchs = rabinKarp.find_multiple_match()
    print matchs

main()
