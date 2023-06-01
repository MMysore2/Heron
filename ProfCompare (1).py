#!/usr/bin/env python
# coding: utf-8

# In[47]:


from textblob import TextBlob
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# In[55]:


# https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1


dataset_Butner = pd.read_csv("C:\\Users\\mysor\\Downloads\\rmp_butner.csv")
data_Butner = dataset_Butner.iloc[:,1:2].values
Butner = str(listToString(data_Butner))
blob_Butner = TextBlob(Butner)

dataset_Posnett = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Daryl Posnett.csv")
data_Posnett = dataset_Posnett.iloc[:,1:2].values
Posnett = str(listToString(data_Posnett))
blob_Posnett = TextBlob(Posnett)

dataset_Solares = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Edwin Solares.csv")
data_Solares = dataset_Solares.iloc[:,1:2].values
Solares = str(listToString(data_Solares))
blob_Solares = TextBlob(Solares)

dataset_Wu = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Felix Wu.csv")
data_Wu = dataset_Wu.iloc[:,1:2].values
Wu = str(listToString(data_Wu))
blob_Wu = TextBlob(Wu)

dataset_Porquet = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Joël Porquet.csv")
data_Porquet = dataset_Porquet.iloc[:,1:2].values
Porquet = str(listToString(data_Porquet))
blob_Porquet = TextBlob(Porquet)

dataset_Stevens = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Kristian Stevens.csv")
data_Stevens = dataset_Stevens.iloc[:,1:2].values
Stevens = str(listToString(data_Stevens))
blob_Stevens = TextBlob(Stevens)

dataset_Eiselt = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Kurt Eiselt.csv")
data_Eiselt = dataset_Eiselt.iloc[:,1:2].values
Eiselt = str(listToString(data_Eiselt))
blob_Eiselt = TextBlob(Eiselt)

dataset_Ma = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Kwan-Liu Ma.csv")
data_Ma = dataset_Ma.iloc[:,1:2].values
Ma = str(listToString(data_Ma))
blob_Ma = TextBlob(Ma)

dataset_Franklin = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Matthew Franklin.csv")
data_Franklin = dataset_Franklin.iloc[:,1:2].values
Franklin = str(listToString(data_Franklin))
blob_Franklin = TextBlob(Franklin)

dataset_Sadoghi = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Mohammad Sadoghi.csv")
data_Sadoghi = dataset_Sadoghi.iloc[:,1:2].values
Sadoghi = str(listToString(data_Sadoghi))
blob_Sadoghi = TextBlob(Sadoghi)

dataset_Rafatirad = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Setareh Rafatirad.csv")
data_Rafatirad = dataset_Rafatirad.iloc[:,1:2].values
Rafatirad = str(listToString(data_Rafatirad))
blob_Rafatirad = TextBlob(Rafatirad)

dataset_Bhaskar = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Vidhyacharan Bhaskar.csv")
data_Bhaskar = dataset_Bhaskar.iloc[:,1:2].values
Bhaskar = str(listToString(data_Bhaskar))
blob_Bhaskar = TextBlob(Bhaskar)

dataset_Frid = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Yelena Frid.csv")
data_Frid = dataset_Frid.iloc[:,1:2].values
Frid = str(listToString(data_Frid))
blob_Frid = TextBlob(Frid)

dataset_Shafiq = pd.read_csv("C:\\Users\\mysor\\Heron\\rmp_Zubair Shafiq.csv")
data_Shafiq = dataset_Shafiq.iloc[:,1:2].values
Shafiq = str(listToString(data_Shafiq))
blob_Shafiq = TextBlob(Shafiq)


data_cs = [*data_Butner, *data_Solares, *data_Posnett, *data_Wu, *data_Porquet, *data_Stevens, *data_Eiselt, *data_Ma, *data_Franklin, *data_Sadoghi, *data_Rafatirad, *data_Bhaskar, *data_Frid, *data_Shafiq]
cs = str(listToString(data_cs))
blob_cs = TextBlob(cs)



