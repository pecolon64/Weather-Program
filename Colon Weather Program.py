# Python program to find current  
# weather details of any city 
# using openweathermap api 


# import required modules
import requests
import json

# function to request for data
try:
    def weather_data(query):
        
    # Enter your API key here
        api_key = "f8b69cac30827ee920f73c9a5b0d60bc"
    # base_url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&" + query
        res=requests.get(complete_url);
        return res.json();
        print("Connection was successful!")
except:
    print("Something ewent wrong when trying to connect.")

try:
    def getweatherInfo(zipcode):
        
    # Enter your API key here
        api_key = "f8b69cac30827ee920f73c9a5b0d60bc"
    # base_url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&" + zipcode
        res=requests.get(complete_url);
        return res.json();
        print("Connection was successful!")
except:
    print("Something went wrong when trying to connect.")


# function to display results
def display_results(weather,city):
    print("{}'s temperature: {} (default in Kelvin) ".format(city,weather['main']['temp']))
    print("Wind speed: {} m/s".format(weather['wind']['speed']))
    print("Description: {}".format(weather['weather'][0]['description']))
    print("Weather: {}".format(weather['weather'][0]['main']))
    
# main function
def main():
    
    city=input('Enter the city or zipcode. Type N to stop: ')
    
    print("Connection was successful!")
    
    try:
        query='q='+city;
        w_data=weather_data(query);
        display_results(w_data, city)        
    except:
        zipcode=input("Enter zip code to get weather info or N to exit: ") 
        if zipcode=='N':
            sys.exit()
        else:
            getweatherInfo(zipcode)
            print('City name not found')

    city=input('Enter the city or zipcode. Type N to stop: ') 

if __name__=='__main__':
    main()
