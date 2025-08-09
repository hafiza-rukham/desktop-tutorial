import pandas as pd

df = pd.read_csv(r"C:\Users\Rukham Ijaz\Downloads\Documents\GitHub\desktop-tutorial\RealEstate-USA.csv", delimiter=',',parse_dates=[11],date_format={'date_time':'%d-%m-%y'})
print(df)
print(df.dtypes)

#Display 10 rows of first
print('first 10 rows')
print(df.head(10))

#display 10 rows of last"
print('last 10 rows')
print(df.tail(10))

print("df.info():",df.info())

#Summary of statistic of data frame using describe method:
print("summary of statistic of data frame using describe method",df.describe())

#Counting the rows and columns in DataFrame using shape().
print("Counting the rows and columns in DataFrame using shape():",df.shape)
print()

#access the name column
acre_lot = df['acre_lot']
print("access the name column :df :")
print(acre_lot)
print()

#access multiple column
acre_lot_house_size= df [["acre_lot","house_size"]]
print("access multiple column")
print(acre_lot_house_size)
print()

#Selecting a single row using .loc
row = df.loc[2]
print("Selecting a single row using . loc:",row)
print(row)
print()

#Selecting multiple row using .loc
row1 = df.loc[[3,5]]
print("Selecting multiple row using .loc:",row1)
print(row1)
print()

#Selecting a slice of rows using .loc
row2 = df.loc[3:6]
print("Selecting a slice of rows using .loc:",row2)
print(row2)
print()

print(df['state'].unique())

#Conditional selection of rows using .loc
row3 = df.loc[df['state'] == 'Puerto Rice']
print("Conditional selection of rows using .loc:",row3)
print(row3)
print()

#Selecting a single column using .loc
row4 = df.loc[:2,'acre_lot']
print("Selecting a single column using .loc")
print(row4)
print()

#Selecting multiple columns using .loc
row5 = df.loc[:1['acre_lot','state']]
print("Selecting multiple columns using .loc:",row5)
print(row5)
print()

#Selecting a slice of columns using .loc
row6 = df.loc[:1,'acre_lot':'state']
print("#Selecting a slice of columns using .loc")
print(row6)
print()

#Combined row and column selection using .loc
row7 = df.loc[df['state'] == 'Puerto Rice','location':'state']
print("#Combined row and column selection using .loc")
print(row7)
print()

