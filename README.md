# HellTriangle

Given a triangle of numbers, find the maximum total from top to bottom

## Problem Description
Given a triangle of numbers, find the maximum total from top to bottom.
Example:
```
     6
    3 5        In this triangle
   9 7 1       the maximum total
  4 6 8 4      is 6 + 5 + 7 + 8 = 26
```
An element can only be summed with one of the two nearest elements in the next row.
So the element 3 in row 2 can be summed with 9 and 7, but not with 1.

Your code will receive an (multidimensional) array as input.
The triangle from above would be:

example = [[6],[3,5],[9,7,1],[4,6,8,4]]

## Solutions
Two solutions were implemented: 

1. Brute force: Test every possibles from top to down and compare what is biggest total sum. O(2^n)
2. Optimazed: Find the biggest total using solution from down to top without test every possibles ways. O(n²)


## Running
Both solutions running with same commands using Python 3.
You can use this commands in a terminal:
```
  python HellTriangle.py [[6],[3,5],[9,7,1],[4,6,8,4]]
  
  python HellTriangle.py "[[6], [3,5], [9,7,1], [4,6,8,4]]"
```
If you don't pass arguments the program load a triangle of example/test:
```
                         55
                        94 48
                       95 30 96
                     77 71 26 67
                    97 13 76 38 45
                  07 36 79 16 37 68
                 48 07 09 18 70 26 06
               18 72 79 46 59 79 29 90
              20 76 87 11 32 07 07 49 18
            27 83 58 35 71 11 25 57 29 85
           14 64 36 96 27 11 58 56 92 18 55
         02 90 03 60 48 49 41 46 33 36 47 23
        92 50 48 02 36 59 42 79 72 20 82 77 42
      56 78 38 80 39 75 02 71 66 66 01 03 55 72
     44 25 67 84 71 67 11 61 40 57 58 89 40 56 36
   85 32 25 85 57 48 84 35 47 62 17 01 01 99 89 52
  06 71 28 75 94 48 37 10 23 51 06 48 53 18 74 98 15
27 02 92 23 08 71 76 84 15 52 92 63 81 10 44 10 69 93             Solution: 1320
```

### Running tests
To run every tests using unittest
```
python TestHellTriangle.py
```
