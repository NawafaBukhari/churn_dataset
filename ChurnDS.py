import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%%
# Import dataset 
df = pd.read_csv('ChurnData.csv')
df
# %%
# find the relation between the gender and the country and the estimated salary plt.figure(figsize=(10, 8))
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
#%%
plt.figure(figsize=(20, 20))
sns.catplot(x="Geography", y="EstimatedSalary",
            hue="Gender", kind="box", data=df)
plt.title("Geography VS Estimated Salary")
plt.xlabel("Geography")
plt.ylabel("Estimated Salary")
# %%
# Which age group is the most active?
bins = [18, 29, 39, 49, 59, np.inf]
labels=['18-29','30-39','40-49','50-59','>60']
age_df = df.filter(['Age','IsActiveMember'], axis=1)
age_df['Age Group'] = pd.cut(age_df['Age'], bins=bins, labels=labels)
#age_df.pivot_table(index='Age Group', columns='IsActiveMember', values='Age', aggfunc='count').fillna(0).astype(int)
sns.displot(data=age_df, x="Age Group", hue="IsActiveMember", multiple="stack")

# %%
#Looking at Gender Distribution against Estimated Salary
sns.boxplot(x="Gender", y="EstimatedSalary", data=df)
plt.ylim(0,250000)
plt.title("Gender VS Estimated Salary")
plt.xlabel("Gender")
plt.ylabel("Estimated Salary")
#%%
# Looking at Geography and Gender Distribution against Estimated Salary
sns.boxplot(x="Geography", y="EstimatedSalary", hue="Gender", data=df)
plt.ylim(0,250000)
plt.title("Geography VS Estimated Salary")
plt.xlabel("Geography")
plt.ylabel("Estimated Salary")
# %%
# Which geography has the highest average balance
dff = df.groupby(by = [df.Geography])['Balance'].mean()
plt.bar(['France','Germany','Spain'], [dff['France'],dff['Germany'],dff['Spain']], color =['cornflowerblue','darkorange','gold'],
        width = 0.4)
plt.xlabel("Geography")
plt.ylabel("Balance")
plt.title("Average Balance According to Geography")
plt.show()# %%
# %%
# Visualizing relationship of Age and Estimated Salary
plt.figure(figsize=(20,20))
sns.relplot(x="Age", y="EstimatedSalary", hue="Geography", data=df)
plt.title("Age VS Estimated Salary")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
# %%
