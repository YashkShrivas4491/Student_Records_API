# Student Management System - Backend APIs

This repository contains the backend APIs for a **Student Management System**. It is built using **FastAPI** and integrates with **MongoDB Atlas** for data storage.

## Tech Stack

- **Programming Language**: Python  
- **Framework**: FastAPI  
- **Database**: MongoDB Atlas (M0 Free Cluster)  
- **Deployment Options**: AWS EC2, Render, GCP, or other cloud services  

## Features

- **CRUD Operations**: Create, Read, Update, and Delete student records.
- **Query Filtering**: Search students by specific parameters such as `country` and `age`.
- **Schema Validation**: Validates input requests and ensures proper response formats.
- **RESTful API Design**: Follows HTTP standards with appropriate status codes.

## API Endpoints

### Base URL

`https://student-records-api.onrender.com`

### Endpoints

| **Method** | **Endpoint**           | **Description**                           | **Status Code** |
|------------|------------------------|-------------------------------------------|-----------------|
| `POST`     | `/students`            | Add a new student record                  | `201`           |
| `GET`      | `/students`            | List all students with optional filters   | `200`           |
| `GET`      | `/students/{id}`       | Retrieve a student by their unique ID     | `200`           |
| `PATCH`    | `/students/{id}`       | Update an existing student record         | `204`           |
| `DELETE`   | `/students/{id}`       | Delete a student by their unique ID       | `200`           |

## Environment Variables

To run this project, you will need to set up the following environment variable in a `.env` file:

```plaintext
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>?retryWrites=true&w=majority
