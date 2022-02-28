#!/usr/bin/env python
# coding: utf-8

# In[113]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv ('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', index_col="order_id")


# In[27]:


df.head()


# In[86]:


number_of_shops=df['shop_id'].nunique()
print("Total number of sneakers shops" + str(), number_of_shops)

AOV = round(df['order_amount'].sum()/len(df), 2)
print("Average order value (AOV) of the sneaker shops is" + str(), AOV)
df.head()


# # Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.
# 
# Ans: The value of order_amount as visualized by the box plot below shows in order to find the problem. By calculating the quantile of the order amount, we can see 50% of the sneaker sold were around $284. 
# 
# order amount and total items features are correlated meaning high amount equals high number of sneakers sold.Thats why the average value not seemed right.
#  

# In[115]:


Correlation_order_amount_total_items = round(df['order_amount'].corr(df['total_items']))
print("Order amount and total items has correlation" + str(), Correlation_order_amount_total_items)
                                             
Quantile_order_amount = round(df['order_amount'].quantile(), 2)
print('the quantile of order amount is $' + str(), Quantile_order_amount)


plt.boxplot(df['order_amount'], showfliers=False)
plt.show()


# # What metric would you report for this dataset?
# 
# Ans: I would recommend to analyze the most sold item from each shop and work on that range items. It helps to increase revenue.

# In[112]:


df['order_amount'].mode()


# # What is its value?
# 
# Ans: $ 153 sneeker most frquently sold item. Its very practical becasue everyone likes sneaker but everyone is not rich. 
