from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get('https://www.nba.com/players')
data = response.text
soup = BeautifulSoup(data, 'html.parser')

results = soup.find_all('td')
length = len(results)

player_list = []
all_player_list = []
for result in results:
    x = result.getText()
    player_list.append(x)

start = 0
end = len(results)

for x in range(start, end, 8):
    y = (player_list[x:x+8])
    all_player_list.append(y)

# itemDict = {item[0]: item[1:] for item in all_player_list}
# print(itemDict)
#####################################
new_dict = {}
for index, element in enumerate(all_player_list):
    new_dict[index] = element

driver = webdriver.Chrome()
for n in range(length):
    driver.get('https://forms.gle/xVQwBPfGXLvsUPGfA')
    time.sleep(5)
    get_name = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_team = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_number = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_position = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_height = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_weight = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_last_team = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    get_country = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')

    get_name.send_keys(new_dict[n][0])
    get_team.send_keys( new_dict[n][1])
    get_number.send_keys(new_dict[n][2])
    get_position.send_keys(new_dict[n][3])
    get_height.send_keys(new_dict[n][4])
    get_weight.send_keys(new_dict[n][5])
    get_last_team.send_keys(new_dict[n][6])
    get_country.send_keys(new_dict[n][7])

    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

