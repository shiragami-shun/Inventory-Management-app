from models import Sale
from collections import defaultdict

def total_sales():
    return sum(s.total for s in Sale.objects.all())

def daily_sales():
    result = defaultdict(int)
    for s in Sale.objects.all():
        result[str(s.date)] += s.total
    return dict(result)

def product_sales():
    result = defaultdict(int)
    for s in Sale.objects.all():
        result[s.product_name] += s.total
    return dict(result)

def monthly_sales():
    result = defaultdict(int)
    for s in Sale.objects.all():
        month = s.date.strftime("%Y-%m")
        result[month] += s.total
    return dict(result)
