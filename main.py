from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import select

from models import Teams, get_session

app = FastAPI()

@app.get("/years")
async def get_years():
    """Return a sorted list of all years available in the teams table."""
    with get_session() as session:
        statement = select(Teams.yearID).distinct().order_by(Teams.yearID)
        results = session.exec(statement).all()

    # SQLModel returns a list of tuples in this case; extract the year values
    years = [row[0] for row in results]
    return {"years": years}


# Serve static files for frontend (if any)
app.mount("/", StaticFiles(directory="static", html=True), name="static")