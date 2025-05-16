# ShopNest - E-commerce Data Analysis Project

This project contains a comprehensive e-commerce data analysis solution using MySQL for data storage and Power BI for visualization. The dataset includes customer information, product details, order data, and seller information from the Nexusgoods e-commerce platform.

## Project Overview

**Project Title:** Shop Nest Store Dashboard  
**Prepared By:** Sachin  
**Tools Used:** MySQL, Power BI, Excel, Python  
**Date:** 12/05/2025  

### Objective
The primary goal of this dashboard is to provide a comprehensive analysis of product orders stored in the MySQL database. The dashboard enables stakeholders to monitor key metrics such as order volume, revenue trends, customer behaviour, payment methods, and product category performance — helping in data-driven decision-making.

### Key Metrics Highlights
- Total Orders Placed: 96.48K
- Total Revenue (Final Amount): $16.01M
- Overall Customer Rating: 4.07 / 5
- Total Unique Customers: 99.44K

## Project Structure

- `upload_csv_to_mysql.py`: Script to upload CSV data to MySQL database
- Multiple CSV datasets containing e-commerce data:
  - Customer data
  - Product information
  - Order details
  - Seller information
  - Geolocation data
  - Order reviews
  - Order payments
- Power BI dashboard (`Shop Nest store.pbix`)
- Documentation (`Shop Nest Store.docx`)

## Data Schema

### Key Attributes
| Attribute | Description |
|-----------|-------------|
| Order_ID | Unique identifier for each order |
| Customer_ID | Identifier for the customer placing the order |
| Product_Category | Category name of the ordered product |
| Order_Date | Date when the order was placed |
| Delivery_Date | Expected or actual delivery date |
| Delivery_Status | Status (e.g., Delayed, On Time) |
| Payment_Method | Mode of payment (e.g., Debit Card, Credit Card, Voucher, Bolete) |
| Order_Amount | Total order value |
| Shipping_Cost | Delivery charges applied |
| Discount_Applied | Discount value or percentage |
| Final_Amount | Net payable amount after discount and shipping |
| Customer_Rating | Feedback rating provided by the customer |
| Delivery_City | City where the order was shipped |

## Dashboard Components

### 1. Total Orders & Revenue Analysis
- Comprehensive overview of total orders and revenue metrics
- Customer rating analysis
- Unique customer tracking

### 2. Category Performance
- Top categories by sales (Clustered Bar Chart)
- Delayed orders by category analysis
- Category-wise customer ratings

### 3. Payment Analysis
- Payment mode distribution (Pie Chart)
- Revenue contribution by payment method
- Trends in payment preferences

### 4. Delivery Performance
- Monthly delivery status tracking
- Delayed vs On-Time order comparison
- Geographical delivery analysis

### 5. Product Category Analysis
- Top rated categories performance
- Bottom rated categories identification
- Category-wise revenue tracking

### 6. Geographical Analysis
- Total sales by state (Geo Map)
- Regional performance metrics
- State-wise revenue distribution

### 7. Temporal Analysis
- Revenue by year and quarter
- Seasonal trends identification
- Quarterly performance comparison

### 8. Interactive Features
- Category-based filtering
- Year range selection
- Dynamic cross-visual filtering

## Prerequisites

1. Python 3.7 or higher
2. MySQL Server 8.0 or higher
3. Power BI Desktop (for viewing and modifying dashboards)

## Required Python Packages

```
pandas
sqlalchemy
pymysql
```

## Setup Instructions

1. **Install Required Python Packages**
   ```bash
   pip install pandas sqlalchemy pymysql
   ```

2. **MySQL Setup**
   - Install MySQL Server if not already installed
   - Create a new database named 'shop_nest':
     ```sql
     CREATE DATABASE shop_nest;
     ```
   - Note your MySQL credentials (username and password)

3. **Configure Database Connection**
   - Open `upload_csv_to_mysql.py`
   - Update the following variables with your MySQL credentials:
     ```python
     db_user = 'root'  # Replace with your MySQL username
     db_pass = 'password'  # Replace with your MySQL password
     db_host = 'localhost'  # Update if your MySQL is on a different host
     db_name = 'shop_nest'
     ```
   - Update the `csv_folder_path` variable to point to the directory containing your CSV files

4. **Data Import**
   - Place all CSV files in the same directory
   - Run the upload script:
     ```bash
     python upload_csv_to_mysql.py
     ```
   - The script will automatically create tables and import data from all CSV files

5. **Power BI Dashboard**
   - Open `Shop Nest store.pbix` with Power BI Desktop
   - Update the data source connection to point to your MySQL database
   - Refresh the data to see the latest information

## Dataset Description

The project includes the following datasets:
- `Nexusgoods_customers_dataset.csv`: Customer information
- `Nexusgoods_products_dataset.csv`: Product details
- `Nexusgoods_orders_dataset.csv`: Order information
- `Nexusgoods_order_items_dataset.csv`: Order items details
- `Nexusgoods_sellers_dataset.csv`: Seller information
- `Nexusgood_geolocation_dataset.csv`: Geographic location data
- `Nexusgoods_order_reviews_dataset.csv`: Customer reviews
- `Nexusgoods_order_payments_dataset.csv`: Payment information
- `product_category_name_translation.csv`: Product category translations

## Technical Implementation

### MySQL Database
- Structured database design for efficient querying
- Optimized table relationships for performance
- Implemented for handling large-scale e-commerce data

### Python Integration
- Automated data upload process
- Efficient handling of large datasets
- Streamlined database population

## Troubleshooting

1. **Database Connection Issues**
   - Verify MySQL server is running
   - Check credentials in the Python script
   - Ensure MySQL user has appropriate permissions

2. **CSV Import Errors**
   - Verify CSV files are in the correct directory
   - Check file permissions
   - Ensure CSV files are not corrupted or open in another program

## Additional Resources

- Refer to `Shop Nest Store.docx` for detailed documentation
- Check `ShopNest Dashboard Sheet.png` for dashboard preview

## Support

For any issues or questions, please refer to the documentation or create an issue in the project repository. 