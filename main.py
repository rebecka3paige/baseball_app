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
        years = session.exec(statement).all()

    return {"years": years}


@app.get("/teams")
async def get_teams(year: int):
    """Return team records for a given year."""
    with get_session() as session:
        statement = select(Teams).where(Teams.yearID == year).order_by(Teams.teamID)
        teams = session.exec(statement).all()

    # Return only the fields needed by the frontend.
    return {"teams": [{"teamID": t.teamID, "name": t.name} for t in teams]}


# Serve static files for frontend (if any)
app.mount("/", StaticFiles(directory="static", html=True), name="static")