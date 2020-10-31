import math
print('**HOW TO PERFORM CALCULATIONS**:\n' +
        '\n\tAdd: a + b' +
        '\n\tSubtract: a - b' +
        '\n\tDivide: a / b' +
        '\n\tDivide - Rounded: a + b' +
        '\n\tMultiply: a * b' +
        '\n\tExponents: a ** b' +
        '\n\tModulo: a % b')

calc = input('\nCalculate: ') #Get equation from user as input and store it in a variable.


def get_int1(): #Get first integer.
    for x in range(len(calc)):
        if calc[x] == ' ':
            num1 = calc[0:x]
            return num1
            break


def get_int2(): # Get the second integer.
    for x in range(len(calc)):
        if calc[x] == '+': # For loop that iterates over the input of the user as + a string and when it finds an operation it adds 2 to it to
                            #find the second value.
            num2 = calc[x+2:len(calc)]
            return num2
            break
        elif calc[x] == '-':
            num2 = calc[x+2:len(calc)]
            return num2
            break
        elif calc[x] == '/':
            num2 = calc[x+2:len(calc)]
            return num2
            break
        elif calc[x] == '//':
            num2 = calc[x+3:len(calc)]
            return num2
            break
        elif calc[x] == '*':
            num2 = calc[x+2:len(calc)]
            return num2
            break
        elif calc[x] == '**':
            num2 = calc[x+3:len(calc)]
            return num2
            break
        elif calc[x] == '%':
            num2 = calc[x+2:len(calc)]
            return num2
            break


def get_op(): #Iterates of equation to find the operation then stores it in a variable.
    for x in range(len(calc)):
        if calc[x] == '+':
            op = calc[x]
            return op
            break
        elif calc[x] == '-':
            op = calc[x]
            return op
            break
        elif calc[x] == '/':
            op = calc[x]
            if calc[x+1] == '/':
                op = '//'
                return op
                break
            return op
            break
        elif calc[x] == '*':
            op = calc[x]
            if calc[x+1] == '*':
                op = '**'
                return op
                break
            return op
            break
        elif calc[x] == '%':
            op = calc[x]
            return op
            break


try:
    num1 = int(get_int1())
    num2 = int(get_int2())
    op = get_op()
except:
    print('This is not a valid calculation.')


def add(num1, num2): #Function for Addition.
    return num1 + num2


def sub(num1, num2): #Function for Subtraction.
    return num1 - num2


def mult(num1, num2): #Function for Multiplication.
    return num1 * num2


def exp(num1, num2): #Function for Exponents.
    return num1 ** num2


def div(num1, num2): #Function for Division.
    return num1 / num2


def div2(num1, num2): #Function for Rounded Division.
    return num1 // num2


def mod(num1, num2): #Function for Modulo.
    return num1 % num2


def answer(a): # Prints answer
    print('Answer: ' + str(a) + '\n')


def calculate(op): #If the 'op' variable is a certain operation it will perform the calculation with the two number equations.
    if op == '+':
        answer(add(num1, num2))
    elif op == '-':
        answer(sub(num1, num2))
    elif op == '*':
        answer(mult(num1, num2))
    elif op == '**':
        answer(exp(num1, num2))
    elif op == '/':
        answer(div(num1, num2))
    elif op == '//':
        answer(div2(num1, num2))
    elif op == '%':
        answer(mod(num1, num2))


if __name__ == '__main__':
    calculate(get_op())
