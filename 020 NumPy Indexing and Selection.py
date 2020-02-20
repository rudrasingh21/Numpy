#20. Numpy Array Indexing

import numpy as np

arr = np.arange(10,20)

print(arr)
#[10 11 12 13 14 15 16 17 18 19]

#***************Getting value using Index

print(arr[8])
#18 :- It's value at Index 8

#**************Getting value in Range

print(arr[0:4])
#[10 11 12 13]
#It gives value from index 0 to index 3

print(arr[1:4])
#[11 12 13]
#It gives value from index 1 to index 3

print(arr[:5])
#[10 11 12 13 14]
#It gives value from starting index i.e. 0 to index 4

print(arr[5:])
#[15 16 17 18 19]

#*******************Broadcast a value************

arr[0:5]=100

#It fills 100 at index 0 , 1 , 2 , 3 , 4 and print other array values

print(arr)
#[100 100 100 100 100  15  16  17  18  19]

#Reset the array

arr = np.arange(0,10)

print(arr)
#[0 1 2 3 4 5 6 7 8 9]

#***********************Slicing of Array***************

slice_of_arr = arr[0:6]
print(slice_of_arr)
#[0 1 2 3 4 5]

slice_of_arr[:] = 99
print(slice_of_arr)
#[99 99 99 99 99 99]

print(arr)
#[99 99 99 99 99 99  6  7  8  9]

'''
IMP NOTE:- 

We can understand the main array has been changed . 

So , data does not copy , it gives you just a view of original array.
i.e. -> It is not a copy , it is just a reference of original Array.

This avoide memory issues of very large array.
'''

#***********To get a copy of original Array************

#Using copy method

arr_copy = arr.copy()

print(arr_copy)
#[99 99 99 99 99 99  6  7  8  9]

arr_copy[:] = 100

print(arr_copy)
#[100 100 100 100 100 100 100 100 100 100]

print(arr)
#[99 99 99 99 99 99  6  7  8  9]

#**************************** INDEXING an Array*****************

#indexing 2 D Array:-

import numpy as np

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

print(arr_2d)

'''
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
'''

print(arr_2d[0])
#[ 5 10 15]

print(arr_2d[0][0])
#5

print(arr_2d[2][1])
#40

#OR Other Way

print(arr_2d[2,1])
#40

#************Grabbing a section of matrics**********

print(arr_2d[:2,1:])
'''

[[10 15]
 [25 30]]
'''

print(arr_2d[:2])
'''
It prints Row 0 and Row 1
[[ 5 10 15]
 [20 25 30]]
'''

print(arr_2d[1:])
'''
Prints every Rows except Row 0th , i.e. Row 1st and Row 2nd
[[20 25 30]
 [35 40 45]]
'''

print(arr_2d[:1])
#[[ 5 10 15]]
#above prints Row 0


#*********************Getting Boolian Results from Array*****

arr = np.arange(1,11)
print(arr)

#[ 1  2  3  4  5  6  7  8  9 10]

print(arr > 5)
#[False False False False False  True  True  True  True  True]

bool_array = arr > 5

#Selecting True Boolian results from main array :-

print(arr[bool_array])
#[ 6  7  8  9 10]

#OR

print(arr[arr>5])
#[ 6  7  8  9 10]

print(arr[arr<3])
#[1 2]

arr_new = np.arange(50).reshape(5,10)

print(arr_new)
'''
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]]
'''

print(arr_new[1:3])
# Grab from index Row 1 and not include from 3
'''
[[10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]]
'''

print(arr_new[1:3,3:5])
#FROM ROW INDEX:-  Grab from index Row 1 and not include from index 3
#FROM COLUMN INDEX:- Grab from index 3 and not include from index 5

[[13 14]
 [23 24]]