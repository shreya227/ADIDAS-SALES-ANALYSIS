<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*T517FScjkArmfF2ezrp6vw.png" alt="Adidas Sales Analysis" width="250" height="170"> 

# **Adidas Sales Analysis**
### **Unraveling the Secrets of Adidas’ Sales Success**

Welcome to the Adidas Sales Analysis project! This repository contains a comprehensive analysis of Adidas' sales data, uncovering key insights and metrics that contribute to the brand's success.

### Project Overview:
This project aims to provide a thorough analysis of Adidas sales performance and market presence by developing an interactive Streamlit dashboard/GUI to visualize and present the analysis effectively. Utilizing a detailed dataset, the project explores various facets of the business, including sales trends, product popularity, regional market performance, and more.

To run this analysis locally, follow these steps:

1. Clone this repository:
    ```sh
    git clone https://github.com/shreya227/ADIDAS-SALES-ANALYSIS.git
    cd ADIDAS-SALES-ANALYSIS
    ```
    
2. Install packages `pip install requirements.txt`

      Requires
      ```
      pandas
      openpyxl>=3.1.0
      matplotlib==3.8.0
      numpy==1.23.2
      pandas==2.2.2
      Pillow==10.4.0
      plotly==5.9.0
      seaborn==0.13.2
      streamlit==1.30.0
      streamlit_option_menu==0.3.13
      streamlit_pills==0.3.0
      us==3.1.1
      altair==4.2.2
      streamlit-aggrid==1.0.5
      ```

3. Run the Streamlit application:
    ```sh
    streamlit run GUI.py
    ```

### Dataset Source 

* [Kaggle Dataset URL](https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset)
* [GitHub Dataset URL]()

## Exploratory Data Analysis:
### 1. Sales Performance Analysis : Which products are generating the highest sales revenue ?
  ![Uploading image.png…]()
  
#### **Key Insight:** 
Men’s Street Footwear emerges as the top-performing category with robust sales amounting to $208,826,244, highlighting a strong market preference. In contrast, Women’s Athletic Footwear shows a relatively lower performance, recording sales of $106,631,896.
This disparity suggests potential growth areas and indicates a need for targeted strategies to enhance the appeal of underperforming categories like Women’s Athletic Footwear.

##

### 2. Retailer Sales Comparison : Which retailer made the highest and least sales?
![image](https://github.com/user-attachments/assets/1004fc06-a032-4d85-94e5-b49b718f0cf6)
#### **Key Insight:** 
West Gear and Foot Locker emerged as the top-performing retailers. Retailer “West gear” made the highest purchases, contributing  to sales 242964333M, while retailer “Walmart” made the least sales of 74558410M.
Retailer Contribution: Analyzing sales by retailer allows us to identify the top-performing retailers and evaluate their contribution to overall revenue. This insight helps in building stronger partnerships with key retailers, optimizing distribution channels, and focusing marketing efforts on retailers that drive significant sales.
Identifying the retailers with the highest and least purchases help in understanding their impact on Adidas’ sales. This visualization aids in optimizing retailer relationships and resource allocation.

## 

### 3. Efficiency of Various Sales Methods: How does sales performance vary across different sales methods?
![image](https://github.com/user-attachments/assets/1f512bc6-2e09-499e-838b-2f1f88791efd)
#### **Key Insight:** 
1. In-store sales have the highest total sales, followed by outlet and then online sales.
2. Similar to total sales, in-store sales lead in operating profit, followed by outlet and then online.
    In terms of Total Sales and Operating Profit: In-store sales method is the most effective, generating the highest total sales and operating profit.
When deciding which sales method is more effective, it depends on what the business prioritizes. If the focus is on maximizing total revenue and profit, then in-store sales are more effective. However, if the focus is on efficiency in terms of profit generated per dollar of sales, then online sales are more effective.

## 

### 4. Time Series Analysis : Which months or years had the highest and lowest sales figures?
![image](https://github.com/user-attachments/assets/818f88d0-52de-4fb8-804d-1f1f34d85e00)
#### **Key Insight:** 
Monthly sales data from January 2020 to January 2022 exhibit significant variability with notable peaks around April 2021 and consistent increases in December and April of each year, potentially correlating with holiday seasons and sales promotions. The data show a general upward trend in sales over the two-year period, despite some notable dips, particularly in July 2020 and October 2021.

Insights:
The observed seasonal patterns, with sales spikes and dips, highlight the importance of understanding customer purchasing behavior and the impact of seasonality on sales. By leveraging these insights, businesses can align their marketing efforts, inventory management, and resource allocation with anticipated periods of high demand, ensuring that opportunities are maximized during peak seasons. This strategic approach can lead to better preparation for demand surges, improved customer satisfaction, and overall enhanced business performance.

## 

### 5. Regional Market Analysis-I: Which regions are experiencing strong sales, and which ones are lagging?
![image](https://github.com/user-attachments/assets/60f2e2fd-6a26-4dcc-9fc4-5878d6e2c121)
#### **Key Insight:** 
California and New York dominate in terms of total sales. The top performing State is New York with a total sales of $64,229,039, while the least performing State is Nebraska with a total sales of $5,929,038. Some states, like Texas, Florida, and Illinois, show moderate sales and units.

![image](https://github.com/user-attachments/assets/34791822-e135-4746-bd8d-67841014aca2)
#### **Key Insight:** 
The top performing Region is West with a total sales of $269,943,182, while the least performing Region Midwest is with a total sales of $135,800,459.

##


### 6. How does sales performance vary across different geographical regions?
![image](https://github.com/user-attachments/assets/4ceb9e27-ea28-4951-b047-df2c52202883)

#### **Key Insight:** 
This map is Demonstrating Total Sales by State, Product, and Sales Method in the US. A choropleth map is created using Plotly, with separate traces added for each unique product and sales method combination, showing total sales by U.S. state.
The layout is enhanced with dropdown menus for product and sales method selection, enabling interactive visualization of sales data across different categories and methods.
The final output is a dynamic, interactive visualization showing total sales across various states, differentiated by products and sales methods.

##

### Streamlit Dashboard






