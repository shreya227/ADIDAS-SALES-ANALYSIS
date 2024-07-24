
from streamlit_pills import pills
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
#from  PIL import ImageChops
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from us import states


st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.markdown('This GUI application serves as a Streamlit dashboard for analyzing Adidas sales.🐦')
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/1200px-Adidas_Logo.svg.png', width=100, use_column_width=False)
DATA_URL = (r"C:\Users\hp\OneDrive\My folder\Streamlit projects\Adidas dashboard\Adidas US Sales Datasets.xlsx")
#@st.cache(allow_output_mutation=True)
#@st.cache(persist=True)
def load_data():
    data = pd.read_excel(DATA_URL)
    return data
    #st.subheader('Dataset')
data = load_data()  


# Create a list of navigation options
selected = option_menu(
    menu_title=None,  # optional menu title
    options=["Home", "Dataset Description", "Data Analysis"],
    icons=["house", "info", "kanban"],  # optional icons from emojis or FontAwesome
    orientation="horizontal",
    styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "blue", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#C9CAFF"},
         }  
)

# st.sidebar.title('Others')



if selected == "Home":
    st.markdown('<p style="font-size:20px; font-weight:bold; font-style:italic;">Home</p>', unsafe_allow_html=True)
    # st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/1200px-Adidas_Logo.svg.png', width=100, use_column_width=False)
    st.title('Adidas-Sales-Analysis: Unraveling the Secrets of Adidas')
    #st.image(r"C:\Users\Shreya\Downloads\pic.jpg", width=700)
    image_url = "https://img.freepik.com/free-photo/businesswoman-using-tablet-analysis-graph-company-finance-strategy-statistics-success-concept-planning-future-office-room_74952-1410.jpg?size=626&ext=jpg"
    st.image(image_url, caption="Sales Analysis Image", use_column_width=True)
    with st.sidebar:
        choose = option_menu("Menu", ["Problem Statement","Objectives"],
                         icons=['dot', 'dot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "blue", "font-size": "23px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#C9CAFF"},
         })
        if choose == "Problem Statement":
            st.sidebar.markdown("""The objective of this project is to analyze the Adidas sales database for the year 2020 and 2021 and 
                identify key insights to help improve sales performance and optimize business strategies.
             By analyzing the sales data, we aim to understand factors influencing sales, identify trends, 
             and uncover opportunities for growth.""")

        elif choose == "Objectives":
            st.sidebar.markdown("1. To identify the products that are generating the highest sales revenue.")
            st.sidebar.markdown("2. To identify which retailer made the highest and least sales.")
            st.sidebar.markdown("3. To identify which months or years had the highest and lowest sales figures.")
            st.sidebar.markdown("4. To study how does sales performance vary across different sales methods.")
            st.sidebar.markdown("5. To identify the regions that are driving the most sales for the business.")



elif selected == "Dataset Description":
    st.markdown('<p style="font-size:20px; font-weight:bold;font-style:italic;">Dataset Description</p>', unsafe_allow_html=True)
    st.write("This is a Adidas sales dataset. It is a collection of data that includes information on the sales of Adidas products.")
    st.write(data)
    st.subheader("Attribute information: ")
    st.write("• Retailer: Represents the business or individual that sells Adidas products directly to consumers.")
    st.write("• Retailer ID: A unique identifier assigned to each retailer in the dataset.")
    st.write("• Invoice Date: The date when a particular invoice or sales transaction took place.")
    st.write("• Region: Refers to a specific geographical area or district where the sales activity or retail operations occur.")
    st.write("• State: Represents a specific administrative division or territory within a country.")
    st.write("• City: Refers to an urban area or municipality where the sales activity or retail operations are conducted.")
    st.write("• Product: Represents the classification or grouping of Adidas products.")
    st.write("• Price per Unit: The cost or price associated with a single unit of a product.")
    st.write("• Units Sold: The quantity or number of units of a particular product sold during a specific sales transaction.")
    st.write("• Total Sales: The overall revenue generated from the sales transactions.")
    st.write("• Operating Profit: The profit earned by the retailer from its normal business operations.")
    st.write("• Sales Method: The approach or channel used by the retailer to sell its products or services.")
    
