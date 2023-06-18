import streamlit as st 

st.title('Demand - Driven Supply Optimization for  Noodles -- Leveraging  Data  Analytics to  Enhance  Inventory  Management  and  Profitability for FMCG Company ')   # Title Generation
st.header('- Machine Learning Approach')
st.subheader('------------------------------------------------------------------------------')
st.subheader('Author : CHANDAN D. CHAUDHARI')
st.subheader('Github Link : https://github.com/chandanc5525/SupplyChain_BusinessModel')
st.subheader('------------------------------------------------------------------------------')
st.markdown("""### Business Scenario: 
A Fast Moving Consumer Goods (FMCG) company has entered into the instant noodles business two years back. Their higher 
management  has  notices  that  there  is  a  miss  match  in  the  demand  and  supply. 
Where  the  demand  is  high,  supply  is  low  and  vice-versa  which  as  a  result  as  a 
loss  in  inventory  cost  and  ultimately  loss  to  the  company.  Hence,  the  higher 
management wants to optimize the supply quantity in each warehouse in entire 
country. 
 
### Goal  &  Objective:  
The  objective  of  this  exercise  is  to  build  a  model,  using 
historical  data  that  will  determine  demand  pattern  and  optimum  weight  of  the 
product to ship each time from the respective warehouse. """)   
st.subheader('------------------------------------------------------------------------------')
st.markdown('### Dataset :')
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  

URL = 'https://raw.githubusercontent.com/chandanc5525/SupplyChain_BusinessModel/main/Dataset/SCM.csv'
df = pd.read_csv(URL)
print(df)

st.dataframe(df,width= 5000,height = 500)
st.subheader('------------------------------------------------------------------------------')
st.markdown('### Feature Selection :')

plt.bar(df['zone'],df['product_wg_ton'])
plt.xlabel('Zone')
plt.ylabel('Product weight in Tons')
st.pyplot()
plt.bar(df['zone'],df['product_wg_ton'])
plt.xlabel('Zone')
plt.ylabel('Product weight in Tons')
st.pyplot()