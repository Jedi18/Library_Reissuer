from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

# --- UNCOMMENT LATER AFTER DEBUGGING ---
#To make the browser not open up i.e. open up a headless chrome browser
# options =  Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver_path = r'C:/Users/targe/Documents/Library_Reissuer/chromedriver_win32/chromedriver.exe'
#
# browser = webdriver.Chrome(driver_path, chrome_options=options)
# browser.get('http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fw27%2fMyInfo%2fw27MyInfo.aspx')

print("Please enter your username :- ")
usern = input().strip()

browser = webdriver.Chrome(r'chromedriver_win32/chromedriver.exe')
browser.get('http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fw27%2fMyInfo%2fw27MyInfo.aspx')

# Login using the given credentials

username = browser.find_element_by_id("txtUserName")
password = browser.find_element_by_id("Password1")

username.send_keys(usern)
password.send_keys("MEMBER")

browser.find_element_by_id("Submit1").click()

# -- Login part over --

# get current date
today = datetime.datetime.today()

soup = BeautifulSoup(browser.page_source, 'lxml')

table = soup.find('table', class_='clsDataGrid')
table_rows = table.find_all('tr')

# Skipping first row because it just contains the table headers
for row_index in range(1,len(table_rows)):
    table_elements = table_rows[row_index].find_all('td')

    # Title of the book and author
    title_str = table_elements[1].text.strip()
    author_str = table_elements[2].text.strip()

    # Convert return date to datetime object
    return_date_str = table_elements[4].text.strip()
    return_date_str = return_date_str.replace('-', ' ')
    return_date = datetime.datetime.strptime(return_date_str,'%d %b %Y')

    if today.date() == return_date.date():
        print("Ruuuuun today's the return date!!!! (If you can't reissue, if you can just sit back and relax)")
    elif today > return_date:
        fine = table_elements[7].span.text.strip()
        print("Whoopsie, too late, your fine for this book is - {}".format(fine))
        print("Reissuing...")
        browser.find_element_by_id("ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl02_Button1").click()
        print("Hurray! Reissued")

    days_remaining = return_date - today

    print('{} by {} - {}'.format(title_str,author_str,return_date))
    print('Number of days remaining before reissuing date is {}'.format(days_remaining.days))
    print()
