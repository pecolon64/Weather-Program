# import required modules
#import requests
import json

# function to request for data
def weather_data(query):
    # Enter your API key here
    api_key = "f8b69cac30827ee920f73c9a5b0d60bc"
    # base_url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&" + query
    res=requests.get(complete_url);
    return res.json();

def getweatherInfo(zipcode):
    # Enter your API key here
    api_key = "f8b69cac30827ee920f73c9a5b0d60bc"
    # base_url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&" + query
    res=requests.get(complete_url);
    return res.json();

# function to display results
def display_results(weathers,city):
    print("{}'s temperature: {}°C ".format(city,weathers['main']['temp']))
    print("Wind speed: {} m/s".format(weathers['wind']['speed']))
    print("Description: {}".format(weathers['weather'][0]['description']))
    print("Weather: {}".format(weathers['weather'][0]['main']))
    
# main function
def main():
   
    city=input('Enter the city:')
    print()
   
    try:
        query='q='+city;
        w_data=weather_data(query);
        display_results(w_data, city)
        print()
    except:
        zipcode=input("Enter zip code to get weather info or N to exit: ") 
        if zipcode=='N':
            sys.exit()
        else:
            getweatherInfo(zipcode)
    print('City name not found')

if __name__=='__main__':
    main()