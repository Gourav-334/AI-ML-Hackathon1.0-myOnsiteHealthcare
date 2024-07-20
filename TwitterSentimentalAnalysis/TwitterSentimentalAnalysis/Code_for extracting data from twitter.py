import tweepy
import pandas as pd

consumer_key = "nQj506cB3MXgFAv4MGUJ3JYyo"
consumer_secret = "zD3Mzd94zotXiW2cEg9TWWbGiEUcTJmbNX66D1fsVKdRI5LCJN"
access_token = "1499644827260289026-nv3c5dsPXpIB1dhxbPcDi8RZDoxJii"
access_token_secret = "8yW4TXn2PTqXEq74XfEfgPVvtyGmkHuw3LunKW9px2UT2"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
number_of_items=10
dateUntil = '2020-07-01'

searchword="#COVID and #DELHI "
tweets=tweepy.Cursor(api.search_tweets(q=searchword,lang='en')).items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

print(df)

searchword="#COVID and #Chennai"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df1=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

searchword="#COVID and #Mumbai"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df2=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

searchword="#COVID and #Bengaluru"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df3=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

searchword="#COVID and #Kolkata"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df4=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

frames=[df,df1,df2,df3,df4]
result = pd.concat(frames)
print(result)


for i in range(len(result)) :
    if "delhi" in result.iloc[i, 3] or "delhi" in result.iloc[i, 1]:
        result.iloc[i, 3]="Delhi"
    elif "mumbai" in result.iloc[i, 3] or "mumbai" in result.iloc[i, 1]:
        result.iloc[i, 3]="Mumbai"
    elif "chennai" in result.iloc[i, 3] or "chennai" in result.iloc[i, 1]:
        result.iloc[i, 3]="Chennai"
    elif "bengaluru" in result.iloc[i, 3] or "bengaluru" in result.iloc[i, 1]:
        result.iloc[i, 3]="Bengaluru"
    elif "kolkata" in result.iloc[i, 3] or "kolkata" in result.iloc[i, 1]:
        result.iloc[i, 3] = "Kolkata"
    else:
        result.iloc[i, 3] = "Other"


result.to_csv('tweets.csv', index=False)
