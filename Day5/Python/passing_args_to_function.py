#!/usr/bin/python

def add ( firstNumber, secondNumber ): 
    return firstNumber + secondNumber

def my_main():
    x = input ('Enter the first number : ')
    y = input ('Enter the second number : ')

    result = add( x, y )

    print('The sum of ' + str(x) + ' and ' + str(y) + ' is ' + str(result))

if __name__ == "__main__":
    my_main()
