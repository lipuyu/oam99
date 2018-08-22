#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: py


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly.")


class Spam(metaclass=NoInstances):
    def __init__(self):
        print('Create Spam')

Spam()
Spam()
Spam()
