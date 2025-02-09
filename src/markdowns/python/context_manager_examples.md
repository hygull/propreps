```python
In [1]: class RegionOnlyBank:
   ...:     def __init__(self, money=0):
   ...:         print(f"Initiating an amount Rs. {money} to the account")
   ...:         self.money = money
   ...: 
   ...:     def __enter__(self):
   ...:         print("Crediting the amount")
   ...:         return self.money
   ...: 
   ...:     def __exit__(self, exc_type, exc_value, traceback):
   ...:         print("Debiting the remaning amount to your account")
   ...:         self.money = 0
   ...: 

In [2]: with RegionOnlyBank(money=100) as bank_money:
   ...:     print("Bank's money", bank_money)
   ...: 
Initiating an amount Rs. 100 to the account
Crediting the amount
Bank's money 100
Debiting the remaning amount to your account
```