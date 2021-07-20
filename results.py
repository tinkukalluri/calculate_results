import pandas as pd

df=pd.read_excel('C:/Users/sintin/OneDrive/Desktop/2_1_results_1.xlsx')
print(df)

dic={"111":[1 ,2 ,3]}
count=0
passed=0
failed=0
failed_log={"tinku":1}
for i in range(0 , len(df)):
    if(df["EXTERNALMARKS"][i]<26 and df["SUBJECT_NAME"][i]!="GENDER SENSITIZATION LAB"):
        failed_log[df["HTNO"][i]]=1
        if(dic.get(df["HTNO"][i])!=None):
            dic.pop(df["HTNO"][i])
    else:
        if(dic.get(df["HTNO"][i])==None and failed_log.get(df["HTNO"][i])==None):
            dic[df["HTNO"][i]]=[]   
        if(failed_log.get(df["HTNO"][i])==None):
            dic[df["HTNO"][i]].append(df["TOTALMARKS"][i])

max=[-1 , "tinku kalluri"]
max_index=0
for row in dic:
    if(row[1]=="9"):
        passed+=1
        total=0
        print(row)
        for i in dic[row]:
            print(i)
            total+=i
        print("========================================" , total/100)
        p=total/100
        if(max[0]<total/100):
            max.clear()
            max.append(p)
            max.append(row)
        elif(max[0]==total/100):
            max.append(p)
            max.append(row)
    # print(df['HTNO'][i] , df["SUBJECT_NAME"])

print("============congratulations===========")
print(max)
i=0
while(i<len(max)-1):
    print(max[i+1],"for scoring" , max[i])
    i+=2

print("passed_outs:" , passed)
j=0

print("=========failed==========")
for p in failed_log:
    if(p[1]=="9"):
        failed+=1
        print(p)

print("failed:" , failed)
