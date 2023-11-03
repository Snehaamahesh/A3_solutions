#!/usr/bin/env python
# coding: utf-8

# # 1
# 

# In[81]:



import pandas as pd
df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\Students.csv")
df


# In[82]:


def studentinfo(students):
        df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\Students.csv")
        

        if df.empty:
            raise ValueError("The file is empty.")
     
        df['Name'] = df['Name'].str.strip()
        df['City'] = df['City'].str.strip()
        most_frequent_city = df['City'].mode().iloc[0]
        most_frequent_name = df['Name'].mode().iloc[0]
    
        df['City'].fillna(most_frequent_city, inplace=True)
        df['Name'].fillna(most_frequent_name, inplace=True)
        
   
        result = df.groupby('City')['Age'].mean().to_dict()
        
        return result


if __name__ == '__main__':
        print(studentinfo('students.csv'))


# In[ ]:


My Datafram-Student.CSV File
Name	Age	City
John	28	Chennai
Ram	24	Hyderabad
Alice	23	Bangalore
Bob	22	Chennai
Eve	25	Hyderabad
Ansh	29	Bangalore
Ankit	28	Chennai
Anjana	27	Hyderabad
Priya	24	Bangalore
Rani	30	Hyderabad
Sharma	21	Chennai


# # 2
# 
# 

# In[17]:


import pandas as pd
df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\ds_salaries (2).csv")
df


# In[18]:


df.columns


# In[41]:


import pandas as pd


def dssalary(dssalaries_file, expected_salary):
    df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\ds_salaries (2).csv")
    

    df = df[(df['employment_type'] == 'FT') & (df['job_title'] == 'Data Scientist') & (df['employee_residence'].str.strip() == 'CA') & (df['company_size'] == 'L')]
    df.dropna(inplace=True)
    average_salary = df['salary'].mean()
    
    
    if average_salary >= expected_salary:
        return "satisfied"
    else:
        return "unsatisfied"

# Example 1
result1 = dssalary('ds_salaries.csv', 90000)
print("Example 1:", result1)

# Example 2
#result2 = dssalary('ds_salaries.csv', 155555)
#print("Example 2:", result2)


# # 3
# 
# 

# In[50]:


import pandas as pd
df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\ds_salaries (2).csv")
df


# In[49]:


import pandas as pd

def increment(filename, salary_raise):

    df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\ds_salaries (2).csv")
    
    # Iterating through the rows of the DataFrame
    for index, row in df.iterrows():
        job_title = row['job_title']
        if job_title in salary_raise:

            increment_percentage = salary_raise[job_title]
            current_salary = row['salary']
            new_salary = current_salary * (1 + increment_percentage / 100)
            df.at[index, 'salary'] = new_salary

            exchange_rate = row['salary_in_usd'] / current_salary
            df.at[index, 'salary_in_usd'] = new_salary * exchange_rate
    

    return df

salary_raise = {
    'AI Developer': 10,
    'Data Analyst': 15,
    'Data Scientist': 20
}

updated_df = increment("ds_salaries", salary_raise)
updated_df


# # 4 
# 
# 

# In[45]:


import pandas as pd
df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\ds_salaries (2).csv")
df


# In[53]:



df = df.drop(columns=['remote_ratio','experience_level'])
df


# In[61]:


import pandas as pd

def preprocess(df):
    df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\ds_salaries (2).csv")

    df['work_year'] = pd.to_datetime(df['work_year'], format='%Y')
    start_date = pd.to_datetime('2020-01-01', format='%Y-%m-%d')
    end_date = pd.to_datetime('2021-01-01', format='%Y-%m-%d')
    

    df = df[(df['work_year'] >= start_date) & (df['work_year'] <= end_date)]
    return df


updated_df = preprocess(df)
updated_df


# # 5
# 
# 

# In[68]:


import pandas as pd
df1=pd.read_csv(r"C:\Users\sneha\Downloads\guvi\buddies.csv")
df1


# In[69]:


import pandas as pd
df2=pd.read_csv(r"C:\Users\sneha\Downloads\guvi\salary.csv")
df2


# In[78]:


import pandas as pd

def jobsearch(buddies_file, salary_file):

    buddies_df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\buddies.csv")
    salary_df = pd.read_csv(r"C:\Users\sneha\Downloads\guvi\salary.csv")
    merged_df = pd.merge(buddies_df, salary_df, on=['job_profile', 'location'])
    
    return merged_df


result = jobsearch('buddies.csv', 'salary.csv')
result


# In[ ]:





# In[ ]:





# In[ ]:




