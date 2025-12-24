from django.shortcuts import render
from .sales import SalesManager, Sale

def dashboard(request):
    manager = SalesManager()

    manager.add_sale(Sale("2025-12-01", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-01", "P002", "サンドイッチ", 600, 1))
    manager.add_sale(Sale("2025-12-02", "P001", "コーヒー", 400, 1))

    context = {
        "total_sales": manager.total_sales(),
        "daily_sales": manager.daily_sales(),
        "product_sales": manager.product_sales(),
        "monthly_sales": manager.monthly_sales(),
    }
    return render(request, "sales/dashboard.html", context)