elif selected == "Data Analysis":
    with st.sidebar:
        choose5 = option_menu("Menu", ["KPI","Sales Performance by Product","Retailer Sales Comparison" ,"Time Series Analysis",'Efficiency of Sales Methods','Regional Market Analysis-I','Regional Market Analysis-II'],
            #icons=['dot', 'dot', 'dot','dot','dot','dot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "blue", "font-size": "23px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#C9CAFF"},
         })


    if choose5 == "KPI":
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Key Performance Indicators</h1>', unsafe_allow_html=True)
        year_options = ['All'] + sorted(data['Invoice Date'].dt.year.unique().tolist())
        selected_year = st.selectbox('Select Year:', year_options,index=0)
        month_options = ['All'] + sorted(data['Invoice Date'].dt.month.unique().tolist())
        selected_month = st.selectbox('Select Month:', month_options,index=0)

        # Filter data based on selected year and month
        filtered_data = data.copy()
        if selected_year != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.year == selected_year]
        if selected_month != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.month == selected_month]

        #Calculate total revenue
        total_revenue = filtered_data['Total Sales'].sum()

        # Calculate total products sold
        total_products_sold = filtered_data.shape[0]

        total_profit = (filtered_data['Total Sales'].sum() - filtered_data['Operating Profit'].sum())
        total_units_sold = round(filtered_data['Units Sold'].sum())
        average_profit = total_profit / total_units_sold

        # Define color based on total revenue
        revenue_color = "green" if total_revenue > 1000000 else "red"

        # Define color based on total products sold
        products_sold_color = "blue" 
        profit_color = 'purple'
        average_profit_color = 'teal'
        # Create two columns for displaying the metrics side by side
        col1, col2 , col3 = st.columns(3)

        # Display total revenue
        with col1:
            st.markdown(f'<div style="background-color: #f0f0f5; padding: 15px; border-radius: 5px;">\
                            <p style="font-size: 18px; color: #333333; text-align: center;">Total Revenue</p>\
                            <p style="font-size: 24px; color: {revenue_color}; font-weight: bold; text-align: center;">{total_revenue:.2f}</p>\
                            <div style="display: flex; justify-content: center;">\
                                <img src="https://img.icons8.com/ios-filled/50/{revenue_color}/money-bag.png"/>\
                            </div>\
                        </div>', unsafe_allow_html=True)

        # Display total products sold
        with col2:
            st.markdown(f'<div style="background-color: #f0f0f5; padding: 15px; border-radius: 5px;">\
                            <p style="font-size: 18px; color: #333333; text-align: center;">Total Products Sold</p>\
                            <p style="font-size: 24px; color: {products_sold_color}; font-weight: bold; text-align: center;">{total_products_sold}</p>\
                            <div style="display: flex; justify-content: center;">\
                                <img src="https://img.icons8.com/ios-filled/50/{products_sold_color}/box.png"/>\
                            </div>\
                        </div>', unsafe_allow_html=True)

        with col3:
            st.markdown(f'<div style="background-color: #f0f0f5; padding: 15px; border-radius: 5px;">\
                            <p style="font-size: 18px; color: #333333; text-align: center;">Total Units Sold</p>\
                            <p style="font-size: 24px; color: {total_units_sold}; font-weight: bold; text-align: center;">{total_units_sold}</p>\
                            <div style="display: flex; justify-content: center;">\
                                <img src="https://img.icons8.com/ios-filled/50/{products_sold_color}/box.png"/>\
                            </div>\
                        </div>', unsafe_allow_html=True)

        st.write(" ")
        col3, col4  = st.columns(2)
        with col3:
            st.markdown(f'<div style="background-color: #f0f0f5; padding: 15px; border-radius: 5px;">\
                            <p style="font-size: 18px; color: #333333; text-align: center;">Total Profit</p>\
                            <p style="font-size: 24px; color: {profit_color}; font-weight: bold; text-align: center;">{total_profit:.2f}</p>\
                            <div style="display: flex; justify-content: center;">\
                                <img src="https://img.icons8.com/ios-filled/50/{profit_color}/money-bag.png"/>\
                            </div>\
                        </div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div style="background-color: #f0f0f5; padding: 15px; border-radius: 5px;">\
                            <p style="font-size: 18px; color: #333333; text-align: center;">Average Profit</p>\
                            <p style="font-size: 24px; color: {average_profit_color}; font-weight: bold; text-align: center;">{average_profit:.4f}</p>\
                            <div style="display: flex; justify-content: center;">\
                                <img src="https://img.icons8.com/ios-filled/50/{average_profit_color}/money-bag.png"/>\
                            </div>\
                        </div>', unsafe_allow_html=True)




    if choose5 == "Sales Performance by Product":
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Sales Performance Analysis : Which products are generating the highest sales revenue ?</h1>', unsafe_allow_html=True)
     
        year_options = ['All'] + sorted(data['Invoice Date'].dt.year.unique().tolist())
        selected_year = st.selectbox('Select Year:', year_options,index=0)
        month_options = ['All'] + sorted(data['Invoice Date'].dt.month.unique().tolist())
        selected_month = st.selectbox('Select Month:', month_options,index=0)

        # Filter data based on selected year and month
        filtered_data = data.copy()
        if selected_year != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.year == selected_year]
        if selected_month != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.month == selected_month]
        
        expander = st.expander("View Data for Top and Underperforming Products by Total Sales")
        result0 = filtered_data.groupby(by="Product")["Total Sales"].sum().reset_index()
        data0 = result0
        expander.write(data0)
        fig1 = px.bar(result0, x="Product", y="Total Sales", title="Bar chart of products Performance by Total Sales", 
              template="gridon")
        #fig1.update_layout(yaxis=dict(tickmode='array', tickvals=result0["Total Sales"]))
        st.plotly_chart(fig1, use_container_width=True)
    
        
       
    if choose5 == "Retailer Sales Comparison":
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Comparing Sales Performance of Major Retailers</h1>', unsafe_allow_html=True)
        year_options = ['All'] + sorted(data['Invoice Date'].dt.year.unique().tolist())
        selected_year = st.selectbox('Select Year:', year_options,index=0)
        month_options = ['All'] + sorted(data['Invoice Date'].dt.month.unique().tolist())
        selected_month = st.selectbox('Select Month:', month_options,index=0)

        # Filter data based on selected year and month
        filtered_data = data.copy()
        if selected_year != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.year == selected_year]
        if selected_month != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.month == selected_month]

        with st.expander("View Data for Retailers Wise Sales"):
            retailer_sales = filtered_data.groupby("Retailer")["Total Sales"].sum()
            st.write(retailer_sales)
       
        fig = px.bar(filtered_data, x = "Retailer", y = "Total Sales", labels={"Total Sales" : "Total Sales"},
        title = "Bar Chart of Total Sales by Retailer", hover_data=["Total Sales"],template="gridon",
        height=500)
        st.plotly_chart(fig,use_container_width=True)
        


    if choose5 == 'Time Series Analysis':
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Which months or years had the highest and lowest sales figures?</h1>', unsafe_allow_html=True)
        data['Invoice Date'] = pd.to_datetime(data['Invoice Date'])
        monthly_sales = data.groupby(data['Invoice Date'].dt.to_period('M'))['Total Sales'].sum()
        monthly_sales.index = monthly_sales.index.to_timestamp()
        #sns.set_style("whitegrid")
        fig, ax = plt.subplots(figsize=(11, 7))
        ax.plot(monthly_sales.index, monthly_sales.values, marker='o', color='#234990', linestyle='-', linewidth = 4)
        ax.set_xlabel('Month', fontsize=17)
        ax.set_ylabel('Total Sales', fontsize=17)
        ax.set_title('Monthly Sales Trends', fontsize=19)
        plt.xticks(rotation=45, fontsize = 17)
        plt.yticks(fontsize = 17)
        st.pyplot(fig)
       


    if choose5 == 'Efficiency of Sales Methods':
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Efficiency of Sales Methods: Which Sales Method Generates the Most Sales?</h1>', unsafe_allow_html=True)
        year_options = ['All'] + sorted(data['Invoice Date'].dt.year.unique().tolist())
        selected_year = st.selectbox('Select Year:', year_options)
        month_options = ['All'] + sorted(data['Invoice Date'].dt.month.unique().tolist())
        selected_month = st.selectbox('Select Month:', month_options)

        # Filter data based on selected year and month
        filtered_data = data.copy()
        if selected_year != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.year == selected_year]
        if selected_month != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.month == selected_month]

        sales_method_grouped = filtered_data.groupby('Sales Method').agg({'Total Sales': 'sum', 'Operating Profit': 'sum'})
        sales_method_grouped['Operating Margin'] = (sales_method_grouped['Operating Profit'] / sales_method_grouped['Total Sales'])
        #st.subheader("Sales Performance by Sales Method")
        st.dataframe(sales_method_grouped.style.format("{:.2%}", subset=["Operating Margin"]))
          # Format the Operating Margin column as a percentage
        best_method = sales_method_grouped.sort_values(by="Operating Margin", ascending=False).index[0]
      
        fig1 = px.pie(sales_method_grouped, values='Total Sales', names=sales_method_grouped.index, title='Total Sales by Sales Method')
        fig2 = px.pie(sales_method_grouped, values='Operating Profit', names=sales_method_grouped.index, title='Operating Profit by Sales Method')
        #fig3 = px.pie(sales_method_grouped, values='Operating Margin', names=sales_method_grouped.index, title='Operating Margin by Sales Method')
        col1, col2= st.columns([1,1])
        with col1:
            st.plotly_chart(fig1,use_container_width=True)
        with col2:
            st.plotly_chart(fig2,use_container_width=True)
        

      

    if choose5 == "Regional Market Analysis-I":
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Regional Market Analysis: Which regions are experiencing strong sales, and which ones are lagging?</h1>', unsafe_allow_html=True)
        year_options = ['All'] + sorted(data['Invoice Date'].dt.year.unique().tolist())
        selected_year = st.selectbox('Select Year:', year_options)
        month_options = ['All'] + sorted(data['Invoice Date'].dt.month.unique().tolist())
        selected_month = st.selectbox('Select Month:', month_options)

        # Filter data based on selected year and month
        filtered_data = data.copy()
        if selected_year != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.year == selected_year]
        if selected_month != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.month == selected_month]

        result5 = filtered_data.groupby(by="State")[["Total Sales","Units Sold"]].sum().reset_index()
        expander = st.expander("View Data for Total Sales by States")
        expander.write(result5)
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x = result5["State"], y = result5["Total Sales"], name = "Total Sales"))
        #fig3.add_trace(go.Scatter(x=result5["State"], y = result5["Units Sold"], mode = "lines",
                          # name ="Units Sold", yaxis="y2"))
        fig3.update_layout(
        title = "Total Sales by State",
        xaxis = dict(title="State"),
        yaxis = dict(title="Total Sales", showgrid = False),
        #yaxis2 = dict(title="Units Sold", overlaying = "y", side = "right"),
        template = "gridon",
        legend = dict(x=1,y=1.1))
        st.plotly_chart(fig3,use_container_width=True)


        result21 = filtered_data[["Region","City","Total Sales"]].groupby(by=["Region","City"])["Total Sales"].sum()
        expander = st.expander("View data for Total Sales by Region and City")
        expander.write(result21)
        treemap = filtered_data[["Region","City","Total Sales"]].groupby(by = ["Region","City"])["Total Sales"].sum().reset_index()
        def format_sales(value):
            if value >= 0:
                return '{:.2f} Lakh'.format(value / 1_000_00)

        treemap["Total Sales (Formatted)"] = treemap["Total Sales"].apply(format_sales)

        fig7 = px.treemap(treemap, path = ["Region","City"], values = "Total Sales",
                  hover_name = "Total Sales (Formatted)",
                  hover_data = ["Total Sales (Formatted)"],
                  color = "City", height = 700, width = 600)
        fig7.update_traces(textinfo="label+value")
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">Total Sales by Region and City in Treemap</h1>', unsafe_allow_html=True)  
        st.plotly_chart(fig7,use_container_width=True)
        



    if choose5 == 'Regional Market Analysis-II':
        st.markdown(f'<h1 style="font-size:20px; font-weight:bold;">How does sales performance vary across different geographical regions?</h1>', unsafe_allow_html=True)
        year_options = ['All'] + sorted(data['Invoice Date'].dt.year.unique().tolist())
        selected_year = st.selectbox('Select Year:', year_options)
        month_options = ['All'] + sorted(data['Invoice Date'].dt.month.unique().tolist())
        selected_month = st.selectbox('Select Month:', month_options)

        # Filter data based on selected year and month
        filtered_data = data.copy()
        if selected_year != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.year == selected_year]
        if selected_month != 'All':
            filtered_data = filtered_data[filtered_data['Invoice Date'].dt.month == selected_month]
        def get_state_abbreviations(state_column):
            state_abbreviations = []
            for state in state_column:
                try:
                    state_abbreviation = states.lookup(state).abbr
                except AttributeError:
                    state_abbreviation = None
                state_abbreviations.append(state_abbreviation)
            return state_abbreviations
        filtered_data['State Abbreviation'] = get_state_abbreviations(filtered_data['State'])
        filtered_data['Total Sales'] = filtered_data['Total Sales'].replace('[\$,]', '', regex=True).astype(float)
        fig = go.Figure()
        products = filtered_data['Product'].unique()
        sales_methods = filtered_data['Sales Method'].unique()
        for product in products:
            for method in sales_methods:
                filtered_df = filtered_data[(filtered_data['Product'] == product) & (filtered_data['Sales Method'] == method)]
                state_sales = filtered_df.groupby('State Abbreviation')['Total Sales'].sum().reset_index()
                fig.add_trace(
                go.Choropleth(
                locations=state_sales['State Abbreviation'],
                z=state_sales['Total Sales'],
                locationmode='USA-states',
                colorscale='Viridis',
                name=f"{product} - {method}",
                showscale=True,
                visible=False  # Initially, all traces are hidden
            )
        )
        product_buttons = [
        {'label': product, 'method': 'update', 'args': [{'visible': [trace.name.startswith(product) for trace in fig.data]}]}
        for product in products
        ]   

        sales_method_buttons = [
        {'label': method, 'method': 'update', 'args': [{'visible': [method in trace.name for trace in fig.data]}]}
        for method in sales_methods
        ]

        fig.update_layout(
            updatemenus=[
            {'buttons': product_buttons, 'direction': 'down', 'showactive': True, 'x': 0.25, 'xanchor': 'left', 'y': 1.15,
            'yanchor': 'top'},
            {'buttons': sales_method_buttons, 'direction': 'down', 'showactive': True, 'x': 0.75, 'xanchor': 'left', 'y': 1.15,
            'yanchor': 'top'}
            ],
            geo=dict(scope='usa'),
            title="Total Sales by State, Product, and Sales Method"
        )
        if fig.data:
            fig.data[0].visible = True
        st.plotly_chart(fig)
       