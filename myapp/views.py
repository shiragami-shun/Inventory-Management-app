from django.shortcuts import render
from .salas import SalesManager, Sale
from datetime import date
from django.utils import timezone



def dashboard(request):
    manager = SalesManager()

    manager.add_sale(Sale("2025-12-01", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-01", "P002", "サンドイッチ", 600, 2))
    manager.add_sale(Sale("2025-12-02", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-02", "P003", "ケーキ", 1500, 10))
    manager.add_sale(Sale("2025-01-15", "P002", "サンドイッチ", 600, 20))
    manager.add_sale(Sale("2026-01-15", "P004", "紅茶", 400, 10))

    context = {
        "total_sales": manager.total_sales(),
        "daily_sales": manager.daily_sales(),
        "product_sales": manager.product_sales(),
        "monthly_sales": manager.monthly_sales(),
    }
    return render(request, "sales/dashboard.html", context)


def index(request):
    manager = SalesManager()

    manager.add_sale(Sale("2025-12-01", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-01", "P002", "サンドイッチ", 600, 2))
    manager.add_sale(Sale("2025-12-02", "P001", "コーヒー", 400, 2))
    manager.add_sale(Sale("2025-12-02", "P003", "ケーキ", 1500, 10))
    manager.add_sale(Sale("2025-01-14", "P002", "サンドイッチ", 600, 20))
    manager.add_sale(Sale("2026-01-15", "P004", "紅茶", 400, 10))

    today = timezone.localdate().isoformat()     # "2026-01-15"
    month = today[:7]     
     
    manager.add_sale(Sale(today, "TEST", "テスト商品", 1000, 1))

    context = {
        "today_sales": manager.sales_by_date(today),
        "month_sales": manager.sales_by_month(month),
        "stock_count": 0,
    }
    return render(request, "sales/index.html", context)




# from django.shortcuts import render
# from .salas import SalesManager, Sale

# def dashboard(request):
#     manager = SalesManager()

#     manager.add_sale(Sale("2025-12-01", "P001", "コーヒー", 400, 2))
#     manager.add_sale(Sale("2025-12-01", "P002", "サンドイッチ", 600, 2))
#     manager.add_sale(Sale("2025-12-02", "P001", "コーヒー", 400, 2))
#     manager.add_sale(Sale("2025-12-02", "P003", "ケーキ", 1500, 1))
#     manager.add_sale(Sale("2025-1-15", "P002", "サンドイッチ", 600, 20))

#     context = {
#         "total_sales": manager.total_sales(),
#         "daily_sales": manager.daily_sales(),
#         "product_sales": manager.product_sales(),
#         "monthly_sales": manager.monthly_sales(),
#     }
#     return render(request, "sales/dashboard.html", context)

#     # context = {
#     #     "today_sales": manager.sales_by_date(today),
#     #     "month_sales": manager.monthly_sales(month),
#     #     "stock_count": 0,  # 在庫管理ができたら差し替え
#     # }

# def index(request):
#     return dashboard(request)

# def index(request):
#     manager = SalesManager()
#     return render(request, "sales/index.html")
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
