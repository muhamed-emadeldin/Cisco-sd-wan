#! /usr/bin/env python

import argparse
from pyats.topology.loader import load
from pyats.utils.exceptions import SchemaTypeError

def __parse_command__(device, command):
    print(device, command)

if __name__ == '__main__':
    #-->load pyats testbed file
    print('Hello Inventory Network Script')

    parse = argparse.ArgumentParser(description='Generate network inventory')

    parse.add_argument('testbed', type=str, help='Testbed file')

    args = parse.parse_args()
    
    #-->Create pyats testbed object
    testbed = load(args.testbed)
    print(f"Connecting to all devices in testbed {testbed.name}")
    try:
        testbed.connect(log_stdout=False)
    except SchemaTypeError:
        print(testbed.devices)


    
    for name in testbed.devices: 
        print(f"Disconnectingfrom device {name}")
        __parse_command__(testbed.devices[name], "show version")
        testbed.devices[name].disconnect()



    

