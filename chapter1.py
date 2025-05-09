### 1.1
def is_multiple(n,m):
    if m == 0 : return False
    if not isinstance(n, int) or not isinstance(m, int): return False
    return n%m ==0                                  ### This is a logic expression, automaticlly return true or false

print(is_multiple(4.5,2))


### 1.2
def is_even(k):
    if not isinstance(k,int): False
    return (k&1) == 0

print(is_even(7))


def is_even(k):
    even = [1, 3, 5, 7, 9]
    if not isinstance(k, int): return False
    k_string = str(k)
    k_list = list(k_string)
    if k_list[-1] is even:
        return True
    return False

print(is_even(128135))
print(is_even(-3.58))


### 1.3
def minmax(data): 
    if not data:
        raise ValueError("The input isn't empty")   
    if len(data):
        min = max = data[0]
        for element in data:
            if element > max:
                max = element
            if element < min: 
                min = element
        return min, max
    else:
        print("Empty collection")


print(minmax([12, 8, -1]))
print(minmax([]))

##1.4
def sum_squares(n):
    if not isinstance(n, int) or n <=0:
        raise ValueError("The number must be a posstive number")
    else:    
        result = 0
        for i in range(1,n):
            result += i*i
        return result

print(sum_squares(12))
print(sum_squares(3))
print(sum_squares(-7))

##1.5
def sum_squares(n):
     if not isinstance(n, int) or n <=0:
        raise ValueError("The number must be a posstive number")
     else:
        return sum(i*i for i in range(1,n))

print(sum_squares(3))
print(sum_squares(2))

##Cuz these example don't mostly care about condition, check the valid of input so I will pass them in below exercise 

##1.6-1.7
def sum_squares(n):
    return sum(i*i for i in range(1,n) if i%2==1)

print(sum_squares(3))
print(sum_squares(2))
print(sum_squares(10))

##1.8  abs(-n) - abs(k) = j
#so  n + k = j (k <0)

##1.9
range(50, 90, 10)

##1.10
print((list(range(8, -9 ,-2))))

##1.11 

result = [pow(2,i) for i in range(0,9)]  ## pow(2,i)~2**1, range(0,9)~rang(9)
print(result)

##1.12
import random

def choice(data):
    return data[random.randrange(0, len(data))]  # Noted that if stop parameter is n, it does not include n in returned randrange

data = [4,5,6,7,1]
print(choice(data))

data = (1.2, -3, 6, 8, 5, 0)
print(choice(data))

##1.13

##Check the len, half len of list
##Assigne new value for a half of list via loop
## Method 1:
def reorder(data):
    lenght = len(data) 
    half_len = lenght // 2
    tmp = 0
    for i in range(lenght):
        if i <= half_len:
            tmp = data[i]
            data[i] = data[lenght -i -1] 
            data[lenght - i - 1] = tmp
            i += 1

return data

print(reorder([0, 1, 2, 3, 4]))

## Method 2：
def reorder(data):
    lenght = len(data) 
    half_len = lenght // 2
    tmp = 0
    for i in range(lenght):
        if i <= half_len:
            data[i], data[lenght - i -1] = data[lenght - i -1], data[i]
            i += 1
    return data


print(reorder([0, 1, 2, 3, 4]))

## Method 3:
def reorder(data):
    n = len(data)
    return [data[n - 1 - i] for i in range(0, n)]

print(reorder([0, 1, 2, 3, 4]))

##1.14

def check_odd(data):
    result = []
    for i in range(len(data)):
        for k in range(i + 1, len(data)):
            if i != k and data[i]*data[k] %2 == 1:
                result.append((data[i], data[k])) 
    return result

print(check_odd([0, 1, 2, 3, 4]))

## Other method is check all the odd:

def check_odd(data):
    result = [ i for i in data if i % 2 == 1]
    return True if len(result) > 1 else False

print(check_odd([0, 1, 2, 3, 4]))

##1.15

