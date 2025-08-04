# def simple_generator():
#     yield "hellooooo"
#     yield "world"


# gen=simple_generator()
# print(next(gen))
# print(next(gen))
   
   
   

# decorator ............................

def my_decorator(func):
    def inner():
        print("kkkkkkk")
        func()
    return inner

@my_decorator
def ordinary():
    print("tttt")

ordinary()
    
    