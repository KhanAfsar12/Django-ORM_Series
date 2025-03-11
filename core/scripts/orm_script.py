import random
from core.models import Rating, Restaurant, Sale, Staff, StaffRestaurant
from django.db.models.functions import Upper
from django.db.models import Count, Avg, Min, Max, Sum
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
def run():
    one_month_ago = timezone.now() - timezone.timedelta(days=31)

    sales = Sale.objects.filter(datetime__gte = one_month_ago)
    print(sales.aggregate(
        min = Min('income'),
        max = Max('income'),
        avg = Avg('income'),
        sum = Sum('income')
        ))
    # print(connection.queries)