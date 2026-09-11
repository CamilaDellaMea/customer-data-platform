import csv
import random
from datetime import datetime, timedelta

products = ["Notebook", "Monitor", "Mouse", "Teclado", "Headset"]

with open("data/sales/sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "sale_id",
        "customer_id",
        "product",
        "quantity",
        "unit_price",
        "sale_date"
    ])

    for sale_id in range(1, 1001):
        writer.writerow([
            sale_id,
            random.randint(1, 100),
            random.choice(products),
            random.randint(1, 5),
            round(random.uniform(50, 5000), 2),
            datetime.now() - timedelta(days=random.randint(0, 730))
        ])

print("1.000 vendas geradas!")