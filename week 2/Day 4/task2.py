# Pattern printer 
#  Start,triangle and diamond pattern

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6)
# , which means values from 2 to 6 (but not including 6):

"""
Control character printing:
Use print("*", end="") to print a star without moving to the next line.
Use print(" ", end="") to print a space without moving to the next line.
Use print() or print("\n") after the inner loop(s) to move to the next line for the subsequent row.

"""
# name = input("Enter you Name: ").capitalize()

# print(f"Hello {name},Welcome to the pattern printer 😁")


# rows = int(input("Enter the number of rows: "))
# n=5

############################   Temple Pattern    ###############################
# def full_pyramid(n):
#     for i in range(1,n +1 ):

#         for j in range(n - 1):
#             print(" ", end = "")

#         for k in range(1, 2*i):
#             print("*", end = "")
#         print()

# full_pyramid(5)

# # Function to print full pyramid pattern
# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()
   
# full_pyramid(5)

# for i in range(1,5):
#     print("*********")






# n = 5
# for row in range(n):   #for  row in range(n)
#     for col in range(n+1): #for col in range(n)
#         print("*",end =" ")  # this end= " " will keep stars on the same line  
#     print() #this will moves to next row 



# for row in range(1, n+1):    ##### here the number 1 in range(1,__)  will start the range from where the total number of stars will begin eg if one then  the triangle of stars will start from 1 if 2 then it will be like ** then *** etc goes on 
#     for col in range(row): # -> star  = row number so if 3 row --> 3 star 
#         print("*",end =" ")
#     print("\t") ## this triangle is in decreasing order 



# ## triangle in increasing order 

# for  row in range(n,0,-1):   # here the range(n) will be the starting of total numbers of stars then it will decrease here n = 5 teherefore it will start from 5 stars - ***** then **** etc 
#     for col in range(row): ## key:- stars = row(start high, goes low)  -  range(5,0,-1)  this means it  will go from 5 to 0 in decreasing order.
#         print("*",end=" ")
#     print()

def Diamond():

    nd = int(input("Enter the number of rows for Triangle/Diamond"))

    for row in range(1,nd + 1):
        print(" " * (nd - row),end ="") ####this will give spaces ## this will star from 1  then it will keep increasing 
        print("* " * row)  #### stars
    #spaces = n - row
    # stars = row




    ###inverted pyramid 

    for row in range(nd,0,-1):
        print(" " * (nd-row),end = "")
        print("* " * row)

# diamond()


def Triangle():

    nt = int(input("Enter the number of rows for Triangle/Diamond"))
    for row in range(1,nt + 1):
        print(" " * (nt - row),end ="") ####this will give spaces ## this will star from 1  then it will keep increasing 
        print("* " * row)  #### stars
    #spaces = n - row
    # stars = row


def main():

    Triangle()
    Diamond()
   

main()