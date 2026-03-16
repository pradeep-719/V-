# 👁️ Vision & Eye Health Surveillance Analysis 
*End-to-End Data Analytics Project | Excel → Python → MySQL → Power BI**

---

## 🎯 Project Overview
I developed a complete data solution to analyze **Vision and Eye Health** trends. The goal was to build a robust pipeline that ensures data integrity and professional-grade processing, transforming raw public health data (from Kaggle) into actionable insights.

---

⚙️ The Technical Workflow
To ensure a professional-grade process, I followed a 4-stage data lifecycle:

1. Data Ingestion: Sourced raw surveillance data from Kaggle and performed initial cleaning in **Excel**.
2. Data Processing: Leveraged Python (Pandas)for complex transformations and data normalization.
3. Database Management: Migrated data into MySQL to perform high-speed aggregations.
4. Business Intelligence:Connected MySQL to Power BI for interactive dashboards.

---

## 💾 MySQL Problem Solving (Queries & Logic)

1. Identifying High-Risk Age Groups**
Query:sql
SELECT Age, SUM(Data_Value) AS Total_Value 
FROM vision_data 
GROUP BY Age 
ORDER BY Total_Value DESC;

2. Risk Factor Impact Analysis
Query: ```sql
SELECT RiskFactor, SUM(Data_Value) AS Total
FROM vision_data
GROUP BY RiskFactor;
Insight:Smoking and Diabetes are leading contributors.

3. Gender-Based Trends**
Result:Females ($205,690$) showed a higher report rate than Males ($190,600$).

4. Top Functional Challenges**
Insight:"Reading Difficulty" and "Seeing well up close" are the top functional issues.



## 🛠️ Tech Stack
Languages:** Python (Pandas), MySQL
Tools:Microsoft Excel, Power BI, MySQL Workbench
Version Control:Git & GitHub

---

 📽️ Project Demo
🔗 [LinkedIn Project Video & Post](https://lnkd.in/d_vEGUv5)
