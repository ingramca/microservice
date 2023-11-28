# Author: Caleb Ingram
# Student ID: 932328804
# Email: ingramca@oregonstate.edu
# Date: 11/20/2023
# Description: This microservice listens to a text file, waiting for currency codes to be written to it.
#              Once the text file has been written to with 2 currencies, this service will replace that text
#              with the conversion rate from the 1st currency to the 2nd. For example, if 1 USD = 0.8029 GBP
#              and the text file reads "USD, GBP", then the text will be replaced with "0.8029".
#
#              This service uses the free version of the API at https://www.exchangerate-api.com/


##############################################################################################
# Sources: 
#
#   https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       Technique inspired by source: How to open a file with the "with" keyword (see below), adapted
#       several times to read/write files throughout this program. Specifically:
#       
#           with open('workfile', encoding="utf-8") as f:
#               read_data = f.read()
#
# --------------------------------------------------------------------------------------------
#   https://www.geeksforgeeks.org/python-string-split/
#       Technique inspired by source: How to split a file with the split() command. Specifically:
#
#           words = ["hi", "hello"]
#           words.split(', ', 4))
#
# --------------------------------------------------------------------------------------------
#   https://www.geeksforgeeks.org/response-json-python-requests/
#       Technique inspired by source: How to submit HTTP requests and parse the JSON object responses
#       Specifically:
#
#           import requests
#           response = requests.get('https://api.github.com')
#           API_Data = response.json()      
#
##############################################################################################

import requests
import time

def get_conversion_rates(base_currency):
    # form the API URL with the given base currency
    API_KEY = "30788d6db2e649e6ab773d68"
    API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

    # send a get request to the api
    response = requests.get(API_URL)

    # if the api request was successful, parse the json response to get list of conversion conversion_rates
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']
    else:
        # printing the error if the request was unsuccessful
        print("Error:", response.status_code, response.text)
        return None

def convert(currency1, currency2):
    # retrieve the conversion rates for the first currency
    conversion_rates = get_conversion_rates(currency1)

    # if conversion_rates were successfully retrieved, print the conversion rate to the second currency
    if conversion_rates:
        desired_rate = conversion_rates.get(currency2, "Not available")
        # print(f"{currency1} to {currency2}:", desired_rate)
        return desired_rate
    else:
        # message if rate retrieval failed
        print("Failed to retrieve rate")
 

# Keep service active indefinitely; read communication pipe file until it is written to,
# read the currencies then obtain the conversion rate between the two
communication_pipe = "conversion-svc.txt"   # TODO: replace this with the communication pipeline file
while True:
    time.sleep(1)
    with open(communication_pipe, "r", encoding="utf-8") as conversionsvc:
        currencies = conversionsvc.read()

    # once currencies is nonempty, write image path to communication pipe
    try:
        cur1, cur2 = currencies.split(", ", 1)
        with open("conversion-svc.txt", "w", encoding="utf-8") as conversionsvc:
            conversionsvc.write(str(convert(cur1, cur2)))
    except:
        pass
