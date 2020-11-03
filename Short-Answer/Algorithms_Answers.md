#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n), because the number of times this while loop
will have to run increases in direct proportion
to the input size n. Also the product of the two n's
inside the loop cancel out the product of the two n's
in the while condition, leaving us with one n.


b) This is O(n log n): first there's a for loop,
which means as input size n increases the loop 
will have to execute more times, and this increases
in a linear way (O(n)). Second, there's a nested 
while loop that executes while j is less than n, 
but j is incremented by multiplying it by 2, 
which is a log n relationship.


c) This seems like a linear relationship, O(n), 
because the function is called recursively on input - 1, 
so the bigger the input the longer the worst case 
will take to run.


## Exercise II
My strategy would be to use a binary search.

First take the number of floors in this n-story building
and divide it by 2 to find the middle
n // 2
Drop an egg from that floor. If it breaks (returns True),
find the new middle by using the old middle (result of n // 2)
as the new n 
(n // 2) // 2
Drop an egg from this floor. If it breaks (returns True), repeat
the process of finding the new middle and dropping eggs
until the egg can fall without breaking (returns False)

Time complexity of a binary search is O(log n)