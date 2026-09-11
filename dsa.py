# print("Hello world)


# def print_items(n):
#     for i in range(n):
#         print(i)        
# print_items(11)

# Big O drop constraints

# def print_items(n):
#     for i in range(n):
#         print(i)
        
#     for j in range(n):
#         print(j)
# print_items(10)

# Big O O(n^2)
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 print(i,j,k)
            
# print_items(10)

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 print(i,j,k)
# print_items(10)
        
    

# Big O Drop Non-Dominants

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
            
#     for k in range(n):
#         print(k)
        
# print_items(10)

# Big O O(1)

# Big O (1)

#Big O Different terms for input


# Classes
# class Cookie:
#     def __init__(self,color):
#         self.color=color
        
#     def get_color(self):
#         return self.color
        
#     def set_color(self,color):
#         self.color=color
    
        
# cookie_one=Cookie("green")
# cookie_two = Cookie('blue')

# print("Cookie one is ",cookie_one.get_color())
# print("Cookie two is",cookie_two.get_color())

# cookie_one.set_color("yellow")

# print("\nCookie one is now",cookie_one.get_color())
# print("Cookie two is still",cookie_two.get_color())

#  

# Pointers

# num1 = 11

# num2=num1
# print("Before num2 value is updated:")
# print("num1=",num1)
# print("num2",num2)

# print("\nnum1 points to:",id(num1))
# print("num2 points to:", id(num2))

# num2=22

# print("\nAfter num2 value is updated: ")
# print("num1=",num1)
# print("num2=",num2)

# print("\nnum1 points to:",id(num1))
# print("num2 points to:", id(num2)) 


    # dict1 ={
    #     'value':10
    # }

    # dict2 = dict1

    # print("Before value is updated:")
    # print("dict1=",dict1)
    # print("dict2=",dict2)

    # print("\ndict1 points to:",id(dict1))
    # print("dict2 points to:", id(dict2))

    # dict2['value']=22

    # print("\nAfter dict2 value is updated: ")
    # print("dict1=",dict1)
    # print("dict2=",dict2)

    # print("\ndict1 points to:",id(dict1))
    # print("dict2 points to:", id(dict2))
# hello\s

# Hello world

# print("Hello")

# head ={
#      "value":11,
#         "next":{
#               "value":3,
#              "next":{
#             "value":23,
#             "next":{
#                 "value":7,
#                 "next":None
#                     }
#               }   
#             }
#         }
# print(head['next']['next']['next']['value'])

# This will only run with a Linked List

# print(head["next"]["next"]["next"]["value"])

# LL Constructor

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class LinkedList:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length=1
        
# my_linked_list = LinkedList(4)

# print(my_linked_list.head.value)

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
        
    
# class LinkedList:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
        
#     def print_list(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
            
#     def append(self,value):
#         new_node=Node(value)
#         if self.length==0:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1
#         return True
#     def pop(self):
#         if self.length==0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre=temp
#             temp=temp.next
            
#         self.tail=pre
#         self.tail.next=None
#         self.length-=1
        
#         if self.length==0:
#             self.head=None
#             self.tail=None
            
#         return temp
        
# my_linked_list=LinkedList(2)

# my_linked_list.append(1)
# my_linked_list.append(6)
# (2)Items- Returns 2 Node
# print(my_linked_list.pop_firt().value)
# (1) Item-Returns 1 Node
# print(my_linked_list.pop_first().value)
# (0) Items-Returns Node
# print(my_linked_list.pop_first())

# my_linked_list.print_list()


# Pop First

# LL Get

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
        



# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print(my_linked_list.get(3).value)


# """
#     EXPECTED OUTPUT:
#     ----------------
#     3

# """


# LL Set

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    



my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)

print('\nLL after set_value():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""


            