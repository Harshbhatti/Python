print("_________________________________")
print("  BANK MANAGMENT SYSTEM  ")
print("___________________________")


data={}
list1=["Name","Address","Phone","Govt Id","Accout Type","Amount"]

def take_data():
    acc_num=input("Enter account number:")

    for item in list1:
        list2.append(input("Enter %s:"%item))
    data[acc_num]=dict(zip(list1,list2))
    print("Account Created")
    print("------------------------------------")
    return

def other_options():
    ch=int(input("1.Check Balance\n2.Withdraw\n3.Deposit\nEnter Choice:"))
    if(ch==1):
        print("Availabel Balance:",data[acc_num]["Amount"])
        print("--------------------------------------------")
        
    elif(ch==2):
        amt=int(input("enter amount to withdraw:"))
        new_amt=int(data[acc_num] ["Amount"])-amt
        data[acc_num] ["Amount"]=new_amt
        print("--------------------------------------------")
        print("aviliable balance:",data[acc_num] ["Amount"])
        print("________________________________________________")

    elif(ch==3):
        amt=int(input("enter amount to deposite:"))
        new_amt=int(data[acc_num] ["Amount"])+amt
        data[acc_num] ["Amount"]=new_amt
        print("--------------------------------------------")
        print("deposit sucessfully")
        print("avaliable balance:",data[acc_num] ["Amount"])
        print("------------------------------------------------")

while True:
    list2=[ ]
    ch=int(input("1.new customer \n2.existing customer \n3.exit \nenter choice:"))
    if (ch==1):
        take_data()
    if (ch==2):
        acc_num=input("enter your account number:")
        if acc_num in data:
            print("record found")
            other_options()
        else:
            print("recond not found")
    if (ch==3):
        break
    
 
     
