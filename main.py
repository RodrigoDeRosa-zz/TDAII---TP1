#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naive import Naive

def main():
    T = "abcxaabcdy"
    P = "abcxaabcdya"
    naive = Naive()
    naive.set_pattern(P)
    naive.set_text(T)
    matchs = naive.find_match()
    print matchs

main()
