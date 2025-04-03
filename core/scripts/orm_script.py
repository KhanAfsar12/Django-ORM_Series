import random
from core.models import Rating, Restaurant, Sale, Staff, StaffRestaurant
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Count, Avg, Min, Max, Sum, CharField, Value, Q
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
def run():
   
   
    name_has_num = Q(restaurant__name__regex = r"[0-9]+")
    print(Sale.objects.filter(name_has_num).values_list('restaurant__name', flat=True))


    pprint(connection.queries)