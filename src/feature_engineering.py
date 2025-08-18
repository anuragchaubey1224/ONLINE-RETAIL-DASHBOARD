# Feature Engineering for Online Retail Dataset
import pandas as pd
import numpy as np
from datetime import datetime
from operator import attrgetter
import os
import warnings
warnings.filterwarnings('ignore')

def load_and_prepare_data():
    """Load and prepare the cleaned dataset"""
    print("Loading cleaned dataset...")
    
    # Get the correct path to the data file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_path = os.path.join(project_root, 'data', 'Online_Retail_Cleaned.csv')
    
    df = pd.read_csv(data_path)
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Create TotalPrice column
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    print(f"Dataset loaded with {len(df)} records")
    return df

def create_time_features(df):
    """Create time-based features"""
    print("Creating time-based features...")
    
    # Basic time features
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Day'] = df['InvoiceDate'].dt.day
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['DayName'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour
    df['Quarter'] = df['InvoiceDate'].dt.quarter
    df['WeekOfYear'] = df['InvoiceDate'].dt.isocalendar().week
    
    # Seasonal features
    df['Season'] = df['Month'].map({
        12: 'Winter', 1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Fall', 10: 'Fall', 11: 'Fall'
    })
    
    # Business-specific time features
    df['IsWeekend'] = df['DayOfWeek'].isin([5, 6]).astype(int)
    df['IsBusinessHour'] = ((df['Hour'] >= 9) & (df['Hour'] <= 17)).astype(int)
    df['IsHolidaySeason'] = df['Month'].isin([11, 12]).astype(int)
    
    return df

def create_transaction_features(df):
    """Create transaction-level features"""
    print("Creating transaction features...")
    
    # Cancellation features
    df['IsCanceled'] = df['InvoiceNo'].astype(str).str.startswith('C').astype(int)
    
    # Revenue features
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['PricePerUnit'] = df['UnitPrice']
    
    # Quantity features
    df['QuantityCategory'] = pd.cut(df['Quantity'], 
                                   bins=[-np.inf, 0, 1, 5, 20, np.inf],
                                   labels=['Negative', 'Single', 'Small_Batch', 'Medium_Batch', 'Large_Batch'])
    
    # Price categories
    df['PriceCategory'] = pd.cut(df['UnitPrice'],
                                bins=[-np.inf, 0, 2, 5, 20, np.inf],
                                labels=['Free/Return', 'Low', 'Medium', 'High', 'Premium'])
    
    # Transaction size categories
    df['TransactionSize'] = pd.cut(df['Revenue'],
                                  bins=[-np.inf, 0, 10, 50, 200, np.inf],
                                  labels=['Negative', 'Small', 'Medium', 'Large', 'XLarge'])
    
    return df

def create_customer_features(df):
    """Create customer-level features"""
    print("Creating customer features...")
    
    # Handle missing CustomerIDs
    df['CustomerID'] = df['CustomerID'].fillna('UNKNOWN_CUSTOMER')
    
    # Latest date for recency calculation
    latest_date = df['InvoiceDate'].max()
    
    # Customer aggregations
    customer_features = df.groupby('CustomerID').agg({
        'InvoiceDate': ['min', 'max', 'count'],
        'InvoiceNo': 'nunique',
        'Revenue': ['sum', 'mean', 'std'],
        'Quantity': ['sum', 'mean'],
        'UnitPrice': 'mean',
        'Country': 'first'
    }).round(2)
    
    # Flatten column names
    customer_features.columns = ['_'.join(col).strip() for col in customer_features.columns]
    customer_features = customer_features.reset_index()
    
    # Rename columns for clarity
    customer_features.columns = [
        'CustomerID', 'FirstPurchase', 'LastPurchase', 'TotalTransactions',
        'UniqueInvoices', 'TotalRevenue', 'AvgRevenue', 'StdRevenue',
        'TotalQuantity', 'AvgQuantity', 'AvgUnitPrice', 'Country'
    ]
    
    # Calculate additional customer metrics
    customer_features['CustomerLifespan'] = (customer_features['LastPurchase'] - customer_features['FirstPurchase']).dt.days
    customer_features['Recency'] = (latest_date - customer_features['LastPurchase']).dt.days
    customer_features['Frequency'] = customer_features['UniqueInvoices']
    customer_features['Monetary'] = customer_features['TotalRevenue']
    
    # RFM Scoring
    customer_features['RecencyScore'] = pd.qcut(customer_features['Recency'], 5, labels=[5,4,3,2,1])
    customer_features['FrequencyScore'] = pd.qcut(customer_features['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
    customer_features['MonetaryScore'] = pd.qcut(customer_features['Monetary'], 5, labels=[1,2,3,4,5])
    
    # Combined RFM Score
    customer_features['RFM_Score'] = (customer_features['RecencyScore'].astype(str) + 
                                     customer_features['FrequencyScore'].astype(str) + 
                                     customer_features['MonetaryScore'].astype(str))
    
    # Customer segments
    def categorize_customer(row):
        if row['RecencyScore'] >= 4 and row['FrequencyScore'] >= 4 and row['MonetaryScore'] >= 4:
            return 'Champions'
        elif row['RecencyScore'] >= 3 and row['FrequencyScore'] >= 3 and row['MonetaryScore'] >= 3:
            return 'Loyal Customers'
        elif row['RecencyScore'] >= 4 and row['FrequencyScore'] <= 2:
            return 'New Customers'
        elif row['RecencyScore'] <= 2 and row['FrequencyScore'] >= 3:
            return 'At Risk'
        elif row['RecencyScore'] <= 2 and row['FrequencyScore'] <= 2:
            return 'Lost Customers'
        else:
            return 'Potential Loyalists'
    
    customer_features['CustomerSegment'] = customer_features.apply(categorize_customer, axis=1)
    
    return customer_features

def create_product_features(df):
    """Create product-level features"""
    print("Creating product features...")
    
    # Handle missing descriptions
    df['Description'] = df['Description'].fillna('UNKNOWN_DESCRIPTION')
    
    # Product aggregations
    product_features = df.groupby('StockCode').agg({
        'Description': 'first',
        'UnitPrice': ['mean', 'std', 'min', 'max'],
        'Quantity': ['sum', 'mean', 'count'],
        'Revenue': ['sum', 'mean'],
        'CustomerID': 'nunique',
        'Country': 'nunique'
    }).round(2)
    
    # Flatten column names
    product_features.columns = ['_'.join(col).strip() for col in product_features.columns]
    product_features = product_features.reset_index()
    
    # Rename columns
    product_features.columns = [
        'StockCode', 'Description', 'AvgPrice', 'PriceStd', 'MinPrice', 'MaxPrice',
        'TotalQuantitySold', 'AvgQuantityPerOrder', 'TotalOrders',
        'TotalRevenue', 'AvgRevenuePerOrder', 'UniqueCustomers', 'CountriesServed'
    ]
    
    # Calculate additional product metrics
    product_features['PriceVariability'] = product_features['PriceStd'] / product_features['AvgPrice']
    product_features['PopularityScore'] = product_features['TotalOrders'] / product_features['TotalOrders'].max()
    product_features['RevenuePerCustomer'] = product_features['TotalRevenue'] / product_features['UniqueCustomers']
    
    # Product categories based on performance
    product_features['ProductCategory'] = pd.cut(product_features['TotalRevenue'],
                                                bins=4,
                                                labels=['Low_Performer', 'Medium_Performer', 'High_Performer', 'Star_Product'])
    
    return product_features

def create_country_features(df):
    """Create country-level features"""
    print("Creating country features...")
    
    country_features = df.groupby('Country').agg({
        'Revenue': ['sum', 'mean', 'count'],
        'CustomerID': 'nunique',
        'StockCode': 'nunique',
        'Quantity': ['sum', 'mean'],
        'UnitPrice': 'mean'
    }).round(2)
    
    # Flatten column names
    country_features.columns = ['_'.join(col).strip() for col in country_features.columns]
    country_features = country_features.reset_index()
    
    # Rename columns
    country_features.columns = [
        'Country', 'TotalRevenue', 'AvgRevenue', 'TotalTransactions',
        'UniqueCustomers', 'UniqueProducts', 'TotalQuantity', 'AvgQuantity', 'AvgUnitPrice'
    ]
    
    # Calculate market share
    country_features['MarketShare'] = country_features['TotalRevenue'] / country_features['TotalRevenue'].sum()
    country_features['RevenuePerCustomer'] = country_features['TotalRevenue'] / country_features['UniqueCustomers']
    country_features['TransactionsPerCustomer'] = country_features['TotalTransactions'] / country_features['UniqueCustomers']
    
    return country_features

def merge_all_features(df, customer_features, product_features, country_features):
    """Merge all features back to main dataset"""
    print("Merging all features...")
    
    # Merge customer features
    df = df.merge(customer_features[['CustomerID', 'CustomerSegment', 'RecencyScore', 'FrequencyScore', 
                                   'MonetaryScore', 'RFM_Score', 'TotalRevenue', 'Frequency', 'Recency']], 
                 on='CustomerID', how='left', suffixes=('', '_customer'))
    
    # Merge product features
    df = df.merge(product_features[['StockCode', 'ProductCategory', 'PopularityScore', 
                                   'TotalRevenue', 'UniqueCustomers']], 
                 on='StockCode', how='left', suffixes=('', '_product'))
    
    # Merge country features
    df = df.merge(country_features[['Country', 'MarketShare', 'RevenuePerCustomer', 
                                   'TransactionsPerCustomer']], 
                 on='Country', how='left', suffixes=('', '_country'))
    
    return df

def create_advanced_features(df):
    """Create advanced analytical features"""
    print("Creating advanced features...")
    
    # Basket analysis features
    basket_features = df.groupby('InvoiceNo').agg({
        'StockCode': 'count',
        'Revenue': 'sum',
        'Quantity': 'sum',
        'CustomerID': 'first',
        'Country': 'first'
    }).rename(columns={'StockCode': 'BasketSize'})
    
    basket_features['AvgItemValue'] = basket_features['Revenue'] / basket_features['BasketSize']
    
    # Merge basket features back
    df = df.merge(basket_features[['BasketSize', 'AvgItemValue']], 
                 left_on='InvoiceNo', right_index=True, how='left')
    
    # Cohort features (simplified)
    df['CohortMonth'] = df.groupby('CustomerID')['InvoiceDate'].transform('min').dt.to_period('M')
    df['PeriodNumber'] = (df['InvoiceDate'].dt.to_period('M') - df['CohortMonth']).apply(attrgetter('n'))
    
    return df

def save_featured_data(df, customer_features, product_features, country_features):
    """Save all featured datasets"""
    print("Saving featured datasets...")
    
    # Get the correct path for saving files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'data')
    
    # Save main dataset with all features
    main_path = os.path.join(data_dir, 'featured_data.csv')
    df.to_csv(main_path, index=False)
    print(f"Main dataset saved as '{main_path}' with {len(df)} records and {len(df.columns)} features")
    
    # Save individual feature datasets
    customer_path = os.path.join(data_dir, 'customer_features.csv')
    product_path = os.path.join(data_dir, 'product_features.csv')
    country_path = os.path.join(data_dir, 'country_features.csv')
    
    customer_features.to_csv(customer_path, index=False)
    product_features.to_csv(product_path, index=False)
    country_features.to_csv(country_path, index=False)
    
    print("Feature engineering completed successfully!")
    print(f"Files saved:")
    print(f"- featured_data.csv: {len(df.columns)} columns")
    print(f"- customer_features.csv: {len(customer_features.columns)} columns")
    print(f"- product_features.csv: {len(product_features.columns)} columns")
    print(f"- country_features.csv: {len(country_features.columns)} columns")

def main():
    """Main feature engineering pipeline"""
    print("=== ONLINE RETAIL FEATURE ENGINEERING PIPELINE ===")
    
    # Load data
    df = load_and_prepare_data()
    
    # Create features
    df = create_time_features(df)
    df = create_transaction_features(df)
    
    # Create aggregated features
    customer_features = create_customer_features(df)
    product_features = create_product_features(df)
    country_features = create_country_features(df)
    
    # Merge features
    df = merge_all_features(df, customer_features, product_features, country_features)
    
    # Advanced features
    df = create_advanced_features(df)
    
    # Save all datasets
    save_featured_data(df, customer_features, product_features, country_features)
    
    return df, customer_features, product_features, country_features

if __name__ == "__main__":
    df, customer_features, product_features, country_features = main()
