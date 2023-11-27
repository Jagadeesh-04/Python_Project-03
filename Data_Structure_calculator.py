# project 3 
# Project name : Data Structures Calculator 
# which is used to perform the DS operations in python.
# Python DataStructure includes , List , Tuple , Set , Dictionary .

# Function to create the list
def cr_list(): 
    list1  = []
    n = int(input('Enter the number of elements you want to add : '))
    for i in range(1,n+1):
        b = int(input(f'Enter the element for {i}-position : '))
        list1.append(b)
    return list1

# Function to create the Tuple
def cr_tuple(): 
    listtu  = []
    n = int(input('Enter the number of elements you want to add : '))
    for i in range(1,n+1):
        b = int(input(f'Enter the element for {i}-position : '))
        listtu.append(b)
    return listtu
    
# Function to create the Set
def cr_set(): 
    print("You have to Create a Set 1st ")
    print("Note : set doesn't allows duplicate values")
    set_list = []
    n = int(input('Enter the number of elements you want to add : '))
    for i in range(1,n+1):
        b = int(input(f'Enter the element : '))
        set_list.append(b)
    set1 = set(set_list)
    return set1

# Function to create the Dictionary
def cr_dict(): 
    a = {}
    n = int(input('Enter the number of elements you want to add : '))
    for i in range (n):
        n = input("Enter the key :")
        m = input("Enter the value :")
        a[n]=m
    return a

#List opreations listed as a individual Functions

def apnd(): # Append
    print(f"Your list is : {c}")
    e =int(input('Enter the number you want to append : '))
    c.append(e)
    return f"Your appended list is : {c}"

def ins(): # Insert
    print(f"Your list is : {c}")
    ele = int(input('Enter the element you want to insert : '))
    pos = int(input('Enter the position you want to insert : '))
    c.insert(pos,ele)
    return f"Your list after insertion is : {c}"
def popp(): # Pop 
    print(f"Your list is : {c}")
    print("Your current list is :",c)
    ele = int(input('Enter the position you want to pop :')) 
    c.pop(ele)
    return f"Your list after pop operation is : {c}"
def sortt(): # Sort
    print(f"Your list is : {c}")
    print('\n Enter 1. for assending order,\n Enter 2. for decending  order')
    m = int(input( "1 or 2 : " ))
    if m == 1:
        c.sort()
        return f"Your list after sorting(asc) : {c}"
    elif m ==2:
        c.sort(reverse=True)
        return f"Your list after sorting(dsc) : {c}"
def coppy(): # Copy
    print(f"Your list is : {c}")
    Newlist=c.copy()
    print(c)
    return f'The copy of the list is : {Newlist}'
def rev(): # Reverse
    print('Original list is : ',c)
    c.reverse()
    return f'The reversed list is :{c}'
def rem(): # Remove
    print("The current list is :",c)
    ele = int(input('Enter the value you want to remove : '))
    c.remove(ele)
    return f"Your list after removing {ele} is : {c}"
def ext(): # Extend
    print("Already existing list is :",c)
    print("Create the list you want to add ,")
    list2 = cr_list()
    c.extend(list2)
    return f"Your extended list is : {c}"

# tuple comments with exception handling !, 
def tup1():
    try: # exception handling 
        # count opreation Function!
        print("Your tuple is :",tu)
        n = int(input('enter the value u need to count : '))
        k =  tu.count(n)
    except Exception as e:
        print(e)
    else:
        return f"The count of the {n} is : {k}"
def tup2():
    # Index operation to find index of the value in tuple 
    print("Your tuple is :",tu)
    n = int(input('enter the value u need to find the index : '))
    try:
        k=tu.index(n)
    except Exception as a:
        print(a)
    else:
        return f"The index of the {n} is : {k}"

# set operations as individual Functions ,
def setadd(): # Add
    print("Your set is :",e)
    n = int(input('Enter the element you want to add :'))
    e.add(n)
    return f"Your set after the addition is : {e}"

def cop(): # Copy
    print('Original Set is :',e)
    e.copy()
    temp = e
    return f"Your set copy is : {temp}"

def diff(): # Difference
    t = e
    h = set2
    print("The First set is ",t)
    print("The second set is ",h)
    print("press 1  if you want to compare set(1) to set(2)\npress 2  if you want to compare set(2) to set(1)")
    n = int(input())
    if n == 1:
        return f"The difference of set 1 to set 2 is : {t.difference(h)}"
    elif n == 2:
        return f"The difference of set 2 to set 1 is : {h.difference(t)}"

def inter(): # Intersection 
    print("1st set is :",e)
    print("2nd set is :",set2)
    t = e
    j = set2
    return f"The intersection is : {t.intersection(j)}"

def diffup(): # difference_update
    print("1st set is :",e)
    print("2nd set is :",set2)
    t = e
    h = set2
    print('press 1 if you want to difference_update set(1) to set(2)\npress 2 if you want to difference_update set(2) to set(1) ')
    n = int(input())
    if n == 1:
        t.difference_update(h)
        tem = t
        return f"The difference_update set(1) to set(2) is {tem}"
    elif n == 2:
        h.difference_update(t)
        tem = h
        print(tem)
        return f"The difference_update set(2) to set(1) is {tem}"

