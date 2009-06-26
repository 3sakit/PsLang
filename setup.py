#!/usr/bin/env python
from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["pslang/*"]

setup(name = "pslang",
    version = "0.0.1",
    description = "A Toolkit language.",
    author = "Mike 'Fuzzy' Partin",
    author_email = "fuzzy@3hci.net",
    url = "http://www.3hci.net",
    packages = ['pslang'],
    package_data = {'pslang' : files },
    #'runner' is in the root.
    scripts = ["bin/pslang"],
    long_description = """
    A simple functional programming language, made the for the sole express purpose,
    of learning how to do it.
    """ 
) 
