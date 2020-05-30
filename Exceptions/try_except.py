try:
    fp=open("test.txt","w")
    fw=open("test1.txt","w")
    fw.write(fp.read())

except:
    print("Exception occured")
else:
    print("written")
finally:
    print("Closing files")
    fp.close()
    fw.close()


l=[1,2,3,4,5]
try:
    i=int(input("Enter index of number from list : "))
    print(l[i])
except IndexError:
    print("Invalid index entered!")
finally:
    print("Code ended")


a=int(input("Enter dividend: "))
b=int(input("Enter divisor: "))
try:
    c = a/b
    print("The division is : ")
    print(c)
    print("d = " + d)
except (ZeroDivisionError,NameError):
    print("The divisor is zero or No variable 'd' found")


try:
    c = a / b
    print("The division is : ")
    print(c)
    print("d = " + d)
except ZeroDivisionError:
    print("The divisor is zero")
except NameError:
    print( "No variable 'd' found")


try:
    raise IndexError
except IndexError:
    print("Exception raised")