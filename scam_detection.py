import pandas as pd
from collections import Counter

#Give the key-words or phrases that you search for in the email 
words = ["Remote","Urgent","Assistance","Clerk","Work","Job","J0b","Work","w0rk","employment","position","internship","Research","appliction","survey","empowerment","graduate","undergraduate","opportunity","opportunities","career","needs","activity","analysis","earning","parttime","fulltime","offer","earn","weekly","hiring","cerf","university of wisconsin","experience"]                                            
path = input("Enter the path to the excel file or the name of the excel file: ")
print()
name=[]
threshold = 10      

try:
    df = pd.read_excel(path)
    try:
        #seraches for the words in the excel file
        for wds in words:                                           
            ind = 0
            for line in df["Subject"]:
                if wds.lower() in str(line).lower():
                    name.append(df.loc[ind,"Sender address"])
                    print()
                ind+=1
    except Exception as e:
        print("An exception has occured while searching for spams")
        print(e)

    print("The possible list of scam emails: \n")

    #Counts the occurances of the sender mail id that had the target words or phrase.
    mailList = Counter(name)                                    
    for i in mailList.keys():
        #If the sender mail id has occured more times than the threshold value it is considered as scam
        if mailList[i]>threshold:               
            print(i)
except Exception as e: 
    print("An exception has occured while reading the file")
    print(e)