

            #    protected 
            
# class bankaccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def __calculate_interest(self):
#         return self.__balance * 0.05  # 5% interest

#     def __show_balance(self):
#         print(f"Account balance: ${self.__balance}")
#         print(f"Interest earned: ${self.__calculate_interest()}")

# account = bankaccount(1000)
# account._bankaccount__show_balance()




class stock:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def _stockinfo(self):
        print(f"Stock Name: {self._name}")
        print(f"Stock Price: ${self._price}")

stock1 = stock("bitcoin", 1000000)
stock1._stockinfo()
            
