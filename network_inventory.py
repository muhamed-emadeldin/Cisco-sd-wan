#! /usr/bin/env python

import argparse
from pyats.topology.loader import load

if __name__ == '__main__':
    #-->load pyats testbed file
    print('Hello Inventory Network Script')

    parse = argparse.ArgumentParser(description='Generate network inventory')

    parse.add_argument('testbed', type=str, help='Testbed file')

    args = parse.parse_args()
    
    #-->Create pyats testbed object
    testbed = load(args.testbed)

    testbed.connect()


