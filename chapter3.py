#R3.1
import matplotlib.pyplot as plt
import numpy as np

x = np.array([10**i for i in range(1, 20)]) #make sure fit with y1,y2,y3,y4,y5
y1 = np.log2(8*x)
y2 = np.log2(4*x* np.log2(x))
y3 = np.log2(2*x**2)
y4 = np.log2(x**3)
y5 = np.log2(2**x)


plt.plot(np.log2(x), y1, label='y = 8n')   #graph the function y = 8n
plt.plot(np.log2(x), y2, label='y = nlogn')   #graph the function y = 4nlogn
plt.plot(np.log2(x), y3, label='y = 2n**2')   #graph the function y = 2n**2
plt.plot(np.log2(x), y4, label='y = n**3')   #graph the function y = n**3
plt.plot(np.log2(x), y5, label='y = 2**n')   #graph the function y = 2**n

#Show the legendlegend
plt.legend()
#Show the graphgraph
plt.show()

#R3.2 I use the graph for finding n0, but the answer is different
"""To find the n0 to make the A is better than B
   8nlogn < 2n**2
   So 4logn < n.
   Cause n is a positive integer. So we have n0 = 17 (4logn = n when n = 16)"""

#R3.3
"""To find the n0 to make the A is better than B
   40n**2 < 2n**3
   So 20 < n.
   Cause n is a positive integer. So we have n0 = 21"""

#R3.4 The function f(n) = n
import matplotlib.pyplot as plt
import numpy as np

x = np.array([10**i for i in range(1, 20)]) #make sure fit with y
y = np.log2(x)


plt.plot(np.log2(x), y, label='y = n')   #graph the function y = n


#Show the legendlegend
plt.legend()
#Show the graphgraph
plt.show()

#R3.5
"""with the function f(n) = n**c (c is constant) we have this in log-log scale like
   f(n) = log n**c
   So we have: f(logn) = c. logn. 
   It's a straight line slope degree c"""

#R3.6 Use the sum of arithmetic progression
"""The sum of even from 0 to 2n with positive n: 2 + 4 + 6 +...+ 2n = (2n + 2). n/2 = n(n + 1)"""
#R3.7 
"""(a) The running time of algorithm A is always O(f(n)):                T(n) <= c.f(n) , n >= n0 > 1, c > 0
   (b) In the worst case, the running time of algorithm A is O(f(n)):    Tmax(n) <= c.f(n), n >= n0 > 1, c > 0
   1. (b) Because T(n) <= Tmax(n) <= c.f(n), so we have T(n) <= c.f(n) => (a)
   2. (a) Because The running time of algorithm A is always O(f(n)), meaning it is suitable for all of input n, so in the best or worst case, we also have Tmax(n) <= f(n) => (b)
"""

#R3.8 Remember log n <= n for n >= 1
""" 4n ~ n
    3n + 100logn <= 3n + 100n <= 103n ~ is O(n)
    nlogn ~ is O(nlogn)
    4nlogn + 2n is O(nlogn)
    n^2 + 10n ~ is O(n^2)
    n^3 is O(n^3)
    2^10 is constant time 
    2^logn = n is O(n)
    2^(2n) is O(2^n) 
    So 2^10, 2^logn, 3n + 100logn, 4n, nlogn, 4nlogn + 2n, n^2 + 10n, n^3, 2^(2n)"""

#R3.9
"""We have d(n) is Of((n)) so d(n) <= c. f(n), with c > 0, n >= n0 >= 1
   ad(n) <= ac. f(n) <= c'.f(n) with c' = ac > 0 so ad(n) is O(f(n))"""

#3.10
"""We have d(n) is O(f(n)) so d(n) <= c. f(n), with c > 0, n >= n0 >= 1
           e(n) is O(g(n)) so e(n) <= c'. g(n), with c' > 0, n >= n0 >= 1
           So d(n).e(n) <= c".f(n). g(n) with c" = c.c'
           d(n).e(n) is O(f(n)g(n))
"""

#3.11
""""We have d(n) is O(f(n)) so d(n) <= c. f(n), with c > 0, n >= n0 >= 1
           e(n) is O(g(n)) so e(n) <= c'. g(n), with c' > 0, n >= n0 >= 1
           So d(n) + e(n) <= c.f(n) + c'.g(n) <= d. (f(n) + g(n))
           d(n).e(n) is O(f(n) + g(n))
"""

