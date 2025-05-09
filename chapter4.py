#R-4.1 The running time O(n), space time O(n)
def find_max(s, start, stop):
    if stop - start == 1:
        return s[start] #use s[start] instead s[0]
    else:
        maxs = find_max(s, 0, stop - 1)
        if s[stop-1] > maxs:
            return s[stop-1]
        else:
            return maxs

print(find_max([0, 1, 3, 8, 5, 10, 2], 0 , 7))

#R-4.2 Trhe recursion trace of 4.11
"""power(2, 5) => return 2*16 = 32

   power(2, 4) => return 2*8 = 16

   power(2, 3) => return 2*4 = 8

   power(2, 2) => return 2*2 = 4

   power(2, 1) => return 2*1 = 2

   power(2, 0)  => return 1
"""

#R-4.3
# recursion algrorithms for computing powers
def power(x, n):
    """Compute the value x**n for integer n"""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)   #rely on truncated division
        result = partial*partial
        if n % 2 == 1:               # if n odd, include extra factor
            result *= x
    return result

print(power(2,18))
""" power(2, 18) => return 512*512 = 262144

    power(2, 9) => return 16*16*2 = 512

    power(2, 4) => return 4*4 = 16

    power(2, 2) => return 2*2 = 4

    power(2, 1) => return 1*1*2= 2

    power(2, 0)  => return 1
"""

#R.4
def reverse(S, start, stop):
    if stop - start > 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)
    return S

print(reverse([1, 2, 3, 4, 5], 0, 5))

"""reverse([4, 3, 6, 2, 6], 0, 5) => [6, 3, 6, 2, 4]

   reverse([4, 3, 6, 2, 6], 1, 4) => [6, 2, 6, 3, 4]

   reverse([4, 3, 6, 2, 6], 2, 3) => [6, 2, 6, 3, 4]
"""

#R-4.5
#Recursion trace of puzzlesolve:

"""PuzzleSolve(3, (), {a, b, c, d})

   ---PuzzleSolve(2, a, {b, c, d})

      ---PuzzleSolve(1, ab, {c, d})

      ---PuzzleSolve(1, ac, {b, d})

      ---PuzzleSolve(1, ad, {b, c})
   
   ---PuzzleSolve(2, b, {a, c, d})

      ---PuzzleSolve(1, ba, {c, d})

      ---PuzzleSolve(1, bc, {a, d})

      ---PuzzleSolve(1, bd, {a, c})
   
   ---PuzzleSolve(2, c, {a, b, d})

      ---PuzzleSolve(1, ca, {b, d})

      ---PuzzleSolve(1, cb, {a, d})

      ---PuzzleSolve(1, cd, {a, b})
   
   ---PuzzleSolve(2, d, {a, b, c})
   
      ---PuzzleSolve(1, da, {b, c})
      
      ---PuzzleSolve(1, db, {a, c})
      
      ---PuzzleSolve(1, dc, {a, b})
"""

