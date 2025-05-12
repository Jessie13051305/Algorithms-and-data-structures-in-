#2.1 Google Map, Microsoft, Gmail
#2.2 Facebook
#2.3 Notepad doesn't show some function like: get_text(), revise_text() and so on.
#2.4
class Flower:
  def __init__(self, name = "Unknow", petal = 0, price = 0):
    """ Initialize a Flower instance"""

    """ Check type and through raise if the input doesn't expect"""
    if not isinstance(name, str):
      raise TypeError("Name must be a string")
    if not isinstance(petal, int) or petal < 0:
      raise TypeError("Petal must be a positive")
    if not isinstance(price, float) or price < 0:
      raise TypeError("Price must be a float")

    self._name = name
    self._petal = petal
    self._price = price

  def get_name(self):
    return self._name

  def get_petal(self):
    return self._petal

  def get_price(self):
    return self._price

if __name__ =='__main__':
  u = Flower('Roses', 12.5, 14 )
  print(u.get_name())

#2.5 To make code clearly, we should check with int and float
    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        try:
           isinstance(price, (int, float))
        except TypeError:
            print("The price must be a number")     #Check the type of price
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        try:
           isinstance(amount, (int, float))
        except TypeError:
           print("The amount must be a number")
        self._balance -= amount
#2.6 
    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        """ Check with non-negative number"""

        if not isinstance(amount, (int, float)): 
            raise TypeError("The amount must be a number")
        elif amount < 0:
          raise ValueError("The amount must be a positive")
        else:
          self._balance -= amount
#2.7
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance = 0):        #Constructor is __init__
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer ('John')
        bank     the name of the bank ('California Savings')
        acnt     the acount identifier ('5523563...')
        limit    credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
