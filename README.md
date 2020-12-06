<h1 align="center">
Instagram Bots
</h2>
<p align="center">

## Overview
This repository contains code written explicitly in [**Python 3**](https://www.python.org/) for creating bots that automate some processes of Instagram. These bots are made to make users life easier, as also help them gain followers, likes, etc. Use them wisely and have fun :satisfied:

All of the bots use the selenium library of python or better stated the selenium python API. Through this you can actually access functionalities of the [Selenium Webdriver](https://www.selenium.dev/), which automates the use of browsers. You can make browser-based regression automation suites and tests, scale and distribute scripts across many environments etc.

You can find the official documentation [here](https://www.selenium.dev/selenium/docs/api/py/api.html), as also an unofficial more extended documentation [here](https://selenium-python.readthedocs.io/index.html).

## Requirements
- Selenium
- Pandas

In order to install the required libraries, run: 

```
pip install -r requirements.txt
```

## Instagram Bot 1 (

Let's examine step by step what does this first bot do. 

1. First of all, as already mentioned, we make use of the Selenium WebDriver bindings in Python, so we have to define the path where our browser driver is. In this implementation we use the chromedriver (which you can very easily download from [here](https://chromedriver.chromium.org/downloads). We set the path of our driver in line 11. 
2. We then navigate to the Instagram site and especially to the login page, where the **username** and **password** are needed. Replace your personal settings in lines 18 and 20. 
3. We login and define the **hashtags** we are interested in. Let's describe now how exactly this bot works. Let's say you are interested in summer sunshine beach photos. You create a hashtag list, which in this occasion would be something like **[summer, beach, sun, sand, sunshine]**.
4. The bot navigates recursively to the hastag list, searches for the first **thumbnail**, saves the username of the first's thumbnail profile, searches how many **likes** does this photo has and tries to find out if we already **follow** this profile 
5. If the likes are more than a given **threshold** (you specify this threshold in line 69) and if we do not follow this profile, then:
a. It follows the profile
b. It appends the username of it on a list
c. It likes the picture
d. It makes a predefined random comment under some probability
e. It navigates to the next thumbnail picture of the current hastag. 
6. This loop is continued as many times as defined in line 55 for each hashtag. 
7. Finally, we create a DataFrame having the new followed accounts and we save it in a .csv file, which can be used the next time we run the script, by uncommenting lines 35 and 36.