def disc(): # Discard
    print("Your set is :",e)
    t = e
    n = int(input('enter the element you want to discard :'))
    t.discard(n)
    return f"The set after the deletion of element is : {t}"

def intup(): # intersection_update
    print("1st set is :",e)
    print("2nd set is :",set2)
    t = e
    j = set2
    t.intersection_update(j)
    return f"The intersection_update set is : {t}"

def up(): # update
    print("Your set is :",e)
    print("To update the set , you want another set with certain elements ,")
    t = e
    j = cr_set()
    print("Your new set is :",j)
    t.update(j)
    return f"The set update is : {t}"

# The Dictionary operations does not have the individual functions , but,the methods are assigned to call directly while using !
# Assign the users guide to access this ,
print('''Enter the data structure you want to work with , 
\t 1. List
\t 2. Tuple
\t 3. set
\t 4. Dictionary''')
a = int(input('Enter the number of the data structure to process... : '))

if a == 1: # Which is heading to the list operations  
    print("You have to Create a List 1st ")
    c = cr_list()
    print(c)
    # After the creation of the list , users allows to perform operations
    print('''
    Enter the list operation you want to perform
    1.append
    2.insert
    3.pop
    4.sort(asc,des)
    5.copy
    6.reverse
    7.len
    8.max
    9.remove
    10.extend
    11.Exit
    ''')
    while True :
        d = int(input('Enter the number of action you want to perform : '))
        if d == 1:
            print(apnd())
        elif d == 2:
            print(ins())
        elif d == 3:
            print(popp())
        elif d ==4:
            print(sortt())
        elif d == 5:
           print(coppy())
        elif d ==6:
            print(rev())
        elif d == 7:
            print(len(c))
        elif d == 8:
            print(max(c))
        elif d == 9:
            print(rem())
        elif d == 10:
            print(ext())
        elif d == 11:
            print("Thanks for the use")
            break
        elif d >11:
            print("Enter the number between 1 to 11 to perform actions")

elif a == 2:  # Which is heading to the Tuple operations  
    print("You have to Create a Tuple 1st ")
    tu = cr_tuple()
    print(tu)
    print('''The tuple operations include..
    1. count
    2. index
    3. Exit''')
    # After the creation of the Tuple , users allows to perform operations
    while True:
        n = int(input('Enter the num to perform : '))
        if n==1:
            print(tup1())
        elif n==2:
            print(tup2())
        elif n==3:
            print("Thanks for the use")
            break
        else:
            print("Enter the number between 1 to 3 to perform actions")

elif a == 3:  # Which is heading to the Set operations  
    e = cr_set()
    print("Your 1st set is :",e)
    print('\n To perform some operations you need 2nd set too so ,' )
    set2=cr_set()
    print("Your Original set is :",e)
    print("Your 2nd set is :",set2 )

    # After the creation of the Set , users allows to perform operations
    print('''\nThe set operations are..
    1. add
    2. copy
    3. difference
    4. intersection
    5. difference_update
    6. discard/
    7. intersection_update
    8. update
    9. Exit''')
    while True:     
        n = int(input('Enter the No of operation you want to perform :'))
        if n == 1:
            print(setadd())
        elif n == 2:
            print(cop())
        elif n ==3:
            print(diff())
        elif n == 4:
            print(inter())
        elif n == 5:
            print(diffup())
        elif n ==6:
            print(disc())
        elif n == 7:
            print(intup())
        elif n == 8:
            print(up())
        elif n == 9:
            print("Thanks for the use")
            break
        else:
            print("Enter the number between 1 to 9 to perform actions")

# Dictionary methods are directly assigned here...!

elif a == 4:  # Which is heading to the Dictionary operations  
    print("You have to Create a dictionary 1st ")
    dt = cr_dict() 
    print("Your dictionary is :",dt)
    # After the creation of the Dictionary , users allows to perform operations
    print('''The Dictionary operations are...
    1. keys
    2. values
    3. items
    4. get
    5. pop
    6. update
    7. Exit''')
    while True:
        num = int(input("Enter the number to perform the action :"))
        if num == 1:
            ans = dt.keys()
            print ("The dictionary keys are :",ans)
        elif num == 2:
            ans = dt.values()
            print("The dictionary values are :",ans)
        elif num == 3:
            ans=dt.items()
            print("The dictionary items are :",ans)
        elif num == 4:
            get_ele =input("Enter the key of element you want :")
            ans = dt.get(get_ele)
            print(f"The value for the key {get_ele} is : {ans}")
        elif num == 5:
            print(dt)
            pop_ele = input("Enter the key element you want to pop :")
            ans = dt.pop(pop_ele)
            print("The popped value is :",ans)
        elif num == 6:
            newdt = cr_dict()
            dt.update(newdt)
            print("Your updated dictionary is :",dt)
        elif num == 7:
            print("Thanks for the use..!")
            break
        else:
            print("Enter the number between 1 to 7 to perform actions")


# End_of_the_project !!!