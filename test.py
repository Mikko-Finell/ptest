#!/usr/bin/python3

import ptest

tests = ptest.Ptest('test framework')
tests.report('bad test', 123)
tests.report('test pass', True)
tests.report('test fail', False)
tests.report('test pass again', True)
tests.print_statistics()
