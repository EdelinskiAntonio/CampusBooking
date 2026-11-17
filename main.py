from fastapi import FastAPI

app = FastAPI(title="CampusBooking")


@app.get("/health")
async def health():
    return {"status": "ok", "aplikacija": "CampusBooking"}