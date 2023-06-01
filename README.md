# Heron
Sentiment Analysis of UC Davis Professors

f10.py
We used this youtube video for inspiration on how to use selenium to webscrape stuff from ratemyprofessor:
https://www.youtube.com/watch?v=mWUOdV2nMOk

Notes for using:
To use it for other professors, change the list of urls to whatever ratemyprofessor urls for the professors you want to run the code for.
If you have Firefox, no change to the code is necessary to make it run locally.

How it runs:
The code uses selenium to open the ratemyprofessor link, extract the professor name and number of ratings on the page, and press the load more ratings button until all the ratings for the page are fully loaded. 
It uses beautiful soup to extract reviews from the page searching by the class name for the reviews on the site.
It uses the textblob package to perform sentiment analysis for the polarity of the reviews.
It uses matplotlib to make a pie chart and histogram distribution for the sentiment across reviews.
It uses the pandas to download a csv for the data. 

-The code iterates through a list of ratemyprofessor urls. 
-For each url, it opens the link in a new firefox window, extracts the professor name and the number of ratings from the website page, and then calculates the number of times the add more ratings button needs to be pressed to load all the ratings, and then iterates through a loop to press the load more ratings button that number of times, and then webscrapes all the reviews using their class name using beautiful soup and then for each web-scraped review it calculates the sentiment polarity using textblob. It then calculates the average sentiment polarity for that professor. Using the calculated sentiments of the reviews it uses matplotlib to create and download a pie chart and histogram figures for the reviews and then uses pandas to make a csv with the reviews data.
-The code will download a csv with all the professor reviews, the sentiment for each review, and the average sentiment across reviews, a pie chart displaying relative numbers of positive, negative, and neutral reviews, and a histogram with the distribution of sentiment for the reviews,  for all the professor links in the list of urls.


ProfCompare.py

READ BEFORE USING:
Each path name must be changed to where each csv file is stored on your computer.
For example,
dataset_Butner = pd.read_csv("C:\\Users\\rmp_butner.csv")
In this piece of code, "C:\\Users\\rmp_butner.csv" must be changed to the path of the file on your computer.
Also make sure to use f10.py first, because it will generate the csv files needed for this code.

How it runs:
This code uses pandas to read each csv and TextBlob to perform sentiment analysis of each comment for each professor.
It generates a pie chart, a bar graph, and a scatter plot to show how many of each type (Positive, Neutral, and Negative) of comments there are.



