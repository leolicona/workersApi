from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel


class WorkerSchema(BaseModel):
    id: int
    name: str
    position: str
    status: str


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
def worker(id: int):
    for worker in workers_list["data"]:
        if worker["id"] == id:
            return worker
    return {"status": "error", "message": "Worker not found"}

@app.get("/workers/")
def workerByQuery(position: str):
    filtered_workers = []
    for worker in workers_list["data"]:
        if worker["position"] == position:
            filtered_workers.append(worker)
    return filtered_workers

@app.post("/workers")
def createWorker(workerSchema: WorkerSchema):
    workers_list["data"].append(workerSchema)
    return workers_list

@app.put("/workers/{id}")
def updateWorker(id: int, workerSchema: WorkerSchema):
    for worker in workers_list["data"]:
        if worker["id"] == id:
            worker["name"] = workerSchema.name
            worker["position"] = workerSchema.position
            worker["status"] = workerSchema.status
            return worker

@app.delete("/workers/{id}")
def deleteWorker(id: int):
    for worker in workers_list["data"]:
        if worker["id"] == id:
            workers_list["data"].remove(worker)
            return workers_list
    return {"status": "error", "message": "Worker not found"}
  


    
