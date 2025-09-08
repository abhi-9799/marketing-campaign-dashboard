# Marketing Campaign Performance Dashboard

This project analyzes Google Analytics sample e-commerce data to understand how different marketing campaigns perform.  
I built an end-to-end pipeline that connects **BigQuery (SQL)** → **Python (data cleaning + automation)** → **Power BI (interactive dashboard)**.  

---

## Why I built this
I wanted to simulate the kind of work a data analyst does in real life:  
- Writing SQL queries to extract data from a large source (BigQuery)  
- Cleaning and enriching the data with Python  
- Calculating business KPIs (CTR, CPC, Conversion Rate, ROI)  
- Presenting the results in a way that stakeholders can act on  

---

## Tech Stack
- **Python**: Pandas, NumPy, BigQuery client  
- **SQL**: BigQuery (Google Cloud public dataset)  
- **Visualization**: Power BI (main), Tableau (optional)  
- **Tools**: GitHub, Jupyter, Codespaces  

---

## Workflow
1. **Data Extraction**  
   - Queried the Google Analytics public dataset in BigQuery  
   - Pulled sessions, clicks, transactions, and revenue by campaign  

2. **Data Transformation (Python)**  
   - Cleaned missing values  
   - Derived KPIs like CTR, Conversion Rate  
   - Since ad spend wasn’t in the dataset, I simulated realistic campaign costs to calculate CPC and ROI  

3. **Storage & Export**  
   - Saved outputs as CSV (`campaign_performance.csv` and `roi_trend.csv`)  
   - These feed into the dashboard  
