from django.shortcuts import render
from core.forms import RestaurantForm
from core.models import Rating, Restaurant, StaffRestaurant

# Create your views here.
def index(request):
    jobs = StaffRestaurant.objects.all()
    for job in jobs:
        print(job.staff.name, job.restaurant.name, job.salary)
    return render(request, 'index.html')