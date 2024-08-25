from fastapi import FastAPI
from pydantic import BaseModel, Field, Path, Query
from fastapi.responses import JSONResponse

class WorkerSchema(BaseModel):
    id: int
    name: str = Field( min_length=3, max_length=20)
    position: str = Field( min_length=3, max_length=30) 
    status: str = Field( min_length=6, max_length=8)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Alice Johnson",
                "position": "Software Engineer",
                "status": "active"
            }
        }

workers_list = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "position": "Software Engineer",
            "status": "active"
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "position": "Project Manager",
            "status": "inactive"
        },
        {
            "id": 3,
            "name": "Charlie Brown",
            "position": "UX Designer",
            "status": "active"
        },
         {
            "id": 4,
            "name": "Charlie Brown",
            "position": "Scrum",
            "status": "active"
        },
        {
            "id": 5,
            "name": "Gorge Brown",
            "position": "Scrum",
            "status": "active"
        }
    ],
    "message": "Workers retrieved successfully"
}

app = FastAPI()

app.title = "My First FastAPI"
app.version = "0.0.1"

@app.get("/workers")
def workers():
    return workers_list


@app.get("/workers/{id}")
def worker(id: int = Path(ge=1, le=200)):
    for worker in workers_list["data"]:
        if worker["id"] == id:
            return JSONResponse(content=worker)
    return JSONResponse(content={"status": "error", "message": "Worker not found"})

@app.get("/workers/")
def workerByQuery(position: str = Query(min_length=3, max_length=30)):
    filtered_workers = []
    for worker in workers_list["data"]:
        if worker["position"] == position:
            filtered_workers.append(worker)
    return JSONResponse(content=filtered_workers)

@app.post("/workers")
def createWorker(workerSchema: WorkerSchema):
    workers_list["data"].append(workerSchema)
    return JSONResponse(content=workers_list)

@app.put("/workers/{id}")
def updateWorker(id: int, workerSchema: WorkerSchema):
    for worker in workers_list["data"]:
        if worker["id"] == id:
            worker["name"] = workerSchema.name
            worker["position"] = workerSchema.position
            worker["status"] = workerSchema.status
            return JSONResponse(content=worker)

@app.delete("/workers/{id}")
def deleteWorker(id: int):
    for worker in workers_list["data"]:
        if worker["id"] == id:
            workers_list["data"].remove(worker)
            return JSONResponse(content=workers_list)
    return JSONResponse(content={"status": "error", "message": "Worker not found"})
  


    
