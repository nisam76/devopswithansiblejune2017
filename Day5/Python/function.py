#!/usr/bin/python

def sayHello():
    greet_msg = "Hello Python!"

    print ( greet_msg )
    a = 100
    print ('Value of a is ' + str(a) )
    print ('Value of a is ', a )

    print ('Type of a is' , type(a) )
    print ('Type of greet_msg is', type(greet_msg) )

def main():
    sayHello()

main()
