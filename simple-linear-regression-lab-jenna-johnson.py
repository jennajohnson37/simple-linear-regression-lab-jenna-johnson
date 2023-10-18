#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Inputtting data
data_points = [

    (2000, 72.5),

    (2001, 73.1),

    (2002, 73.8),

    (2003, 74.2),

    (2004, 74.7),

    (2005, 75.3),

    (2006, 75.9),

    (2007, 76.5),

    (2008, 76.9),

    (2009, 77.4),

    (2010, 78.0),

    (2011, 78.5),

    (2012, 79.0),

    (2013, 79.5),

    (2014, 80.0),

    (2015, 80.5),

    (2016, 81.0),

    (2017, 81.5),

    (2018, 82.0),

    (2019, 82.5)
    
]


# In[16]:


def mean_calc(x):
    total = 0
    count = 0
    
    for year, expectancy in data_points:
        total += expectancy
        count += 1
        
    if count > 0:
        average = total / count
        return average
    else:
        return None


# In[17]:


mean_life = mean_calc(data_points)

print(f"Average Life Expectancy): {mean_life}")


# In[19]:


def regression_coefficients(data_points):
    x_sum = 0
    y_sum = 0
    n = len(data_points)
    
    for x, y in data_points:
        x_sum += x
        y_sum += y
        
        x_mean = x_sum / n
        y_mean = y_sum / n
        
        numerator = 0
        denominator = 0
        
        # Calculate the slope
        for x, y in data_points:
            numerator += (x - x_mean) * (y - y_mean)
            denominator += (x - x_mean) ** 2
            
            slope = numerator / denominator
            
        # Calculate the intercept
        intercept = y_mean - (slope * x_mean)
        
        return slope, intercept


# In[20]:


slope, intercept = regression_coefficients(data_points)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")


# In[14]:


# Making predictions
def predictions(data_point, slope, intercept):
    y_predicted = slope * data_point + intercept
    
    return y_predicted


# In[26]:


# Using the prediction formula
slope = 0.5221052631578948
intercept = -971.5305263157698

year_prediction = int(input("What year would you like to predict? "))

predicted_value = predictions(year_prediction, slope, intercept)

print(f"For x = {year_prediction}, the predicted life expectancy is {predicted_value}")


# In[ ]:




