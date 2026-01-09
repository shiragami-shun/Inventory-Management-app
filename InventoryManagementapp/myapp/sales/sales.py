from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime
import csv

# 売上データ
@dataclass
class Sale:
    date: str          
    product_id: str
    product_name: str
    price: int
    quantity: int

    @property
    def total(self) -> int:
        return self.price * self.quantity


# 売上管理
class SalesManager:
    def __init__(self):
        self.sales: List[Sale] = []

    def add_sale(self, sale: Sale):
        self.sales.append(sale)
    
    # マイナス売上防止のためのバリデーション追加
    def add_sale(self, sale: Sale):
        if sale.price < 0 or sale.quantity <= 0:
            raise ValueError("価格・数量が不正です")
        self.sales.append(sale)
    
    # CSV読み込み
    def load_from_csv(self, path: str):
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_sale(Sale(
                    row["date"],
                    row["product_id"],
                    row["product_name"],
                    int(row["price"]),
                    int(row["quantity"])
                ))



    # 総売上
    def total_sales(self) -> int:
        return sum(s.total for s in self.sales)
    

    # 日別売上集計
    def daily_sales(self) -> Dict[str, int]:
        result = {}
        for s in self.sales:
            result.setdefault(s.date, 0)
            result[s.date] += s.total
        return result

    # 商品別売上集計
    def product_sales(self) -> Dict[str, int]:
        result = {}
        for s in self.sales:
            result.setdefault(s.product_name, 0)
            result[s.product_name] += s.total
        return result

    # 月別売上集計
    def monthly_sales(self) -> Dict[str, int]:
        result = {}
        for s in self.sales:
            month = s.date[:7]  
            result.setdefault(month, 0)
            result[month] += s.total
        return result
    # 特定商品の売上取得
    def sales_by_product(self, product_name: str) -> int:
        return sum(s.total for s in self.sales if s.product_name == product_name)   
    