from fastapi import APIRouter, HTTPException, Query
from bson import ObjectId
from typing import Optional, List, Dict, Any
from schemas import StudentCreate, StudentUpdate, StudentResponse
from database import get_students_collection

router = APIRouter(prefix="/students", tags=["Students"])
students_collection = get_students_collection()


@router.post("/", response_model=Dict[str, str], status_code=201)
def create_student(student: StudentCreate):
    student_dict = student.model_dump()
    result = students_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}



@router.get("/", response_model=Dict[str, List[Dict[str, Any]]])
def list_students(country: Optional[str] = Query(None), age: Optional[int] = Query(None)):
    query_filter = {}
    if country:
        query_filter['address.country'] = country
    if age:
        query_filter['age'] = {'$gte': age}
    students = list(students_collection.find(query_filter))
    for student in students:
        student['id'] = str(student['_id'])
        del student['_id']
    return {"data": students}



@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: str):
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student['id'] = str(student['_id'])
    del student['_id']
    return student



@router.patch("/{student_id}", status_code=204)
def update_student(student_id: str, student_update: StudentUpdate):
    update_data = {k: v for k, v in student_update.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")
    result = students_collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")



@router.delete("/{student_id}", status_code=200)
def delete_student(student_id: str):
    result = students_collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
