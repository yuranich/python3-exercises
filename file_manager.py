'''
Created on Mar 22, 2014

@author: yuranich
'''

import os

def execute_with_one_arg(command):
    if command[0] == "mkdir":
        os.mkdir(command[1])
        print("execute mkdir")
    elif command[0] == "mkfile":
        os.mknod(command[1])
        print("execute mkfile")
    elif command[0] == "rmfile":
        os.remove(os.path.abspath(command[1]))
        print("execute rmfile")
    elif command[0] == "rmdir":
        os.rmdir(os.path.abspath(command[1]))
        print("execute rmdir")
    else :
        print("unknown command!")
        
        
def execute_with_two_args(command):
    print("it's very boring task...")

print("input your command:")
command = input()
args = command.split(" ")
if len(args) < 2 or len(args) > 3:
    print("invalid number of arguments")
    print("usage: command arg1 [arg2]")  
    
if len(args) == 2:
    execute_with_one_arg(args)
else :
    execute_with_two_args(args)
