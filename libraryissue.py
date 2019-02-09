from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# --- UNCOMMENT LATER AFTER DEBUGGING ---
#To make the browser not open up i.e. open up a headless chrome browser
# options =  Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver_path = r'C:/Users/targe/Documents/Library_Reissuer/chromedriver_win32/chromedriver.exe'
#
# browser = webdriver.Chrome(driver_path, chrome_options=options)
# browser.get('http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fw27%2fMyInfo%2fw27MyInfo.aspx')

browser = webdriver.Chrome(r'C:/Users/targe/Documents/Library_Reissuer/chromedriver_win32/chromedriver.exe')
browser.get('http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fw27%2fMyInfo%2fw27MyInfo.aspx')

username = browser.find_element_by_id("txtUserName")
password = browser.find_element_by_id("Password1")

username.send_keys("18179")
password.send_keys("MEMBER")

browser.find_element_by_id("Submit1").click()

soup = BeautifulSoup(browser.page_source, 'lxml')

table = soup.find('table', class_='clsDataGrid')
table_rows = table.find_all('tr')

# Skipping first row because it just contains the table headers
for row_index in range(1,len(table_rows)):
    table_elements = table_rows[row_index].find_all('td')

    return_date = table_elements[4].text.strip()
    print(return_date)
