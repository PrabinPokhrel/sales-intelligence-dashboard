import os
import pandas as pd

RAW_DIR = r"C:\Users\WELCOME\Desktop\sales-intelligence-dashboard\Data\Raw Data"
OUT_DIR = r"C:\Users\WELCOME\Desktop\sales-intelligence-dashboard\Data\Processed Data"

os.makedirs(OUT_DIR, exist_ok=True)

def load_csv(name: str) -> pd.DataFrame:
    path = os.path.join(RAW_DIR, name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)

# ---- Load required files ----
orders = load_csv("olist_orders_dataset.csv")
items  = load_csv("olist_order_items_dataset.csv")
customers = load_csv("olist_customers_dataset.csv")

# ---- Clean: standardize columns ----
for df in [orders, items, customers]:
    df.columns = [c.strip().lower() for c in df.columns]

# ---- Orders cleaning ----
# Parse datetimes safely (some columns may be missing in some versions, so check)
dt_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
for c in dt_cols:
    if c in orders.columns:
        orders[c] = pd.to_datetime(orders[c], errors="coerce")

# Remove duplicates
orders = orders.drop_duplicates(subset=["order_id"])
items  = items.drop_duplicates()

# ---- Items cleaning ----
# Ensure numeric
for c in ["price", "freight_value"]:
    if c in items.columns:
        items[c] = pd.to_numeric(items[c], errors="coerce").fillna(0)

# ---- Build order-level revenue from items ----
item_agg = (items.groupby("order_id", as_index=False)
            .agg(item_revenue=("price", "sum"),
                 freight_revenue=("freight_value", "sum")))

item_agg["total_revenue"] = item_agg["item_revenue"] + item_agg["freight_revenue"]

# ---- Merge orders + item revenue ----
fact_orders = orders.merge(item_agg, on="order_id", how="left")
fact_orders[["item_revenue","freight_revenue","total_revenue"]] = (
    fact_orders[["item_revenue","freight_revenue","total_revenue"]].fillna(0)
)

# Keep minimum columns for BI
keep_cols = [
    "order_id", "customer_id", "order_status", "order_purchase_timestamp",
    "item_revenue", "freight_revenue", "total_revenue"
]
keep_cols = [c for c in keep_cols if c in fact_orders.columns]
fact_orders = fact_orders[keep_cols]

# ---- Customers dimension ----
dim_customers = customers[[
    c for c in [
        "customer_id", "customer_unique_id",
        "customer_zip_code_prefix", "customer_city", "customer_state"
    ] if c in customers.columns
]].drop_duplicates(subset=["customer_id"])

# ---- Save cleaned outputs ----
fact_orders_path = os.path.join(OUT_DIR, "fact_orders.csv")
dim_customers_path = os.path.join(OUT_DIR, "dim_customers.csv")

fact_orders.to_csv(fact_orders_path, index=False)
dim_customers.to_csv(dim_customers_path, index=False)

print("✅ Saved:", fact_orders_path)
print("✅ Saved:", dim_customers_path)
print("Rows fact_orders:", len(fact_orders))
print("Rows dim_customers:", len(dim_customers))
