# to get all videosUrl of youtube playlist using python with beautifulSoup and Selenium
from bs4 import BeautifulSoup as bs
from selenium import webdriver


def getPlaylist(playlistUrl):
    playlist= []
    driver = webdriver.Chrome()
    driver.get(playlistUrl)
    soup=bs(driver.page_source,'html.parser')
    mainDiv = soup.find('div',id='contents')
    for link in mainDiv.find_all('a',id='video-title'):
        playlist.append('https://www.youtube.com'+link.get('href'))
    driver.quit()
    return playlist

# place your playlist url in here , playlist must be public
videoUrlList = getPlaylist('URL')
print(videoUrlList)