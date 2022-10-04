class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    length = 0
    
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        if value == None:
            raise Exception("Sorry Can't add None vlue")

        new_value = Node(value=value)
        
        if self.head == None:
            self.head = new_value
            self.length +=1

        else:
            old_head = self.head
            self.head = new_value
            self.head.next = old_head
            self.length +=1

    def appned(self, value):
        if value == None:
            raise Exception("Sorry Can't add None vlue")

        new_value = Node(value=value)
        
        if self.head == None:
            self.head = new_value
            self.length +=1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_value
            self.length +=1

    def add_after(self, target_value, value):
        if value == None:
            raise Exception("Sorry Can't add None vlue")

        if self.head == None:
            self.insert(value)
            
        else:
            new_value = Node(value=value)
            if self.head.value == target_value:
                new_value.next = self.head.next
                self.head.next = new_value
                self.length +=1
                return
            else:
                current = self.head
                while current:
                    if current.value == target_value:
                        new_value.next = current.next
                        current.next = new_value
                        self.length +=1
                        return
                    else:
                        current = current.next
                        continue

                raise Exception(f'Value {{{target_value}}} not exists in the Lenked-List')
    
    def add_before(self, target_value, value):
        if value == None:
            raise Exception("Sorry Can't add None vlue")

        if self.head == None:
            self.insert(value)
            
        else:
            new_value = Node(value=value)
            if self.head.value == target_value:
                new_value.next = self.head
                self.head = new_value
                self.length +=1
                return
            else:
                current = self.head
                while current.next:
                    if current.next.value == target_value:
                        new_value.next = current.next
                        current.next = new_value
                        self.length +=1
                        return
                    else:
                        current = current.next
                        continue

                raise Exception(f'Value {{{target_value}}} not exists in the Lenked-List')

    def remove(self, value):
        if self.head == None:
            print("Can't remove from empity Linked-List" )
            return
        
        if self.head.value == value:
            self.head = self.head.next
            self.length -=1
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.length -=1
                return
            else:
                current = current.next
                continue

        raise Exception(f'Value {{{value}}} not exists in the Lenked-List')

    
    def includes(self, value):
        if self.head == None:
            return False
        else:
            if self.head.value == value:
                return True
            else:
                current = self.head

                while current:
                    if current.value == value:
                        return True
                    else:
                        current = current.next
                        continue

                return False


    def get_number_of_nudes(self):

        return f"The number of nudes is: {self.number_of_nudes}"

    def __str__(self) -> str:
        output = ' '

        current = self.head
        while current:
            output += f'{current.value} -> '
            current = current.next
        output += ' None'
        print(output) 



ll = LinkedList()
ll.insert('A')
ll.appned('B')
ll.appned('C')
ll.appned('D')
ll.appned('E')

# ll.add_after('C', 'DD')

# ll.add_before('N', 'K')

# ll.add_before('E', 'AZIZ')
# ll.add_before('B', 'AZIZ')

# ll.remove('AZIZ')
# ll.remove('DD')
# ll.remove('AZIZ')
# ll.remove('E')
# ll.remove('D')
# ll.remove('C')
# ll.remove('B')
# ll.remove('A')
# print(ll.head.value)
# print(ll.head.next)

ll.__str__()
# print(ll.includes('n'))
print(ll.get_number_of_nudes())
ll.remove('A')
ll.__str__()
print(ll.get_number_of_nudes())
ll.remove('E')
ll.__str__()
print(ll.get_number_of_nudes())
ll.insert('A')
print(ll.get_number_of_nudes())
ll.__str__()