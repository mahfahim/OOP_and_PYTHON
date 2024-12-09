from Bank import User,Admin

Admin.create_account("Fahim","mahf10@gmail.com","01988188260","Feni","current")
Admin.create_account("Mahi","mahi23@gmail.com","01865432876","Faridpur","savings")
Admin.create_account("Bablu","bablu33@gmail.com","01736754321","Dhaka","current")
Admin.create_account("Raj","raj76@gmail.com","01843265789","comilla","savings")
Admin.create_account("Atiq","atiq33@mail.com","01532752197","Chittagong","savings")





print("\nWellcome to Islami Bank Bangladesh Limited")

while True:
    print("\n1. ADMIN ")
    print("2. USER")
    print("3. Exit")
    print()

    op1 = input("Enter option : ")
    
    if op1 == '1':


            name = input("Enter Admin Name : ")
            pswd = input("Enter Password : ")
            if name == "admin" and pswd == "123":

                        print("\n1. CREATE USER ACCOUNT")
                        print("2. DELETE USER ACCOUNT")
                        print("3. SEE ALL USER ACCOUNT")
                        print("4. CHECK TOTAL BANK BALANCE")
                        print("5. CHECK TOTAL LOAN BALANCE")
                        print("6. ON OR OFF LOAN FEATURE")
                        print("7. Exit")
                        print()

                        op2 = input("Enter option : ")

                        if op2 == '1':
                                    name = input("Enter Name : ")
                                    email = input("Enter Email : ")
                                    phone = input("Enter Phone : ")
                                    address = input("Enter Address : ")
                                    account_type = input("Enter Account Type : ")

                                    Admin.create_account(name,email,phone,address,account_type)

                        elif op2 == '2':
                                    acc = input("Enter Account Number : ")

                                    Admin.delete_user_account(acc)

                        elif op2 == '3':
                                     Admin.see_all_user_account_list()

                        elif op2 == '4':
                                     Admin.check_all_total_bank_banlance()

                        elif op2 == '5':
                                     Admin.check_total_loan_balance()
                        
                        elif op2 == '6':
                                    p = input("Enter press 1 for ON or  0 for OFF : ")
                                    Admin.on_off_loan_feature(p)
                        
                        elif op2 == '7':
                                    break
                    

            else:
                 print("Wrong Name and Password")



    elif op1 == 2: 
        
                account_no = input("Enter User Account No : ")

                if account_no not in Admin.All_Account_obj:
                             print("\nThis Account Number does not exits")

                else:
                        obj = Admin.All_Account_obj[account_no]

                        print("\nUser:")
                        print("1. DEPOSIT")
                        print("2. WITHDRAW")
                        print("3. CHECK BALANCE")
                        print("4. CHECK TRANSECTION HISTORY")
                        print("5. TAKE LOAN ")
                        print("6. TRANSFER AMOUNT")
                        print("7. Exit")

                        op3 = input("Enter Option : ")

                        if op3 == '1':
                                    amt = input("Enter Amount")
                                    obj.deposit(amt)

                        elif op3 == '2':
                                    amt = input("Enter Amount")
                                    obj.withdraw(amt)

                        elif op3 == '3':
                                    obj.check_balance()

                        elif op3 == '4':
                                    obj.check_transection_history()

                        elif op3 == '5':
                                    amt = input("Enter Amount :") 
                                    obj.take_loan(amt)    

                        elif op3 == '6':
                                    acc = input("Enter Receiver Account : ")
                                    amt = intput("Enter Amount")
                                    obj.transfer_amount(acc,amt)
                                
                        elif op3 == '7':
                                    break
        


    elif op1 == '3':
               break