#3.12
"""We have example: d(n) = 10n + 2 is O(n) 
                    e(n) = n -16 is O(n) 
           So d(n) - e(n) = 9n - 14 is O(n)  
           d(n).e(n) is not necessarily O(f(n) - g(n))
"""
#3.13
"""d(n) is O(f(n)): d(n) <= c. f(n)
   f(n) is O(g(n)): f(n) <= c'. g(n)
   So d(n) <= c'.g(n) or d(n) is O(g(n))"""
#3.14
"""max{f(n), g(n)}) <= f(n) + g(n)
   max{f(n), g(n)}) is O(f(n) + g(n)))
   so O(max{f(n), g(n)})) = O(f(n) + g(n)))
   """
#3.15
"""f(n) is O(g(n)) so f(n) <= c.g(n)
   Similar g(n) >= 1/c . f(n)
   g(n) >= c'.f(n) means g(n) is Ω(f(n))
"""
#3.16
"""p(n) = ak.n^k + ak-1 . n^k-1 +...+ c
   log p(n) = log (ak.n^k + ak-1 . n^k-1 +...+ c) < log (ak.n^k . k)
   log p(n) <= log k. ak + log n^k <= c . k. logn
   So log pn is O(logn)
"""
#3.17
"""(n + 1)^5 <= 6.n^5
   (n + 1)^5 is O(n^5)
"""
#3.18
"""2^(n + 1) < 2. 2^n
   So 2^(n + 1) is O(2^n)
"""
#3.19
"""We have logn <= n with n >= 1
   So n <= n. logn <= c. nlogn
   n is O(nlogn)
"""
#3.20
"""log n <= n
   So n^2 >= n.logn >= c. nlogn
   n^2 is Ω(nlogn)
"""
#3.21
"""n >= logn with n >= 1 so nlogn >= n
   We also have nlogn >= c. n
   nlogn is Ω(n)
"""
#3.22
"""We have f(n) is a positive nondecreasing funcition greater than 1 
   So ⌈f(n)⌉ <= f(n) + 1 <= c. f(n)
   We can say ⌈f(n)⌉ is O(f(n))"""
#3.23 1 + n + n + 1  ~ n so is O(n)
#3.24 1 + n/2 + n + 1 ~ n so is O(n)
#3.25 1 + n + n^2 + n^2 + 1 ~ n^2 so is O(n^2)
#3.26 1 + n + n + n + 1 ~n so is O(n)
#3.27 1+ n.n^2 + n^2 + n + 1 ~ n^3 so is O(n^3)

#3.28 f(n) is the time (microseconds) to solve n input, so the f(n max) will also be the time to solve n-max input.
#Because t is given time, so f(n-max) <= t. We can find the value of n-max from that.

#3.29 
"""We have n elements, 
   each element take O(logn). 
   So the worst-case running time (aka big Oh) is nlogn
"""

#3.30
"""We have n elements, take O(n)
   Choose logn elements in S at random, take O(logn) and excute O(n) time for each
   So we have O(n) + O(nlogn) ~ O(nlogn)
"""
#3.31
"""n elements sequence S of integer: O(n)
   even number O(n)
   odd number O(logn)
   The best case- all of them is oddodd number: O(nlogn)
   The worst- all of them is even number: O(n^2) 
"""

#3.32
"""n element sequence S, S[i] is O(i)
   We have 1 + 2 +...+n(n+1), also O(n^2)
"""
#3.33
"""Al's claim wasn't correct, not 'always'. When n >= n0 such that f(n) <= c.g(n).
   We also have the constant c, we mint it but it still exist.
   If the c1 in O(logn) is larger than c2 in O(n^2). In these first input (n < 100), we can see the running time of O(logn) is greater, but when n is enough larger.
   The O(nlogn) will show the excellent of running time
"""
#3.34
"""Each inhabitant have n-element meals in their life.
   The first meal has: 1 probability (enjoy it)
   The second meal has: 1/2
   The third meal has: 1/3
   ...
   So we have 1 + 1/2 + 1/3 +...+ 1/n = Hn (Harmonic number) is O(logn)
"""
#3.35
"""Join three sets take O(3n)
   Sort the new set take O(3nlog3n)
   So we have O(nlogn)
"""
#3.36
# This algorithm is O(nlogn) - sorted function
def find_ten_elements(sequence):
    list_sequence = list(sequence)
    return sorted(list_sequence, reverse=True)[:10]       