#2.8
 for val in range(1,17):     #The first Credit Card go to over limit
        wallet[0].charge(20*val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
#2.9 
    def __sub__(self, other):
        """Return subtract of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
#2.10
    def __neg__(self):
        """Return neg vector"""
        result = Vecto(len(self))
        for j in range(len(self)):
            result[j] = - self[j]
        return result
#2.11 Because __add__ will check the first element, should use __radd__
#2.12
    def __mul__(self):
      """Return v*3 vector"""
      result = Vecto(len(self, value))
      for j in range(len(self)):
        result[j] = self[j] * value
      return result

#2.13
    def __rmul__(self, value):
      return self.__mull__(value)
#2.14
    def __mul__(self, other):
      """Return a dot product of the vector"""
      if len(self) != len(other):
        raise ValueError("dimensions must agree")
      result = 0
      for j in range(len(self)):
        result += self[j]* other[j]
      return result

#2.15

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0]*d      #Make a list with len(d) and all elements are zero
        else:                         #Check it non-iterable
            try:
                self._coords = list(d)
            except TypeError:
                raise TypeError("The input must be a iterable or interger")
#2.16 """(stop-start) equals all the numbers from start to (stop-1), plus (step-1) to ensure that the total value exceeds stop, 
#        but is not yet the value of the nearest step after stop. So that when //stepping, there is no missing space
#        and make sure the result is non-negative max(0, x)"""

#2.17 object have three class 1. Goat 2. Pig 3. Horse (-->Racer and Equestrian class)

#2.18
  
    def __getitem__(self, n):
        """Get the value in n index"""
        if n < 1:
            raise ValueError("The number must be greater than 0")
        else:
            print([str(next(self)) for j in range(n+1)][n-1])

if __name__ == '__main__':
    print("The 8th value:")
    print(FibonacciProgression(2, 2).__getitem__(8))

#2.19
    def _gettime(self, factor):
            return (factor - self._current)//self._increment - 1



if __name__ == '__main__':
    print("The 8th value:")
    print(FibonacciProgression(2, 2).__getitem__(8))
    print(f"The number of call to next reach 2**63 is: { ArithmeticProgression(128,0)._gettime(2**63)}")
 
#2.20 Many methods are overlapped, making it difficult to call functions, rewriting the extension structure many times. Becarefull with extend method
#2.21 Each extend subclass must be define new method, make confused to reuse code

#2.22
from abc import ABCMeta, abstractmethod   # need these definitions

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val founld in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True               # found match
        return False
    
    def index(self, val):
        """Return the leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in sequence")     #never found a match

    def count(self, val):
        """Return the number of elements equal to give value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    
    def __eq__(self, other):
        """Return True if the two sequence are elemnt by element quivalent"""
        if len(self) != len(other): return False            #Make sure if the first sequence longer but have a lot of characters seem the seconde sequence
        else:
            for j in range(len(self)):
                if self[j] != other[j]:
                    return False
            return True

class SubclassSequence(Sequence):
    """Iterator producing a generalized Sequence."""

    def __init__(self, data):
        self._data = data
    
    def __len__(self):
        """Return the length of sequence"""
        return len(self._data)
    
    def __getitem__(self, j):
        """Return the element of sequence"""
        return self._data[j]


m = SubclassSequence('HelloWorld').__len__()
print(m)
m1 = SubclassSequence('Hello')
m2 = SubclassSequence('Hello')
print(m1 == m2)

#2.23 Before review code
  def __lt__(self, other):
        """Return True if sq1 < sq2"""
        if not isinstance(other, Sequence):
            raise TypeError('The second parameter must agree type')
        else: 
            j = 0
            if len(self) < len(other):
                while j < len(self):  
                    if self[j] > other[j]:
                        return False 
                    elif self[j] < other[j]:
                        return True 
                    else:
                        j += 1 
                return True                    # The seq2 contains seq1      
            else:
                while j < len(other):  
                    if self[j] > other[j]:
                        return False 
                    elif self[j] < other[j]:
                        return True 
                    else:
                        j += 1 
                return False                    # The seq1 contains seq2

      #We can determine any seq contain other by check len of them, afrer review code:
  def __lt__(self, other):
        """Return True if sq1 < sq2"""
        if not isinstance(other, Sequence):
            raise TypeError('The second parameter must agree type')
        else: 
            length = min(len(self), len(other))    #Make sure not out of range
            for j in range(length):  
                if self[j] > other[j]:
                    return False 
                elif self[j] < other[j]:
                    return True 
            return len(self) < len(other)          #Determine any seq contains other  
#2.24
#EbookReader:
#     1. EBook:     _namebook, _nameauthor, _price
#                    get_infor(), search(), view(), get_price()
#     2. User(Ebook):_account, _library
#                    buy(), remove(), save(), count_book(), read(), view() 
# 2.25       
def __mul__(self, other):
      """Return a dot product of the vector or a new vecto"""
      if isinstance(other, (int, float)):
        return Vector([self[j]*other for j in range(len(self))])               # Create a new vecto with v*OTHER via Vector type

      elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            else:
                return sum((self[j]*other[j] for j in range(len(self))))       # Compute a dot product of two vecto
      else:
            raise TypeError('The input must be vector or a number')
          
#2.26
class ReversedSequenceIterator:
    """An iterator for any of Python's  sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  #Keep a reference to the underlying
        self._k = len(sequence)
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1 
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """Return ifself as an iterator"""
        return self

m = ReversedSequenceIterator('hello')
print(next(m))
print(next(m))
k = ReversedSequenceIterator('Go to styding abroad')
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(iter(k))

#1.27
class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance"""

        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1)// step)

        # need knowledgee of start and step and stop to support __getitem__
        self._start = start
        self._step = step
        self._stop = stop    # for __containt__
    
    def __len__(self):
        """Return number of entries in the range."""
        return self._length
    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if nagative)"""
        if k < 0:
            k += len(self)
        if not 0 <= k < len(self):
            raise ValueError('index out of range')
        
        return self._start + k*self._step
    
    def __contains__(self, value):
        """Return True if value is in Range"""
        if not self._start <= value < self._stop:
            return False
        else:
            if (value - self._start) % self._step == 0: 
                return True
        return False

m = Range(0, 2000000, 100)
print(1000 in m)
print(pow(1 + 0.0825, 1/12))
        
#2.28
from time import strftime, gmtime
## Superclass
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer ('John')
        bank     the name of the bank ('California Savings')
        acnt     the acount identifier ('5523563...')
        limit    credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
        self._count_charge = 0
        self._times = strftime('%b %Y', gmtime())   # get current time include month and year
    
    ### Subclass
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied
    """
        if self._times != strftime('%b %Y', gmtime()):   #check current time make sure the charge in a month
            self._times = strftime('%b %Y', gmtime())
            self._count_charge = 0
        success = super().charge(price)  #call inherited method

        if not success:
            self._balance += 5           # assess penalty
        else:
            self._count_charge += 1
            self._balance += 1 if self._count_charge > 10 else 0       #Greater than 10 call charge will add 1$ each addition call
        return success

