#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naive import Naive
from RabinKarp import RabinKarp
import pyhash

def main():
    T = "abcxaabcdy"
    P = "a"
    rabinKarp = RabinKarp()
    hasher = pyhash.murmur1_32()
    rabinKarp.setHasher(hasher)
    rabinKarp.set_pattern(P)
    rabinKarp.set_text(T)
    matchs = rabinKarp.find_match()
    print matchs

main()
