import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('FIFA19.csv')

#1. Which countries have the highest number of players represented in the dataset?
player_count={}
for i in df['Nationality']:
        if i not in player_count:
            player_count[i]=0
        else:
            player_count[i]=player_count[i]+1

most_player=sorted(player_count.items(), key= lambda x:x[1],reverse=True)[:5]

for country, count in most_player:
    print(country,":",count)
print('\n')

#5. How many players in the dataset have a crossing rating above 80?

crossing_players=df[df.Crossing>80]
no_of_players=crossing_players.shape[0]
print("There are {} players with Crossing above 80 \n".format(no_of_players))

#6. What is the average heading accuracy of players in the dataset?

average_heading=df['HeadingAccuracy'].mean()
print('The average heading accuracy: \n',average_heading)

#3. Which players have the highest market values and wages?

df1=df.query('Overall>=88')

df1['Value']=df1['Value'].str.replace('€','')
df1['Value']=df1['Value'].str.replace('M','')
df1['Wage']=df1['Wage'].str.replace('€','')
df1['Wage']=df1['Wage'].str.replace('K','')

df1.Value=df1.Value.astype('float')
df1.Wage=df1.Wage.astype('int')
df1.Name=df1.Name.astype('category')

df1=df1.sort_values(['Value','Wage'],ascending=False)

for index,row in df1.iloc[:5].iterrows():
        print(f"{row['Name']},{row['Value']},{row['Wage']} \n")

#2. How does the overall rating of players vary with age?

plt.hist(df['Age'])
plt.xlabel('Player Age')
plt.ylabel('No of Players')
plt.show()

oldest=df.loc[df['Age'].idxmax()]
print('The oldest player is ',oldest['Name'],' with age ',df['Age'].max())

#4. Which club/country has the highest total value of players in the dataset?

df2=df

df2['Value']=df2['Value'].str.replace('€','')
df2['Value']=df2['Value'].str.replace('M','')
df2['Value']=df2['Value'].str.replace('K','')
df2['Wage']=df2['Wage'].str.replace('€','')
df2['Wage']=df2['Wage'].str.replace('K','')

df2.Value=df2.Value.astype('float')
df2.Wage=df2.Wage.astype('int')

df3=df2.groupby('Nationality')['Value'].sum()
most_country=sorted(df3.items(), key= lambda x:x[1],reverse=True)[:5]
print(most_country)


