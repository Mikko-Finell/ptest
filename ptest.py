#!/usr/bin/python3

from sys import exit

class Ptest(object):

    def __init__(self, module_name):
        self.module_name = module_name
        self.passed = 0
        self.failed = 0

        print('\nRunning tests for module "', module_name, '"', sep='')

    def report(self, test_name, test_result):
        if test_result not in (True, False):
            print('Invalid report argument for test "', test_name, '"', sep='')
            exit(1)

        NORMAL  = '\x1B[0m'
        RED     = '\x1B[31m'
        GREEN   = '\x1B[32m'

        if test_result:
            self.passed += 1
            print('[', GREEN, 'PASSED', NORMAL, '] ', test_name, sep='')
        else:
            self.failed += 1
            print('[', RED, 'FAILED', NORMAL, '] ', test_name, sep='')

    def print_statistics(self):
        test_count = self.passed + self.failed
        if test_count == 0:
            print('No tests yet...')
            return
        pass_rate = 0
        if self.passed != 0:
            pass_rate = round(float(self.passed) / float(test_count), 3) * 100
        print('Passed: ', self.passed, '/', test_count,
                ' (', pass_rate, '%)', sep='', end='\n\n')

