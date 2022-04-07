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

# TODO: Write code for api.weather.com/v3/wx/conditions/historical/dailysummary/30day
# DOCS: https://weather.com/swagger-docs/ui/sun/v3/SUNv3HistoricalConditionsDailySummary.json

# TODO: Write code for api.weather.com/v1/location/{postalCode}/forecast/precipitation.json
# https://weather.com/swagger-docs/ui/sun/v1/sunV1Short-RangeForecastPrecipitation.json

if __name__ == "__main__":
    print('Here is your daily news update!')
    print('-------------------------------')
    forecast = getForecast()
    print(forecast)
    print(forecast['narrative_512char'])
    activeAlerts = getActive()
    print (f"There are currently {activeAlerts['total']} Active Weather Alerts in the U.S. Today.")
    print('Done!')
