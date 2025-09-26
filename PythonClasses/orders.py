
catalog = {
    "Laptop": ("Electronics", 1200.0),
    "Headphones": ("Electronics", 80.0),
    "Phone Case": ("Electronics", 15.0),
    "Jeans": ("Clothing", 45.0),
    "T-Shirt": ("Clothing", 20.0),
    "Coffee Maker": ("Home Essentials", 70.0),
    "Vacuum": ("Home Essentials", 150.0),
    "Pillow": ("Home Essentials", 25.0),
}

orders = [
    (1001, "Erol", [("Laptop", 1), ("Headphones", 1)]),
    (1002, "Desak", [("T-Shirt", 3), ("Jeans", 1), ("Phone Case", 2)]),
    (1003, "Alex", [("Vacuum", 1), ("Pillow", 4)]),
    (1004, "Erol", [("Coffee Maker", 1), ("Phone Case", 1)]),
    (1005, "Mia", [("Laptop", 1), ("T-Shirt", 2)]),
    (1006, "Sam", [("Headphones", 2), ("Pillow", 2), ("Jeans", 2)]),
    (1007, "Erol", [("T-Shirt", 1), ("Jeans", 1)]),
    (1008, "Mia", [("Vacuum", 1)]),
    (1009, "Desak", [("Coffee Maker", 1), ("Pillow", 2)]),
    (1010, "Kia", [("Headphones", 1), ("Phone Case", 3)]),
]


def line():
    print("-" * 64)

def money(x):
    return f"${x:,.2f}"


product_units = {}        # product -> total units sold
product_revenue = {}      # product -> total revenue
customer_spend = {}       # customer -> total spend
category_revenue = {}     # category -> total revenue
customers = set()         # set of customer names
products_sold = set()     # set of unique products sold

# Process orders
for (order_id, customer, items) in orders:
    customers.add(customer)
    order_total = 0.0

    for (product, qty) in items:
        if product not in catalog:
            # Skip unknown products defensively
            continue
        category, price = catalog[product]
        revenue = price * qty

        # product units & revenue
        product_units[product] = product_units.get(product, 0) + qty
        product_revenue[product] = product_revenue.get(product, 0.0) + revenue
        products_sold.add(product)

        # category revenue
        category_revenue[category] = category_revenue.get(category, 0.0) + revenue

        # customer spend (accumulate per order)
        order_total += revenue

    customer_spend[customer] = customer_spend.get(customer, 0.0) + order_total


def classify(amount):
    if amount >= 800:
        return "High-Value"
    if amount >= 300:
        return "Mid-Value"
    return "Low-Value"

customer_segment = {cust: classify(spend) for cust, spend in customer_spend.items()}

# Top products by units
top_products_units = sorted(product_units.items(), key=lambda x: x[1], reverse=True)

# Top products by revenue
top_products_revenue = sorted(product_revenue.items(), key=lambda x: x[1], reverse=True)

# Top customers by spend
top_customers = sorted(customer_spend.items(), key=lambda x: x[1], reverse=True)

# Categories by revenue
top_categories = sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)

# -----------------------------
# 6) Report
# -----------------------------
print("\nANALYZING CUSTOMER ORDERS — REPORT")
line()
print("Overview")
print(f"• Unique customers: {len(customers)}")
print(f"• Unique products sold: {len(products_sold)}")
print(f"• Total orders: {len(orders)}")
total_revenue = sum(product_revenue.values())
print(f"• Total revenue: {money(total_revenue)}")
line()

print("Top Products (by units)")
for product, units in top_products_units[:5]:
    print(f"  - {product:<16} {units:>3} units")
line()

print("Top Products (by revenue)")
for product, rev in top_products_revenue[:5]:
    print(f"  - {product:<16} {money(rev)}")
line()

print("Top Customers (by spend)")
for cust, spend in top_customers:
    print(f"  - {cust:<10} {money(spend)}  [{customer_segment[cust]}]")
line()

print("Revenue by Category")
for cat, rev in top_categories:
    print(f"  - {cat:<16} {money(rev)}")
line()

print("Customer Segments")
segments = {"High-Value": [], "Mid-Value": [], "Low-Value": []}
for cust, seg in customer_segment.items():
    segments[seg].append((cust, customer_spend[cust]))

for seg_name in ["High-Value", "Mid-Value", "Low-Value"]:
    people = segments[seg_name]
    print(f"  {seg_name} ({len(people)}):")
    for cust, spend in sorted(people, key=lambda x: x[1], reverse=True):
        print(f"    - {cust:<10} {money(spend)}")
line()

# -----------------------------
# 7) Simple insights
# -----------------------------
most_popular = top_products_units[0][0] if top_products_units else "N/A"
best_seller_rev = top_products_revenue[0][0] if top_products_revenue else "N/A"
best_category = top_categories[0][0] if top_categories else "N/A"
top_customer = top_customers[0][0] if top_customers else "N/A"

print("Key Insights")
print(f"• Most purchased product (units): {most_popular}")
print(f"• Top product by revenue:         {best_seller_rev}")
print(f"• Most profitable category:       {best_category}")
print(f"• Highest-spending customer:      {top_customer}")
line()
