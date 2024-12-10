#_______________________ User Start ___________________________________

class User:

    def __init__(self,name,email,phone,address,account_type):
         self.name = name
         self.email = email
         self.phone = phone
         self.address = address
         self.account_type = account_type 
         self.account_number = self.phone
         self.current_balance = 0 
         self.loan_num = 0 
         self.loan_balance = 0
         self.transec_history = [] 


        
    def deposit(self,amount):
         self.current_balance += amount
         Admin.bank_total_balance += amount
         print(f"Deposited: {amount} BDT and Avl Bal: {self.current_balance} BDT")
         self.transec_history.append(f"Deposited: {amount} BDT and Avl Bal: {self.current_balance} BDT")


    def withdraw(self,amount):
         if self.current_balance < amount :
             print("Withdrawal amount exceeded")
         elif Admin.bankrupt :
             print("Bank is bankrupted and Withdrawal is not possible")
         elif Admin.bank_total_balance < amount:
            print("There is no available balance in the bank")
         else:
             self.current_balance -= amount
             Admin.bank_total_balance -= amount
             print(f"Withdrawn: {amount} BDT and Avl Bal: {self.current_balance} BDT")
             self.transec_history.append(f"Withdrawn: {amount} BDT and Avl Bal: {self.current_balance} BDT")
         


    def check_balance(self):
          print(f"Current Balance : {self.current_balance}")



    def check_transection_history(self):
        print("\nTransection History : \n")
        for x in self.transec_history:
               print(x)



    def take_loan(self,amount):
        if self.loan_num >= 2:
            print("You have already taken two times loan")
        elif not Admin.is_loan_active:
            print("Loan feature is currently disabled")
        elif Admin.bankrupt:
            print("Bank is bankrupted and taking loan is not possible.")
        elif Admin.bank_total_balance < amount:
            print("There is no available balance in the bank")
        else:
            self.loan_num += 1
            self.current_balance += amount
            Admin.bank_total_balance -= amount
            Admin.total_loan_balance += amount
            print(f"Taken Loan amount : {amount} BDT and Avl Bal : {self.current_balance} BDT")
            self.transec_history.append(f"Taken Loan amount : {amount} BDT and Avl Bal : {self.current_balance} BDT")



    def transfer_amount(self,receiver_acc,amount): 
         
         if receiver_acc not in Admin.All_Account_obj: 
            print("Account does not exits")

         elif self.current_balance < amount:
            print("Insufficient balance for transfer")

         else:
            receiver_obj = Admin.All_Account_obj[receiver_acc]
            self.current_balance -= amount
            receiver_obj.current_balance += amount
            print(f"Transfered : {amount} BDT to Ac: {receiver_obj.account_number} And now your Avl Bal : {self.current_balance} BDT")
            self.transec_history.append(f"Transfered : {amount} BDT to Ac: {receiver_obj.account_number} And now your Avl Bal : {self.current_balance} BDT") 
            receiver_obj.transec_history.append(f"Transfered : {amount} BDT from Ac: {self.account_number} And now your Avl Bal : {receiver_obj.current_balance} BDT") 


#_____________________________ Admin Start_____________________________________________


class Admin:

    All_Account_obj = {} 
    bankrupt = False
    bank_total_balance = 1000000000 # initially Bank openning balance
    total_loan_balance = 0  
    is_loan_active = True
    
    @classmethod
    def create_account(cls,name,email,phone,address,account_type):#

         if phone not in cls.All_Account_obj:
                cls.All_Account_obj[phone]=User(name,email,phone,address,account_type)
                print(f"Account- {phone} is created successfully")    
         else:
                print("Same account is exits")
               

    @classmethod
    def delete_user_account(cls,user_acc): #

         if user_acc not in cls.All_Account_obj:
             print("This account is not exist")
         else:
             del cls.All_Account_obj[user_acc]
             print("Deleted Successfully")


    
    @classmethod
    def see_all_user_account_list(cls):

          print("All users accounts of bank : ")
          for x in cls.All_Account_obj.values():
               print(f"Name: {x.name}, Account Number: {x.account_number},Balance: {x.current_balance} BDT.")


    @classmethod
    def check_all_total_bank_banlance(cls):

         print(f"Total Bank Balance : {cls.bank_total_balance} BDT.")


    
    @classmethod
    def check_total_loan_balance(cls):

         print(f"Total Loan Amount : {cls.total_loan_balance} BDT.")


    
    @classmethod
    def on_off_loan_feature(cls,press):

         if press == '1' :
             cls.is_loan_active = True
             print("Taking Loan Acivated.")
         elif press == '0': 
             cls.is_loan_active = False
             print("Taking Loan Stopped")
         else : 
             print("Pressed wrong option")
    
    @classmethod
    def on_off_bankrupt(cls,press):
         if press == '1' :
            cls.bankrupt = True
            print("Bankrupted")
         elif press == '0': 
            cls.bankrupt = False
            print("Not Bankrupted")
         else:
            print("Pressed wrong option")
         
