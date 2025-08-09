import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from a CSV file
df = pd.read_csv(r"C:\Users\Rukham Ijaz\Downloads\Documents\GitHub\desktop-tutorial\RealEstate-USA.csv", delimiter=',',parse_dates=[11],date_format={'date_time':'%d-%m-%y'},index_col='brokered_by')
print(df)
print(df.dtypes)

df = df.head(20)
df100 = df.head(30)
print(df)
print(df100)

sns.set_theme(style ='darkgrid')

#sns.histplot
s = sns.histplot(data = df,x = "price",y = "acre_lot" , hue = "state" , multiple="stack" )
s.figure.suptitle("sns.suptitle(data = df , x = 'price', y = 'acre_lot',hue = 'state',multiple ='stack')")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#sns.barplot
s = sns.barplot(data = df, x = "price",y = "acre_lot", legend=False)
s.figure.suptitle("sns.barplot(data = df,x = price , y = acre_lot , legend = False)")
# Display the plot
s.figure.show()
read = input("Wait for me.... ")

#sns.lineplot
s = sns.lineplot(data=df,x = "price", y = "acre_lot",hue = "state")
s.figure.suptitle("sns.lineplot(data = df,x= price, y = acre_lot)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#sns.kdeplot
s = sns.kdeplot( data = df,x = "price",y = "acre_lot" )
s.figure.suptitle("sns.kdeplot,x = 'price",y = 'acre_lot')
# Display the plot
s.figure.show()
read = input("Wait for me....")

#sns.catplot
s = sns.catplot(data=df , x = "price", y = "acre_lot")
s.figure.suptitle("sns.catplot(data = df , x = 'price', y = 'acre_lot')")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#.pivot(index = "Model", column = "acre_lot", values = "price")
var = df.pivot(columns= "acre_lot", values = "price")

s = sns.heatmap(var)
s.figure.suptitle("sns.heatmap(var) - var = df.pivot(columns=acre_lot , values= price)")
#Display the plot
s.figure.show()
read = input("Wait for me....")
