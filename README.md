# Sales & Customer Performance Dashboard

## Overview
This project presents an end-to-end Business Intelligence solution built using SQL Server, Python, and Power BI to analyze sales performance, customer behavior, and churn trends from an e-commerce dataset.

## Tech Stack
- SQL Server (SSMS) – Data cleaning & modeling  
- Python (Pandas, NumPy) – Data preprocessing  
- Power BI – Data modeling, DAX measures, dashboards  
- Kaggle Olist Dataset – Source data  

## Data Model
A star schema was implemented:
- fact_orders – transactional sales data  
- dim_customers – customer attributes  
- Date table – time intelligence  

## Key KPIs
- Revenue  
- Orders  
- Average Order Value (AOV)  
- Monthly Growth %  
- Active Customers  
- Customer Lifetime Value (CLV)  
- 90-day Churn Rate  

## Dashboard Pages

### 1. Executive Overview
- Revenue trend over time  
- Geographic revenue distribution  
- Core KPIs for management monitoring  

### 2. Customer Intelligence
- Top customers by CLV  
- Customer segmentation (High / Mid / Low)  
- Active customer trend  

### 3. Churn Analysis
- Churn rate and churned customers  
- State-level churn comparison  
- Monthly churn trend  

## Business Insights
- Revenue is concentrated among a small group of high-value customers.  
- Certain regions show higher churn risk.  
- Customer retention strategies can significantly improve lifetime value.  

## How to Run
1. Download the Olist dataset from Kaggle.  
2. Place raw CSV files in `Data/Raw Data
