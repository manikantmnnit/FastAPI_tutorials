def main():
    print("Hello from http-methods!")

import fastapi
from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello learners!"}

@app.get('/about')
def read_about():
    return  "This is a simple API to demonstrate HTTP methods."

def view_csv():
    df = pd.read_csv('1000_ml_jobs_us.csv')
    return df.sample(5)  

@app.get('/view_data')  # lowercase URLs are preferred
def view_data():
    data = view_csv()
    return data.to_dict(orient="records") 
def company_list():
    df = pd.read_csv('1000_ml_jobs_us.csv')
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
