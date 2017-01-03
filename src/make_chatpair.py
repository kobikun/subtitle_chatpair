#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
description of code
__author__ = 'byeongil.ko@gmail.com'
__copyright__ = 'Copyright (C) 2016-, kobi. All rights reserved.'
"""

###########
# imports #
###########
import argparse
import os
import re
import sys
import logging

###########
# options #
###########

#############
# functions #
#############
def to_unicode(text):
    if isinstance(text, unicode) :
        return text
    return text.decode('utf-8')

def to_utf8(text):
    if isinstance(text, str):
        return text
    return text.encode('utf-8')

def make_pair(fin, fout):
    prev = ""
    for text in fin:
        text = text.strip()
        if prev !="":
            yield (prev, text)
        prev = text

########
# main #
########
'''
main
'''
def main(fin, fout):
    pairs = make_pair(fin,fout)
    for pair in pairs:
        print >> fout, "\t".join(pair)

if __name__ == '__main__':
    _PARSER = argparse.ArgumentParser(description = 'Test Python Code')
    _PARSER.add_argument('--input', type=file, default = sys.stdin, help='system input')
    _PARSER.add_argument('--output', type=argparse.FileType('w'), default = sys.stdout, help='system output')
    _PARSER.add_argument('--verbose', help='verbose', action='store_true')
    _ARGS = _PARSER.parse_args()
    if _ARGS.verbose == True:
        logging.basicConfig(level= logging.DEBUG
            , format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')
    main(_ARGS.input, _ARGS.output)
