import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # Load data from JSON file
    df = pd.read_json('data.json')
    return df

def main():
    # Load data
    df = load_data()

    # Title
    st.title('Real Time BI Dashboard with Sample Data')

    # Sidebar - Filters
    st.sidebar.header('Filters')
    # Example: Dropdown for 'Region' filter
    unique_regions = df['Region'].unique()
    selected_region = st.sidebar.selectbox('Region', unique_regions)

    # Filter data based on selection
    if selected_region != 'All':
        df_filtered = df[df['Region'] == selected_region]
    else:
        df_filtered = df

    # Display filtered data
    st.subheader('Sample Data')
    st.dataframe(df_filtered)

    # Line chart - Sales over time
    st.subheader('Sales Over Time')
    fig_sales = px.line(df_filtered, x='Date', y='Sales', title='Sales Over Time')
    st.plotly_chart(fig_sales)

    # Bar chart - Expenses over time
    st.subheader('Expenses Over Time')
    fig_expenses = px.bar(df_filtered, x='Date', y='Expenses', title='Expenses Over Time')
    st.plotly_chart(fig_expenses)

    # Additional Matrices & Analyzers
    # Example: Profit over time
    st.subheader('Profit Over Time')
    fig_profit = px.line(df_filtered, x='Date', y='Profit', title='Profit Over Time')
    st.plotly_chart(fig_profit)

    # Example: Units Sold over time
    st.subheader('Units Sold Over Time')
    fig_units_sold = px.line(df_filtered, x='Date', y='Units Sold', title='Units Sold Over Time')
    st.plotly_chart(fig_units_sold)

    # Add more charts as needed based on available data

if __name__ == '__main__':
    main()
