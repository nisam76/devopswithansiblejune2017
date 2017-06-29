#!/usr/bin/python

class MyClass: 
    def __init__(self):
        self.x = 0
        self.y = 0
        print('MyClass constructor')

    def __readInputs(self):
        self.x = input ('Enter the first value :')
        self.y = input ('Enter the second value :')

    def printValues(self):
        print('Value of x is ', self.x )
        print('Value of y is ', self.y )

    def add(self):
        self.__readInputs()
        result = self.x + self.y 
        return result

def main():

    instance1 = MyClass()
    instance1.__readInputs()
    instance1.printValues()
    print ( 'Instance 1 => result is ' + str ( instance1.add( ) ) )

    instance2 = MyClass()
    #instance2.__readInputs()
    instance2.printValues()
    print ( 'Instance 2 => result is ' + str ( instance2.add( ) ) )

if __name__ == "__main__":
    main()
