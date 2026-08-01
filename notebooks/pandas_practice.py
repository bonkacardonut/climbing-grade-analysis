import pandas as pd
import numpy as np 

df = pd.read_csv("/Users/bianca/_BIANCA_/climbing-prediction/data/raw/climbharder_df.csv")

print(df.count())
print(df.loc["Sex", "Height (cm)"])

df.loc

# Practice with dataframes
'''df2 = pd.DataFrame( 
    {
        "age": np.random.randint(40, size=10),
        "wingspan": np.random.randint(20, size=10),
        "isMale": np.random.choice([0,1], size=10),
        "vgrade": np.random.randint(12, size=10)
    }
)

print(df2)
print(df2.dtypes)
print(df2["age"])

x=0
for i in range(10, 2, -2):
    print(i)
    x+=1
print(x)

vgrades = [1,2,3,4]
print("unmodified list:" + str(vgrades))

for i in vgrades:
    print(f"index: {i}")
    vgrades[i-1] = vgrades[i-1]*3

print(f"list after: {vgrades}")'''