#2.29
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
     
    def __init__(self, customer, bank, acnt, limit, apr, per, late_fee):
        """Create a new predatpry credit card instance:

        The initial balance is zero
        customer name 
        bank the name of the bank
        acnt the acount identifier
        limit credit limit
        apr annual percentage rate
        per a percentage of the balance must pay before next monthly cyle
        late_fee assess if the customer does not subsequently pay that minumum amount
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._per = per
        self._late_fee = late_fee
        self._create_time = datetime.datetime.now()  #get the current time like 2025-03-07 13:15:42.918850        

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied
    """
        if self._times != strftime('%b %Y', gmtime()):   #check current time make sure the charge in a month
            self._times = strftime('%b %Y', gmtime())
            self._count_charge = 0
        success = super().charge(price)  #call inherited method

        if not success:
            self._balance += 5           # assess penalty
        else:
            self._count_charge += 1
            self._balance += 1 if self._count_charge > 10 else 0       #Greater than 10 call charge will add 1$ each addition call
        return success

    def process_month(self):
        """Assess monthly interst on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1+ self._apr, 1/12)
            self._balance *= monthly_factor
    
    def payment_month(self, value):
        """Monthly payment: a percentage of the balance
           Value: the payment the user pay in this monthly"""

        minumum_payment = self._per*self._balance
        actual_payment = max(minumum_payment, value)
        current_time = datetime.datetime.now()
        count_month = (current_time.year - self._create_time.year)*12 + (current_time.month - self._create_time.month) + 1
        
        if minumum_payment > value:
            raise ValueError('Must pay a minimum per of the balance')
        else:
            total_due = actual_payment + (late_fee*count_month if count_month > 1 else 0)
            if self._balance < total_due:       # check ._balance whether pay
                raise ValueError("The balance isnt enough to pay")
            else:
                self._balance -= total_due
                self._create_time = current_time

m = PredatoryCreditCard('John', 'California Savings', '5319 0237 4563 1235', 2500, 0.085, 0.05, 200)
print(m.charge(200))
print(m._balance)
print(m.get_balance())
m.payment_month(100)
print(m.get_balance())

#2.30
def _set_balance(self, money):
        """Change the balance without directly access _balance data member"""
        if isinstance(money, (int, float)):
            raise TypeError('Money must be a non-nagative number')
        self._balance = money         #In subclass, use _set_balance(money) to access _balance without directly access it

#2.31

class TheAbsoluteValue(Progression):
    """Iterator producing a set of the absolute value of the difference between the previous two values"""
    def __init__(self, frist = 2, second = 200):
        """Create a new set of the absolute value of the difference between the previous two values
         first the frist item
        second the second item
        """
        super().__init__(frist)
        self._next = second
    def _advance(self):
        """Update current value by taking the absolute value between them"""
        self._current, self._next = self._next, abs(self._current - self._next)

#2.33
import math
class TheSquareRoot(Progression):
    """Iterator producing a set of the absolute value of the difference between the previous two values"""
    def __init__(self, frist = 65536):
        """Create a new set of the absolute value of the difference between the previous two values
         first the frist item
        second the second item
        """
        super().__init__(frist)
    def _advance(self):
        """Update current value by taking the absolute value between them"""
        self._current = math.sqrt(self._current)

#2.34
#Before
def first_derivative():
    polynomial = input("Type polynomial (defined by ax^n and use space in expression):")
    firstderivative = []
    coefficient = str()
    exsponent = str()
    list_polynomial = polynomial.split(' ')
    for i in range(len(list_polynomial)):
        if i % 2 == 0:                                             # Define ax^n 
            if len(list_polynomial[i]) == 1:
                temp = 0 if list_polynomial[i] == 'x' else 0       # if constant is 0 or x is 1

            elif len(list_polynomial[i]) == 2:                     # degree is 1: ax
                temp = list_polynomial[i][0]
            else:
                coefficient, exsponent = map(int, list_polynomial[i].split('x^'))
                temp = str(coefficient*exsponent) + 'x^' + str(exsponent-1)
        else:                                                      # Expression +, -
            temp = list_polynomial[i]
        firstderivative.append(str(temp))

    if firstderivative[-1] == '0':                                 # Delete the consant and expression in last list
        del firstderivative[-2:]
    return (' ').join(firstderivative)


print(first_derivative())
        
# After 
# def first_derivative():
    polynomial = input("Type polynomial (defined by ax^n and use space in expression):")
    firstderivative = []
    coefficient = str()
    exsponent = str()
    list_polynomial = polynomial.split(' ')
    for i in range(len(list_polynomial)):
        length = len(list_polynomial[i])
        if i % 2 == 0:                                             # Define ax^n 
            if length == 1:
                temp = 0 if list_polynomial[i] == 'x' else 0       # if constant is 0 or x is 1

            elif length == 2:                                      # degree is 1: ax
                temp = list_polynomial[i][0]

            elif length == 3:                                       # define x^n
                temp = str(list_polynomial[i][-1]) + 'x^' + str(int(list_polynomial[i][-1])-1)

            else:
                coefficient, exsponent = map(int, list_polynomial[i].split('x^'))
                temp = str(coefficient*exsponent) + 'x^' + str(exsponent-1)

        else:                                                       # Expression +, -
            temp = list_polynomial[i]
        firstderivative.append(str(temp))
    if firstderivative[-1] == '0':                                 # Delete the consant and expression in last list
        del firstderivative[-2:]
    return (' ').join(firstderivative)

    print(first_derivative())
        
#2.35
# Before
# import matplotlib.pyplot as plt

    def count_alphabet():
        file = input('Input file name: ')
        with open(file, 'r', encoding='utf-8') as fp:         # instead fp = open(file, 'r', encoding = 'utf-8') and automally close file
            alphabet = {}
            characters = [0] * 26
            frequencies = [0] * 26
            for line in fp:
                for char in line:
                    if char.isalpha():                                # focus alpha character
                        char_caplock = char.upper()
                        if char_caplock not in alphabet:
                            alphabet[char_caplock] = 1
                        else:
                            alphabet[char_caplock] += 1

        for key, value in alphabet.items():                                # Sort the alphabet
            characters[(ord(key) - 65)] = key
            frequencies[(ord(key) - 65)] = alphabet[key]
        
        #Vertical bar plots
        plt.bar(characters, frequencies, color='lightgreen')
        plt.xlabel('Alphabet Character')
        plt.ylabel('Number of Character')
        plt.title('Bar chart plot of the frequencies of each alphabet character')
        plt.show()
    


    count_alphabet()
#After
    import matplotlib.pyplot as plt

    def count_alphabet():
        file = input('Input file name: ')
        characters = []
        frequencies = []
        with open(file, 'r', encoding='utf-8') as fp:         # instead fp = open(file, 'r', encoding = 'utf-8') and automally close file
            alphabet = {}
            for line in fp:
                for char in line:
                    if char.isalpha():                         # focus alpha character
                        char_caplock = char.upper()
                        alphabet[char_caplock] = alphabet.get(char_caplock, 0) + 1  # get method to get value by char_caplock key, if not return 0

        sorted_alphabet = sorted(alphabet.items())            # Sort the alphabet by the first item in each element (key) after get items return a tuple in a list
        characters = [key for key, value in sorted_alphabet]
        frequencies = [value for key, value in sorted_alphabet]
        
        #Vertical bar plots
        plt.bar(characters, frequencies, color='lightgreen')
        plt.xlabel('Alphabet Character')
        plt.ylabel('Number of Character')
        plt.title('Bar chart plot of the frequencies of each alphabet character')
        plt.show()
    

    count_alphabet()

#2.35
import random

class AliceBot():
    """Iterator Alicebot"""

    #Use a likelihood value 0.3 not to larger to make sure Alice can creat or not creat packets
    LIKELIHOOD_VALUE = 0.3
    def __init__(self):
        """Create a new packets"""
        self._currentpacket = None
    
    def get_packet(self):
        if self.check_create():
            self._currentpacket = self.create_packet()
        return (f'Alice create packets named {self._currentpacket}')
    
    def check_create(self):
        return random.random() <= self.LIKELIHOOD_VALUE

    
    def create_packet(self):
        length = random.randint(4,10)
        # return a list of packets character with randint from A to Z (included)
        packet_name = [chr(random.randint(65, 90)) for _ in range(length)]
        return ('').join(packet_name)

    def delete(self):
        self._currentpacket = None

class Internet():
    """Check and delivery whether has packets from Alice"""
    def __init__(self):
        self._packet = None
    
    # Access the currentpacket in Alice class to check the packets
    def check_alice(self):
        if alice._currentpacket:
            self._packet = alice._currentpacket
            alice.delete()
            return(f'Check to have packets {self._packet}')
        return f'Not packets'
    
    def delivery(self):
        if self._packet:
            return(f'Delivery {self._packet} from Alice to Bob')
        else:
            return('Not delivery any packets')

class BodBot():
    """Check, read and remove packet"""

    def __init__(self):
        self._get_packet = None
    
    def check_delivery(self):
        if ship._packet:
            self._get_packet = ship._packet
            ship._packet = None
            return (f'Bob has packets from Alice is {self._get_packet}')
        else:
            return ('Bob doesnt receive packets from Alice')
    
    def read_remover(self):
        if self._get_packet:
            return (f'Bod read and removed packets {self._get_packet} from Alice')
        else:
            return ('Bod doesnt read and remove any packets')

if __name__== '__main__':
    alice = AliceBot()
    ship = Internet()
    bod = BodBot()
    for i in range(2):
        print(f'Time {i}: ')
        print(alice.get_packet())
        print(ship.check_alice())
        print(ship.delivery())
        print(bod.check_delivery())
        print(bod.read_remover())
    
#2.36
import random

class Animal():
    """Iterator animal"""

    def __init__(self, name):
        """Create a bear"""
        self._animal = name
    
    def get_animal(self):
        return self._animal
    
class Fish(Animal):
    """"Iterator fish"""    

    def __init__(self):
        """"Create a fish"""
        super().__init__('F')

