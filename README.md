## FastAPI Iris Classification Project

Overview
In this project, we expose a machine learning model as an API using FastAPI and uvicorn.

1. FastAPI: A modern and high-performance web framework for building APIs in Python.
2. Uvicorn: An ASGI (Asynchronous Server Gateway Interface) web server used to serve FastAPI applications.

The workflow involves the following steps:

1. Training a Random Forest Classifier on the Iris Dataset.
2. Saving the trained model in pickle format.
3. Serving the trained model as an API using FastAPI and uvicorn.

---

Project Structure

mlops\_labs
└── fastapi\_lab
├── assets/
├── fastapi\_lab\_env/
├── model/
│   └── iris\_model.pkl
├── src/
│   ├── **init**.py
│   ├── data.py
│   ├── main.py
│   ├── predict.py
│   └── train.py
├── README.txt
└── requirements.txt

Note:

* fastapi\[all] in requirements.txt will also install uvicorn.

---

Running the Project

Step 1: Create and activate a virtual environment.
Step 2: Install the required packages using:
pip install -r requirements.txt

Step 3: Train the Random Forest Classifier. From inside the src/ folder, run:
python train.py

This will train the Random Forest model on the Iris dataset and save the trained model as iris\_model.pkl inside the model folder.

Step 4: Run the FastAPI application with:
uvicorn main\:app --reload

Step 5: Test the API endpoints.
Open your browser and go to:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
or
[http://localhost:8000/docs](http://localhost:8000/docs)

Here you can test out the endpoints interactively.

---

FastAPI Syntax

* The FastAPI application instance is created as:
  app = FastAPI()

* To run the application:
  uvicorn main\:app --reload

* The --reload flag allows automatic reloading when code changes.

* Functions used as API endpoints are defined with decorators like:
  @app.get("/endpoint")
  @app.post("/endpoint")

---

Data Models in FastAPI

1. IrisData class
   Defines the input format for prediction:

   class IrisData(BaseModel):
   petal\_length: float
   sepal\_length: float
   petal\_width: float
   sepal\_width: float

2. IrisResponse class
   Defines the format of the response:

   class IrisResponse(BaseModel):
   response: int

---

FastAPI Features

1. Request Body Reading: FastAPI reads the request body as JSON automatically.
2. Data Conversion: Pydantic models convert JSON into proper Python data types.
3. Data Validation: Ensures data types and required fields are correct.
4. Error Handling: Handled using HTTPException.

Example:

```
from fastapi import FastAPI, HTTPException  

app = FastAPI()  

@app.get("/items/{item_id}")  
async def read_item(item_id: int):  
    if item_id <= 0:  
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")  
    return {"item_id": item_id}  
```

If no valid item is found, the response will look like:
{ "detail": "Item with ID 1 not found" }

---

Summary

* We trained a Random Forest Classifier on the Iris dataset.
* The trained model was saved as iris\_model.pkl.
* We exposed the model as an API using FastAPI and uvicorn.
* The API accepts Iris flower features and predicts the class.

