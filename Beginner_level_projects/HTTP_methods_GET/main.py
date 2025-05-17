def main():
    print("Hello from http-methods!")

import fastapi
from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
app=FastAPI()
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


df = pd.read_csv('1000_ml_jobs_us.csv')
df.drop(columns=['Unnamed: 0'], inplace=True)
df.dropna(inplace=True)


@app.get('/')
def read_about():
    return  "This is a simple API to demonstrate HTTP methods."


@app.get('/view')  # lowercase URLs are preferred
def view_data():
    # Convert the DataFrame to a dictionary
    
    data = df.to_dict(orient="records")
    
    return data
# show job pasting using company_address_region

@app.get('/view/{company_address_region}')
def view_data_by_region(company_address_region: str):
    filtered = df[df['company_address_region'].str.lower() == company_address_region.lower()]

    # Select desired columns
    filtered = filtered[['company_name', 'company_website', 'company_address_locality',
                          'job_posted_date', 'job_title', 'seniority_level']]

    return jsonable_encoder(filtered.to_dict(orient="records"))
    

@app.get("/view_job_title")
def view_data_by_job_title():
   
    df['job_title'] = df['job_title'].astype(str)
    unique_titles = df['job_title'].unique().tolist()
    return {"unique_job_titles": unique_titles}

@app.get("/search_job_titles/{keyword}")
def search_job_titles(keyword: str):
        
    
    df['job_title'] = df['job_title'].astype(str)
    
    # Filter using contains (case-insensitive, and handle NaNs)
    filtered = df[df['job_title'].str.contains(keyword, case=False, na=False)]
    
    filtered = filtered[['job_title', 'company_name', 'company_address_locality', 'job_posted_date']]
    return jsonable_encoder(filtered.to_dict(orient="records"))

def company_list():
    
    comp_list=df['company_name'].unique()
    return comp_list

@app.get('/companies')
def get_company_list():
    data = company_list()
    return data.tolist()

@app.get('/companies/{company_name}')
def get_company_jobs(company_name: str):
    df = pd.read_csv('1000_ml_jobs_us.csv')
    company_jobs = df[df['company_name'] == company_name]
    if company_jobs.empty:
        return {"message": "No jobs found for this company."}
        
    return company_jobs[['job_posted_date','company_address_locality','seniority_level','job_title']].to_dict(orient="records")


if __name__ == "__main__":
    main()