class Bear(Animal):
    """"Iterator bear"""    

    def __init__(self):
        """"Create a bear"""
        super().__init__('B')

class NoneType(Animal):
    """"Iterator nonetype"""    

    def __init__(self):
        """"Create a nonetype"""
        super().__init__('-')
    
class River():
    """Create a ecosystem list"""   
    def __init__(self, length):
        """length   the number of index
           system   the list name
        """
        self._length = length
        self._system = []

    def create_system(self):
        #Random the number of each type and create a list
        self._system = [random.choice([Bear(), Fish(), NoneType()]) for i in range(self._length)]
        
        #Reoders the elements of the system list
        random.shuffle(self._system)
    
    def __str__(self): #use __str__ not str
        return ('').join([self._system[k].get_animal() for k in range(len(self._system))])[1:-1]
    
    def move_system(self):
        for i in range(self._length):
            print(self.__str__())     
            temp = i
            i += random.randint(-1, 1)
            # Check the first and the last index
            if 0 <= i < self._length:
                if isinstance(self._system[i], NoneType):          # if the next index is NoneType, must be change value
                    self._system[i] = self._system[temp]
                    self._system[temp] = NoneType()
                elif isinstance(self._system[i], type(self._system[temp])):
                    for j in range(len(self._system)):
                        if isinstance(self._system[j], NoneType):   # self._system[i] is a instance, not a type so dont write self._system[j] == type(NoneType()
                            self._system[j] = self._system[temp] 
                            break
                elif isinstance(self._system[i], Fish) and isinstance(self._system[temp], Bear):
                    self._system[i] = NoneType()
                elif isinstance(self._system[temp], Fish) and isinstance(self._system[i], Bear):
                    self._system[temp] = NoneType()

