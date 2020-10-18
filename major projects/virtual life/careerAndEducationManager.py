import pickle
import random
from currencyManager import *
import datetime
from datetime import datetime, timedelta

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#update someone's file so that they can have a job and shit
def joinWorkAndEducation(ID):
        with open('userData.pickle', 'rb') as handle:
                b = pickle.load(handle)
                
        
        if "hasJob" in list(b[ID].keys()) :
                return "You're already in here"
        #if they don't exist at all in the system
        if not ID in list(b.keys()):
                return "PLEASE RUN '~ADD ME' FIRST"
        
        #IF THEY EXIST UPDAT THEIR ENTRY
        b[ID]["hasJob"] = False
        b[ID]["beenToCollege"] = False
        b[ID]["Salary"] = 0
        b[ID]["timeSincePay"] = 0
        b[ID]["job"] = None
        b[ID]["careerField"] = None
        b[ID]["hasJob"] = False
        b[ID]['educationDLCCheck'] = True
        b[ID]["timeRecievedJob"] = None
        b[ID]["timeSincePromotion"] = None
        b[ID]["timeSinceLastPaid"] = None
        b[ID]["jobLevel"] = 0
        
        with open('userData.pickle', 'wb') as handle:
                pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)    
        return "it worked"
                
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def inEducationDLC(ID):
        #___________________________________________
        #CHECK IF THEY HAVE EVEN JOINED THE DLC
        #___________________________________________
        with open('userData.pickle', 'rb') as handle:
                b = pickle.load(handle)
        #if they don't exist at all in the system
        if not ID in list(b.keys()):
                return False
        #if they are in the system, but haven't joined up
        if  'educationDLCCheck' not in list( b[ID].keys() ):
                return False
        #if they are in
        else:
                return True
        
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------       
def joinCollege(ID, Method): ## RETURNS "YOU ARE FUCKING BROKE" -> don't have enough cash to go to college , "YOU OWE TOO MUCH" -> you have too much out for loans , "YOU GOT IN CASH / LOAN" -> you were added in using the specified method
        if inEducationDLC(ID) == True:
                #if they are paying with cash
                if Method == "cash":
                        #if they have enough money for it 
                        if checkBalance(ID) >= 40000:
                                #subtract 40,000 instantly from their wallet
                                removeMoney(ID,40000)
                                #update their dictionary
                                with open('userData.pickle', 'rb') as handle:
                                        b = pickle.load(handle)                
                                b[ID]["beenToCollege"] = True
                                #save their dictionary
                                with open('userData.pickle', 'wb') as handle:
                                        pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL) 
                                return "YOU GOT IN CASH"
                        #if they don't have enough money for it
                        else:
                                return "YOU ARE FUCKING BROKE"
                #if they are taking a loan
                elif Method == "loan":
                        #if they are eligable to take 40k on loan
                        if (getLoan(ID) + 40000) <= 100000:
                                #takeout the loan for them
                                takeLoan(ID, 40000)
                                removeMoney(ID,40000)
                                with open('userData.pickle', 'rb') as handle:
                                        b = pickle.load(handle)                
                                b[ID]["beenToCollege"] = True
                                #save their dictionary
                                with open('userData.pickle', 'wb') as handle:
                                        pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL) 
                                return "YOU GOT IN LOAN"
                        else:
                                return "YOU OWE TOO MUCH"
                #if METHOD is neither cash nor loan
                else:
                        return "that isn't a valid option"
        else:
                return "YOU HAVEN'T AGREED TO THE DLC"
        
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def checkCollegeOptions(ID): ## RETURNS "YOU'VE BEEN TO COLLEGE" -> you're already graduated , otherwise returns list with options
        if inEducationDLC(ID) == True:
                with open('userData.pickle', 'rb') as handle:
                        b = pickle.load(handle)                
                if b[ID]["beenToCollege"] == True:
                        return "YOU'VE BEEN TO COLLEGE"
                #list that contains options
                toReturn = []
                #check their cash
                if checkBalance(ID) >= 40000:
                        toReturn.append("You can attend college using cash with **~Enroll Cash**, you have ${:,} right now !".format(checkBalance(ID)))
                if getLoan(ID) + 40000 <= 100000:
                        toReturn.append("You can attend college by taking a loan **~Enroll Loan**, you have ${:,} in loans right now".format(getLoan(ID)))
                return toReturn
        else:
                return "YOU HAVEN'T AGREED TO THE DLC"        

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------        
def availableJobs(ID):
        #if they are in the system + DLC
        if inEducationDLC(ID) == True:
                #if they have been to college
                if checkCollegeOptions(ID) == "YOU'VE BEEN TO COLLEGE":
                        #create a list that contains all the entry-level jobs they are capable of having
                        toReturn = []
                        #open the jobs file
                        with open('Jobs.pickle', 'rb') as handle:
                                b = pickle.load(handle)      
                        for category in list(b.keys()):
                                if 1 in b[category]:
                                        toReturn.append(b[category][1])
                        for key in list(b["misc"].keys()):
                                toReturn.append(b["misc"][key])
                        return toReturn
                else:
                        with open('Jobs.pickle', 'rb') as handle:
                                b = pickle.load(handle)
                        return b["misc"]
                                
                        
                
                
        else:
                return "YOU HAVEN'T AGREED TO THE DLC"
        
        
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------                
def makeJobs():
        with open('Jobs.pickle', 'rb') as handle:
                b = pickle.load(handle)        
        b = { "misc" : { 
                "Farm Hand" : { "college" : False, "salary" : 500, "title" : "Farm Hand", "level" : 0  , "Field" : "misc" } ,
                "Dog Groomer" : { "college" : False, "salary" : 500, "title" : "Dog Groomer", "level" : 0   , "Field" : "misc"} ,
                "Barista" : { "college" : False, "salary" : 600, "title" : "Barista", "level" : 0  , "Field" : "misc" } ,
                "Ride-Share Driver" : { "college" : False, "salary" : 700, "title" : "Ride-Share Driver", "level" : 0  , "Field" : "misc" } ,
                "Gun Smith" : { "college" : False, "salary" : 800, "title" : "Gun Smith", "level" : 0  , "Field" : "misc" } ,
                "Grave Digger" : { "college" : False, "salary" : 800, "title" : "Grave Digger", "level" : 0  , "Field" : "misc"}  
                },
              "criminal justice" : {
                1 : { "college" : True, "salary" : 1000, "title" : "Morgue Worker", "level" : 1 , "Field" : "Criminal Justice"} ,
                2 : { "college" : True, "salary" : 1000, "title" : "Police Officer", "level" : 2 , "Field" : "Criminal Justice"} ,
                3 : { "college" : True, "salary" : 1200, "title" : "Security Agent", "level" : 3 , "Field" : "Criminal Justice"} ,
                4 : { "college" : True, "salary" : 1500, "title" : "Forensic Investigator", "level" : 4 , "Field" : "Criminal Justice"} ,
                5 : { "college" : True, "salary" : 1800, "title" : "Prosecutor", "level" : 5 , "Field" : "Criminal Justice"} ,
                6 : { "college" : True, "salary" : 2400, "title" : "Judge", "level" : 6, "Field" : "Criminal Justice" }                
              }
              }
        with open('Jobs.pickle', 'wb') as handle:
                pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)            

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------                   
def isPayAvailable(ID):
        if inEducationDLC(ID) == True:
                with open('userData.pickle', 'rb') as handle:
                        b = pickle.load(handle)
        
                now = datetime.now()
                return b[ID]["timeSinceLastPaid"] <= now-timedelta(hours=24)
        else:
                return "YOU AREN'T IN THE SYSTEM"
        
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def collectSalary(ID):
        if inEducationDLC(ID) == True:
                with open('userData.pickle', 'rb') as handle:
                        b = pickle.load(handle)
                if isPayAvailable(ID):
                        addMoney(ID, b[ID]["Salary"])
                        print("You've been paid")
                else:
                        return "Salary isn't ready"
        else:
                return "YOU DONT EXIST"        
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def isPromotionAvailable(ID):
        if inEducationDLC(ID) == True:
                with open('userData.pickle', 'rb') as handle:
                        b = pickle.load(handle)
        
                now = datetime.now()
                return b[ID]["timeSincePromotion"]<= now-timedelta(hours=0) 
        
        else:
                return "YOU AREN'T IN THE SYSTEM"
        
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def getPromotion(ID):
        if inEducationDLC(ID) == True:
                if isPromotionAvailable(ID):
                        with open('userData.pickle', 'rb') as handle:
                                b = pickle.load(handle)
                        with open('Jobs.pickle', 'rb') as handle:
                                jobs = pickle.load(handle)
                        
                        #career field they are in:
                        Field = b[ID]["careerField"]
                        Field = Field.lower()
                        
                        if Field != "misc":
                        
                                #get their position level in that field
                                positionLevel = b[ID]["jobLevel"]
                                
                                #get their new job
                                newJob = jobs[Field][positionLevel + 1]
                                
                                #update values
                                b[ID]["Salary"] = newJob["salary"]
                                b[ID]["job"] = newJob["title"]
                                b[ID]["timeRecievedJob"] = datetime.now()
                                b[ID]["timeSincePromotion"] = datetime.now()
                                b[ID]["jobLevel"] += 1     
                                with open('userData.pickle', 'wb') as handle:
                                        pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)     
                        else:
                                return "misc cannot get promoted"
                else:
                        return "ineligable for a promotion"
        else:
                return "YOU DONT EXIST"       
        


