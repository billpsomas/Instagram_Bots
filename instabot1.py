# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import re

# The chromedriver path
# Replace the path according to where chromedriver is located in your PC
chromedriver_path = 'C:/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

# Replace USERNAME and PASSWORD 
username = driver.find_element_by_name('username')
username.send_keys('USERNAME')
password = driver.find_element_by_name('password')
password.send_keys('PASSWORD')

# Login
button_login = driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')                                                   
button_login.click()
sleep(3)

notnow = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

# Define the hashtags that you are interested in
hashtag_list = ['ENTER THE HASTHAGS YOU ARE INTERESTED IN HERE']

prev_user_list = [] # if it's the first time you run it, use this line and comment out the two below
#prev_user_list = pd.read_csv('20190907-163153_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    # It navigates to the hashtags of the list previous defined
    driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    # It searches for the first thumbnail
    first_thumbnail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    try:        
        for x in range(1,9):
            # It saves the username of the first's thumbnail profile
            username = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2').text
            
            if username not in prev_user_list:
                
                # Searches how many likes does the photo has
                likes_string= driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div').text
                likes_wrong= re.findall('\d+', likes_string )
                likes_wrong[:] = [''.join(likes_wrong[:])]
                likes = int(likes_wrong[0])
                    
                # It tries to find out if we already follow this profile and if the likes are more than 800
                # This is done in order to escape cases following fake profiles or profiles with not so good content
                if driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow' and likes > 200:

                    # If we do not follow and likes are > 800, then it follows the profile
                    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    
                    # It appends the name in the new_followed list
                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                    
                    button_like.click()
                    likes += 1
                    sleep(randint(18,25))

                    # Comments and tracker
                    comm_prob = randint(1,10)
                    print('{}_{}: {}'.format(hashtag, x,comm_prob))
                    # Comments when the probability is larger than 50%
                    if comm_prob > 5:
                        comments += 1
                        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                        comment_box = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div[1]/form/textarea')

                        if (comm_prob == 6):
                            comment_box.send_keys('Amazing!')
                            sleep(1)
                        elif (comm_prob == 7):
                            comment_box.send_keys('Nice work!')
                            sleep(1)
                        elif comm_prob == 8:
                            comment_box.send_keys('Nice photo')
                            sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('So cool!')
                            sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('Very nice')
                            sleep(1)
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        sleep(randint(22,28))

                # Next picture
                driver.find_element_by_link_text('Next').click()
                sleep(randint(25,29))
            else:
                driver.find_element_by_link_text('Next').click()
                sleep(randint(20,26))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

# Add the new followed userd to the prev_user_list
for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))