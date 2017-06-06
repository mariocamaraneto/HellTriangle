# Brute Force

Sum every possible solutions and verify what is biggest.
Use ways like route to control what number is necessary sum and save how has maximum total. 

The route (way) use binary solution to 'say' if next number to sum is in the left (0) or the right(1).
Example:
```
     6              Way 3
    3 5             3 in binary is 011 
   9 7 1  
  4 6 8 4                              0      1      1
                    Then the way is 6  ->  3  ->  7  ->  8
                                      left   right  right
```

This methods show every possible represents by numbers and make easy save how way eas used last time and what is biggest.
