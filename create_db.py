import pandas as pd
import sqlite3
from sqlalchemy import create_engine, text

# Create SQLite engine
engine = create_engine('sqlite:///baseball.db')

# Read CSV files with specified dtypes
people_dtypes_read = {
    'ID': 'int64',
    'playerID': 'string',
    'birthYear': 'Int64',
    'birthMonth': 'Int64',
    'birthDay': 'Int64',
    'birthCity': 'string',
    'birthCountry': 'string',
    'birthState': 'string',
    'deathYear': 'Int64',
    'deathMonth': 'Int64',
    'deathDay': 'Int64',
    'deathCountry': 'string',
    'deathState': 'string',
    'deathCity': 'string',
    'nameFirst': 'string',
    'nameLast': 'string',
    'nameGiven': 'string',
    'weight': 'Int64',
    'height': 'Int64',
    'bats': 'string',
    'throws': 'string',
    'debut': 'string',
    'bbrefID': 'string',
    'finalGame': 'string',
    'retroID': 'string'
}

teams_dtypes_read = {
    'yearID': 'int64',
    'lgID': 'string',
    'teamID': 'string',
    'franchID': 'string',
    'divID': 'string',
    'Rank': 'int64',
    'G': 'int64',
    'Ghome': 'Int64',
    'W': 'int64',
    'L': 'int64',
    'DivWin': 'string',
    'WCWin': 'string',
    'LgWin': 'string',
    'WSWin': 'string',
    'R': 'int64',
    'AB': 'int64',
    'H': 'int64',
    '2B': 'int64',
    '3B': 'int64',
    'HR': 'int64',
    'BB': 'int64',
    'SO': 'int64',
    'SB': 'int64',
    'CS': 'int64',
    'HBP': 'Int64',
    'SF': 'Int64',
    'RA': 'int64',
    'ER': 'int64',
    'ERA': 'float64',
    'CG': 'int64',
    'SHO': 'int64',
    'SV': 'int64',
    'IPouts': 'int64',
    'HA': 'int64',
    'HRA': 'int64',
    'BBA': 'int64',
    'SOA': 'int64',
    'E': 'int64',
    'DP': 'int64',
    'FP': 'float64',
    'name': 'string',
    'park': 'string',
    'attendance': 'Int64',
    'BPF': 'int64',
    'PPF': 'int64',
    'teamIDBR': 'string',
    'teamIDlahman45': 'string',
    'teamIDretro': 'string'
}

batting_dtypes_read = {
    'playerID': 'string',
    'yearID': 'int64',
    'stint': 'int64',
    'teamID': 'string',
    'lgID': 'string',
    'G': 'int64',
    'AB': 'int64',
    'R': 'int64',
    'H': 'int64',
    '2B': 'int64',
    '3B': 'int64',
    'HR': 'int64',
    'RBI': 'Int64',
    'SB': 'Int64',
    'CS': 'Int64',
    'BB': 'Int64',
    'SO': 'Int64',
    'IBB': 'Int64',
    'HBP': 'Int64',
    'SH': 'Int64',
    'SF': 'Int64',
    'GIDP': 'Int64'
}

people_df = pd.read_csv('people.csv', dtype=people_dtypes_read)
teams_df = pd.read_csv('teams.csv', dtype=teams_dtypes_read)
batting_df = pd.read_csv('Batting(1).csv', dtype=batting_dtypes_read)

# Define data types for people table
people_dtypes = {
    'ID': 'INTEGER',
    'playerID': 'TEXT PRIMARY KEY',
    'birthYear': 'INTEGER',
    'birthMonth': 'INTEGER',
    'birthDay': 'INTEGER',
    'birthCity': 'TEXT',
    'birthCountry': 'TEXT',
    'birthState': 'TEXT',
    'deathYear': 'INTEGER',
    'deathMonth': 'INTEGER',
    'deathDay': 'INTEGER',
    'deathCountry': 'TEXT',
    'deathState': 'TEXT',
    'deathCity': 'TEXT',
    'nameFirst': 'TEXT',
    'nameLast': 'TEXT',
    'nameGiven': 'TEXT',
    'weight': 'INTEGER',
    'height': 'INTEGER',
    'bats': 'TEXT',
    'throws': 'TEXT',
    'debut': 'TEXT',
    'bbrefID': 'TEXT',
    'finalGame': 'TEXT',
    'retroID': 'TEXT'
}

