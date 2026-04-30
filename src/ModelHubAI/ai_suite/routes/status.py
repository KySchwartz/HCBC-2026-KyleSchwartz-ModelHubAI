from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Suite is Online"}

@app.get("/status")
def get_status():
    # Show online status
    return {"status": "online", "version": "1.0.0"}