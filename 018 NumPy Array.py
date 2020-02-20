#018 NumPy Array :-

'''
one D   -> []
two D   -> [[]]
three D -> [[[]]]
'''
my_list = [1,2,3]

print(my_list)
#[1, 2, 3]

print(type(my_list))
#<class 'list'>

import numpy as np
arr = np.array(my_list)

print(arr)
#[1 2 3]

print(type)
#<class 'type'>

#*************

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(my_matrix)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(type(my_matrix))
#<class 'list'>

my_matrix_arr = np.array(my_matrix)

print(my_matrix_arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

print(type(my_matrix_arr))
#<class 'numpy.ndarray'>

arr_range = np.arange(0,10)

print(arr_range)
#[0 1 2 3 4 5 6 7 8 9]

arr_range_subset = np.arange(0,10,2)

print(arr_range_subset)
#[0 2 4 6 8]

#**************Generating an Array of all Zeros:-

arr_zeros = np.zeros(3)
print(arr_zeros)
#[0. 0. 0.]

arr_2D = np.zeros((2,3))
print(arr_2D)
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''

arr_1D = np.ones(6)
print(arr_1D)
#[1. 1. 1. 1. 1. 1.]

arr_2D_ones = np.ones((2,2))
print(arr_2D_ones)
'''
[[1. 1.]
 [1. 1.]]
'''

#*******************linspace

#linspace(start , stop , evenly space point)

#Third Argument :-  NUmber of points you want.

linspae_arr = np.linspace(0,10,3)
#between 0 to 10 , 3 evenly space points

print(linspae_arr)
#[ 0.  5. 10.]

linspae_arr_another = np.linspace(0,10,12)
print(linspae_arr_another)
'''
[ 0.          0.90909091  1.81818182  2.72727273  3.63636364  4.54545455
  5.45454545  6.36363636  7.27272727  8.18181818  9.09090909 10.        ]
'''

#****************Identity Matrix****************

Iden_Mat = np.eye(4)

print(Iden_Mat)
'''
Ountput:- Will be a 4*4 identity Matrix
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''

#************************Create Array of random numbers**********

rand_array = np.random.rand(5)

print(rand_array)
#[0.073011   0.35436969 0.72476755 0.75223365 0.0692636 ]

#2 D Random Numbers Matrix

rand_array_2D = np.random.rand(3,3)
print(rand_array_2D)
'''
[[0.25336486 0.05801956 0.09694529]
 [0.48460495 0.80074545 0.09981986]
 [0.74957578 0.89116841 0.64404476]]
'''

#Randint

rand_int = np.random.randint(1,100)
print(rand_int)
#25

rand_int_size = np.random.randint(1,100,10)
#size is defined as 10
print(rand_int_size)
#[39 36 25 82 77 66 96 80 60 78]

#**********************reshape****************

arr1 = np.arange(25)

print(arr1)
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]

rand_array = np.random.randint(1,100,5)
print(rand_array)
#[90 36 28 50 55]

arr1_reshape = arr1.reshape(5,5)

print(arr1_reshape)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''

'''
NOTE:- IF all matrix will not fill up , it will through an error.

EG:- reshape(5,5) :- must have 25 element on driver array

reshape(5,6) :- must have 30 element , otherwise it will through an error.
'''

print(arr1_reshape.shape)
#(5, 5) :- It has a shape of (5,5) and two dimentional array.

#*************Max and Min value***************

max_value = rand_array.max()
print(max_value)
#above will give max number in rand_array (which is randomly generated)

#TO get index location of max value:-
print(rand_array.argmax())
#4 :- it's a index location

min_value = rand_array.min()
print(min_value)
#12 :- #above will give min number in rand_array (which is randomly generated)

print(rand_array.argmin())
#1 :- :- it's a index location

print(rand_array.shape)
#(5,) :- It is showing rand_array has 5 element and one dimentional array

#*******************datatype******************

print(rand_array.dtype)
#int32