# Define data types for teams table
teams_dtypes = {
    'yearID': 'INTEGER',
    'lgID': 'TEXT',
    'teamID': 'TEXT',
    'franchID': 'TEXT',
    'divID': 'TEXT',
    'Rank': 'INTEGER',
    'G': 'INTEGER',
    'Ghome': 'INTEGER',
    'W': 'INTEGER',
    'L': 'INTEGER',
    'DivWin': 'TEXT',
    'WCWin': 'TEXT',
    'LgWin': 'TEXT',
    'WSWin': 'TEXT',
    'R': 'INTEGER',
    'AB': 'INTEGER',
    'H': 'INTEGER',
    '2B': 'INTEGER',
    '3B': 'INTEGER',
    'HR': 'INTEGER',
    'BB': 'INTEGER',
    'SO': 'INTEGER',
    'SB': 'INTEGER',
    'CS': 'INTEGER',
    'HBP': 'INTEGER',
    'SF': 'INTEGER',
    'RA': 'INTEGER',
    'ER': 'INTEGER',
    'ERA': 'REAL',
    'CG': 'INTEGER',
    'SHO': 'INTEGER',
    'SV': 'INTEGER',
    'IPouts': 'INTEGER',
    'HA': 'INTEGER',
    'HRA': 'INTEGER',
    'BBA': 'INTEGER',
    'SOA': 'INTEGER',
    'E': 'INTEGER',
    'DP': 'INTEGER',
    'FP': 'REAL',
    'name': 'TEXT',
    'park': 'TEXT',
    'attendance': 'INTEGER',
    'BPF': 'INTEGER',
    'PPF': 'INTEGER',
    'teamIDBR': 'TEXT',
    'teamIDlahman45': 'TEXT',
    'teamIDretro': 'TEXT'
}

# Define data types for batting table
batting_dtypes = {
    'playerID': 'TEXT',
    'yearID': 'INTEGER',
    'stint': 'INTEGER',
    'teamID': 'TEXT',
    'lgID': 'TEXT',
    'G': 'INTEGER',
    'AB': 'INTEGER',
    'R': 'INTEGER',
    'H': 'INTEGER',
    '2B': 'INTEGER',
    '3B': 'INTEGER',
    'HR': 'INTEGER',
    'RBI': 'INTEGER',
    'SB': 'INTEGER',
    'CS': 'INTEGER',
    'BB': 'INTEGER',
    'SO': 'INTEGER',
    'IBB': 'INTEGER',
    'HBP': 'INTEGER',
    'SH': 'INTEGER',
    'SF': 'INTEGER',
    'GIDP': 'INTEGER'
}

# Create tables with constraints
with engine.connect() as conn:
    # Create people table
    people_columns = ', '.join([f'{col} {dtype}' for col, dtype in people_dtypes.items()])
    conn.execute(text(f'CREATE TABLE people ({people_columns})'))

    # Create teams table
    teams_columns = ', '.join([f'{col} {dtype}' for col, dtype in teams_dtypes.items()])
    teams_columns += ', PRIMARY KEY (teamID, yearID)'
    conn.execute(text(f'CREATE TABLE teams ({teams_columns})'))

    # Create batting table
    batting_columns = ', '.join([f'{col} {dtype}' for col, dtype in batting_dtypes.items()])
    batting_columns += ', PRIMARY KEY (playerID, yearID, stint)'
    batting_columns += ', FOREIGN KEY (playerID) REFERENCES people (playerID)'
    batting_columns += ', FOREIGN KEY (yearID, teamID) REFERENCES teams (yearID, teamID)'
    conn.execute(text(f'CREATE TABLE batting ({batting_columns})'))

# Insert data
people_df.to_sql('people', engine, if_exists='append', index=False)
teams_df.to_sql('teams', engine, if_exists='append', index=False)
batting_df.to_sql('batting', engine, if_exists='append', index=False)

print("Database created successfully!")