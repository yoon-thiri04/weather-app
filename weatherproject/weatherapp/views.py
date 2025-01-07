from django.shortcuts import render,HttpResponse
import requests
import datetime
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'paris'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ac13a3164644b30602d088dd74b48e66"
    PARAMS={'units':'metric'}
    try:
        data = requests.get(url, PARAMS).json()

        description = data.get('weather', [{}])[0].get('description', 'No description available')
        icon = data['weather'][0]['icon']
        temp = data.get('main', {}).get('temp', 'No temperature data available')

        day = datetime.date.today()
        return render(request, 'index.html',
                      {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city,'exception_occured':False})
    except:
        exception_occured = True
        print("entered error")
        return render(request,'index.html',{'description':'cleear sky','icon':'01d','temp':25,'day':day,'city':'Paris','exception_occured':True})


