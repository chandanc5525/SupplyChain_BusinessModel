import streamlit as st 
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import pickle




rad = st.sidebar.radio("NAVIAGTION",["PROJECT INFO","DATASET","VISUALIZATION","MODEL BUILDING"])


if rad == "PROJECT INFO":
    st.title('Demand - Driven Supply Optimization for  Noodles -- Leveraging  Data  Analytics to  Enhance  Inventory  Management  and  Profitability for FMCG Company ')   # Title Generation
    st.header('- Machine Learning Approach')
    st.subheader('------------------------------------------------------------------------------')
    st.subheader('Author : CHANDAN D. CHAUDHARI')
    st.subheader('Github Link : https://github.com/chandanc5525/SupplyChain_BusinessModel')
    st.subheader('------------------------------------------------------------------------------')
    st.markdown("""### Business Scenario: 
    A Fast Moving Consumer Goods (FMCG) company has entered into the instant noodles business two years back. 
    Their higher management  has  notices  that  there  is  a  miss  match  in  the  demand  and  supply. Where  the  demand  is  high,  supply  is  low  and  vice-versa  which  as  a  result  as  a 
    loss  in  inventory  cost  and  ultimately  loss  to  the  company.  Hence,  the  higher management wants to optimize the supply quantity in each warehouse in entire country.""")
    
    st.markdown("""### Goal  &  Objective:  
    The  objective  of  this  exercise  is  to  build  a  model,  using historical  data  that  will  determine  demand  pattern  and  optimum  weight  of  the 
    product to ship each time from the respective warehouse. """)   
    st.subheader('------------------------------------------------------------------------------')

if rad == "DATASET":
    st.subheader('------------------------------------------------------------------------------')
    st.markdown('### Dataset :')
    import pandas as pd  
    import numpy as np
    import matplotlib.pyplot as plt 
    import seaborn as sns 
    URL = 'https://raw.githubusercontent.com/chandanc5525/SupplyChain_BusinessModel/main/Dataset/SCM.csv'
    df = pd.read_csv(URL)
    print(df)

    st.dataframe(df,width= 9000,height = 500)
    st.subheader('------------------------------------------------------------------------------')

if rad == "VISUALIZATION":
    st.markdown('### Bar Plot Visualization:')
    import pandas as pd  
    import numpy as np
    import matplotlib.pyplot as plt 
    import seaborn as sns 
    URL = 'https://raw.githubusercontent.com/chandanc5525/SupplyChain_BusinessModel/main/Dataset/SCM.csv'
    df = pd.read_csv(URL)
    
    fig,axes = plt.subplots(6,3,figsize = (20,30))
    sns.barplot(ax = axes[0][0],x = df['zone'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[0][1],x = df['Location_type'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[0][2],x = df['num_refill_req_l3m'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[1][0],x = df['transport_issue_l1y'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[1][1],x = df['distributor_num'][:10] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[1][2],x = df['Competitor_in_mkt'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[2][0],x = df['WH_capacity_size'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[2][1],x = df['WH_regional_zone'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[2][2],x = df['retail_shop_num'][:10] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[3][0],x = df['wh_owner_type'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[3][1],x = df['workers_num'][:10] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[3][2],x = df['dist_from_hub'][:10] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[4][0],x = df['flood_proof'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[4][1],x = df['flood_impacted'][:10] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[4][2],x = df['storage_issue_reported_l3m'][:10] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[5][0],x = df['temp_reg_mach'] , y = df['product_wg_ton'])
    sns.barplot(ax = axes[5][1],x = df['approved_wh_govt_certificate'], y = df['product_wg_ton'])
    sns.barplot(ax = axes[5][2],x = df['wh_est_year'][:15] , y = df['product_wg_ton'])
    plt.show()
    st.pyplot()
    st.subheader('------------------------------------------------------------------------------')
    st.markdown('### Count Plot Visualization:')

    fig,axes = plt.subplots(6,3,figsize = (20,30))
    sns.countplot(ax = axes[0][0],x = df['zone'])
    sns.countplot(ax = axes[0][1],x = df['Location_type'])
    sns.countplot(ax = axes[0][2],x = df['num_refill_req_l3m'])
    sns.countplot(ax = axes[1][0],x = df['transport_issue_l1y'])
    sns.countplot(ax = axes[1][1],x = df['distributor_num'][:10])
    sns.countplot(ax = axes[1][2],x = df['Competitor_in_mkt'])
    sns.countplot(ax = axes[2][0],x = df['WH_capacity_size'])
    sns.countplot(ax = axes[2][1],x = df['WH_regional_zone'])
    sns.countplot(ax = axes[2][2],x = df['retail_shop_num'][:10])
    sns.countplot(ax = axes[3][0],x = df['wh_owner_type'])
    sns.countplot(ax = axes[3][1],x = df['workers_num'][:10])
    sns.countplot(ax = axes[3][2],x = df['dist_from_hub'][:10])
    sns.countplot(ax = axes[4][0],x = df['flood_proof'])
    sns.countplot(ax = axes[4][1],x = df['flood_impacted'][:10])
    sns.countplot(ax = axes[4][2],x = df['storage_issue_reported_l3m'][:10])
    sns.countplot(ax = axes[5][0],x = df['temp_reg_mach'])
    sns.countplot(ax = axes[5][1],x = df['approved_wh_govt_certificate'])
    sns.countplot(ax = axes[5][2],x = df['wh_est_year'][:15])
    plt.show()
    st.pyplot()

    st.subheader('------------------------------------------------------------------------------')
    st.markdown('### Scatter Plot Visualization:')

    plt.figure(figsize=(15,9))
    col = st.sidebar.selectbox("Selection of A cloumn",df.columns)
    plt.scatter(df[col],df['product_wg_ton'])
    plt.ylabel('product_wg_ton')
    st.pyplot()
    
#if rad == "MODEL BUILDING":
    