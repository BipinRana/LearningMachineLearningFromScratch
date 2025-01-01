import requests
#get the API_key from the openweathermap.org before running the code
API_key = 'abcd'

city = input('Enter the city: ')

#api url
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'

# Make the request
res = requests.get(url)

# Check if the request was successful
if res.status_code == 200:
    data = res.json()
    weather = data['weather'][0]['main']
    
    #print data after obtaining
    print(f"Weather:{weather}")
    for key in data['main']:
        print(f'{key} : {data["main"][key]}')
else:
    print(f"Error: {res.status_code} - {res.text}")  # Print the error if the request failed
