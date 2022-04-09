import requests
import os
from dotenv import load_dotenv

load_dotenv('config.env')

apiKey = os.getenv('API_KEY')

def getActive():    
    response = requests.get('https://api.weather.gov/alerts/active/count')
    response = response.json()
    return response

def getForecast():
    response = requests.get(f'https://api.weather.com/v1/location/84604:4:US/forecast/nowcast.json?language=en-US&units=e&apiKey={apiKey}')
    response = response.json()
    forecast = response['forecast']
    return forecast

def getRain():
    response = requests.get(f'https://api.weather.com/v1/location/84604:4:US/forecast/precipitation.json?language=en-US&units=e&apiKey={apiKey}')
    response = response.json()
    characteristic = ''
    intensity = ''
    event = "raining"
    if response['forecasts'][0]['characteristic'] == 0:
        characteristic = "not currently"
    elif response['forecasts'][0]['characteristic'] == 1:
        characteristic = "intermittently"
    elif response['forecasts'][0]['characteristic'] == 2:
        characteristic = "currently"
        
    if response['forecasts'][0]['intensity'] == 1:
        intensity = " lightly"
    elif response['forecasts'][0]['intensity'] == 2:
        intensity = " moderately"
    elif response['forecasts'][0]['intensity'] == 3:
        intensity = " heavily"
    
    elif response['forecasts'][0]['event_type'] == 2:
        event = "snowing"
    elif response['forecasts'][0]['event_type'] == 3:
        event = "raining and snowing"
    elif response['forecasts'][0]['event_type'] == 4:
        event = "thunderstorming"
    
    print(f"It is {characteristic}{intensity} {event}")
    

if __name__ == "__main__":
    print('Here is your daily news update!')
    print('-------------------------------')
    forecast = getForecast()
    print(forecast['narrative_512char'])
    activeAlerts = getActive()
    print (f"There are currently {activeAlerts['total']} Active Weather Alerts in the U.S. Today.")
    getRain()
    print('Done!')
