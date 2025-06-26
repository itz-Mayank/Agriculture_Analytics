# Agriculture_Analytics
India's agricultural sector is vital for the economy, but the management of agricultural data remains a challenge due to its complexity, fragmented nature, and lack of easy access. Various stakeholders such as farmers, policymakers, and researchers face difficulties in accessing, analyzing, and making informed decisions based on agricultural data.

# 🚜 AgriData Explorer: Analyzing Indian Agriculture with Power BI

Welcome to the **AgriData Explorer** — a comprehensive data analytics and visualization project designed to analyze the agricultural landscape of India using **Python**, **SQL**, and **Power BI**.

---

## 📌 Project Objective

The primary goal of this project is to understand and visualize agricultural trends across Indian states and districts. We analyze key metrics like **crop area**, **production**, and **yield** over time and across regions, providing insightful trends and actionable recommendations.

---

## 🧾 Dataset Description

The dataset includes historical agricultural statistics of various crops across Indian states and districts for multiple years.

### Key Fields Include:
- `Year`, `State_Name`, `Dist_Name`
- Crop-specific columns like:
  - `RICE_AREA`, `RICE_PRODUCTION`, `RICE_YIELD`
  - `WHEAT_AREA`, `MAIZE_YIELD`, `COTTON_PRODUCTION`, etc.

### Data Source:
Data was preprocessed using **Python (Pandas)** and stored in a **MySQL** database. It was then connected to **Power BI** for visualization.

---

## 🔄 Project Workflow

### 1. Data Preprocessing (Python)
- Loaded the dataset using `pandas`
- Cleaned and renamed columns for consistency
- Uploaded the cleaned dataset into MySQL using `SQLAlchemy`

### 2. SQL Queries
Used SQL for data retrieval and analysis such as:
- Aggregating total production/yield
- Ranking states/districts
- Performing 5-year comparisons

### 3. Power BI Visualizations
- Connected to MySQL as a data source
- Created DAX measures for dynamic analysis
- Designed visualizations to explore year-wise and state-wise trends

---

## 📊 Visualizations and Insights

### Included Charts:
- **Line Charts** – Year-wise yield/production trends
- **Bar Charts** – Top crops/states/districts
- **Donut Charts** – Share of production
- **KPI Cards** – Dynamic indicators using slicers
- **Heatmaps and Tables** – Detailed breakdowns

### Interactive Features:
- Slicers for Crop, Year, State, and District
- Dynamic DAX measures based on selected crop

---

## 💡 Key Insights

- **Rice production** is highly concentrated in Eastern and Southern states.
- **Punjab and Rajasthan** show highest wheat yields.
- **Maize** shows a strong correlation between area and yield.
- Certain districts show stagnant productivity and are candidates for policy intervention.

---

## 📈 DAX Measures

### Sample: Crop Yield (Dynamic)
```DAX
CROP_YIELD = 
SWITCH(
    SELECTEDVALUE(CropTable[Crop]),
    "RICE", DIVIDE(SUM(agri_data[RICE_PRODUCTION]), SUM(agri_data[RICE_AREA])),
    "WHEAT", DIVIDE(SUM(agri_data[WHEAT_PRODUCTION]), SUM(agri_data[WHEAT_AREA])),
    "MAIZE", DIVIDE(SUM(agri_data[MAIZE_PRODUCTION]), SUM(agri_data[MAIZE_AREA])),
    ...
)
```

---

## 🧪 Evaluation Metrics

| Metric | Description |
|--------|-------------|
| 📊 Accuracy | Visuals clearly represent underlying data |
| ⚡ Performance | Fast loading and filtering |
| 🎯 Engagement | Slicers and interactivity |
| ✅ Completeness | All important metrics are included |
| 😊 User Feedback | Easy to interpret and explore |

---

## 🛠️ Tech Stack

- **Python** (Pandas, SQLAlchemy)
- **MySQL** (Data storage & SQL analysis)
- **Power BI** (Dashboards, DAX measures)
- **DAX** (Calculated metrics and dynamic filters)

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `agriculture.pbit` | Power BI template with all visuals |
| `README.md` | GitHub documentation |
| `AgriData_Explorer_Documentation.docx` | Detailed report |
| `sql_queries.sql` *(optional)* | SQL used for visualizations |
| `data_cleaning.py` *(optional)* | Python preprocessing script |

---

## 🚀 How to Use This Project

1. Clone or download the repository
2. Open `agriculture.pbit` in **Power BI Desktop**
3. Update MySQL server credentials when prompted
4. Refresh and explore the interactive dashboard

---

## 🙌 Author & Acknowledgement

Created by: **Mayank Meghwal**  
For academic and analytical purposes. Open to improvements and community contributions.

---

## 🖼️ Screenshots

*(Add exported visuals here for better GitHub preview)*

---

## 📝 License

This project is open for learning and analysis. Not for commercial use without permission.

