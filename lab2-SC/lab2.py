import unittest
import math
from random import randint
import numpy as np

"""function to populate single matrix using user input"""
def populate(rows,cols):
    matrix = [[0 for x in range(cols)] for j in range(rows)]
    for x in range(0,int(rows)):
        for y in range(0,int(cols)):
            matrix[x][y] = int(raw_input("Enter digit: "))
    return matrix
"""populate single matrix randomly"""
def populate_random(rows,cols):
    matrix = [[0 for x in range(cols)] for j in range(rows)]
    for x in range(0,int(rows)):
        for y in range(0,int(cols)):
            matrix[x][y] = randint(0,100)
    return matrix

"""print matrix"""
def print_matrix(A):
    for x in A:
        print x

"""Multiply iteratively"""
def iterative(A,B):
    if(len(A[0])!=len(B)):
        print "Cannot multiply; Dimensions don't match"
        return
    else:
        C = [[0 for x in range(len(B[0]))] for j in range(len(A))]
        for x in range(len(A)):
            for y in range(len(B[0])):
                for z in range(len(B)):
                    C[x][y] += A[x][z] * B[z][y]
        return C

"""get user input"""
def get_input():
    row1 = int(raw_input("Please enter no of rows of first matrix: "))
    col1 = int(raw_input("Please enter no of columns of first matrix: "))
    row2 = int(raw_input("Please enter no of rows of second matrix: "))
    col2 = int(raw_input("Please enter no of columns of second matrix: "))
    return row1,col1,row2,col2

"""add two matrices"""
def add(A,B):
    C = [[0 for x in range(len(A))] for j in range(len(B))]
    for x in range(0,len(A)):
        for y in range(0,len(B)):
            C[x][y] = A[x][y] + B[x][y]
    return C

"""subtract two matrices"""
def subtract(A,B):
    C = [[0 for x in range(len(A))] for j in range(len(B))]
    for x in range(0,len(A)):
        for y in range(0,len(B)):
            C[x][y] = A[x][y] - B[x][y]
    return C

"""strassen algorithm to solve matrices"""
def strassen_recursive(A,B,n):
    if (n<=len(A)):
        return iterative(A,B)
    else:
        half_size = len(A)/2

        #get new matrices

        a1 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        a2 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        a3 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        a4 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        b1 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        b2 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        b3 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        b4 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        c1 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        c2 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        c3 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]
        c4 = [[0 for x in range(0, half_size)] for j in range(0,half_size)]


        #split original matrices to new ones

        for x in range(0,half_size):
            for j in range(0, half_size):
                a1[x][y]=A[x][y]
                a2[x][y]=A[x][y+half_size]
                a3[x][y]=A[x+half_size][y]
                a4[x][y]=A[x+half_size][y+half_size]
                b1[x][y]=B[x][y]
                b2[x][y]=B[x][y+half_size]
                b3[x][y]=B[x+half_size][y]
                b4[x][y]=B[x+half_size][y+half_size]

        p1 = strassen(add(a1,a4),add(b1,b4),half_size/2)
        p2 = strassen(add(a3,a4), b1,half_size/2)
        p3 = strassen(a1,subtract(b2,b4),half_size/2)
        p4 = strassen(a4,subtract(b3-b1),half_size/2)
        p5 = strassen(add(a1,a2), b4,half_size/2)
        p6 = strassen(subtract(a3,a1),add(b1,b2),half_size/2)
        p7 = strassen(subtract(a2,a4), add(b3,b4),half_size/2)

        # c11 = p1 + p4 - p5 + p7
        # c12 = p3 + p5
        # c21 = p2 + p4
        # c22 = p1 + p3 - p2 + p6
        c1 = add(subtract(add(p1,p4),p5),p7)
        c2 = add(p3,p5)
        c3 = add(p2,p4)
        c4 = add(subtract(add(p1,p3),p2),p6)

        #merge result
        result = [[0 for x in range(0, len(c1)*2)] for j in range(0,len(c1)*2)]
        lim = len(c1)
        for x in range(0,lim):
            for j in range(0, lim):
                result[x][y]=A[x][y]
                result[x+lim][y]=A[x][y]
                result[x][y+lim]=A[x][y]
                result[x+lim][y+lim]=A[x][y]
        return result

"""Pad matrices to nearest power of two"""
def padding(a):
     z = math.log(len(a),2)
     if(z%1.0 != 0.0):
          y = math.floor(z) + 1
          limit = pow(2,y)
          a = np.array(a)
          h,w = a.shape
          result = np.zeros((int(limit),int(limit)))
          result[:h,:w] = a
          a = result

     return a

"""Padd if needed and then call strassen recursively"""
def strassen(a,b,q):
    if(len(a[0])!=len(b)):
        print "Cannot multiply; Dimensions don't match"
        return
    elif(len(a[0])!=len(a[1])):
        print "matrix not square"
        return
    elif(len(b[1])!=len(b[0])):
        print "matrix not square"
        return
    else:
        a = padding(a)
        b = padding (b)
        return strassen_recursive(a,b,q)

"""Randomly fill matrices"""
def start_random_population(row1,col1,row2,col2):

    matrix_first = populate_random(row1,col1)

    matrix_second = populate_random(row2,col2)
    return matrix_first, matrix_second

"""fill matrices using user input"""
def start_population(row1,col1,row2,col2):

    matrix_first = populate(row1,col1)

    matrix_second = populate(row2,col2)
    return matrix_first, matrix_second
