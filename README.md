This task is create the stock selection tool and it also can help to analysis stock performance over the specified period.
In this task need to install the yfinance libraries to get the data and enter "pip install yfinance"
For main () files
Frist, user must choose the option is whether to register become the new user or log in when you already have account.
if you choose option of register you need to enter the email with contain symbol "@" and password must contain capital letter and number.
if you choose the login you must enter the right email and passwor, if not it can not be run.
enter the stock ticker with specified code then enter the start date and end date.
So that, the system will get the closing prices from the yfinance that we have download in python.
Enter the email to save the analysis data and when will the data must enter the email first, then can see the analysis data.
Last enter you want to exit or not, if not it will loop again the stock ticker. 

for function () files
check the email is contain the symbol "@" for the register part and the passwrod contian with capital letter and number.
from the main() files register the new user it will save the data into csvfile.
existing_user,it will read the data from the csv file to confirm the email do not appear the same email.
authenticate_user it will read the data from csv file and use to confirm login email is consistency in csv file that being saving.
get_closing_prices is to know the closing price from the yfinance.
analyze_closing_prices to solve average price, percentade price, highest price and lowest price and save to csv file.
save_to_csv is saving email, ticker, start date, end date, average price, percentade price, highest price and lowest price.
read_from_csv it is read from the csv file.