if __name__ == '__main__':
    new = River(100)
    new.create_system()
    print(new.__str__())
    new.move_system()


#3.37 Review code: 
# Do not create NoneType, 
# We can directly assign current_value = self._system[i] instead temp = i. The loop refresh new value of i, but the loop will run with iterator
    
 
import random

class Animal():
    """Iterator animal"""

    def __init__(self, name):
        """Create a animal with gender and strength, dont create a method because this value will change every each called new instance"""
        self._animal = name
        self._gender = random.choice([False, True])
        self._strength = random.randint(1,100)

    
    def get_animal(self):
        return self._animal
    
class Fish(Animal):
    """"Iterator fish"""    

    def __init__(self):
        """"Create a fish"""
        super().__init__('F')

class Bear(Animal):
    """"Iterator bear"""    

    def __init__(self):
        """"Create a bear"""
        super().__init__('B')

class River():
    """Create a ecosystem list"""   
    def __init__(self, length):
        """length   the number of index
           system   the list name
        """
        self._length = length
        self._system = []

    def create_system(self):
        #Random the number of each type and create a list
        self._system = [random.choice([Bear(), Fish(), None]) for i in range(self._length)]
        
        #Reoders the elements of the system list
        random.shuffle(self._system)
    
    def __str__(self): #use __str__ not str
        return ('').join([self._system[k].get_animal() if isinstance(self._system[k], Animal) else '-' for k in range(len(self._system)) ])[1:-1]
    
    def move_system(self):
        for i in range(self._length):
            print(self.__str__())     
            if self._system[i] is None:
                pass
            else:
                temp = i
                i += random.randint(-1, 1)
                # Check the first and the last index
                if 0 <= i < self._length:
                    if self._system[i] is None:          # if the next index is NoneType, must be change value
                        self._system[i] = self._system[temp]
                        self._system[temp] = None
                    elif type(self._system[i]) == type(self._system[temp]):
                        if self._system[i]._gender != self._system[temp]._gender:
                            for j in range(len(self._system)):
                                if self._system[j] is None:   # self._system[i] is a instance, not a type so dont write self._system[j] == type(NoneType()
                                    self._system[j] = self._system[temp] 
                                    break
                        else:
                            if self._system[temp]._strength > self._system[i]._strength:
                                self._system[i] = None
                            elif self._system[i]._strength < self._system[temp]._strength:
                                self._system[temp] = None
                            else:
                                pass

                    elif isinstance(self._system[i], Fish) and isinstance(self._system[temp], Bear):
                        self._system[i] = None
                    elif isinstance(self._system[temp], Fish) and isinstance(self._system[i], Bear):
                        self._system[temp] = None

