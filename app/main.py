from fastapi import FastAPI

app = FastAPI(title="AI Support Intelligence Platform")

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/version")
def get_version():
    return {"version": "0.0.1"}