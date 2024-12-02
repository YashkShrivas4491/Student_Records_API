from fastapi import FastAPI
from . import students

app = FastAPI(
    title="Student Management System",
    description="APIs for managing student records",
)

app.include_router(students.router)

@app.get("/", response_model=str)
def read_root():
    return "Backend is running ✅"

def startup_db_client():
    # Optionally, initialize MongoDB client here if needed
    print("Application started. MongoDB connection established.")

def shutdown_db_client():
    # Clean up MongoDB client or close any connections if necessary
    print("Application shutdown. MongoDB connection closed.")

# Register the functions as event handlers
app.add_event_handler("startup", startup_db_client)
app.add_event_handler("shutdown", shutdown_db_client)