if __name__ == '__main__':
    new = River(100)
    new.create_system()
    print(new.__str__())
    new.move_system()

#2.38
import requests
import json

class User():
    """Create user information"""

    def __init__(self, name):
        self._name = name
        self._list = []

    def get_name(self):
        return self._name
     
    def view_list(self):
        if self._list:
            for i in range(len(self._list)):
                print(self._list[i])
        else:
            raise ValueError('No book to show')

    
class Book():
    """Create the books information from create a API key in google console (google books)"""
    API_KEY = 'AIzaSyBiN18C6-MXQQVxgDEuI0-QRQQRPeHL***'
    URL = 'https://www.googleapis.com/books/v1/volumes'
    

    def __init__(self, query):
        self._query = query
        self._title = None
        self._authors = None
        self._description = None
        self._amount = None # use None type to avoid the second call search() will display self._amount
        self._currency = None 
  
    def search(self):
        # Check amount if it exists, not wil update and avoid to miss this value
        if self._amount is not None:
            return self._amount
        
        params = {'q': self._query, 'key': self.API_KEY, 'langRestrict':'en'}
        # Pass the real parameter in URL
        reponses = requests.get(self.URL, params = params)

        if reponses.status_code == 200:
            # change the result by json from and show it in terminal
            data = reponses.json()
            items = data.get('items', ())
            # the result which we want to find in the items
            if items:
                for i in range(len(items)):
                    # both volumeInfo and saleInfor in same filed in items
                    volumeInfo = items[i].get('volumeInfo', {})
                    language = volumeInfo.get('language')
                    saleInfo = items[i].get('saleInfo', {})

                    # Just show off with the named english book
                    if language == 'en':
                        self._title = volumeInfo.get('title', 'No title')
                        self._authors = volumeInfo.get('authors', [])
                        self._description = volumeInfo.get('description', 'No description')
                        listPrice = saleInfo.get('listPrice', {})
                        self._amount = listPrice.get('amount', 'Not price')
                        self._currency = listPrice.get('currencyCode', 'Not price')
                        return self._amount
        else:
            raise ValueError('Can not find this book')
    
    def display(self):
        """Print the result of search"""
        print('\n'.join([f'Title: {self._title}',
              f'Authors: {', '.join(self._authors)}',
              f'Price: {self._amount} {self._currency}',
              f'Discription: {self._description}'
              ]))
        

