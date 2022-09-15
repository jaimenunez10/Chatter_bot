import random

name = input("What's your name? ")
print("Hi " + name)

question = input("Do you have a question for me? ")
num = random.randint(1, 3)

question_1 = "How are you?"
question_2 = "What are some words of wisom?"
question_3 = "What is your biggest fear?"
question_4 = "What is the weather today?"
question_5 = "Tell me something about the Tesla stock market on the most recent completed business day"

def stock_market():
    # Import yfinance package
    import yfinance as yf
    # Set the start and end date
    start_date = '1990-01-01'
    end_date = '2021-07-12'
    # Set the ticker
    ticker = 'TSLA'
    # Get the data
    data = yf.download(ticker)
    # Print price
    print(data.tail(1))

while question == question_1 or question_2 or question_3 or question_4 or question_5:
  if question == question_1:
        if num == 1:
            print("I'm doing good!")
        elif num == 2:
            print("I'm doing alright.")
        else:
            print("I'm doing bad.")
  elif question == question_2:
        if num == 1:
            print("Save money.")
        elif num == 2:
            print("Stay in school")
        else:
            print("Don't do drugs")
  elif question == question_3:
        if num == 1:
            print("Good question.")
        elif num == 2:
            print("The power going out.")
        else:
            print("I'm a robot. I don't feel fear.")
  elif question == question_4:
        if num == 1:
            print("Look outside and find out.")
        elif num == 2:
            print("might rain might not.")
        else:
            print("Couldn't compute.")
  elif question == question_5:
        stock_market()
  else:
        print("Try asking another question ")
        question = input("Do you have a question for me? ")
  question = input("Do you have another question for me? ")
