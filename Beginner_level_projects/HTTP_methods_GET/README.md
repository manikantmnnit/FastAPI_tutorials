# FastAPI Tutorials Series

This repository contains a series of projects built using **FastAPI**, designed to help learners progress from beginner to advanced levels.

---

## Project: HTTP Methods API

A simple FastAPI project demonstrating how to create APIs that interact with a CSV file containing job listings data. This project includes endpoints for viewing job data, listing companies, and filtering jobs by company.

---

## Setup Instructions (using `uv` CLI)

| Step | Command / Description                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------|
| 1️⃣    | **Clone the repository**                                                                             |
|       | `git clone https://github.com/yourusername/FastAPI_tutorials.git`                                    |
|       | `cd FastAPI_tutorials/Beginner_level_projects/HTTP_methods`                                          |
| 2️⃣    | **Create a new virtual environment**                                                                |
|       | `uv env create`                                                                                      |
| 3️⃣    | **Activate the environment**                                                                         |
|       | `uv env activate`                                                                                   |
| 4️⃣    | **Install dependencies**                                                                             |
|       | `uv install fastapi uvicorn pandas numpy`                                                           |
| 5️⃣    | **Run the FastAPI server using Uvicorn**                                                             |
|       | `uv run uvicorn main:app --reload`                                                                   |
| 6️⃣    | **Test the API in your browser or API client**                                                     |
|       | Visit: `http://127.0.0.1:8000` (root endpoint) or `http://127.0.0.1:8000/docs` (Swagger UI)          |

---

## Usage

- `/` : Root endpoint - simple greeting.
- `/about` : About this API.
- `/view_data` : View a random sample of job listings from CSV.
- `/companies` : List all unique companies in the dataset.
- `/companies/{company_name}` : Get job details for a specific company.

---

## Requirements

- Python 3.11+ (for `uv` CLI)
- FastAPI
- Uvicorn
- Pandas
- NumPy

---

## Author

Manikant - Open for contributions and feedback!

---

Feel free to open issues or submit pull requests for improvements!

