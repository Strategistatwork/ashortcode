from email._header_value_parser import get_phrase
print("Hello World")
print("I am the Strategist")
phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)
# Changing don't panic in to on tap
for i in range(4):
    plist.pop()
plist.remove("'")
plist.remove("D") 
plist.extend([plist.pop(), plist.pop()]) 
plist.insert(2, " ")
plist.pop(4) 
new_phrase="".join(plist)
print(plist)
print(new_phrase)
vowels=['a','e','i','o','u']
word=input('Enter a word to search for vowels')
found=[]
for letter in word:
    
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found) 
sentence="Six little kitten kept mewing all the time"     
psce=list(sentence)
for twitter in psce[:3]:
    print(twitter)
    print()
for twitter in psce[-1:-5:-1]:
    print('\t'*2,twitter)
    print() 
for twitter in psce[::-1]:
    print('\t'*3,twitter)
    print()
psce.remove("m")    
newsentence=''.join(psce)
print(newsentence)
from fractions import Fraction
print("Hello python")
print("Hello Saithon")
x=8**(1/3)
print(x)
f=Fraction(3,5)
print(f+1+4)
a=2+4j
print(type(a))
b=3+5j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.real)
print(a.imag)
print(a.conjugate())
print("the magnitude of a :",abs(a))
print("Enter something : ")
s=input()
print("you have entered :",s)
r="2"
e=int(r)+2
print(e)      
try:
    v=float(input("Enter a number"))
except ValueError:
    print("you have entered a wrong value")
z=Fraction(input("Enter a fraction"))
print("you have entered: ",z)
try:
    t=complex(input("Enter a complex number: "))
except ValueError:
    print("you have entered a wrong number ")
print("the complex number you've entered is ",t)
print("enter two numbers and find if they can be factored:")  
def is_factor(ru,tu):
    if(tu%ru==0):
        print("Yes",tu," is a factor of ",ru)
    else:
        print("no",tu," ain't no factor of ",ru)       
is_factor(2,1023)
def factors(b):
    for i in range(1,b+1):
        if(b%i==0):
            print(i) 
print("enter a number and find out it's factors: ")
b=input()
b=float(b)
if(b>0 and b.is_integer()):
    factors(int(b))
else:
    print("enter a valid integer..")                    
def multi_table(a):
    for i in range(1,11):
        print('{0}*{1}={2}'.format(a,i,a*i))
        
print("enter a number for multiplication tables : ")
s=input()
s=float(s)
if(s>0 and s.is_integer()):
    multi_table(int(s))
else:
    print("enter a positive integer : ")            
de="{0:.2f}".format(3.1415) 
print(de)

def menu():
    print("choice:1,kilometers to miles")
    print("choice:2,miles to kilometers")
def km_to_miles():
    km=float(input("enter kilometers: "))
    print("miles is equal to :")
    miles=km/1.609
    print("distance in miles:{0}".format(miles))
def miles_to_km():
    miles=float(input("Enter the miles: "))
    print("kilometers is equal to :")
    km=miles*1.609
    print("distance in kilometers:{0}".format(km))
print(menu())
print("which conversion are you going to do :")
choice=input()
if(choice=="1"):
    km_to_miles()                 
if(choice=="2"):
    miles_to_km()
def roots(a,b,c):
    D=(b**2-4*a*c)**0.5
    x_1=(-b+D)/2*a 
    x_2=(-b-D)/2*a 
    print("The first root is :{0}".format(x_1))
    print("The second root is :{0}".format(x_2))
           
a=input("Enter the value of a :")
b=input("Enter the value of b :")
c=input("Enter the value of c :")

roots(float(a),float(b),float(c))
# Even Odd vending machine...
print("Enter a positive integer...")
s=input()
s=float(s)

def vendormachine(num):
    if(num%2==0):
        print("the number is an even number..") 
    else:
        print("the number is an odd number..")    
    for i in range(1,11):
        print(num)
        num+=2        

if(s>0 and s.is_integer()):
    vendormachine(int(s))
else:
    print("enter a valid number..")    
    
