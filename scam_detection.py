import pandas as pd
from collections import Counter

words = ["Remote","Urgent","Assistance","Clerk","Work","Job","J0b","Work","w0rk","employment","position","internship","Research","appliction","survey","empowerment","graduate","undergraduate","opportunity","opportunities","career","needs","activity","analysis","earning","parttime","fulltime","offer","earn","weekly","hiring","cerf","university of wisconsin","experience"]                                         #Give the words that you search for in the excel file
path = input("Enter the path to the excel file or the name of the excel file: ")
print()
name=[]


try:
    df = pd.read_excel(path)
    try:
        for wds in words:                                           #seraches for the words in the excel file
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
    mailList = Counter(name)
    for i in mailList.keys():
        if mailList[i]>10:
            print(i)
except Exception as e: 
    print("An exception has occured while reading the file")
    print(e)