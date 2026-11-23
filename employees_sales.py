import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print(udaiveersingh)


import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print(udaiveersingh.head(10))
print(udaiveersingh.info())
print(udaiveersingh.isnull())


import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print(udaiveersingh["Sales"].sum())

import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print(udaiveersingh["City"].isnull().sum())


import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
result = udaiveersingh.map(lambda x: x.strip() if isinstance(x, str) else x)
print(result)

import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
udaiveersingh["Profit"] = (
    udaiveersingh["Sales"] -
    udaiveersingh["Quantity"] * udaiveersingh["Cost_Per_Unit"]
)


import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print(udaiveersingh["Sales"].sum())

import pandas as pd 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print(udaiveersingh.groupby(["City","Product"])["Sales"].sum())

import matplotlib.pyplot as plt 
udaiveersingh = pd.read_csv("employees_sales_project.csv")
print()




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees_sales_project.csv")

df["Sales"] = df["Quantity"] * df["Unit_Price"]

city_sales = df.groupby("City")["Sales"].sum()

plt.figure(figsize=(12, 6))
plt.bar(city_sales.index, city_sales.values)

plt.title("City-wise Total Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


import pandas as pd
df = pd.read_csv("employees_sales_project.csv")

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print(df.isnull().sum())

df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned data saved successfully!")




















