def ground_shipping(weight):
    if(weight<=2):
        cost=(weight*1.5)+20
        return cost
    elif(weight>2 and weight<=6):
        cost=(weight*3)+20
        return cost
    elif(weight>6 and weight<=10):
        cost=(weight*4)+20
        return cost 
    elif(weight>10):
        cost=(weight*4.75)+20
        return cost 

print(ground_shipping(8.4)) 

premium_ground_shipping=125

def drone_shipping(weight):
    if(weight<=2):
        cost=weight*4.50
        return cost
    elif(weight>2 and weight<=6):
        cost=weight*9
        return cost
    elif(weight>6 and weight<=10):
        cost=weight*12    
        return cost
    elif(weight>10):
        cost=weight*14.25
        return cost  

print(drone_shipping(1.5))

def cheapest_shipping(weight):
    if(drone_shipping(weight)<ground_shipping(weight) and drone_shipping(weight)<premium_ground_shipping):
        print("The cheapest shipping method is: drone shipping")
        print("It will cost you:$ ",drone_shipping(weight)) 
    if(ground_shipping(weight)<drone_shipping(weight) and ground_shipping(weight)<premium_ground_shipping):
        print("The cheapest shipping method is ground shipping")
        print("It will cost you:$ ",ground_shipping(weight))
    if(premium_ground_shipping<drone_shipping(weight) and premium_ground_shipping<ground_shipping(weight)):
        print("The cheapest shipping method is premium ground shipping") 
        print("It will cost you:$",premium_ground_shipping)

print("Enter the weight of the package:")      
package_weight=int(input())
cheapest_shipping(package_weight)

#Examples of lists and tuples..
simplelst=[1,2,3,4,5,6]
stringlist=["rose","bose","shows"]
emptylist=[]

simpletuple=(1,2,3,4,5,6)
stringtuple=("sambo","simbho","bimbo")

# add elements to the empty list...
emptylist.append(83)
emptylist.append(5)
emptylist.append(22)

print(emptylist)
print(simplelst)
print(stringlist)

print(simpletuple)
print(stringtuple) 
print(simpletuple[-1])

for index,item in enumerate(simpletuple):
    print(index,item)

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price=0
for i in prices:
    total_price+=i
average_price=total_price/len(prices)
print("Average Haircut Price: ",average_price)
new_prices=[price-5 for price in prices]
print(new_prices)
total_revenue=0
for i in range(0,len(hairstyles)):
    total_revenue+=prices[i]*last_week[i]
print("Total Revenue: ",total_revenue)
average_daily_revenue=total_revenue/7
print("Average Daily Revenue: ",average_daily_revenue)
cuts_under_30=[]
for i in range(0,len(new_prices)-1):
    if(new_prices[i]<30):
        cuts_under_30.append(hairstyles[i])
print("Cuts under 30: ",cuts_under_30)
from numpy.random.mtrand import randint
from matplotlib.dates import seconds
toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices=[2,6,1,3,2,7,2]
num_pizzas=len(toppings)
print('We sell',num_pizzas,'different kinds of pizza!')
pizzas=list(zip(prices,toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza=pizzas[0]
priciest_pizza=pizzas[-1]
three_cheapest=pizzas[0:3]
print(list(three_cheapest))
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects= ["physics","calculus","poetry","history"]
grades=[98,97,85,88]
subjects.append("computerscience")
grades.append(100)
gradebook=list(zip(subjects,grades))
gradebook.append(("visual arts",93))
print(gradebook)
full_gradebook=(gradebook+last_semester_gradebook)

list1 = range(2, 20, 3)
list1_len=len(list1)
print(list1_len)

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4=(employees[4])
print(len(employees))
print(employees[6])

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element=shopping_list[-1]
element5=shopping_list[5]
print(last_element,element5)

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:4]
print(beginning)
middle=suitcase[2:4]

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start=suitcase[:3]
end=suitcase[-2:]

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes=votes.count('Jake')
print(jake_votes)

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)
### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)
print(cities)

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted=sorted(games)
print(games_sorted)

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len=len(inventory)
first=inventory[0]
last=inventory[-1]
inventory_2_6=inventory[2:6]
first_3=inventory[:3]
twin_beds=inventory.count('twin bed')
inventory.sort()

