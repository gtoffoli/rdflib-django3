#! /usr/bin/env python3
"""
Unittests and doctests for the rdflib_django app.
"""
import os
import sys
import doctest
import unittest
import django
from django.test.utils import get_runner
from django.conf import settings
up = os.path.dirname
rp = os.path.realpath
sys.path.insert(0, up(up(rp(__file__))))
import test.testsettings  # noqa: E402
settings.configure(default_settings=test.testsettings)
django.setup()

import rdflib_django  # noqa: E402
from rdflib_django import store  # noqa: E402

from test import (
    test_store, test_rdflib, test_seq, test_namespaces
)  # noqa: E402


def suite():
    """
    Generate the test suite.
    """
    s = unittest.TestSuite()
    s.addTest(doctest.DocTestSuite(rdflib_django))
    s.addTest(doctest.DocTestSuite(store))
    s.addTest(unittest.findTestCases(test_store))
    s.addTest(unittest.findTestCases(test_rdflib))
    s.addTest(unittest.findTestCases(test_seq))
    s.addTest(unittest.findTestCases(test_namespaces))
    return s


test_labels = [
    "test.test_store", "test.test_rdflib",
    "test.test_seq", "test.test_namespaces"
]

if __name__ == '__main__':

    test_runner = unittest.TextTestRunner()
    failures = test_runner.run(suite())

    if failures:
        sys.exit(1)