class Ebook():
    """Create functions of a ebook reader"""
    def __init__(self, money, book: Book, user):
        self._money = money
        self._book = book
        self._price = book.search()
        self._user = user
    
    def buy(self):
        if self._book._title not in self._user._list:
            if self._price == 'Not price':
                raise ValueError('Can\'t find the price of this book')
            else:
                if self._money >= self._price:
                    self._user._list.append(self._book._title)
                    self._money = self._money - self._price
                    print(f'Bought {self._book._title}!')
                else:
                    raise ValueError("Dont enough money")
        else:
            raise NameError("This book purchased")
   

    def remove(self, other):
        if other in self._user._list:
            for i in range(len(self._user_list)):
                if self._user_list[i] == other:
                    del self._user._list[i]
        else:
            raise NameError('This named book didnt exist')

if __name__ == '__main__':
    alice = User('alice')
    book = Book('Cann\'t hurt me')
    book.search()
    book.display()
    book1 = Book('Deep Work')
    book1.search()
    book1.display()
    ebook = Ebook(300000, book, alice).buy()
    ebook1 = Ebook(500000, book1, alice).buy()
    alice.view_list()


#2.39
from abc import ABCMeta, abstractmethod 

class Polygon(metaclass=ABCMeta):
    """A class compute area and perimeter"""

    def __init__(self, side: list):
        """The sides must be consecutive sides of pylogon"""
        self._side = side

    @abstractmethod
    def perimeter(self):
        """Return perimeter"""

    @abstractmethod
    def area(self):
        """Return area"""

    
class Triangle(Polygon):
    """Compute area and perimeter with 3 sides length"""
    
    def __init__(self, side = [1,1,1]):
        super().__init__(side)
        self._side = side
  
    def perimeter(self):
        return sum(self._side)
        
    def area(self):
        p = self.perimeter()*0.5
        result = p
        for i in self._side:
             result *= (p - i)
        return result**0.5

        
class Quadrilateral(Polygon):
     """Compute area and perimeter with 4 sides length"""
    
     def __init__(self, diagonal, side=[1, 1, 1, 1]):
        super().__init__(side)
        self._side = side
        self._diagonal = diagonal
  
     def perimeter(self):
        return sum(self._side)
        
     def area(self):
        result = 0
        first_triangle = []
        second_triangle = []
        for i in range(len(self._side)):
            for j in range(i + 1, len(self._side)):
                if j % 2 == 1:
                    if abs(self._side[i] - self._side[j]) < self._diagonal < self._side[i] + self._side[j]:
                        first_triangle = [self._side[i], self._side[j], self._diagonal]
                        second_triangle = [self._side[m] for m in range(len(self._side)) if m != i and m != j]
                        second_triangle.append(self._diagonal)

            break
 
        print(second_triangle)
        result = Triangle(first_triangle).area() + Triangle(second_triangle).area()
        return result
 
             

if __name__ == '__main__':
    triangel = Triangle([3, 4, 5])
    print(triangel.perimeter(), triangel.area())
    quadrilateral = Quadrilateral(5, [3, 4, 3, 4])
    print(quadrilateral.perimeter(), quadrilateral.area())









                        









    
    









    