print("Overall Sentiment:", blob_cs.sentiment.polarity)
print()
print("Ranked Sentiment:")
print("1. Kristian Stevens:", blob_Stevens.sentiment.polarity)
print("2. Joël Porquet:", blob_Porquet.sentiment.polarity)
print("3. Mohammad Sadoghi:", blob_Sadoghi.sentiment.polarity)
print("4. Setareh Rafatirad:", blob_Rafatirad.sentiment.polarity)
print("5. Yelena Frid:", blob_Frid.sentiment.polarity)
print("6. Matthew Butner:", blob_Butner.sentiment.polarity)
print("7. Kurt Eiselt:", blob_Eiselt.sentiment.polarity)
print("8. Felix Wu:", blob_Wu.sentiment.polarity)
print("9. Edwin Solares:", blob_Solares.sentiment.polarity)
print("10. Zubair Shafiq:", blob_Shafiq.sentiment.polarity)
print("11. Daryl Posnett:", blob_Posnett.sentiment.polarity)
print("12. Vidhyacharan Bhaskar:", blob_Bhaskar.sentiment.polarity)
print("13. Kwan-Liu Ma:", blob_Ma.sentiment.polarity)
print("14. Matthew Franklin:", blob_Franklin.sentiment.polarity)


positive = []
positiveVals = []
neutral = []
neutralVals = []
negative = []
negativeVals = []
allVals = []

for i in range (len(data_cs)):
    blob = TextBlob(str(data_cs[i]))
    blob_round = round(blob.sentiment.polarity * 10)/10
    allVals.append(blob.sentiment.polarity)
    
    if blob_round > 0.3:
        positive.append(i)
        positiveVals.append(round(blob.sentiment.polarity * 10)/10)
    
    elif blob_round < -0.3:
        negative.append(i)
        negativeVals.append(round(blob.sentiment.polarity * 10)/10)
    
    else:
        neutral.append(i)
        neutralVals.append(round(blob.sentiment.polarity * 10)/10)
    
for i in positive:
    blob2 = TextBlob(str(data_cs[i]))
    #print(blob2.sentiment.polarity)
    
types = ['Positive','Neutral','Negative']
values = [len(positive), len(neutral), len(negative)]
fig = plt.figure(figsize =(10, 7))
plt.pie(values, labels = types)
plt.show()

plt.bar(types, values)
plt.show()

positiveValsCount = []
positiveValsCount.append(positiveVals.count(0.4))
positiveValsCount.append(positiveVals.count(0.5))
positiveValsCount.append(positiveVals.count(0.6))
positiveValsCount.append(positiveVals.count(0.7))
positiveValsCount.append(positiveVals.count(0.8))
positiveValsCount.append(positiveVals.count(0.9))
positiveValsCount.append(positiveVals.count(1.0))

negativeValsCount = []
negativeValsCount.append(negativeVals.count(-1.0))
negativeValsCount.append(negativeVals.count(-0.9))
negativeValsCount.append(negativeVals.count(-0.8))
negativeValsCount.append(negativeVals.count(-0.7))
negativeValsCount.append(negativeVals.count(-0.6))
negativeValsCount.append(negativeVals.count(-0.5))
negativeValsCount.append(negativeVals.count(-0.4))

neutralValsCount = []
neutralValsCount.append(neutralVals.count(-0.3))
neutralValsCount.append(neutralVals.count(-0.2))
neutralValsCount.append(neutralVals.count(-0.1))
neutralValsCount.append(neutralVals.count(0.0))
neutralValsCount.append(neutralVals.count(0.1))
neutralValsCount.append(neutralVals.count(0.2))
neutralValsCount.append(neutralVals.count(0.3))



plt.scatter(x = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], y = [negativeValsCount, neutralValsCount, positiveValsCount])
plt.show()


# In[ ]:




