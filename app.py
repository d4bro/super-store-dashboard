import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
data = pd.read_excel('sample_-_superstore.xls')

state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

data['State Abbr'] = data['State'].map(state_abbreviations)
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

# Create Ship Time column
data['Ship Time'] = (data['Ship Date'] - data['Order Date']).dt.days

st.title('Superstore Sales Dashboard')
st.sidebar.header('Select Report')
report_type = st.sidebar.selectbox('Report Type', 
    ['Sales by Category',
     'Regional Report',
     'Sales Trends Over Time',
     'Margin and Profit',
     'Shipping Efficiency',
     'Customer Segment',
     'Discounts and Promotions'])

if report_type == 'Sales by Category':
    st.title('Sales by Category Report')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Sales and Profit')
        category_sales_profit = data.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
        fig1 = px.bar(category_sales_profit, x='Category', y=['Sales', 'Profit'], barmode='group', 
                      title="Total Sales and Profit by Category")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.header('Order Count')
        subcategory_orders = data['Sub-Category'].value_counts().reset_index()
        subcategory_orders.columns = ['Sub-Category', 'Order Count']
        fig2 = px.bar(subcategory_orders, x='Order Count', y='Sub-Category', orientation='h', 
                      title="Order Count by Sub-Category")
        st.plotly_chart(fig2, use_container_width=True)
    with col3:
        st.header('Average Discounts by Category')
        category_discount = data.groupby('Category')['Discount'].mean().reset_index()
        fig3 = px.bar(category_discount, x='Discount', y='Category', orientation='h', 
                      title="Average Discounts by Category")
        st.plotly_chart(fig3, use_container_width=True)

if report_type == 'Regional Report':
    state_sales = data.groupby(['State', 'State Abbr']).agg({'Sales': 'sum'}).reset_index()
    state_sales = state_sales.sort_values('Sales', ascending=False)
    st.header('Sales Map by State')
    fig1 = px.choropleth(state_sales, 
                         locations='State Abbr',
                         locationmode='USA-states',
                         color='Sales', 
                         color_continuous_scale='Blues', 
                         labels={'Sales': 'Sales'},
                         scope="usa", 
                         title="Sales Across USA States")
    st.plotly_chart(fig1, use_container_width=True)
    col11, col22 = st.columns(2)
    with col11:
        st.header('Cities with Highest Sales')
        city_sales = data.groupby('City').agg({'Sales': 'sum'}).reset_index()
        top_cities = city_sales.nlargest(10, 'Sales')
        fig2 = px.bar(top_cities, x='Sales', y='City', orientation='h', 
                      title='Top 10 Cities by Sales')
        st.plotly_chart(fig2, use_container_width=True)
    with col22:
        st.header('Sales by State')
        fig3 = px.bar(state_sales, x='Sales', y='State', orientation='h', 
                      title='Sales by State')
        st.plotly_chart(fig3, use_container_width=True)

if report_type == 'Sales Trends Over Time':
    st.header('Time Report')
    # Monthly Sales
    st.subheader('Monthly Sales')
    monthly_sales = data.resample('M', on='Order Date')['Sales'].sum().reset_index()
    fig1 = px.line(monthly_sales, x='Order Date', y='Sales', 
                   title='Monthly Sales')
    st.plotly_chart(fig1, use_container_width=True)
    # Quarterly Profit
    st.subheader('Quarterly Profit')
    quarterly_profit = data.resample('Q', on='Order Date')['Profit'].sum().reset_index()
    fig2 = px.line(quarterly_profit, x='Order Date', y='Profit', 
                   title='Quarterly Profit')
    st.plotly_chart(fig2, use_container_width=True)
    # Year-over-Year Sales Growth
    st.subheader('Year-over-Year Sales Growth')
    yearly_sales = data.resample('Y', on='Order Date')['Sales'].sum()
    yearly_growth = yearly_sales.pct_change().dropna().reset_index()
    yearly_growth.columns = ['Year', 'Growth']
    fig3 = px.bar(yearly_growth, x='Year', y='Growth', 
                  title='Year-over-Year Sales Growth')
    st.plotly_chart(fig3, use_container_width=True)

