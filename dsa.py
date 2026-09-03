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
        
        
# print_items(10 )

# Big O O(n^2)
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

#  

# Pointers

num1 = 11

num2=num1
print("Before num2 value is updated:")
print("num1=",num1)
print("num2",num2)

print("\nnum1 points to:",id(num1))
print("num2 points to:", id(num2))

num2=22

print("\nAfter num2 value is updated: ")
print("num1=",num1)
print("num2=",num2)

print("\nnum1 points to:",id(num1))
print("num2 points to:", id(num2))