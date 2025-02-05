```markdown
```
# Superstore Sales Dashboard
```
```
This repository contains a Streamlit application for visualizing and analyzing sales data from a sample superstore dataset. The dashboard provides several interactive reports, including sales by category, regional distribution, time-based trends, and more.

## Features

- **Sales by Category**: Visualize total sales and profit by category, order count by sub-category, and average discounts.
- **Regional Report**: Explore sales distribution across states and cities using a choropleth map and bar charts.
- **Sales Trends Over Time**: Analyze monthly sales, quarterly profit, and year-over-year sales growth trends.
- **Margin and Profit**: Examine profitability and profit margins by category and product.
- **Shipping Efficiency**: Assess shipping times and mode popularity.
- **Customer Segment**: Investigate sales and average order value across customer segments.
- **Discounts and Promotions**: Evaluate the impact of discount strategies on sales and profit.

## Installation

To run this application, you need to have Python installed on your system. Follow these steps to set up and run the application:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/d4bro/super-store-dashboard.git
   cd super-store-dashboard
   ```

2. **Install Required Packages**
   Make sure to install the necessary Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the Streamlit app using the following command:
   ```bash
   streamlit run streamlitapp.py
   ```

## Usage

Once the app is running, you can access it via the URL provided in your terminal (usually `http://localhost:8501`). Use the sidebar to select different report types and visualize the data.

## Dataset
https://public.tableau.com/app/learn/sample-data

Superstore Sales

The application uses a sample dataset named `sample_-_superstore.xls`, which should be placed in the root directory of the project. This dataset includes information about sales orders, such as order date, ship date, category, sub-category, sales figures, profit, discounts, and customer segments.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your changes are well-documented and tested.
```