#Method 1: 
def check_number(data):
    result = []
    for i in range(len(data)):
        for k in range(i + 1, len(data)):
            if data[i] == data[k]:
               return False 
    return True

print(check_number([0, 1, 2, 3, 4]))
print(check_number([1, 1, 1, 1]))

#Method 2:
def is_unique(data):
    return True if len(data) == len(set(data)) else False

print(is_unique([0, 1, 2, 3, 4]))
print(is_unique([1, 1, 1, 1]))

#Method 3:
def is_unique(data):
     return True if data[0] == data [1] else False

print(is_unique([0, 1, 2, 3, 4]))
print(is_unique([1, 1, 1, 1]))

## 1.16
##Although it does not change the value of immutable, but scale creats a new instance, which reassign data[j] value. 
##So we have the new actual parameter.

## 1.17
## Nope. Cuz the function just creat a new instance, it doesn't clearly effect the original list

## 1.18
print([ n*(n+1) for n in range(0, 10)])

## 1.19
print([ chr(n) for n in range(97, 123)])

## 1.20
## Method 1:
import random

def shuff_funcition(data):
      length = len(data)
      index = []
      len_index = 0
      while len_index < length:
        num = random.randint(0, length - 1)
        if num not in index:
          index.append(num)
          len_index = len(index)
      return [data[j] for j in index]

print(shuff_funcition([1, 2, 3, 4, 5, 6, 7, 8, 9]))

## Method 2:
import random

def shuff_funcition(data):
  length = len(data)
  i = 0
  while i < length - 1:
    j = random.randint(i + 1, length - 1)
    data[i], data[j] = data[j], data[i] 
    i += 1
  return data

print(shuff_funcition([1, 2, 3, 4, 5]))

## Method 3:
import random

def shuff_funcition(data):
  length = len(data)
  for i in range(0, length - 1, 1):  ## Use for loop to save some code like:
    j = random.randint(i + 1, length - 1)
    data[i], data[j] = data[j], data[i] 
  return data

print(shuff_funcition([1, 2, 3, 4, 5]))

##1.21

## Refer from a method
def print_reverse() -> None:
    lines = []
    while 1:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    for line in reversed(lines):
        print(line)
print_reverse()

##1.22 OR use zip(a,b)
def dot_product(a, b):
  length = len(a)
  return [a[i]*b[i] for i in range(length)]

a = [1, 2, 3]
b = [4, 5, 6]
print(dot_product(a,b))

##1.23
def example(a, b):
  length = len(a)
  ab = a + b
  try:
    s= [a[i]*a[i + length] for i in range(2*length) if i < length - 1]
  except IndexError:
    print("Don't try buffer overflow attacks in Python!")

a= [1, 2, 3]
b = [4, 5, 6]
print(example(a,b))

##1.24
def count_vowels(s):
  vowels = ['a', 'o', 'e', 'u', 'i']
  return len([char for char in s.lower() if char in vowels])  #Make sure just have lowercase

print(count_vowels("Don’t try buffer overflow attacks in Python!"))

##1.25
#Method 1:
def remove_punctuation(s):
  lenght = len(s)
  string =""
  copy = [s[i] for i in range(lenght) if s[i].isalpha() or s[i].isspace()]
  for j in range(len(copy)):
    copy[j] = str(copy[j])
    string += copy[j]
  print(type(string)) 
  return string

print(remove_punctuation("Let's try, Mike."))

#Method 2:
def remove_punctuation(s):
  lenght = len(s)
  copy = [s[i] for i in range(lenght) if s[i].isalpha() or s[i].isspace()]
  return ''.join(copy)        #use '' to imply don't separate each character 

print(remove_punctuation("Let's try, Mike."))

##1.26

def check_formula(a,b,c):

  print("a=b+c is True") if a == b + c else print("a=b+c is False")
  print("a=b-c is True") if a == b - c else print("a=b-c is False")
  print("a*b == c is True") if a*b == c else print("a*b == c is False")
  


check_formula(1,2,3)
check_formula(0,0,0)