#{'college': True, 'salary': 1000, 'title': 'Police Officer', 'level': 2, 'Field': 'Criminal Justice'}


#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------  
def takeJob(ID, Field, Name = None):
        if inEducationDLC(ID) == True:
                #if a name hasn't been specified, then we know we are going for a career field
                if Name == None:
                        #If they haven't been in college fucking deny them
                        if checkCollegeOptions(ID) == "YOU'VE BEEN TO COLLEGE":
                                #check if the field fucking exist
                                with open('Jobs.pickle', 'rb') as handle:
                                        jobList = pickle.load(handle)
                                if Field in list(jobList.keys()):
                                        newJob = jobList[Field][1]
                                        
                                        with open('userData.pickle', 'rb') as handle:
                                                b = pickle.load(handle)
                                                
                                        # 1 : { "college" : True, "salary" : 1000, "title" : "Morgue Worker", "level" : 1 , "Field" : "Criminal Justice"} ,
                                        b[ID]["hasJob"] = True
                                        b[ID]["Salary"] = newJob["salary"]
                                        b[ID]["job"] = newJob["title"]
                                        b[ID]["careerField"] = Field
                                        b[ID]["timeRecievedJob"] = datetime.now()
                                        b[ID]["timeSincePromotion"] = datetime.now()
                                        b[ID]["timeSinceLastPaid"] = datetime.now()
                                        b[ID]["jobLevel"] = 1   
                                        #update the user
                                        with open('userData.pickle', 'wb') as handle:
                                                pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)                                     
                                else:
                                        return "that field doesn't exist"
                                
                        else:
                                return "this field requires a college degree"
                #otherwise throw them in a fucking misc career
                else:
                        print("YOU ARE GETTING A MISC JOB")
                        
                        with open('Jobs.pickle', 'rb') as handle:
                                jobList = pickle.load(handle)
                        if Field in list(jobList.keys()):
                                newJob = jobList["misc"][Name]
                                
                                with open('userData.pickle', 'rb') as handle:
                                        b = pickle.load(handle)
                                        
                                # 1 : { "college" : True, "salary" : 1000, "title" : "Morgue Worker", "level" : 1 , "Field" : "Criminal Justice"} ,
                                b[ID]["hasJob"] = True
                                b[ID]["Salary"] = newJob["salary"]
                                b[ID]["job"] = newJob["title"]
                                b[ID]["careerField"] = Field
                                b[ID]["timeRecievedJob"] = datetime.now()
                                b[ID]["timeSincePromotion"] = datetime.now()
                                b[ID]["timeSinceLastPaid"] = datetime.now()
                                b[ID]["jobLevel"] = 0
                                #update the user
                                with open('userData.pickle', 'wb') as handle:
                                        pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)                        
        else:
                return "YOU AREN'T IN THE SYSTEM"