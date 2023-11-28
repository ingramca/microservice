# Currency converter microservice

The program written herein is intended to be used as a microservice to convert between currencies. It uses the free version of the API at https://www.exchangerate-api.com/. The API_KEY variable contains my personal API key for this service.

# To REQUEST data from the microservice
1. Ensure all necessary libraries have been installed. This includes "requests", "time".
2. Run micro_converter.py
3. Write 2 currency symbols to conversion-svc.txt, separated by a comma and a space (e.g. "USD, GBP")

Example call: write/save "USD, GBP" to conversion-svc.txt

# To RECEIVE data from the microservice.
1. After requesting data as outlined above, the microservice will replace the currency symbols in conversion-svc.txt with a string containing the conversion factor.


# UML Diagram
<img width="834" alt="Screenshot 2023-11-28 at 1 24 54 PM" src="https://github.com/ingramca/microservice/assets/67073894/55a17e41-ff99-4bd1-8804-521f701116a8">
