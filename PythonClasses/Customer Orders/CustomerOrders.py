orders = [
  (1001, "Alice", "Phone Case", "Elictronics", 2, 15.99),
  (1002, "Bob", "Jeans", "Clothing", 1, 49.99),
  (1003, "Alice", "USB-C Cable", "Electronics", 3, 9),
  (1004, "Diana", "Blender", "Home", 1, 89.50),
  (1005, "Charlie", "T-Shirt", "Clothing", 2, 19.00),
]

customer_spend = {}
product_count = {}
category_revenue = {}
costomer_product = {}

unique_customers = set()
unique_products = set()
unique_categories = set()


for (order_id, customer, product, category, qty, price) in orders:

    unique_customers.add(customer)
    unique_products.add(product)
    unique_categories.add(category)

    line_total = qty * price
    customer_spend[customer] = customer_spend.get(customer, 0.0) + line_total


