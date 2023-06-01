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
import pandas as pd
import re
import math
import time
from textblob import TextBlob
from selenium.webdriver import FirefoxOptions

list_of_urls=['https://www.ratemyprofessors.com/professor/2830184','https://www.ratemyprofessors.com/professor/2827331','https://www.ratemyprofessors.com/professor/148973','https://www.ratemyprofessors.com/professor/2438561',  'https://www.ratemyprofessors.com/professor/2509572',   'https://www.ratemyprofessors.com/professor/255974',   'https://www.ratemyprofessors.com/professor/2229763',  'https://www.ratemyprofessors.com/professor/2241323',   'https://www.ratemyprofessors.com/professor/2784321',   'https://www.ratemyprofessors.com/professor/2633957',  'https://www.ratemyprofessors.com/professor/149778',   'https://www.ratemyprofessors.com/professor/2080850',   'https://www.ratemyprofessors.com/professor/2469276']

for a in list_of_urls:
    driver = webdriver.Firefox()
    driver.get(a)
    #delay=3
    try: 
        #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "IL_IFR_DIV0")))
        driver.find_element("xpath","//div[starts-with(@class, 'FullPageModal__')]//button").click()
    except:
        print("")
    numratings = driver.find_element("xpath","//a[@href='#ratingsList']")
    numratings_text = numratings.text
    #print(numratings_text)
    profName=driver.find_element("xpath","//div[starts-with(@class,'NameTitle__Name')]").text
    #print(profName)
    a=[]
    a=[int(s) for s in numratings_text.split() if s.isdigit()]
    number_of_button_presses = math.ceil((a[0]-20)/10)
    if number_of_button_presses>1:
        for i in range(1,number_of_button_presses+1):
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "");
            bl=0
            while(bl!=1):            
                try:
                    driver.find_element("xpath","//button[text()='Load More Ratings']")
                    bl=1
                except:
                    driver.execute_script("window.scrollBy(0,-500)", "");           
            bl=0
            element = driver.find_element("xpath","//button[text()='Load More Ratings']")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("window.scrollBy(0,-400)", "");
            driver.find_element("xpath","//button[text()='Load More Ratings']").click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    average=[]
    revs_list= []
    polarity_list= []
    pos=0
    neg=0
    neutral=0
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
    #print(revs_list)
    #print(polarity_list)
    av=0
    av=sum(polarity_list)/(a[0])
    average.append(av)
    #print(average)
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
    #plt.show()
    matplotlib.pyplot.close()
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(polarity_list, bins = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    hsn='histogram_'+profName+'.png'
    plt.savefig(hsn)
    #plt.show()
    matplotlib.pyplot.close()
    str1='Reviews for '
    str1+=profName
    str2='Polarity for '
    str2+=profName
    str3='Average Sentiment for '
    str3+=profName
    revs_data = {str1: revs_list, str2:polarity_list, str3:av}
    df = pd.DataFrame(revs_data)
    filename='Rmp_'+profName+'.csv'
    df.to_csv(filename)
    driver.quit()
#while(True):
    #pass
