from stack import Stack

s = Stack()

choice=0
while choice<5:
        print('STACK OPERATIONS')
        print('1 Push element')
        print('2 Pop element')
        print('3 Peep element')
        print('4 Search for element')
        print('5 Exit')
        choice = int(input('Your choice: '))

        if choice==1:
            element = int(input('Enter element: '))
            s.push(element)
        
        elif choice==2:
            element = s.pop()
            if element == -1:
                print('The stack in empty')
            else:
                print('Popped element= ', element)
        
        elif choice==3:
            element = s.peep()
            print('Topmost element = ', element)

        elif choice==4:
            element == int(input('Enter element: '))
            pos = s.search(element)
            if pos == -1:
                print('The stack is empty')
            elif pos == -2:
                print('Element not found in the stack')
            else:
                print('Element found at position: ', pos)
            
        else:
            break 

        print('Stack = ', s.display())

        


 
    
