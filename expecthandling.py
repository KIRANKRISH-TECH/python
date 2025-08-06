# Try and expect handling in Python


# try:
#      numerator = 10
#      denominator = 0
#      result =numerator/denominator
#      print("result")
# except:
#   print("Error: Division by 0.")


# try:
#       evennumber=[2,4,6,8,]
#       print(evennumber[4])
# except ZeroDivisionError:
#       print("denominator cannot be 0")
# except IndexError:
#       print("index out of bound.")



# else and finally blocks



# try:
#       num=int(input("enter a number"))
#       assert num %2==0
# except:
#       print("not an even number")

# else:
#       reciprocal=1/num
#       print(reciprocal)


# finally:
#       print("this is finally block")


try:
    f = open("hello.txt", "r")
    context = f.read()
except FileNotFoundError:
    print("file not found")
finally:
    try:
        f.close()
    except NameError:
        pass
    print("file closed")





