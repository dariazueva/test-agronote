from django.shortcuts import redirect, render

from .forms import CityForm
from .models import City


def get_weather_for_city(city_name):
    return {"city": city_name, "temperature": 20, "description": "Sunny", "icon": "01d"}


def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CityForm()

    cities = City.objects.all()
    weather_data = [get_weather_for_city(city.name) for city in cities]

    context = {"form": form, "weather_data": weather_data}
    return render(request, "weather/index.html", context)
