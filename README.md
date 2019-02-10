# AIT LIBRARY REISSUER



  - Uses selenium webdriver to log into the AIT (Army Institute of Technology) E-Library and login using given credentials.
  - Uses beautiful soup to parse the website
### # What it does so far

  - Prints out various data related to issued book on the terminal
  - Reissues if the current date is greater than or equal to the due date.
  - Sends a email to the user to remind him of the remaining days

### # TODO

    - Improve the email content
    - Provide an option to reissue immediately

### Required Python Modules

Library Reissuer requires the following modules to be installed

* [selenium] - Selenium WebDriver
* [bs4] - Beautiful Soup 4
* [py36] - Python 3.6
* [datetime] - Datetime Python Module



   [selenium]: <https://www.seleniumhq.org/>
   [bs4]: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
   [py36]: <https://www.python.org/downloads/release/python-360/>
   [datetime]: <https://docs.python.org/2/library/datetime.html>

   -- Jedi18 (Akhil J Nair)