#R-4.5
# Return the result of nth harmonic number
def harmonic_number(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_number(n - 1)

print(harmonic_number(2))

#R-4.7
# Return a string of digits into the integer it represents. 
# We can improve code as defind start = 0, and don't have stop, start, instead start = 0 and len(string) = stop - start
def change_integer(string, start, stop):
    if stop - start <= 1:
        return int(string[stop - 1])
    else:
        number = change_integer(string, start + 1, stop)
        return int(string[start]) *10**(stop - start - 1) + number

print(change_integer('45996', 0, 5))

#R-4.8
# Return a sum of the values in a sequence A of n integer and change it instead of sequence B
def isabel_problem(setA):
    n = len(setA)
    setB = [0]*(n // 2)
    if n == 1:
        return setA[0]
    else:
        for i in range(n // 2):
            setB[i] = setA[2*i] + setA[2*i + 1]
        return isabel_problem(setB, n // 2)
    
print(isabel_problem([1,2,3,4], 4))

"""The number of recursion is logn
   The running time is n + n/2 + n /4 +.... O(n)
"""

#R.4-9
#Return min and max without using the loop
def find_minmax(S, start, stop):
    if stop - start <= 1:
        return (S[start], S[start])
    else:
        mins, maxs = find_minmax(S, start, stop - 1)
        if mins > S[stop - 2]:
            mins = S[stop - 2]
        if maxs < S[stop - 2]:
            maxs = S[stop - 2]
        return (mins, maxs)
    
print(find_minmax([1, 3, 4, 5, 0, 3, 10, 6], 0, 8))

#R.4-10
#Return the result which is the integer part of the base-two logarithm of n using only +, -
def logarithm(n):
    if n < 2:  #Don't use n== 1 because the nagetive will computed
        return 0
    else:
        return 1 + logarithm(n // 2)
    
print(logarithm(0))

#R-4.11
#Return a recursive function for solving the element uniqueness problem which O(n**2)
def uniqueness(S, index = 0):
    n = len(S)
    if n - index < 2:
        return True
    else:
        if S[index] not in S[index +1 : n]:
            return uniqueness(S, index + 1)
        return False 

print(uniqueness([1, 2, 17, 27, 7, 21, 6]))

#R-4.12
#Return a result of the product of two positive integers m and n
def compute_product(m, n):
    if n == 1:
        return m
    else:
        return m + compute_product(m, n -1)
        
print(compute_product(500, 5))

#R-4.13
#Prove induction the number of dashes printed by draw_interval(c) is 2**(c+1) - c - 2
"""Base case: draw_interval(0) = 2**1 - 2 = 0
   Induction step: The number of dashes printed by draw_interval(c) is more than twice the number generated by a call to draw_interval(c - 1) and the number of dashes by the center c.
   By induction, we have that the number of lines is thus 
   2*(2**(c-1 + 1) - (c -1) + 2) + c = 2*(2**c - c - 1) + c = 2**(c + 1) - c - 2"""

            
#R-4.14
"""Step 1: Move n-1 disks from A to B
   Step 2: Move the largest disk from A to C
   Step 3: Move n - 1 disks from B back to A 
   Return with the remainder disk - 1 in A 
"""

#R-4.15
#Return all of subsets of S with n elements
def find_subset(S, start = 0, stop = None):
    if len(S) - start == 0:
        return [[]]   #return a set of subset, the first is empty set
    else:
        rest = find_subset(S, start + 1, stop) 
        return rest + [ [S[start]]+ each for each in rest]


print(find_subset([1, 2, 3, 4, 5]))

#R.4-16
#Return a reverse of a string
def reverse_string(string, start, stop):
    if stop - start <= 1:
        return string[start]
    else:
        return reverse_string(string, start + 1, stop) + string[start]
    
print(reverse_string('pots&pans', 0, 9))
#Reveiw code:
def reverse_string(string):
    n = len(string)
    if n <= 1:
        return string
    return reverse_string(string[1:]) + string[0]

#R.4-17
#Define a palindromes: can use start = 0, end = None (len of string) as parameters
def is_palindromes(string, index = 0):
    n = len(string) - index
    if n <= 1:
        return True
    else:
        if string[index] == string[n-1]:
            return is_palindromes(string, index + 1)
        else:
            return False
    
print(is_palindromes('racecar'))
print(is_palindromes('gohangasalamiimalasagnahog'))

#R.4-18
#Return True if the vowel of a string is more than consonant
def compute_char(string, start, stop):
    if stop - start == 0:
        return (0, 0)
    else:
        vowel_count, consonant_count = compute_char(string, start + 1, stop)
        if string[start].isalpha():
            if string[start].lower() in ['a', 'o', 'e', 'u', 'i']:  #We should use quickly set instead of list 
                return (vowel_count + 1, consonant_count)
            else:
                return (vowel_count, consonant_count + 1)
        else:
            return (vowel_count, consonant_count)

def is_morevowel(string):
    v, c= compute_char(string, 0, len(string))
    return v > c

    
print(is_morevowel('hello'))
print(is_morevowel('number12'))
print(is_morevowel('oiel'))

#R-4.19
#Return a sequence so that all the even values appear before all the odd values
def rearrange(s, start = 0, stop = None):
    stop = len(s)
    if stop - start <= 1:
        return [s[start]]
    else:
        if s[start] % 2 == 1:
            return rearrange(s, start + 1, stop) + [s[start]]  #avoid to use append and del to change the original s
        return [s[start]] + rearrange(s, start + 1, stop)
print(rearrange([i for i in range(10, 25)]))

#R-4.20
#Return a sequence which all elements less than or equal to k come before any elements larger than k
# This approach is O(n^2)
def rearrange_with_k(S, k, start = 0):
    if len(S) - start <= 1:
        return [S[start]]
    else:
        if S[start] <= k:
            return [S[start]] + rearrange_with_k(S, k, start + 1)
        return rearrange_with_k(S, k, start + 1) + [S[start]]

print(rearrange_with_k([3, 25, 14, 16, 7, 5, 6, 10, 33, 1, 0], 9))

# This approach is O(n)
def rearrange_with_k(S, k, start = 0, stop = None):
    if stop is None: stop = len(S)
    if stop - start <= 0:
        return S
    else:
        if S[start] > k:
            S[start], S[stop - 1] = S[stop - 1], S[start]
            return rearrange_with_k(S, k, start, stop - 1)
        return rearrange_with_k(S, k, start + 1, stop)
print(rearrange_with_k([3, 25, 14, 16, 7, 5, 6, 10, 33, 1, 0], 9))
            

#R-4.21
#Return a two integers in S that Sum to k, if such a pair of exsit
# This approach is O(n^2)
def find_sum_number(S, k, start = 0):
    if len(S) - start == 0:
        return (None, None)
    else:
        result = k - S[start]
        if result not in S[start + 1:]: #beacause we search the result in the S[start + 1:] so we don't need to check the condition result == S[start]
            return find_sum_number(S, k, start + 1)
        else:
            return(S[start], result)

print(find_sum_number([1,2,3,4,5,6,7], 10))
            

# This approach is O(n)
def find_sum_number(S, k, start = 0, stop = None):
    if stop is None: stop = len(S)
    if len(S) - start == 0:
        return (None, None)
    else:
        if S[stop - 1] + S[start] == k:
            return (S[start], S[stop - 1])
        elif S[stop - 1] + S[start] > k:
            return find_sum_number(S, k, start, stop - 1)
        else:
            return find_sum_number(S, k, start + 1, stop)
        
print(find_sum_number([1,2,3,4,5,6,7], 10))

#We also use a set to save all of element which is not result to make O(n)

#R-4.22
#Return a result to compute a power of number without nonrecursive
def power_nonrecursive(x, n):
    if n == 0: return 1
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result
print(power_nonrecursive(5 , 0))
        
#R-4.23
# Return all entries of the file system rooted at the given path having the given file name
import os

def find(path, filename, result):
    if result is None:
        result = set()
    if os.path.isfile(path) and os.path.basename(path) == filename: #check if the path is a file and matches the filename
        return result.add(path)
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                childpath = os.path.join(path, file)
                find(childpath, filename, result)
    return result
            
    
print(find(r"C:\Users\THAI TUYET KHA\OneDrive\Desktop\TOEFL", "Track 01.mp3", set()))    

#R-4.24
# Solve summation puzzle
class PuzzleSolve():
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._count = 0

    def _change_integer(self, text, number):
        length = len(text)
        result = 0
        for i in range(length):
            result += number[text[i]]*10**(length - i - 1)
        return result
    
    def _solve(self, S, nums, start, U):
        if start >= len(S):  #if the index is geater than the len of sequence, we must return the result and check conditions
            return self._summation_result(U)
        elif S[start] in U:
            return self._solve(S, nums, start + 1, U)  #if we have the same characters in dict we'll pass it
        else:
            for each in nums.copy():  # we use copy of nums set to make sure loop to the last index will finish recursion
                U[S[start]] = each
                nums.remove(each)
                self._solve(S, nums, start + 1, U)
                nums.add(each)
                del U[S[start]]    

    def _summation_result(self, U):
        if self._change_integer(self._a, U) + self._change_integer(self._b, U) == self._change_integer(self._c, U):
            self._count += 1  
            print(f'The result is {self._change_integer(self._a, U)} + {self._change_integer(self._b, U)} = {self._change_integer(self._c, U)}, check {self._change_integer(self._a, U) + self._change_integer(self._b, U)}')
            
            print(f'The numbers correspond the characters {U}')
            return self._count
        else:
            return False

    def check_equal(self):
        S = list(self._a) + list(self._b) + list(self._c)  # join the characters
        nums = set(range(10))
        U = {}
        self._solve(S, nums, 0, U)
        if self._count == 0:  # if it doesn't match any result, return false
            print("Don't find result to match the puzzle")
        else:
            print(f'We have the {self._count} solutions')

if __name__ == "__main__":
    problem = PuzzleSolve('dot', 'cat', 'pig')
    problem.check_equal()
        
#R-4.25
#Draw the English ruler project without using recursion
#The lines of output are 2**c-1, and the number of dashes for each tick line is more 
# than one the number of consecutive 1's at the end of the binary representation of the counter.

def print_line(nums_tick, tick_label = ''):
    line = '-'*nums_tick
    if tick_label:
        line += ' ' + tick_label  # join the label in the tick line
    print(line)

def counter_one(number):
    binary = f'{number: 08b}'  #represent the binary number =>> use bin 
    counter = 0
    for i in reversed(binary):  # count the number of consecutive 1's at the end of the binary, we can use loop and bitwise and to compute counter value
        if i == '1':
            counter += 1
        else:
            return counter

def draw_interval(nums_tick):
    for i in range(2**(nums_tick) - 1):  # from 0 to 2**c - 2
        print_line(counter_one(i) + 1)

def draw_ruler(num_inches, major_length):
    print_line(major_length, '0')
    for i in range(1, num_inches + 1):  # we can't loop invloving the index 0, because we have more than the line when num_inches 3
        draw_interval(major_length - 1)
        print_line(major_length, str(i))

draw_ruler(3, 3)
            

 #After review:
def print_line(nums_tick, tick_label = ''):
    line = '-'*nums_tick
    if tick_label:
        line += ' ' + tick_label  # join the label in the tick line
    print(line)

def counter_one(number):
    counter = 0
    while number & 1:  #making sure the last bit of n is always 1, return true and continue while loop 
        counter += 1
        number >>= 2   # when the value is added in counter, delete it as shift right bitwise (move the bit to right) 
    return counter 

def draw_interval(nums_tick):
    for i in range(2**(nums_tick) - 1):  # from 0 to 2**c - 2
        print_line(counter_one(i) + 1)

def draw_ruler(num_inches, major_length):
    print_line(major_length, '0')
    for i in range(1, num_inches + 1):  # we can't loop invloving the index 0, because we have more than the line when num_inches 3
        draw_interval(major_length - 1)
        print_line(major_length, str(i))

draw_ruler(3, 3)

#R-4.26
# # Noted that we don't care any parameters passing the function, we just remind the order of it
def move_disk(pega, pegb):
    pegb.insert(0, pega[0])
    del pega[0]

def hanoi(fro, temp, to, n):
    if n == 1:
        move_disk(fro, to)
    else:
        hanoi(fro, to, temp, n - 1)  #change n-1 first of from peg to temp peg
        print(fro,temp, to)
        move_disk(fro, to)           #change the largest disk from peg to to peg
        hanoi(temp, fro, to, n - 1)  #continue n-1 in temp to to peg
        return fro,temp, to
    

A = [1,2,3,4]
B = []
C = []
print(hanoi(A, B, C, 4))    
           
#R-4.27
#Implementation of the walk function 
import os

def my_walk(path):
    dirnames = []
    filenames = []
    for each in os.listdir(path):   
        childpath = os.path.join(path, each)
        name = os.path.basename(childpath)
        if os.path.isdir(childpath):
            dirnames.append(name)
        else:
            filenames.append(name)

    yield path, dirnames, filenames

    for dir in dirnames:
        subpath = os.path.join(path, dir)  #loop the direction folder
        yield from my_walk(subpath)  #yield all of the yield value from my_walk function

for value in my_walk(r"C:\Users\THAI TUYET KHA\OneDrive\Desktop\CS50"):
    print(value[0], value[1], value[2])   #print value from yield, it's not from yield from, yield from just connects the result of yield in the previous to it

           
    






    






    






