# 🛒 Online Retail Dashboard

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12.5-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.48.1-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Plotly-6.3.0-purple?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/Pandas-2.3.1-green?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</div>

<div align="center">
  <h3>💎 Executive Performance Dashboard for Retail Analytics</h3>
  <p><em>Advanced Business Intelligence & Data Science Solution</em></p>
</div>

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🚀 Quick Start](#-quick-start)
- [📊 Dashboard Features](#-dashboard-features)
- [🔧 Installation](#-installation)
- [📈 Usage Guide](#-usage-guide)
- [📁 Data Files](#-data-files)
- [🛠️ Technical Details](#️-technical-details)
- [🎨 Dashboard Tabs](#-dashboard-tabs)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🎯 Project Overview

The **Online Retail Dashboard** is a comprehensive business intelligence solution built with Python and Streamlit. It transforms raw retail transaction data into actionable insights through advanced analytics, interactive visualizations, and predictive modeling.

### 🌟 What This Project Does

- **📊 Data Processing**: Automated feature engineering and data cleaning
- **🎯 Business Intelligence**: Real-time KPIs, metrics, and performance indicators
- **📈 Advanced Analytics**: Customer segmentation, RFM analysis, and cohort analysis
- **🔮 Predictive Insights**: Revenue forecasting and churn prediction
- **🌍 Geographic Analysis**: Market penetration and country-wise performance
- **⏰ Time Series Analysis**: Seasonal patterns and trend identification

---

## ✨ Key Features

### 🔥 Core Capabilities

| Feature | Description | Benefits |
|---------|-------------|----------|
| **🎛️ Interactive Dashboard** | Real-time filtering and visualization | Quick decision making |
| **📊 7 Analytics Tabs** | Comprehensive business views | 360° business insights |
| **🤖 Automated Feature Engineering** | 46+ engineered features | Rich data analysis |
| **🎯 Customer Segmentation** | RFM analysis with 6 segments | Targeted marketing |
| **📈 Predictive Analytics** | Revenue forecasting & churn prediction | Strategic planning |
| **🌍 Geographic Intelligence** | Country-wise performance analysis | Market expansion insights |
| **⚡ Real-time Processing** | Fast data loading and caching | Excellent user experience |

### 💼 Business Value

- **💰 Revenue Optimization**: Identify high-value customers and products
- **📉 Churn Prevention**: Predict and prevent customer churn
- **🎯 Marketing Efficiency**: Segment customers for targeted campaigns
- **📊 Operational Insights**: Optimize inventory and staffing
- **🌐 Market Expansion**: Identify growth opportunities

---

## 🏗️ Project Structure

```
Online-Retail-Dashboard/
│
├── 📊 dashboard.py              # Main Streamlit dashboard
├── 🚀 run_dashboard.py          # Easy launcher script
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                 # Project documentation
├── 🔒 .gitignore               # Git ignore rules
│
├── 📁 data/                     # Data directory
│   ├── 🗂️ Online_Retail_Cleaned.csv    # Cleaned source data
│   ├── 🗂️ Online_Retail_data.csv       # Raw data
│   ├── 🔄 featured_data.csv             # Main dataset (46 features)
│   ├── 👥 customer_features.csv         # Customer analytics
│   ├── 🛍️ product_features.csv          # Product analytics
│   └── 🌍 country_features.csv          # Geographic analytics
│
├── 📁 src/                      # Source code
│   └── ⚙️ feature_engineering.py       # Feature engineering pipeline
│
└── 📁 notebooks/                # Jupyter notebooks
    ├── 🧹 Online_Retail_cleaning.ipynb  # Data cleaning
    └── 📊 Online_Retail_eda.ipynb       # Exploratory analysis
```

---

## 🚀 Quick Start

### ⚡ Option 1: One-Command Launch

```bash
# Clone and run everything automatically
git clone https://github.com/anuragchaubey1224/Online-Retail-Dashboard.git
cd Online-Retail-Dashboard
python run_dashboard.py
```

### 🎯 Option 2: Step-by-Step

```bash
# 1. Clone the repository
git clone https://github.com/anuragchaubey1224/Online-Retail-Dashboard.git
cd Online-Retail-Dashboard

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run feature engineering (if needed)
python src/feature_engineering.py

# 5. Launch dashboard
streamlit run dashboard.py
```

### 🌐 Access Dashboard

Once running, open your browser and navigate to:
- **Local URL**: http://localhost:8501
- **Network URL**: Will be displayed in terminal

---

## 📊 Dashboard Features

### 🎛️ Interactive Controls

- **📅 Date Range Filter**: Select specific time periods
- **🌍 Country Filter**: Focus on specific markets
- **👥 Customer Segment Filter**: Analyze customer groups

### 📈 Real-time Metrics

| Metric | Description | Use Case |
|--------|-------------|----------|
| 💰 **Total Revenue** | Sum of all transactions | Financial performance |
| 📊 **Total Orders** | Number of unique orders | Business volume |
| 👥 **Total Customers** | Unique customer count | Market reach |
| 💳 **Average Order Value** | Revenue per order | Transaction insights |

---

## 🔧 Installation

### 📋 Prerequisites

- **Python 3.8+** (Recommended: 3.12.5)
- **pip** package manager
- **Git** for cloning

### 🏃‍♂️ Quick Installation

```bash
# Install from requirements.txt
pip install -r requirements.txt
```

### 📦 Manual Installation

```bash
# Core packages
pip install streamlit==1.48.1 pandas==2.3.1 numpy==2.3.2
pip install plotly==6.3.0 seaborn==0.13.2 matplotlib==3.10.5
pip install scikit-learn==1.7.1

# Optional: For enhanced performance
pip install watchdog
```

---

## 📈 Usage Guide

### 🎯 Running the Dashboard

#### Method 1: Using the Launcher (Recommended)
```bash
python run_dashboard.py
```

#### Method 2: Direct Streamlit
```bash
streamlit run dashboard.py
```

#### Method 3: Custom Port
```bash
streamlit run dashboard.py --server.port 8502
```

### 🔄 Feature Engineering

To regenerate features or process new data:

```bash
python src/feature_engineering.py
```

This will create/update:
- `data/featured_data.csv` (main dataset)
- `data/customer_features.csv` (customer analytics)
- `data/product_features.csv` (product analytics)
- `data/country_features.csv` (geographic analytics)

### 📊 Exploring the Data

Use the Jupyter notebooks for detailed analysis:

```bash
# Start Jupyter
jupyter notebook

# Open notebooks
notebooks/Online_Retail_eda.ipynb      # Exploratory analysis
notebooks/Online_Retail_cleaning.ipynb # Data cleaning process
```

---

## 📁 Data Files

### 📥 Input Data

| File | Description | Records | Purpose |
|------|-------------|---------|---------|
| `Online_Retail_data.csv` | Raw transaction data | ~540K | Original dataset |
| `Online_Retail_Cleaned.csv` | Cleaned data | ~505K | Analysis-ready |

### 📤 Generated Files

| File | Description | Features | Use Case |
|------|-------------|----------|----------|
| `featured_data.csv` | Main analysis dataset | 46 | Dashboard source |
| `customer_features.csv` | Customer analytics | 21 | Customer insights |
| `product_features.csv` | Product performance | 17 | Product analysis |
| `country_features.csv` | Geographic data | 12 | Market analysis |

---

## 🛠️ Technical Details

### 🧠 Feature Engineering

The project creates **46 engineered features** across multiple categories:

#### ⏰ Time-Based Features (13)
- Year, Month, Day, Hour, Quarter
- Day of week, Season, Weekend indicator
- Business hours, Holiday season
- Week of year, Day name

#### 💰 Transaction Features (8)
- Revenue calculations
- Price categories (Free/Low/Medium/High/Premium)
- Quantity categories (Single/Small/Medium/Large batch)
- Transaction size categories
- Cancellation indicators

#### 👥 Customer Features (12)
- RFM Analysis (Recency, Frequency, Monetary)
- Customer segments (Champions, Loyal, At Risk, etc.)
- Customer lifetime value
- Purchase patterns
- Loyalty indicators

#### 🛍️ Product Features (7)
- Product performance categories
- Popularity scores
- Revenue per customer
- Cross-selling indicators

#### 🌍 Geographic Features (6)
- Market share by country
- Revenue per customer by region
- Transaction density
- Market penetration metrics

### 🔧 Advanced Analytics

#### 📊 Customer Segmentation
- **Champions**: High RFM scores across all dimensions
- **Loyal Customers**: Regular purchasers with good value
- **Potential Loyalists**: Good recent activity
- **New Customers**: Recent first-time buyers
- **At Risk**: Declining activity, need attention
- **Lost Customers**: Haven't purchased recently

#### 📈 Predictive Models
- **Revenue Forecasting**: Linear trend analysis with 30-day predictions
- **Churn Prediction**: Risk scoring based on recency patterns
- **Demand Forecasting**: Product-level demand trends

---

## 🎨 Dashboard Tabs

### 1. 📈 Revenue Analytics
- Daily and monthly revenue trends
- Revenue forecasting
- Growth rate analysis
- Seasonal patterns

### 2. 👤 Customer Intelligence
- Customer segmentation pie chart
- Top customers by revenue
- Customer lifetime value analysis
- RFM analysis visualization

### 3. 🛍️ Product Performance
- Top products by quantity and revenue
- Product category analysis
- Inventory insights
- Cross-selling opportunities

### 4. 🌍 Geographic Analysis
- Revenue by country
- Customer distribution worldwide
- Market penetration analysis
- Expansion opportunities

### 5. 📊 Advanced Insights
- Hourly revenue patterns
- Customer value distribution
- Order frequency analysis
- Cohort analysis
- Growth trends

### 6. ⏱️ Time Analytics
- Revenue heatmaps (day vs hour)
- Seasonal analysis
- Quarterly performance
- Customer acquisition timeline

### 7. 🎯 Predictive Analytics
- Revenue forecasting (30 days)
- Customer churn risk analysis
- Product demand forecasting
- Market opportunity matrix

---

## 🎯 Key Business Insights

### 💡 Performance Insights
- **Peak Hours**: Identify optimal business hours
- **Customer Value**: Focus on high-LTV customers
- **Order Patterns**: Understand purchase frequency
- **Growth Trends**: Month-over-month analysis
- **Seasonality**: Weekly patterns for optimization

### 🚀 Strategic Recommendations
- **Price Optimization**: Analyze demand elasticity
- **Product Portfolio**: Focus on high-performers
- **Customer Segmentation**: Tailor marketing strategies
- **Market Expansion**: Leverage geographic data
- **Revenue Diversification**: Balance order sizes

---

## 🎨 Design Features

### 🌟 Professional UI/UX
- **Gradient Backgrounds**: Modern professional design
- **Interactive Elements**: Hover effects and animations
- **Responsive Layout**: Works on all screen sizes
- **Color-coded Metrics**: Easy visual identification
- **Professional Typography**: Clean, readable fonts

### ⚡ Performance Optimizations
- **Data Caching**: Fast loading with Streamlit cache
- **Lazy Loading**: Charts load as needed
- **Efficient Queries**: Optimized data processing
- **Memory Management**: Handles large datasets

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 🔧 Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/Online-Retail-Dashboard.git
cd Online-Retail-Dashboard

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

### 📝 Contribution Guidelines

1. **🧪 Add tests** for new features
2. **📖 Update documentation** as needed
3. **🎨 Follow code style** (PEP 8)
4. **✅ Ensure all tests pass**
5. **📋 Update README** if needed

### 🐛 Reporting Issues

- Use the GitHub issue tracker
- Include system information
- Provide steps to reproduce
- Add screenshots if relevant

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Contact

### 🆘 Getting Help

- **📖 Documentation**: Check this README first
- **🐛 Issues**: Use GitHub Issues for bugs
- **💡 Features**: Submit feature requests
- **❓ Questions**: Use GitHub Discussions

### 👨‍💻 Author

**Anurag Chaubey**
- GitHub: [@anuragchaubey1224](https://github.com/anuragchaubey1224)
- Project: [Online-Retail-Dashboard](https://github.com/anuragchaubey1224/Online-Retail-Dashboard)

---

## 🌟 Acknowledgments

- **Dataset**: UCI Machine Learning Repository
- **Streamlit**: Amazing framework for ML dashboards
- **Plotly**: Beautiful interactive visualizations
- **Pandas**: Powerful data manipulation library

---

<div align="center">
  <h3>🚀 Made with streamlit and Python</h3>
  <p><em>Transform your retail data into actionable business insights!</em></p>
  
  **⭐ Star this repository if you found it helpful!**
</div>

---

## 📊 Project Stats

- **📈 Features**: 46 engineered features
- **🎯 Analytics Tabs**: 7 comprehensive views
- **📊 Visualizations**: 20+ interactive charts
- **🎨 UI Components**: Professional design system
- **⚡ Performance**: Optimized for large datasets
- **🔧 Dependencies**: 25+ carefully chosen packages

---

<div align="center">
  <sub>Built with Python 🐍 • Streamlit ⚡ • Plotly 📊 </sub>
</div>