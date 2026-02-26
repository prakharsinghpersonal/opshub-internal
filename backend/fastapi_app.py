"""
OpsHub Python Backend
=====================
FastAPI and PostgreSQL backend specifically designed for tracking 
cross-team engineering metrics and human resource workflows.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Health check for the Python OpsHub API."""
    return {"status": "success", "message": "OpsHub Internal FastAPI Backend Running"}
