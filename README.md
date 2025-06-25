
# 📊 iFood Campaign Marketing Analytics Dashboard

This project is an **interactive Streamlit dashboard** built to analyze and visualize the effectiveness of various iFood marketing campaigns. The dashboard provides insightful exploratory data analysis, campaign A/B testing, PCA-based dimensionality reduction, and consumer behavior metrics, allowing data-driven marketing decisions.

---

## 🚀 Features

- 🧮 **Summary Statistics** for demographic and transaction data
- 📊 **Interactive Visualizations** using Plotly and Seaborn
- 🧪 **A/B Testing** on individual marketing campaigns
- 📉 **PCA Analysis** for dimensionality reduction
- 💡 **Business Insights** including top campaigns and spending patterns
- 📥 **Downloadable Word Report** for offline insights
- 👤 **About the Developer** section for portfolio and contact

---

## 📁 Project Structure

```
📦 iFoodCampaignDashboard/
│
├── app.py                                  # Main Streamlit application
├── ifood_df.csv                            # Marketing dataset
├── iFood_Campaign_Insights_Report.docx     # Word report (if generated)
├── My image7.jpg                           # Developer photo
├── README.md                               # Project documentation
└── requirements.txt                        # Dependencies
```

---

## 📊 Dataset Description

The dataset `ifood_df.csv` contains anonymized customer information related to iFood's marketing campaigns. Key columns include:

| Column                        | Description                                      |
|------------------------------ |--------------------------------------------------|
| `Income`                      | Customer yearly income                           |
| `Kidhome`, `Teenhome`         | Number of children/teens in household            |
| `MntWines` - `MntGoldProds`   | Spending across product categories               |
| `NumDealsPurchases`           | Purchases made using discounts                   |
| `AcceptedCmp1-5`              | Whether customer accepted each campaign          |
| `Response`                    | Overall response to campaigns                    |
| `Complain`                    | Complaint flag (1 = Yes, 0 = No)                 |
| `Age`, `Customer_Days`        | Demographics-related derived columns             |
| `education_*`, `marital_*`    | One-hot encoded education/marital status         |

---

## 📊 Dashboard Sections

### 🔍 Exploratory Data Analysis
- Summary statistics
- Histogram of responses
- Heatmap of feature correlations

### 📊 A/B Testing
- Uses `ttest_ind` to compare campaign performance
- Evaluates statistical significance of responses

### 📉 PCA Analysis
- Standardizes numeric features
- Reduces to 5 principal components
- Visualizes explained variance

### 💡 Business Insights
- Overall campaign response rate
- Complaint rate
- Best performing campaign by acceptance rate
- Average customer spending by category

### 📄 Downloadable Report
- Button to download a `.docx` report (if available)

---

## 🧰 Technologies Used

- **Python 3.9+**
- **Streamlit** — App development
- **Pandas, NumPy** — Data manipulation
- **Seaborn, Matplotlib, Plotly** — Visualization
- **SciPy** — Statistical testing
- **Scikit-learn** — PCA analysis

---

## 🛠️ Setup Instructions

### ✅ Prerequisites
- Python 3.8 or higher
- pip package manager

### 🧪 Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the App

```bash
streamlit run app.py
```

Then navigate to `http://localhost:8501` in your browser.

---

## 📥 Sample Report Output

If `iFood_Campaign_Insights_Report.docx` is present in the directory, a download button will appear on the dashboard for users to export key insights.

---

## 👨‍💻 About the Developer

**Kajola Gbenga**

📇 Certified Data Analyst | Certified Data Scientist | Certified SQL Programmer | Mobile App Developer | AI/ML Engineer  

🔗 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
📜 [Certifications & Licences](https://www.datacamp.com/portfolio/kgbenga234)  
💻 [GitHub](https://github.com/prodigy234)  
🌐 [Portfolio](https://kajolagbenga.netlify.app/)  
📧 k.gbenga234@gmail.com  

✅ Created using Python and Streamlit

---

## 📄 License

This project is licensed under the MIT License.