from datetime import datetime
import time
for i in range(1,4):
    right_this_minute=datetime.today().minute
    if(right_this_minute%2==0):
        print("This minute is even so go away!!!")
    else:
        print("This minute is more odd than you")
    time.sleep(randint(1,60))
        
from os import getcwd
where_am_i=getcwd()
print(where_am_i) 
import sys
sam=sys.platform
print(sam)   
print(sys.version)  
print(datetime.today())
print(datetime.isoformat(datetime.today())) 
# Even Odd vending machine...
print("Enter a positive integer...")
s=input()
s=float(s)

 

#Examples of lists and tuples..
simplelst=[1,2,3,4,5,6]
stringlist=["rose","bose","shows"]
emptylist=[]

simpletuple=(1,2,3,4,5,6)
stringtuple=("sambo","simbho","bimbo")

# add elements to the empty list...
emptylist.append(83)
emptylist.append(5)
emptylist.append(22)

print(emptylist)
print(simplelst)
print(stringlist)

print(simpletuple)
print(stringtuple) 
print(simpletuple[-1])

for index,item in enumerate(simpletuple):
    print(index,item)

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price=0
for i in prices:
    total_price+=i
average_price=total_price/len(prices)
print("Average Haircut Price: ",average_price)
new_prices=[price-5 for price in prices]
print(new_prices)
total_revenue=0
for i in range(0,len(hairstyles)):
    total_revenue+=prices[i]*last_week[i]
print("Total Revenue: ",total_revenue)
average_daily_revenue=total_revenue/7
print("Average Daily Revenue: ",average_daily_revenue)
cuts_under_30=[]
for i in range(0,len(new_prices)-1):
    if(new_prices[i]<30):
        cuts_under_30.append(hairstyles[i])
print("Cuts under 30: ",cuts_under_30)
#Write your function here
def divisible_by_ten(nums):
    count=0
    for i in nums:
        if(i%10==0):
            count+=1
    return count    


#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Write your function here
def add_greetings(names):
    greeting="Hello, "
    gnames=[]
    for i in names:
        gnames+=[greeting+i]
    return gnames  

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


#Write your function here
def delete_starting_evens(lst):
    for i in lst:
        if(len(lst)!=0 and int(lst[0])%2==0):
            lst=lst[1:]
    return lst 


#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Write your function here
def odd_indices(lst):
    new_lst=[]
    for index in range(1,len(lst),2):
        new_lst.append(lst[index])
    return new_lst  
    

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Write your function here
def exponents(bases, powers):
    lst=[]
    for i in bases:
        for j in powers:
            lst.append(i**j)
    return lst     

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#Write your function here
def larger_sum(lst1,lst2):
    lst1sum=0
    lst2sum=0
    for i in lst1:
        lst1sum+=i
    for j in lst2:
        lst2sum+=j 
    if(lst1sum>lst2sum):
        return lst1
    elif(lst2sum>lst1sum):
        return lst2
    else:
        return lst1       

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
    sumi=0
    if(len(lst)==0):
        return 0
    else:
        for i in lst:
            sumi+=i
            if(sumi>9000):
                break
    return sumi    
      

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here
def max_num(nums):
    sims=max(nums)
    for i in nums:
        if(i>=sims):
            sims=i
    return sims    

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
print(max_num([-50,-20]))

#Write your function here
def same_values(lst1,lst2):
    new_lst=[]
    if(len(lst1)==len(lst2)):
        for i in range(0,len(lst1)):
            if(lst1[i]==lst2[i]):
                new_lst.append(i)
        return new_lst    
    elif(len(lst1)!=len(lst2)):
        return "unequal lists"

      

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Write your function here
def reversed_list(lst1,lst2):
    lst1.reverse()
    if(len(lst1)==len(lst2)):
        if(lst1==lst2):
            return True
    else:
        return False    

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
                  