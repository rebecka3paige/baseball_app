from sqlmodel import SQLModel, Field, Relationship, ForeignKeyConstraint
from typing import Optional
from sqlalchemy import Column, Integer, Float, Text, and_


class People(SQLModel, table=True):
    __tablename__ = "people"

    ID: Optional[int] = Field(default=None)
    playerID: str = Field(primary_key=True)
    birthYear: Optional[int] = Field(default=None)
    birthMonth: Optional[int] = Field(default=None)
    birthDay: Optional[int] = Field(default=None)
    birthCity: Optional[str] = Field(default=None)
    birthCountry: Optional[str] = Field(default=None)
    birthState: Optional[str] = Field(default=None)
    deathYear: Optional[int] = Field(default=None)
    deathMonth: Optional[int] = Field(default=None)
    deathDay: Optional[int] = Field(default=None)
    deathCountry: Optional[str] = Field(default=None)
    deathState: Optional[str] = Field(default=None)
    deathCity: Optional[str] = Field(default=None)
    nameFirst: Optional[str] = Field(default=None)
    nameLast: Optional[str] = Field(default=None)
    nameGiven: Optional[str] = Field(default=None)
    weight: Optional[int] = Field(default=None)
    height: Optional[int] = Field(default=None)
    bats: Optional[str] = Field(default=None)
    throws: Optional[str] = Field(default=None)
    debut: Optional[str] = Field(default=None)
    bbrefID: Optional[str] = Field(default=None)
    finalGame: Optional[str] = Field(default=None)
    retroID: Optional[str] = Field(default=None)

    # Relationships
    batting_records: list["Batting"] = Relationship(back_populates="player")


class Teams(SQLModel, table=True):
    __tablename__ = "teams"

    yearID: int = Field(primary_key=True)
    lgID: Optional[str] = Field(default=None)
    teamID: str = Field(primary_key=True)
    franchID: Optional[str] = Field(default=None)
    divID: Optional[str] = Field(default=None)
    Rank: Optional[int] = Field(default=None)
    G: Optional[int] = Field(default=None)
    Ghome: Optional[int] = Field(default=None)
    W: Optional[int] = Field(default=None)
    L: Optional[int] = Field(default=None)
    DivWin: Optional[str] = Field(default=None)
    WCWin: Optional[str] = Field(default=None)
    LgWin: Optional[str] = Field(default=None)
    WSWin: Optional[str] = Field(default=None)
    R: Optional[int] = Field(default=None)
    AB: Optional[int] = Field(default=None)
    H: Optional[int] = Field(default=None)
    b2: Optional[int] = Field(default=None, sa_column=Column("2B", Integer))
    b3: Optional[int] = Field(default=None, sa_column=Column("3B", Integer))
    HR: Optional[int] = Field(default=None)
    BB: Optional[int] = Field(default=None)
    SO: Optional[int] = Field(default=None)
    SB: Optional[int] = Field(default=None)
    CS: Optional[int] = Field(default=None)
    HBP: Optional[int] = Field(default=None)
    SF: Optional[int] = Field(default=None)
    RA: Optional[int] = Field(default=None)
    ER: Optional[int] = Field(default=None)
    ERA: Optional[float] = Field(default=None)
    CG: Optional[int] = Field(default=None)
    SHO: Optional[int] = Field(default=None)
    SV: Optional[int] = Field(default=None)
    IPouts: Optional[int] = Field(default=None)
    HA: Optional[int] = Field(default=None)
    HRA: Optional[int] = Field(default=None)
    BBA: Optional[int] = Field(default=None)
    SOA: Optional[int] = Field(default=None)
    E: Optional[int] = Field(default=None)
    DP: Optional[int] = Field(default=None)
    FP: Optional[float] = Field(default=None)
    name: Optional[str] = Field(default=None)
    park: Optional[str] = Field(default=None)
    attendance: Optional[int] = Field(default=None)
    BPF: Optional[int] = Field(default=None)
    PPF: Optional[int] = Field(default=None)
    teamIDBR: Optional[str] = Field(default=None)
    teamIDlahman45: Optional[str] = Field(default=None)
    teamIDretro: Optional[str] = Field(default=None)



class Batting(SQLModel, table=True):
    __tablename__ = "batting"

    playerID: str = Field(primary_key=True, foreign_key="people.playerID")
    yearID: int = Field(primary_key=True)
    stint: int = Field(primary_key=True)
    teamID: str
    lgID: Optional[str] = Field(default=None)
    G: Optional[int] = Field(default=None)
    AB: Optional[int] = Field(default=None)
    R: Optional[int] = Field(default=None)
    H: Optional[int] = Field(default=None)
    b2: Optional[int] = Field(default=None, sa_column=Column("2B", Integer))
    b3: Optional[int] = Field(default=None, sa_column=Column("3B", Integer))
    HR: Optional[int] = Field(default=None)
    RBI: Optional[int] = Field(default=None)
    SB: Optional[int] = Field(default=None)
    CS: Optional[int] = Field(default=None)
    BB: Optional[int] = Field(default=None)
    SO: Optional[int] = Field(default=None)
    IBB: Optional[int] = Field(default=None)
    HBP: Optional[int] = Field(default=None)
    SH: Optional[int] = Field(default=None)
    SF: Optional[int] = Field(default=None)
    GIDP: Optional[int] = Field(default=None)

    # Composite foreign key for (yearID, teamID) -> teams(yearID, teamID)
    __table_args__ = (
        ForeignKeyConstraint(['yearID', 'teamID'], ['teams.yearID', 'teams.teamID']),
    )

    # Relationships
    player: People = Relationship(back_populates="batting_records")


# Database engine and session configuration
from sqlmodel import create_engine, Session

# Create SQLite engine
DATABASE_URL = "sqlite:///baseball.db"
engine = create_engine(DATABASE_URL, echo=False)  # Set echo=True for SQL logging

# Create session maker
def get_session():
    return Session(engine)

# Function to create all tables (if needed)
def create_tables():
    SQLModel.metadata.create_all(engine)