from django.shortcuts import render
from .sales import SalesManager, Sale

def dashboard(request):
    manager = SalesManager()

    manager.add_sale(Sale("2025-12-01", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-01", "P002", "サンドイッチ", 600, 2))
    manager.add_sale(Sale("2025-12-02", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-02", "P003", "ケーキ", 1500, 1))

    context = {
        "total_sales": manager.total_sales(),
        "daily_sales": manager.daily_sales(),
        "product_sales": manager.product_sales(),
        "monthly_sales": manager.monthly_sales(),
    }
    return render(request, "sales/dashboard.html", context)
# from django.shortcuts import render, redirect
# from .forms import SaleForm
# from . import services

# def dashboard(request):
#     if request.method == "POST":
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard")
#     else:
#         form = SaleForm()

#     context = {
#         "form": form,
#         "total_sales": services.total_sales(),
#         "daily_sales": services.daily_sales(),
#         "product_sales": services.product_sales(),
#         "monthly_sales": services.monthly_sales(),
#     }
#     return render(request, "sales/dashboard.html", context)