if report_type == 'Margin and Profit':
    st.header('Margin and Profit Report')
    # Category Profitability
    st.subheader('Category Profitability')
    category_profit = data.groupby('Category').agg({'Profit': 'sum'}, numeric_only=True).reset_index()
    fig1 = px.bar(category_profit, x='Category', y='Profit', 
                  title='Profit by Category')
    st.plotly_chart(fig1, use_container_width=True)
    # Product Profitability
    st.subheader('Product Profitability')
    product_profit = data.groupby('Product Name').agg({'Profit': 'sum'}, numeric_only=True).reset_index()
    top_products = product_profit.nlargest(10, 'Profit')
    fig2 = px.bar(top_products, x='Profit', y='Product Name', orientation='h', 
                  title='Top 10 Products by Profit')
    st.plotly_chart(fig2, use_container_width=True)
    # Profit Margin by Product
    st.subheader('Profit Margin by Product')
    data['Profit Margin'] = data['Profit'] / data['Sales']
    product_margin = data.groupby('Product Name').agg({'Profit Margin': 'mean'}, numeric_only=True).reset_index()
    top_margins = product_margin.nlargest(10, 'Profit Margin')
    fig3 = px.bar(top_margins, x='Profit Margin', y='Product Name', orientation='h', 
                  title='Top 10 Products by Profit Margin')
    st.plotly_chart(fig3, use_container_width=True)

if report_type == 'Shipping Efficiency':
    st.header('Shipping Efficiency Report')
    # Average Shipping Time
    st.subheader('Average Shipping Time')
    avg_shipping_time = data['Ship Time'].mean()
    st.write(f'Average Shipping Time: {avg_shipping_time:.2f} days')
    # Shipping Time Histogram
    st.subheader('Shipping Time')
    fig1 = px.histogram(data, x='Ship Time', nbins=20, 
                        title='Shipping Time Distribution')
    st.plotly_chart(fig1, use_container_width=True)
    # Shipping Mode Popularity
    st.subheader('Shipping Mode Popularity')
    ship_mode_counts = data['Ship Mode'].value_counts().reset_index()
    ship_mode_counts.columns = ['Ship Mode', 'Count']
    fig2 = px.pie(ship_mode_counts, values='Count', names='Ship Mode', 
                  title='Distribution by Shipping Mode')
    st.plotly_chart(fig2, use_container_width=True)

if report_type == 'Customer Segment':
    st.header('Customer Segment Report')
    # Total Sales by Customer Segments
    st.subheader('Sales by Customer Segments')
    segment_sales = data.groupby('Segment').agg({'Sales': 'sum'}).reset_index()
    fig1 = px.bar(segment_sales, x='Segment', y='Sales', 
                  title='Sales by Customer Segment')
    st.plotly_chart(fig1, use_container_width=True)

    # Average Order Value in Customer Segments
    st.subheader('Average Order Value in Segments')
    segment_avg_order = data.groupby('Segment').agg({'Sales': 'mean'}).reset_index()
    segment_avg_order.columns = ['Segment', 'Avg Order Value']
    fig2 = px.bar(segment_avg_order, x='Segment', y='Avg Order Value',
                  title='Average Order Value by Customer Segment')
    st.plotly_chart(fig2, use_container_width=True)

if report_type == 'Discounts and Promotions':
    st.header('Discounts and Promotions Report')
    
    # Average Discount Value
    st.subheader('Average Discount Value')
    avg_discount = data['Discount'].mean()
    st.write(f'Average Discount Value: {avg_discount:.2%}')

    # Impact of Discounts on Sales
    st.subheader('Impact of Discounts on Sales')
    fig1 = px.scatter(data, x='Discount', y='Sales',
                      trendline='ols',
                      title='Relationship between Discounts and Sales')
    st.plotly_chart(fig1, use_container_width=True)

    # Impact of Discounts on Profit
    st.subheader('Impact of Discounts on Profit')
    fig2 = px.scatter(data, x='Discount', y='Profit',
                      trendline='ols',
                      title='Relationship between Discounts and Profit')
    st.plotly_chart(fig2, use_container_width=True)
