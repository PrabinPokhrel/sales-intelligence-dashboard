# 📊 Sales & Customer Performance Dashboard

## 🔎 Overview

This project presents an **end-to-end Business Intelligence solution** built using **SQL Server, Python, and Power BI** to analyze **sales performance, customer behavior, and churn trends** from an e-commerce dataset.

The objective is to transform raw transactional data into **actionable business insights** through data cleaning, modeling, KPI design, and interactive dashboards.

---

## 🛠 Tech Stack

* **SQL Server (SSMS)** – Data cleaning and star-schema modeling
* **Python (Pandas, NumPy)** – Data preprocessing and transformation
* **Power BI** – Data modeling, DAX measures, and dashboard visualization
* **Kaggle Olist Dataset** – Source e-commerce data

---

## 🧱 Data Model

A **star schema** was implemented:

* **fact_orders** – transactional sales data
* **dim_customers** – customer attributes
* **Date table** – time intelligence for trend analysis

This structure enables **efficient KPI calculation and scalable BI reporting**.

---

## 📈 Key KPIs

The dashboard measures core business performance:

* Revenue
* Orders
* Average Order Value (AOV)
* Monthly Growth %
* Active Customers
* Customer Lifetime Value (CLV)
* 90-Day Churn Rate

All KPIs are created using **DAX in Power BI**.

---

## 📊 Dashboard Pages

### 1️⃣ Executive Overview

* Revenue trend over time
* Geographic revenue distribution
* Core KPIs for management monitoring

**Insight:**
Revenue fluctuates across months with strong concentration in a few key regions, indicating opportunities for **market expansion and diversification**.

---

### 2️⃣ Customer Intelligence

* Top customers ranked by CLV
* Customer segmentation (High / Mid / Low)
* Active customer trend over time

**Insight:**
A small proportion of **high-value customers generates a large share of revenue**, highlighting the importance of **retention strategies and loyalty programs**.

---

### 3️⃣ Churn Analysis

* Churn rate and churned customers
* State-level churn comparison
* Monthly churn trend

**Insight:**
Churn peaks during specific periods, suggesting potential **customer retention or service quality issues** that require targeted intervention.

---

## 💡 Business Recommendations

Based on the analysis:

* Prioritize **retention campaigns** in high-churn regions
* Implement **loyalty programs** for high-CLV customers
* Monitor **monthly churn spikes** as early warning signals
* Reduce dependency on a small set of high-value customers

---

## 📸 Dashboard Screenshots

### Executive Overview
![Executive Overview](Screenshot/Page%201/Screenshot%202026-02-18%20210907.png)

### Customer Intelligence
![Customer Intelligence](Screenshot/Page%202/Screenshot%202026-02-18%20210918.png)

### Churn Analysis
![Churn Analysis](Screenshot/Page%203/Screenshot%202026-02-18%20205533.png)




## ▶️ How to Run the Project

1. Download the **Olist dataset** from Kaggle.
2. Place raw CSV files inside `Data/Raw Data/`.
3. Run the cleaning script:

   ```
   python Python/Clean_olist.py
   ```
4. Import processed data into **SQL Server**.
5. Open **PowerBI/Viz.pbix** and refresh the data.

---

## 👨‍💻 Author

**Prabin Pokhrel**
Aspiring **Data Analyst / BI Analyst**
Based in **Sweden Stockholm**

---

⭐ *If you find this project useful, consider giving it a star on GitHub.*

