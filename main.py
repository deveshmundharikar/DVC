import pandas as pd 
import os 
#create a sample DataFreame with in cloumns name 

data = {'name':['rooknight','luffy','zoro'],
        'age':[21,22,23],
        'city':['mumbai','pune','bangalore']}

df = pd.DataFrame(data)
print(df)


 
 #add on extra data v1
data = {"name":"kitagawa","age":21,"city":"mumbai"}
df.loc[len(df.index)] = data

#another data add v2
data = {"name":"yamato","age":21,"city":"mumbai"}
df.loc[len(df.index)] = data

#another data add v3
data = {"name":"eren","age":21,"city":"mumbai"}
df.loc[len(df.index)] = data



#ensure the dara directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#define the file path 
file_path = os.path.join(data_dir, 'sample.csv')

#save the dataframe to the csv files , including columns names 
df.to_csv(file_path, index=False)

print(f"csv files saved to {file_path}")