##1.27
#Method 1:
def factor(n):    # The worst fashion
  k = 1
  while k <= n:
    if n % k == 0:
        yield k
    k += 1
  

print(list(factor(12210)))

#Method 2:
def factor(n):
  k = 1
  larger = []
  while k*k < n:
    if n % k == 0:
      yield k
      larger.append(n // k)
    k += 1
  if k*k == n:
    yield k
  for num in larger:
    yield k

print(list(factor(12212220146612220)))

## 1.28
def norm(v, p = 2):
  return sum(v[i]**p for i in v)**(1/p)

print(norm([1, 2], 2))

## 1.29
#Method 1: 6 nets loop ===> the worst fashion but I have no idea for recursion
def make_string():
  chars = ['c', 'a', 't', 'd', 'o', 'g']
  strings = []
  count = 0
  for i in range(6):
    for j in range(6):
      if j == i:
        continue         # Use continue to make sure the next index is different with the previous index
      else: 
        for k in range(6): 
          if k == i or k == j:
            continue
          else:
            for l in range(6): 
              if l == i or l == j or l == k:
                continue
              else:
                for m in range(6): 
                  if m == i or m == j or m == k or m == l:
                    continue
                  else:
                    for n in range(6): 
                      if n == i or n == j or n == k or n == l or n == m:
                        continue
                      else:
                        print(chars[i], chars[j], chars[k], chars[l], chars[m], chars[n], sep ='', end=' ')

make_string()
  
#Meththod 2: reference from wdlcameron
def recursion(sub_data, string):
    if len(sub_data) == 1: 
        print (''.join(list(map(str, string+sub_data))), end = ',')
        return
    else:
        for i in range(len(sub_data)):
            new_subdata = [sub_data[x] for x in range(len(sub_data)) if x!=i] #Make a list with everything but your current item
            recursion(new_subdata, string+ [sub_data[i]])
            
            
def all_combos(data):
    recursion(list(data), [])
       
all_combos('abc')


## 1.30
#Method 1:
import math

def find_log2(number):
    return int(math.log(number, 2))

print(find_log2(6))

#Method 2: with recursion

def find_log2(n):
    if n < 2:
      return 0
    else:
      return 1 + find_log2(n // 2) 

print(find_log2(9))

## 1.30
def make_change(n, m):
  coins = [1, 5, 10, 25, 50, 100]
  change_coins = n - m
  make_coins(coins, change_coins)


def make_coins(list_money, money):
  len_list = len(list_money)
  for i in range(len_list):
    if money >= list_money[-1 - i]:
      count, money = divmod(money, list_money[-1 - i])
      print(f"Use {list_money[-1-i]} $: {count} coin(s)")
      
make_change(278, 10)


#After review code
def make_change(n, m):  
  coins = [1, 5, 10, 25, 50, 100]
  if n > m:
    change_coins = n - m  
  else:
    return print("Money charged must be greater than money given")
  make_coins(coins, change_coins)


def make_coins(list_money, money):
  coin_word = ''
  for i in reversed(list_money):                       #Loop reverse funcition to make sure use at least the coins
    if money >= i:
      count, money = divmod(money, i)
      coin_word = "coin" if count == 1 else "coins"    #Define use s for coin word
      print(f"Use {i} $: {count} {coin_word}")
      
make_change(278, 10)

##1.32
import math
def make_calculate():
    a = float(input())
    calculate = input()
    b = float(input())
    print('=')
    symbol = ['+', '-', '*', '/']
    operator = [a+b, a-b, a*b, a/b]
    for i in range(len(symbol)):
      if calculate == symbol[i]:
        return print((operator[i]))
     
    
make_calculate()

##1.33
def calculate():
    print("""Welcome to handheld calculator
    You can perform the following operation:
    + <value> : Add
    - <value> : Subtract
    * <value> : Multiple
    / <value> : Divide
    reset     : Reset the calculator
    exit      : Exit the program
    """)
    result = 0 
    while True:
        strings = input('Enter operation: ')
        exp = None
        if strings == 'exit':
            break
        elif strings == 'reset':
            result = 0
        elif len(strings) == 3:
            exp, number = map(str, strings.split())
            number = int(number)
            if exp == '+':
                result = result + number
                print(f'Result: {result}')
            elif exp == '-':
                result = result - number
                print(f'Result: {result}')
            elif exp == '/':
                result = number/result
                print(f'Result: {result}')
            else:
                result = number*result
                print(f'Result: {result}')
        else:
            raise TypeError("Must type expression with value")

calculate()
##1.34
# Before review code
import random

def make_mistakes(m):
    string = "I will never spam my friends again."
    tmp = str(string)
    words = string.split(' ') 
    copy = list(words)                     # Make a list of words
    length = len(words)
    list_number = make_listrandom(m)
    print(list_number)
    for i in range(1,m+1):
        if i in list_number:
            num = random.randint(0, length-1)
            words[num] = make_word(words[num])
            print(' '.join(words) + "-->mistake sentence")
            words = list(copy)
        else:
            print(string)

def make_listrandom(number):             # Make a list random sentence
    random_sentence = []
    length = 0
    while length < 8:
        num = random.randint(1, number)
        if num not in random_sentence:
            random_sentence.append(num)
            length = len(random_sentence)
    return random_sentence
        
def make_word(word):
    change_word = list(word)
    change_word[random.randint(0,len(change_word)-1)] = chr(random.randint(97,122))
    return ''.join(change_word)

    

make_mistakes(20)

#After review code =>> use random.sample(range(1, m+1), 8)

##1.35
import random
def check_birthday(brithdays):                    # Check duplicate brithday
  person_brithday = set()
  for j in range(len(brithdays)):
    if brithdays[j] in person_brithday: return True
    else: person_brithday.add(brithdays[j])
  return False

def brithday_paradox(n, try_time):                              
  count_true = 0
  for j in range(try_time):
    brithdays = []                              # Create a random list brithdays of n persons with each time call brithdays list, it must be refresh
    for i in range(n): 
      month = random.randint(1, 12)
      date = random.randint(1, get_date(month))
      brithdays.append((month, date))
    if check_birthday(brithdays):
      count_true += 1
  return count_true/ try_time

def get_date(month):                                # Get date from the different month
  if month in (1, 3, 5, 7, 8, 10, 12):
    return 31
  elif month == 2:
    return 28
  else:
    return 30 

def print_result():
  for n in range(5, 101, 5):
    print(f'The probability that two people in a room with {n} persons have the seem brithay is {brithday_paradox(n, 100 )}')


print_result()




##1.36
#Before review code
def count_word():
  strings = input("Type your input: ")
  list_str = list(strings)
  dic_word = {}
  for i in list_str:                             # Use while loop still empty
    if list_str:                                 # We can delete it cuz for loop will break if it is a empty list
      end = recursion(list_str, 0, dic_word)
      del list_str[0 : end]
    else:
      break
  return dic_word

def recursion(list_str, num, dic):
  word_temp = []                                # Consider check condition which delete non-alphabet
  while num < len(list_str) and not list_str[num].isspace():
      word_temp.append(list_str[num])
      num += 1
  key = ''.join(word_temp)
  if key not in dic:
      dic[key] = 1
  else: 
      dic[key] = dic[key] + 1  
  return (num + 1)
print(count_word())

#Afer review code
def count_word():
  list_str = list(strings.lower())                  # Change lowercase
  list_str = list(strings)
  dic_word = {}
  while list_str:
    end = recursion(list_str, 0, dic_word)
    del list_str[0 : end]
  return dic_word

def recursion(list_str, num, dic):
  word_temp = []
  while num < len(list_str) and list_str[num].isspace():   # Check non-alphabet
      num += 1
  while num < len(list_str) and not list_str[num].isspace():
      word_temp.append(list_str[num])
      num += 1
  key = ''.join(word_temp)
  if key not in dic:
      dic[key] = 1
  else: 
      dic[key] = dic[key] + 1  
  return (num + 1)
print(count_word())

  





  

