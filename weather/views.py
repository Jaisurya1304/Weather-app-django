from django.shortcuts import render
import requests

def weather(request):
    data = {}

    if request.method == 'POST':
        city = request.POST.get('city', '')  # Safely retrieve city from POST data
        if city:
            try:
                source = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=767c689df962234d3387eb325f7780c9"
                response = requests.get(source)
                response.raise_for_status()  # Raises an exception for HTTP errors (e.g., 404)
                list_of_data = response.json()

                data = {
                    "country_code": str(list_of_data['sys']['country']),
                    "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                    "temp": round((list_of_data['main']['temp'] - 32) * 5.0 / 9.0, 2),
                    "humidity": str(list_of_data['main']['humidity']),
                    "feels_like": round((list_of_data['main']['feels_like'] - 32) * 5.0 / 9.0, 2),
                    "description": list_of_data['weather'][0]['description'].capitalize(),
                    "icon": list_of_data['weather'][0]['icon'],
                    "city": list_of_data['name']
                }

            except requests.exceptions.RequestException as e:
                print(f"Error fetching weather data for city '{city}': {e}")

    elif request.method == 'GET' and 'lat' in request.GET and 'lon' in request.GET:
        latitude = request.GET['lat']
        longitude = request.GET['lon']

        try:
            source = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid=767c689df962234d3387eb325f7780c9"
            response = requests.get(source)
            response.raise_for_status()  # Raises an exception for HTTP errors (e.g., 404)
            list_of_data = response.json()

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": round((list_of_data['main']['temp'] - 32) * 5.0 / 9.0, 2),
                "humidity": str(list_of_data['main']['humidity']),
                "feels_like": round((list_of_data['main']['feels_like'] - 32) * 5.0 / 9.0, 2),
                "description": list_of_data['weather'][0]['description'].capitalize(),
                "icon": list_of_data['weather'][0]['icon'],
                "city": list_of_data['name']
            }

        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")

    return render(request, 'index.html', {'data': data})
