import pickle

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def createUser(name,ID):
    #Open file
    with open('userData.pickle', 'rb') as handle:
        b = pickle.load(handle) 
    
    #check if user exist
    if ID in list(b.keys()):
        return "YOU ARE ALREADY IN THERE"
    
    #if user doesn't exist
    else:
        b[ID] = {"Name" : name, "Money" : 10000, "Loan" : 0 }
        with open('userData.pickle', 'wb') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return "you're in"

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def addMoney(ID, amount):
    #Open file
    with open('userData.pickle', 'rb') as handle:
        b = pickle.load(handle) 
        
    if ID in list(b.keys()):
        b[ID]["Money"] += amount
        with open('userData.pickle', 'wb') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)    
        return "I have added {} to {}'s account. They Now Have {}".format(amount, b[ID]["Name"],  b[ID]["Money"])
    
    else:
        return "YOU ARE NOT IN THERE"
    
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def removeMoney(ID, amount):
    #Open file
    with open('userData.pickle', 'rb') as handle:
        b = pickle.load(handle) 
        
    if ID in list(b.keys()):
        b[ID]["Money"] -= amount
        with open('userData.pickle', 'wb') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)    
        #check bankrupt
        if checkBankrupt(ID):
            return "YOU ARE NOW BROKE"
        #if not 
        else:
            return "I have removed {} from {}'s account. They Now Have {}".format(amount, b[ID]["Name"],  b[ID]["Money"])
            
        
    
    else:
        return "YOU ARE NOT IN THERE"
    
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def checkBankrupt(ID):
    with open('userData.pickle', 'rb') as handle:
        b = pickle.load(handle)
    if not ID in list(b.keys()):
        return "YOU DONT EXIST"    
    if b[ID]["Money"] <= 0:
        return True
    else:
        return False
    
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------        
def checkBalance(ID):
    with open('userData.pickle', 'rb') as handle:
        b = pickle.load(handle)
    if not ID in list(b.keys()):
        return "YOU DONT EXIST"
    return b[ID]["Money"]


#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------  
def pay(ID1, ID2, amount):
    if checkBalance(ID1) >= amount:
        removeMoney(ID1,amount)
        addMoney(ID2,amount)
    else:
        return "AHHHHHHHHHH CANT COMPLETE"

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------  
def getLoan(ID): 
    try:
        with open('userData.pickle', 'rb') as handle:
            b = pickle.load(handle)
        if not ID in list(b.keys()):
            return "YOU DONT EXIST"
        return b[ID]["Loan"] 
    except:
        with open('userData.pickle', 'rb') as handle:
            b = pickle.load(handle)
        if not ID in list(b.keys()):
            return "YOU DONT EXIST"
        b[ID]["Loan"] = 0
        with open('userData.pickle', 'wb') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)      
        print("created a loan")
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------          
def takeLoan(ID, amount):
    #check if amount is greater than 100k
    if amount > 100000:
        return "I can't loan you that"
    getLoan(ID)
    with open('userData.pickle', 'rb') as handle:
        b = pickle.load(handle)
    if not ID in list(b.keys()):
        return "YOU DONT EXIST"
    #if they have borrowed too much
    if  b[ID]["Loan"] > 100000 or  b[ID]["Loan"]  + amount > 100000:
        return "You've borrowed too much!"    
    #if they are good to go
    b[ID]["Loan"] += amount    
    with open('userData.pickle', 'wb') as handle:
        pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)   
    addMoney(ID, amount)
    print(getLoan(ID))
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------  
def payLoan(ID, amount):
    if checkBalance(ID) >= amount:
        removeMoney(ID, amount)
        getLoan(ID)
        with open('userData.pickle', 'rb') as handle:
            b = pickle.load(handle)
        if not ID in list(b.keys()):
            return "YOU DONT EXIST"
        b[ID]["Loan"] -= amount    
        with open('userData.pickle', 'wb') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)   
        print(getLoan(ID))    