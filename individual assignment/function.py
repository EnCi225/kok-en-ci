import pandas as pd
import yfinance as yf
import csv
import os

def check_email(email):
    return "@" in email

def check_password(password):
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_digit

def register_user(email, password):
    try:
        file_exists = os.path.exists("user.csv")
        with open("user.csv", "a", newline="") as csvfile:
            fieldnames = ["email", "password"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({"email": email, "password": password})
            return True
    except Exception as e:
        print(f"User creation failed. Please try again. (Error: {e})")
        return False

def existing_user(filename, email):
    try:
        if not os.path.exists(filename):
            return False
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == email:
                    return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def authenticate_user(email, password):
    try:
        if not os.path.exists("user.csv"):
            print("No users registered yet. Please register.")
            return False
        with open("user.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] == email and row["password"] == password:
                    return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_closing_prices(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data['Close']
    except Exception as e:
        print(f"Error retrieving data for {ticker}: {e}")
        return None

def analyze_closing_prices(closing_prices):
    try:
        average_price = closing_prices.mean()
        percentage_change = ((closing_prices.iloc[-1] - closing_prices.iloc[0]) / closing_prices.iloc[0]) * 100
        highest_price = closing_prices.max()
        lowest_price = closing_prices.min()

        return average_price, percentage_change, highest_price, lowest_price
    except Exception as e:
        print(f"Error analyzing closing prices: {e}")
        return None, None, None, None

def save_to_csv(email, ticker, start_date, end_date, average_price, percentage_change, highest_price, lowest_price):
    filename = f"{email}_stock_analysis.csv"

    try:
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Ticker", "Start Date", "End Date", "Average Price", "Percentage Change", "Highest Price", "Lowest Price"])
            writer.writerow([
                ticker,
                start_date,
                end_date,
                round(average_price, 2),
                f"{round(percentage_change, 2)}%",
                round(highest_price, 2),
                round(lowest_price, 2),
            ])
        print("Analysis appended to your CSV file.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def read_from_csv(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    print(f"Ticker: {row[0]}")
                    print(f"Start Date: {row[1]}")
                    print(f"End Date: {row[2]}")
                    print(f"Average Price: {row[3]}")
                    print(f"Percentage Change: {row[4]}")
                    print(f"Highest Price: {row[5]}")
                    print(f"Lowest Price: {row[6]}")
                    print("-" * 20)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
    else:
        print(f"File {filename} not found.")
