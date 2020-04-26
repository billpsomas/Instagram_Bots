# Instagram-Bots
This repository contains some Instagram Bots implemented in Python. They are uploaded for educational purposes, and not for gaining engagement, followers, likes etc. Please use them wisely and have fun!

All of the bots use the selenium library of python or better stated the selenium python API. Through this you can actually access functionalities of the [Selenium Webdriver](https://www.selenium.dev/), which automates the use of browsers. You can make browser-based regression automation suites and tests, scale and distribute scripts across many environments etc.

You can find the official documentation [here](https://www.selenium.dev/selenium/docs/api/py/api.html), as also an unofficial more extended documentation [here](https://selenium-python.readthedocs.io/index.html).

# Requirements
In order to install all the required libraries for this project, run pip install -r requirements.txt

## Instagram Bot 1

Let's examine step by step what does this first bot do. 

First of all, as already mentioned, we make use of the Selenium WebDriver bindings in Python, so we have to define the path where our browser driver is. In this implementation we use the chromedriver (which you can very easily download from [here](https://chromedriver.chromium.org/downloads). We set the path of our driver in line 11. 

We then navigate to the Instagram site and especially to the login page, where the username and password are needed. Replace your personal settings in lines 18 and 20. We login and define the hashtags we are interested in. Let's describe now how exactly this bot works. Let's say you are interested in summer sunshine beach photos. You create a hashtag list, which in this occasion would be something like [summer, beach, sun, sand, sunshine] and this bot navigates recursively to the hastag list, searches for the first thumbnail, saves the username of the first's thumbnail profile, searches how many likes does this photo have, tries to find out if we already follow this profile and if the likes are more than a given threshold (you specify this threshold in line 69), and if both statements are true, then it follows the profile, it appends it in a list, it likes the picture, it makes a predefined random comment under some probability and navigates to the next thumbnail picture of the current hastag. This loop is continued as many times as defined in line 55 for each hashtag. Finally, we create a DataFrame having the new followed accounts and we save it in a .csv file, which can be used the next time we run the script, by uncommenting lines 35 and 36.
