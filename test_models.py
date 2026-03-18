from sqlmodel import Session
from models import People, Teams, Batting, engine, get_session

# Test querying using the engine from models.py
with get_session() as session:
    # Get a sample player
    player = session.get(People, "aardsda01")
    if player:
        print(f"Player: {player.nameFirst} {player.nameLast}")
        print(f"Batting records: {len(player.batting_records)}")
    else:
        print("Player not found")

    # Get a sample team
    team = session.get(Teams, ("SFN", 2004))  # composite key
    if team:
        print(f"Team: {team.name} ({team.yearID})")
        print(f"Batting records: {len(team.batting_records)}")
    else:
        print("Team not found")

print("Models work correctly with the database!")