'''
Created on 1 Mar 2017
@author: liga
'''
from builtins import int
errorMessage = "Input details were invalid"


def parse_line(obj, size):
    """function to extract coordinates and command from a line"""
    def marginCheck(rowFrom, columnFrom, rowTo, columnTo,  size):
        """Function to check m=out of range values and convert to valid values """
        if columnTo >= size:
            columnTo = size - 1
        if size <= rowTo:
            rowTo = size - 1
        if rowFrom < 0:
            rowFrom = 0
        if 0 > columnFrom:
            columnFrom = 0
        return rowFrom, columnFrom, rowTo, columnTo
    try:
        if obj[0] == "turn" and (obj[1] == "on" or obj[1] == "off"):
            rowFrom = int(obj[2])
            columnFrom = int(obj[3])
            rowTo = int(obj[5])
            columnTo = int(obj[6])
            rowFrom, columnFrom, rowTo, columnTo = marginCheck(
                rowFrom, columnFrom, rowTo, columnTo, size)
            if obj[1] == "off":
                cmd = "turn off"
                return rowFrom, rowTo + 1, columnFrom, columnTo + 1, cmd
            elif obj[1] == "on":
                cmd = "turn on"
                return rowFrom, rowTo + 1, columnFrom, columnTo + 1, cmd
            else:
                print("Parse_line error: ", errorMessage)
                return False

        elif obj[0] == "switch":
            rowFrom = int(obj[1])
            columnFrom = int(obj[2])
            rowTo = int(obj[4])
            columnTo = int(obj[5])
            rowFrom, columnFrom, rowTo, columnTo = marginCheck(
                rowFrom, columnFrom, rowTo, columnTo, size)
            cmd = "switch"
            return rowFrom, rowTo + 1, columnFrom, columnTo + 1, cmd
        else:
            print("Parse_line error: ", errorMessage)
            return False
    except IndexError:
        return False


def instructions(obj, matrix, size):
    """Function to execute commands from data line"""
    (rowFrom, rowTo, columnFrom, columnTo, cmd) = parse_line(obj, size)
    print(cmd, rowFrom, columnFrom, "through", rowTo, columnTo)
    if cmd == "turn on":
        return switchOn(rowFrom, rowTo, columnFrom, columnTo, matrix)
    elif cmd == "turn off":
        return switchOff(rowFrom, rowTo, columnFrom, columnTo, matrix)
    elif cmd == "switch":
        return toggle(rowFrom, rowTo, columnFrom, columnTo, matrix)
    else:
        print(errorMessage)


def testValues(obj, size):
    """Function to test if input values are valid, returns boolean values """
    x = parse_line(obj, size)
    if x:
        (rowFrom, rowTo, columnFrom, columnTo, cmd) = x
        if (rowFrom <= rowTo and columnFrom <= columnTo and columnFrom >= 0 and rowFrom >= 0):
            return True
    else:
        print("Test_values error: ", errorMessage)
        return False


def switchOn(rowFrom, rowTo, columnFrom, columnTo, matrix):
    """Function to switch LEDs on, returns updated matrix"""
    for j in range(columnFrom, columnTo):
        for i in range(rowFrom, rowTo):
            matrix[j][i] = 1
    return matrix


def switchOff(rowFrom, rowTo, columnFrom, columnTo, matrix):
    """Function to switch LEDs off, returns updates matrix"""
    for j in range(columnFrom, columnTo):
        for i in range(rowFrom, rowTo):
            matrix[j][i] = 0
    return matrix


def toggle(rowFrom, rowTo, columnFrom, columnTo, matrix):
    """Function to toggle LEDs on off, returns updated matrix"""
    for j in range(columnFrom, columnTo):
        for i in range(rowFrom, rowTo):
            if (matrix[j][i] == 1):
                matrix[j][i] = 0
            elif(matrix[j][i] == 0):
                matrix[j][i] = 1
    return matrix


def countLed(matrix, size):
    """Function to calculate number of LEDs ON, returns integer value"""
    count = 0
    for j in range(size):
        for i in range(size):
            if (matrix[j][i] == 1):
                count += 1
    print("Number of LEDs on is:", count)
    return count


def Matrix(size):
    """Function to create multidimensional array of LED lights, initially all LEDs are off.
     0 is assigned for LED which is off, 1 is assigned for LED which is on.
     Function also checks if size input is valid which is size>0"""
    if size > 0:
        matrix = [[0 for x in range(size)] for x in range(size)]
        return matrix
    else:
        return False
