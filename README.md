# Precipitation-Project

 Wep Scrapping from https://www.cnrfc.noaa.gov/ and Data Visualization

## Purpose of this project
These days, it is obvious to see extreme weather change. Many natural disasters have been occurring throughout the whole world. Even though we could easily encounter these news through a lot of media, it seems that many people do not recognize the seriousness of the situation. For example, drought have been an issue in United States for a long time, but people's lifestyle have not changed. They still use a lot of water and while they are using it, they do not consider the situation. 

I thought people do not consider and take it lightly because they just heard about it from someone else. I believed that if they see something visual that shows how the earth's environment is going on right now since past few years, they might have took it heavier and recognize the situation properly. Therefore, I decided to webscrape from official government precipitation website and visually help them to understand the situation easily.

## Web Scraping

 Used Library: BeautifulSoup4, csv

 By using beautifulsoup4 library, scrapper scrapped all the rows of the talbe from https://www.cnrfc.noaa.gov/. While scrapping, I decided to drop rows which had 'M' in index because all the rows that had 'M' in the index had missing value for 'Total WY' and 'Pct Avg to Date'

cities_precipitation.png
