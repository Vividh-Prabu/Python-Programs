n = 5
print("RIGHT TRIANGLE")
for i in range(n):
     for j in range(i+1):
         print('*',end=' ')
     for j in range(i,n):
         print(" ",end=' ')
     print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

n = 5
print("LEFT TRIANGLE")
for i  in range(n):
     for j in range(i+1):
         print(" ", end=' ')
     for j in range(i,n):
         print('*',end=' ')
     print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

n = 5
print("UPWARD MOUNTAIN")
for i in range(n):
     for j in range(i,n):
         print(' ',end=' ')
     for j in range(i):
         print("*",end=' ')
     for j in range(i+1):
         print("*",end=' ')
     print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

n = 5
print("DOWNWARD MOUNTAIN")
for i in range(n):
     for j in range(i+1):
         print(" ",end=" ")
     for j in range(i,n-1):
         print("*",end=" ")
     for j in range(i,n):
         print("*",end=" ")
     print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
n = 5
print("DIAMOND")
for i in range(n-1):
     for j in range(i,n):
         print(" ",end=" ")
     for j in range(i):
         print("*",end=" ")
     for j in range(i+1):
         print("*",end=" ")
     print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

n = 5
print("DOUBLE HILL")
for i in range(n+1):
     for j in range(i,n):
         print(" ",end="")
     for j in range(i):
         print("*",end=" ")
     for j in range(i,n):
         print(" ",end="")
     for j in range(i,n):
         print(" ",end="")
     for j in range(i):
         print("*",end=" ")
     print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

v = input("Enter the string:")
n = len(v)
a = "abcdefghijklmnopqrstuvwxyz"
for row in range(n):
    for col in range(n):
        if row == col or row+col==n-1:
            print(f"{v[row]}",end=" ")
        else:
            print("  ",end="")
    print()
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")


print("HEART")
for row in range(6):
    for col in range(7):
        if (row == 0 and col%3 != 0) or (row == 1 and col%3 == 0) or (row-col==2) or  (row+col==8):
            print("❤️",end="  ")
        else:
            print(" ",end=" ")

    print()


