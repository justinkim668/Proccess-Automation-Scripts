### Process Automation Scripts
This is collection of simple Python & Javascript/Typescript scripts I use to automate multiple processes at work. Feel free to use these if you want to automate some of your own tedious tasks at work and make life a little easier.

Frameworks used: Pandas, Requests-HTML, BeautifulSoup, Office Scripts API

## Descriptions of the scripts

date_reformatter.py - Given a .csv file with a list of dates formatted as 'MMDDYYYY' (US Date format), this script will convert all the dates to 'DDMMYYYY' (UK + Western Europe Date format).  This also works in the reverse i.e. 'DDMMYYYY' -> 'MMDDYYYY' if you switch some of the variables around.

date_reformatter2.py - Given a .csv file with a list of dates formatted as 'DDMMYYYY', this script will convert all dates to 'DD/MM/YYYY' (slashes separating the days, months, and years).  This also works for dates formatted 'MMDDYYYY' if you switch some of the variables around.

email_extractor.py - Given a URL, the script will scrape the HTML of the website and return with a list of email addresses.

columnAbsVal.js - Given an excel sheet, the script will convert the values stored within columns into absolute values of themselves, which turns all the values positive.  This process can be looped over multiple columns.

compose_email.py - Given a list of emails ina .csv file and a template email, this script will take the names and and compose your emails for you.  No more copying from excel into the body of the email, especially when you have to do this for 100+ names. 
