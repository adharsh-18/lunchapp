import pandas as pd
import random
import numpy

df = pd.read_excel("main.xlsx","data")


used = []
a = ''
d = {"Arab League":"AL","NATO":"NO","Plenary":"PL","ECOSOC":"EC","NITI Aayog":"NA","UNHRC":"UH","IPC":"IP"}
# for i in range(len(df)):
#     s = random.randrange(100,999)
#     while s in used:
#         s = random.randrange(100,999)    
#     used.append(s)
#     s1 = d[df.iat[i,3]]
    

#     df.iat[i,0]=s1+str(s)
#     print(df.iat[i,0],i)

for i in range(len(df)):
    if isinstance(df.iat[i,3],int):
        print("yooo")
        df.iat[i,3] = '+91'+str(df.iat[i,3])
    else:
        "".join(df.iat[i,3])

print(df)
# df.to_excel("main.xlsx","data")
