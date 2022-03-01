#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs Maq

# ### Importing csv library to import the data to my notebook

# In[52]:


import csv


# ### Creating different lists to store the data in.

# In[53]:


children = []
ages = []
bmi = []
sex = []
location = []
charges = []
smoker = []


# ### Importing the data from the CSV to my lists.

# In[54]:


with open("insurance.csv") as insurance_data:
    data_imported = csv.DictReader(insurance_data)
    for data in data_imported:
        ages.append(int(data['age']))
        sex.append(data['sex'])
        bmi.append(float(data['bmi']))
        children.append(int(data['children']))
        smoker.append(data['smoker'])
        location.append(data['region'])
        charges.append(float(data['charges']))


# ### Changing my smoker/sex lists to numbers for easy analysis

# In[55]:


smoker = [1 if smoke == 'yes' else 0 for smoke in smoker]


# In[56]:


sex = [1 if gen == 'male' else 0 for gen in sex]


# ### Created a Patient class that will store the information of each patient and have methods that will help me with my analysis

# In[106]:


class Patient:
    def __init__(self, my_sex, my_bmi, smoke, my_location, my_charges, my_children, age):
        self.my_sex = my_sex
        self.my_bmi = my_bmi
        self.smoke = smoke
        self.my_location = my_location
        self.my_charges = my_charges
        self.my_children = my_children
        self.age = age
    
    def estimated_cost(self):
        return 250 * self.age - 128 * self.my_sex + 370 * self.my_bmi + 425 * self.my_children + 24000 * self.smoke - 12500
    
    def calculate_diff(self):
        return abs(self.estimated_cost() - self.my_charges)


# ### Empty patients list to later store patient objects

# In[107]:


patients = []


# ### Function to create patients incase the data changes and we have an increase in patinets

# In[108]:


def create_patients():
    for i in range(len(ages)):
        patients.append(Patient(sex[i], bmi[i], smoker[i], location[i], charges[i], children[i],ages[i]))
    


# In[109]:


create_patients()


# ### 3 Functions that I have used for my analysis. Finding the average charges, average bmi, and average difference.
# 
# - We can see that from the first function, that many people are charged higher than 13K dollars.
# 
# - In the second function, we can see that many of the patients are actually obese or close to it.
# 
# - Finally, we can see that the actual accuracy of predicting your insurance charges is difficult, since theres a +/- 4400K dollars in difference from the predicted formula

# In[110]:


def avg_charges():
    total = 0
    for patient in patients:
        total += patient.my_charges
        
    return total/len(patients)


# In[111]:


avg_charges()


# In[112]:


def avg_bmi():
    total = 0
    for patient in patients:
        total += patient.my_bmi
        
    return total/len(patients)


# In[113]:


avg_bmi()


# In[115]:


def avg_diff():
    total = 0
    for patient in patients:
        total += patient.calculate_diff()
        
    return total/len(patients)


# In[116]:


avg_diff()


# ### I hope you found my analysis useful
