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

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
    
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        
my_linked_list=LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()
            