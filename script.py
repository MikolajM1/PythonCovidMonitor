from covid import Covid
import time

covid = Covid()  # Create instance of class Covid

country = input("Please enter your country ")  # Create variable holding user's country


def printCases():
    print("                                                                ")
    print("Active cases worldwide:  " + str(covid.get_total_active_cases()))
    print("Deaths worldwide:  " + str(covid.get_total_deaths()))
    print("Confirmed cases worldwide:  " + str(covid.get_total_confirmed_cases()))
    print("Recovered worldwide:  " + str(covid.get_total_recovered()))
    yourCountry = covid.get_status_by_country_name(country)
    print("-----------------------------------------------------------")
    print("Active cases in " + country + ":  " + str(yourCountry.get('active')))
    print("Deaths in " + country + ":  " + str(yourCountry.get('deaths')))
    print("Confirmed cases in " + country + ":  " + str(yourCountry.get('confirmed')))
    print("Recovered in " + country + ":  " + str(yourCountry.get('recovered')))
    print("-----------------------------------------------------------")


while True:
    printCases()
    time.sleep(60)  # Wait for 60 senconds before printing the info again
