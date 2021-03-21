# deque Operation
from collections import deque

# create an emtpy deque 
d = deque()

choice=0
while choice<7:
    print('DEQUE OPERATION')
    print('1 Add element at front')    
    print('2 Remove element at front')
    print('3 Add element at rear')
    print('4 Remove element at rear')
    print('5 Remove element in the middle') 
    print('6 Search for element')
    print('7 Exit')
    choice = int(input('Your choice: '))

# perform a task depending on user choice
    if choice==1:
        element = input('Enter element: ')
        d.appendleft(element)

    elif choice==2:
        if len(d) == 0:
            print('Deque is empty')
        else:
            d.popleft()

    elif choice==3:
        element = input('Enter element: ')
        d.append(element)
    
    elif choice==4: 
        if len(d) == 0:
            print('Deque is empty')
        else:
            d.pop()
    
    elif choice==5:
        element = input('Enter element: ')
        try:
            d.remove(element)
        except ValueError:
                print('Element no found')
    
    elif choice==6:
        element = input('Enter element: ')  
        c = d.count(element)
        print('No of times the element found: ', c )
    else:
        break

# display the deque element using for loop 
    print('Deque= ', end='')
    for i in d:
        print(i, ' ', end='')
    print( ) # move cursor to next line 
