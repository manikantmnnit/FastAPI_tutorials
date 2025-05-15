 Features
Basic GET API endpoints.

Reads a CSV file (1000_ml_jobs_us.csv) and returns:

Random sample job listings.

Unique company names.

Job listings for a specific company.

Returns data in JSON format using FastAPI response model.

| Method | Endpoint            | Description                              |
| ------ | ------------------- | ---------------------------------------- |
| GET    | `/`                 | Root route with welcome message          |
| GET    | `/about`            | Project description                      |
| GET    | `/view_data`        | View sample job listings (5 random rows) |
| GET    | `/companies`        | List all unique company names            |
| GET    | `/companies/{name}` | Job details for a specific company       |


| Step | Command / Description                                                               |
| ---- | ----------------------------------------------------------------------------------- |
| 1️⃣  | **Clone the repository**                                                            |
|      | `git clone https://github.com/yourusername/FastAPI_tutorials.git`                   |
|      | `cd FastAPI_tutorials/Beginner_level_projects/HTTP_methods`                         |
| 2️⃣  | **Create a new virtual environment**                                                |
|      | `uv env create`                                                                     |
| 3️⃣  | **Activate the environment**                                                        |
|      | `uv env activate`                                                                   |
| 4️⃣  | **Install dependencies**                                                            |
|      | `uv install fastapi uvicorn pandas numpy`                                           |
| 5️⃣  | **Run the FastAPI server using Uvicorn**                                            |
|      | `uv run uvicorn main:app --reload`                                                  |
| 6️⃣  | **Open browser to test**                                                            |
|      | `http://127.0.0.1:8000` for API root or `http://127.0.0.1:8000/docs` for Swagger UI |

