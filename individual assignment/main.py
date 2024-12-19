import function as fc
import pandas as pd

def main():
    print("Welcome to the Stock Selection Tool!")

    while True:
        choice = input("Do you want to 1. Register or 2. Login? Please enter 1 or 2: ")
        if choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 to register or 2 to login.")
            continue

        if choice == '1':
            if not new_user():
                continue
            else:
                break
        elif choice == '2':
            if not existing_user():
                continue
            else:
                break

    stock_ticker()

def new_user():
    while True:
        email = input("Please enter your email (should include '@'): ")
        if not fc.check_email(email):
            print("Invalid email. Please ensure it contains '@'.")
            continue

        while True:
            password = input("Please enter your password: ")
            if not fc.check_password(password):
                print("Password must contain at least one capital letter and one number.")
                continue

            if fc.existing_user('user.csv', email):
                print("This email is already registered. Please login instead.")
                return False

            if fc.register_user(email, password):
                print("Registration successful! You can now log in.")
                return True

            print("Failed to register. Please try again.")

def existing_user():
    while True:
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        if fc.authenticate_user(email, password):
            print("Login successful. Welcome back!")
            return True
        else:
            print("Invalid email or password. Please try again.")
            return False
      
def stock_ticker():
    while True:
        ticker = input("Please enter the stock ticker (e.g., AAPL, TSLA): ")
        start_date = input("Please enter the start date (YYYY-MM-DD): ")
        end_date = input("Please enter the end date (YYYY-MM-DD): ")

        try:
            closing_prices = fc.get_closing_prices(ticker, start_date, end_date)
            if closing_prices is None or closing_prices.empty:
                print(f"Error retrieving data for {ticker}. Please check the ticker and date range.")
                continue

            average_price, percentage_change, highest_price, lowest_price = fc.analyze_closing_prices(closing_prices)
            
            email = input("Please enter your email to save this analysis: ")
            if fc.existing_user('user.csv', email):
                fc.save_to_csv(email, ticker, start_date, end_date, average_price, percentage_change, highest_price, lowest_price)
            else:
                print("Email not found. Please ensure you are logged in.")

        except Exception as e:
            print(f"An error occurred: {e}")

        view_data = input("Do you want to view stored data? (yes/no): ")
        if view_data.lower() == "yes":
            email = input("Please enter your email to view your data: ")
            filename = f"{email}_stock_analysis.csv"
            fc.read_from_csv(filename)

        exit_choice = input("Do you want to exit? (yes/no): ")
        if exit_choice.lower() == "yes":
            print("Thank you for using the Stock Selection Tool. Goodbye!")
            break

if __name__ == "__main__":
    main()