print(find_ten_elements([1, 4, 2, 8, 3, 9, 12, 45, 16, -58, 23, 19, 52]))

#3.37
"""f(n) = n^2: f(n) is O(n^2) and Ω(nlogn)"""

#3.38
"""Sum <= n.n^2 <= n^3
   We have the sum is O(n^3)
"""

#3.39
# I can't deal with this.
"""S =   1/2 + 2/2^2 + 3/2^3 + 4/2^4 +...+ (n-1)/2^n-1 + n/ 2^n
   S = ( 1+1/2 + 2+1/2^2 + 3+1/2^3 + 4+1/2^4 +...+ (n-2)+1/2^n-1 + (n-1)+1/2^n-1 ) * 1/2
   2S - S = 1/2 + 1/2^2 + 1/2^3 + 1/2^4 +...+ 1/2^n-1 - n/2^n
   So S = 1.(1-0.5^n)/(1-0.5) - n/2^n = 2(1-0.5^n) - n/2^n = 2- (n+2)/2^n < 2
"""
#3.40
"""b > 1 is a constant. We have b/ logb . logf(n) >= logb(f(n)) >= 1/logb . logf(n)
   c'. logf(n) >= logb(f(n)) >= c" * logf(n)
   So logb(f(n)) is Big-Meta(logf(n)) 
 """

#3.41
#Find min max with 3n/2 comparisons: first make two group through find the min, max of each couple numbers
def find_minmax(sequence):
    max_list = []
    min_list = []
    length = len(sequence)
    if length % 2 == 0:
        for i in range(0, length, 2):
            if sequence[i] > sequence[i + 1]:
                max_list.append(sequence[i])
                min_list.append(sequence[i + 1])
            else:
                min_list.append(sequence[i])
                max_list.append(sequence[i + 1])
    else:
        for i in range(0, length - 1, 2):
            if sequence[i] > sequence[i + 1]:
                max_list.append(sequence[i])
                min_list.append(sequence[i + 1])
            else:
                min_list.append(sequence[i])
                max_list.append(sequence[i + 1])
        max_list.append(sequence[-1])
        min_list.append(sequence[-1])
    result_max = max(max_list)
    result_min = min(min_list)

    return result_max, result_min
    
