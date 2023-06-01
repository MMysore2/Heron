import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import requests
from bs4 import BeautifulSoup
#from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
#from selenium.webdriver.chrome.service import Service
import re
import math
import time
from textblob import TextBlob
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxOptions
#opts = FirefoxOptions()
#opts.add_argument('--headless')
"""
options=FirefoxOptions()
opts = options.add_argument("--no-sandbox")
driver = webdriver.Firefox(options=opts)
"""
driver = webdriver.Firefox()
list_of_urls=['https://www.ratemyprofessors.com/professor/148973','https://www.ratemyprofessors.com/professor/2827331','https://www.ratemyprofessors.com/professor/2438561',  'https://www.ratemyprofessors.com/professor/2509572',   'https://www.ratemyprofessors.com/professor/255974',   'https://www.ratemyprofessors.com/professor/2229763',  'https://www.ratemyprofessors.com/professor/2241323',   'https://www.ratemyprofessors.com/professor/2784321',   'https://www.ratemyprofessors.com/professor/2633957',  'https://www.ratemyprofessors.com/professor/149778',   'https://www.ratemyprofessors.com/professor/2080850',   'https://www.ratemyprofessors.com/professor/2469276',  'https://www.ratemyprofessors.com/professor/2830184']

for a in list_of_urls:
    driver.get(a)

    #driver.get('https://www.ratemyprofessors.com/professor/1961070')
    delay=3
    #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "IL_IFR_DIV0")))
    #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(("xpath","//div[starts-with(@class, 'FullPageModal__')]//button")))
    try: 
        #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "IL_IFR_DIV0")))
        driver.find_element("xpath","//div[starts-with(@class, 'FullPageModal__')]//button").click()
    except:
        print("")
    numratings = driver.find_element("xpath","//a[@href='#ratingsList']")
    numratings_text = numratings.text
    print(numratings_text)
    profName=driver.find_element("xpath","//div[starts-with(@class,'NameTitle__Name')]").text
    print(profName)
    a=[]
    a=[int(s) for s in numratings_text.split() if s.isdigit()]
    looprepeats = math.ceil((a[0]-20)/10)
    print(looprepeats)
    if looprepeats>1:
        for i in range(1,looprepeats+1):
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "");
            element = driver.find_element("xpath","//button[text()='Load More Ratings']")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("window.scrollBy(0,-500)", "");
            driver.find_element("xpath","//button[text()='Load More Ratings']").click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #classifier = TextClassifier.load('en-sentiment')
    average=[]
    revs_list= []
    polarity_list= []
    pos=0
    neg=0
    neutral=0
    #subjectivity_list = []
    for item in soup.select("div[class^=Comments__StyledComments]"):
        sent=""+item.get_text()
        revs_list.append(sent)
        test = TextBlob(sent)
        polar=test.sentiment.polarity
        polarity_list.append(polar)
        if polar>-0.15 and polar<0.15:
            neutral+=1
        elif polar>=0.15:
            pos+=1
        else:
            neg+=1
    
    #subjectivity_list.append(test.sentiment.subjectivity)
    print(revs_list)
    print(polarity_list)
    av=0
    av =sum(polarity_list)/(a[0])
    average.append(a)
    print(average)
    cum = ""
    cum.join(revs_list)
    cum_test=TextBlob(cum)
    cum_totalsent= cum_test.sentiment.polarity
    print(cum_totalsent)
    pnn_data=[]
    pnn_data.append(pos)
    pnn_data.append(neg)
    pnn_data.append(neutral)
    type=[]
    type=['Positive','Negative','Neutral']
    fig = plt.figure(figsize =(10, 7))
    plt.pie(pnn_data, labels = type)
    pch='pie_chart_'+profName+'.png'
    plt.savefig(pch)
    plt.show()

    #matplotlib.pyplot.close()
    fig, ax = plt.subplots(figsize =(10, 7))
    #ax.hist(polarity_list, bins = [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
    ax.hist(polarity_list, bins = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    hsn='histogram_'+profName+'.png'
    plt.savefig(hsn)
    plt.show()
    #matplotlib.pyplot.close()
    """
    #print(sum(sent_list)/a[0])
    #b=round(---)
    pos=0
    neutral
    neg=0
    if(b==1)
        pos++
    """
    str1='Reviews for '
    str1+=profName
    str2='Polarity for '
    str2+=profName
    str3='Average Sentiment for '
    str3+=profName
    revs_data = {str1: revs_list, str2:polarity_list, str3:av}
    df = pd.DataFrame(revs_data)
    filename='rmp_'+profName+'.csv'
    df.to_csv(filename)
    #parent = driver.window_handles[0]
    #chld = driver.window_handles[1]
    #driver.switch_to.window(chld)
    #driver.close()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
while(True):
    pass