print(find_minmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#After review code: Actually, we can use another like assigning a max, min value with the second first element, and compare it with 
#Find min max with 3n/2 comparisons: first make two group through find the min, max of each couple numbers
def find_minmax(sequence):
    max_list = []
    min_list = []
    length = len(sequence)
    #Return the min max when empty sequence
    if length == None:
        return None, None
    if length % 2 == 0:
        for i in range(0, length, 2):
            # use () cuz python can unpack and has a mistake with smaller two value, so we want to be careful when we use it with ()
            larger, smaller = (sequence[i], sequence[i + 1]) if sequence[i] > sequence[i + 1] else sequence[i+1], sequence[i]
            max_list.append(larger)
            min_list.append(smaller)
    else:
        for i in range(0, length - 1, 2):
            larger, smaller = sequence[i], sequence[i + 1] if sequence[i] > sequence[i + 1] else sequence[i+1], sequence[i]
            min_list.append(smaller)
            min_list.append(smaller)
        max_list.append(sequence[-1])
        min_list.append(sequence[-1])

    result_max = max(max_list)
    result_min = min(min_list)

    return result_max, result_min

## Review code one more time:
# import random
#Find min max with 3n/2 comparisons: first make two group through find the min, max of each couple numbers
def find_minmax(sequence):
    max_list = []
    min_list = []
    length = len(sequence)
    #Return the min max when empty sequence
    if not seq:
        return None, None
    if length == 1:
         return sequence[0], sequence[0]
    
    min_list.append(min(sequence[0], sequence[1]))
    max_list.append(max(sequence[0], sequence[1]))
    start = 2 if length % 2 == 0 else 1

    for i in range(start, length, 2):
            # use () cuz python can unpack and has a mistake with smaller two value, so we want to be careful when we use it with ()
            larger, smaller = (sequence[i], sequence[i + 1]) if sequence[i] > sequence[i + 1] else (sequence[i+1], sequence[i])
            max_list.append(larger)
            min_list.append(smaller)

    return max(max_list), min(min_list)

seq = [random.randint(0, 100) for i in range(20)]
print(seq)
print(find_minmax(seq))   

    
print(find_minmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#3.42
"""The number of URL sent by Bob which is read by his friends: 1 + 2 +...+ n = n(n+1)/2
   So the minimum value of C such that Bod can kno that one of his friend has vistied their maximum allowed number of times: ⌈n(n+1)/2⌉
"""
#3.43
"""
Box Method 3.3 when n is odd:

The (n+1) is even, so we have
         ___
        |   |
   (n)  |   |
        |   | 
        |___| (n+1)/2
     
"""

#3.44
"""a. When r have 100 bits, r = 2^100 - 1.
      We don't loop 0 and 1, so the number of computing 2^100 - 1 -2 + 1 = 2^100 - 2
      And the times is (2^100 -2)/10^6
   b. In the worst case, we want to loop r-1 times O(r), each time we take O(n) for division.
      Hence O(r.n) ~ O(2^(8n).n)
      """
#3.45
def find_val(seq):
    # Find a value with O(n) and just use O(1) additional space besides the sequence S in range [0, n - 1]
    length = len(seq)
    sum_couple = length - 2  #The maximum value is n - 1 and min is 0 so sum: n - 1
    for i in range(length):
        j = sum_couple - i
        if j not in seq:
            return j
        
print(find_val([0, 1, 3, 4, 5, 6]))
print(find_val([0,1,2,3,4,6,7,8,9]))

#3.46
"""The problem occurs when sheep b is taken out, we aim to prove that sheep a is the same color as b or resuming the induction
"""
#3.47
"""Base case: 1 lines, we have 1 >= 0 intersections >= 1.0
   Induction step (n lines): Assume claim trues for n' < n. We have c'. n'^2 >= inter >= c.n'^2
   Consider n lines: the last n th lines have the intersection's maximum and min with other lines is repectively n and (n-1).
   So we have c'. (n-1)^2 + (n-1)>= inter(n lines) >= c.(n-1)^2 + (n-1), we have Big-Meta(n^2)
"""

#3.48
"""In the induction step, we have F(n') <= c. n'. Using this in the proof, but it's wrong"""

#3.49
"""Base case (n<=2): 2/3. 3/2 <= F(1) <= 3/2, 
                     2/3 . 9/4 <= F(2) <= 9/4
   Induction step (n>2): Suppose our claim is true for all n'<n. Consider F(n).
   F(n) = F(n-2) + F(n-1) <= c1. (3/2)^(n-2) + c1. (3/2)^(n-1)
                          <= (3/2)^n . 10c1/9 <= c. (3/2)^n So F(n) is O((3/2)^n)

   F(n) = F(n-2) + F(n-1) >= c2. (3/2)^(n-2) + c2. (3/2)^(n-1)
                          >= (3/2)^n . 10c2/9 >= c'. (3/2)^n So F(n) is Ω((3/2)^n)
                  
   Finish proof.
                                                 
"""

#3.50
#a: O(n^2) time algorithm
def compute_poly(coef, x):
    n = len(coef) # the degree of polynomial is n-1, not n because have a constant c
    total = 0
    for i in range(n):
        value_x = 1
        #compute the value of x when the power increases
        for _ in range(i):
            value_x *= x
        total += coef[i]*value_x
    return total

print(compute_poly([1, 2, 3], 1))

#b: the O(nlogn) algthorithm: break out computing the x^n
# This is actually wrong, cuz the inner loop with x**2 not really efficent, we have a another manner below
def compute_x(degree, x):
    value_x = x if degree == 1 else 1
    time_loop = degree // 2  #break the time of loop with logn
    while time_loop > 0:
        if degree % 2 == 1:
            value_x *= x 
        value_x *= x**2
        time_loop -= 1
    return value_x
        
def compute_poly(coef, x):
    total = 0
    n = len(coef) # the degree of polynomial is n-1, not n because have a constant c
    for i in range(n):
        total += coef[i]*compute_x(i, x)
    return total

print(compute_poly([3, 2, 1], 2))

#After reveiw code: x^n = x. x^2. x^4. x^6...
def compute_x(degree, x):
    value_x = 1
    while degree > 0:
        if degree % 2 == 1:
            value_x *= x 
        x *= x
        degree //= 2 #break the time of loop with logn
    return value_x
        
def compute_poly(coef, x):
    total = 0
    n = len(coef) # the degree of polynomial is n-1, not n because have a constant c
    for i in range(n):
        total += coef[i]*compute_x(i, x)
    return total

print(compute_poly([3, 2, 1], 2))

#c: The number of arithmetic operations is O(n). The first time, we compute a'n-1 +a'n*x, a'n-2 +a'n-1 *x.. a'0 + a'1*x 
#   Every time we take an operation so O(n)

#3.51
""" log1 + log2 + log3 +...+ logn <= n.logn
    The given summation is O(nlogn)
"""

#3.52
"""log 1 + log2 + log 3+...+ log n/2 + ...+ log n >= Sum(n/2 to n) * log n/2
                                                  >= Sum(n/2 to n) (logn - log 2)
                                                  >= Sum(n/2 to n)logn - n/2* log2
                                                  >= n/2*log n/2 - n/2 *log2
                                                  >= n/2 * ( logn/2 - log2)
                                                  >= n/2 * log n/4 is Ω(nlogn)
   So sum is Big- Theta(nlogn)
"""
#3.53
# Actually I spent a lot times but I cannot deal with it. And I was helped by other people
"""Because each n integer can represent a binary with the number of bits is less than ⌈logn⌉ 
   and we give the number of testers by O(logn), the remainder is a bottle.
"""
#3.54
#Before review code
import random
def find_frequency(n):
    # Find a value which is the most frequency in seq, O(n)
    seq = [random.randint(0, 4*n-1) for i in range(n)]
    length = len(seq)
    list_val = {}
    max = 0
    list_mostval = []
    
    for i in range(length):
        if seq[i] not in list_val:
            list_val[seq[i]] = 1
        else:
            list_val[seq[i]] += 1
        if list_val[seq[i]] > max:
            max = list_val[seq[i]]
    print(seq, list_val, sep='\n')
    for i in list_val:
        if list_val[i] == max:
            list_mostval.append(i)
    return list_mostval    

print(find_frequency(20))

#After review code
import random
def find_frequency(n):
    # Find a value which is the most frequency in seq, O(n)
    seq = [random.randint(0, 4*n-1) for i in range(n)]
    length = len(seq)
    list_val = {}
    max_freq = 0
    
    for i in range(length):
        #If the dict doesn't containt the value i, will return 0
        list_val[seq[i]] = list_val.get(seq[i], 0) + 1
        if list_val[seq[i]] > max_freq:
            max_freq = list_val[seq[i]]
            value_max = seq[i]
    print(seq, list_val, sep='\n')

    return value_max, max_freq

print(find_frequency(20))

#R-3.55
import matplotlib.pyplot as plt
import timeit

class PrfixAverage():
    def __init__(self):
        self._run_time = []
    
    def _runtime(func):
        def wrapper(*argc, **kwargs):
            def wrapper_five():
                func(*argc, **kwargs) 
            time_excute = timeit.timeit(wrapper_five, number = 5)  #use timeit.timeit to measure the time of func 5 times
            print('The total time is:', time_excute)
            argc[0]._run_time.append(time_excute)  #this saves into self._run_time
        return wrapper
    
    @_runtime
    def prefix_average1(self, S):
        """Return list such that, for all j, A[j] equals average of S[0],,,,S[j]"""
        n = len(S)
        A = [0] *n
        for j in range(n):
            total = 0
            for i in range(j + 1):
                total += S[i]
            A[j] = total / (j + 1)
        return A
    
    @_runtime
    def prefix_average2(self, S):
        """Return list such that, for all j, A[j] equals average of S[0],,,S[j]"""
        n = len(S)
        A = [0]* n
        for j in range(n):
            A[j] = sum(S[0: j+1])/ (j+1)
        return A
    
    @_runtime
    def prefix_average3(self, S):
        """Return list such that, for all j, A[j] equals average of S[0],...,S[j]"""
        n = len(S)
        total = 0
        A = [0]*n
        for j in range(n):
            total += S[j]
            A[j] = total/(j+1)
        return A

    def reset(self):
        self._run_time = list()

    def implement_run(self, expert = 4):
        result = {}
        for num, func in [('1', self.prefix_average1),('2', self.prefix_average2),('3', self.prefix_average3)]:
            for i in range(1, expert):
                S = list(range(10**i))
                func(S)
            result[num] = self._run_time  #each input, we loop 5 times, and just save a value in run_time, result is a dict with key is the number of function and the value is a list with expert value
            self.reset()
        x = list(map(lambda x: 10**x, range(1, expert))) 
        return x, result
    
prfix = PrfixAverage()
x, result = prfix.implement_run()

plt.xscale('log')  #change the x,y axes becomes logarit, means the distance between of 10,100,1000,.. equal
plt.yscale('log')
for y in result.values():
    plt.plot(x, y)

plt.show()

#R.4-56 Perform an experimental analysis that compares the relative running times of the functions show in Code Fragment 3.10
# We spent 68962mms for the third time of example5 (O(n^3)), it is larger
import matplotlib.pyplot as plt
import timeit

class CompareRunningTime():
    def __init__(self):
        self._run_time = []
    
    def _runtime(func):
        def wrapper(*argc, **kwargs):
            def wrapper_five():
                func(*argc, **kwargs) 
            time_excute = timeit.timeit(wrapper_five, number = 5)*1000  #use timeit.timeit to measure the time of func 5 times
            argc[0]._run_time.append(time_excute)  #this saves into self._run_time
            return time_excute
        return wrapper
    
    @_runtime
    def example1(self, S):
        """Return the sum of the elments in sequence S"""
        n = len(S)
        total = 0
        for j in range(n):
            total += S[j]
        return total
    
    @_runtime
    def example2(self, S):
        """Return the sum of the elments with even index in sequence S"""
        n = len(S)
        total = 0
        for j in range(0, n, 2):
            total += S[j]
        return total
    
    @_runtime
    def example3(self, S):
        """Return the sum of the prefix sums of sequence S"""
        n = len(S)
        total = 0
        for j in range(n):
            for k in range(1 + j):
                total += S[k]
        return total 
    
    @_runtime
    def example4(self, S):
        """Return the sum of the prefix sums of sequence S"""
        n = len(S)
        prefix = 0
        total = 0
        for j in range(n):
            prefix += S[j]
            total += prefix
        return total 
    
    @_runtime
    def example5(self, A, B):
        """Return the number of elements in B equal to the sum of prefix sums in A )(n^3)"""
        n = len(A)
        count = 0
        for i in range(n):
            total = 0
            for j in range(n):
                for k in range(1+j):
                    total += A[k]
            if B[i] == total:
                count += 1
        return count

    def reset(self):
        self._run_time = list()

    def implement_run(self, expert = 4):
        result = {}
        for num, func in [('1', self.example1),('2', self.example2),('3', self.example3), ('4', self.example4), ('5', self.example5)]:
            for i in range(1, expert):
                S = list(range(10**i))
                if num == '5':
                    compute_time = func(S, S)
                else:
                    compute_time = func(S)
                print(f'The total time of function {num} is:', compute_time)
            result[num] = self._run_time
            self.reset()
        x = list(map(lambda x: 10**x, range(1, expert)))
        return x, result
    
compute_sum = CompareRunningTime()
x, result = compute_sum.implement_run()

plt.xscale('log')
plt.yscale('log')
for name,y in result.items():
    plt.plot(x, y, label=name)

#show the legend
plt.legend()
plt.show()

#R.4-57 We can directly use function without class or wrapper 
import matplotlib.pyplot as plt
import timeit
import math
import random

class TestSortedFunc():
    def __init__(self):
        self._run_time = []
    
    def _runtime(func):
        def wrapper(*argc, **kwargs):
            def wrapper_five():
                func(*argc, **kwargs) 
            time_excute = timeit.timeit(wrapper_five, number = 5)/5*1000  #use timeit.timeit to measure the time of func 5 times
            argc[0]._run_time.append(time_excute)  #this saves into self._run_time
            return time_excute
        return wrapper
    
    @_runtime
    def sorted_function(self, S):
        """Sorted function in Python"""
        S = sorted(S)
        return S
    
    
    def implement_run(self, expert = 7):
        result = {}
        logarit = []
        for i in range(1, expert):
            S = list(range(1,10**i))
            random.shuffle(S)
            compute_time = self.sorted_function(S)
            print(f'The total time of sorted function is:', compute_time)
            logarit.append(len(S)*math.log(len(S),2))

        result['1'] = self._run_time
        result['2'] = logarit              #noted that don't make the value of logarit in the loop, the value will be assigned

        x = list(map(lambda x: 10**x, range(1, expert)))
        return x, result
    
sorted_test = TestSortedFunc()
x, result = sorted_test.implement_run()

plt.xscale('log')
plt.yscale('log')
for name,y in result.items():
    plt.plot(x, y, label=name)

#show the legend
plt.legend()
plt.show()




