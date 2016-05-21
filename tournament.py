#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    query = "DELETE FROM matches"
    c.execute(query)
    db.commit()
    db.close()
              

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    query = "DELETE FROM players"
    c.execute(query)
    db.commit()
    db.close()
              

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = "SELECT count(players.id) as num from players"
    c.execute(query)
    players = c.fetchone()[0]
    db.close()
    return players
              

def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    clean_name = bleach.clean(name)
    parameter =(clean_name,)
    query = "INSERT INTO players (name) VALUES (%s)"
    c.execute(query,parameter)
    db.commit()
    db.close()
              

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    query = ("SELECT matches_and_wins.id, players.name, matches_and_wins.wins, "
             "matches_and_wins.matches "
             "FROM players, matches_and_wins "
             "WHERE players.id = matches_and_wins.id "
             "ORDER BY matches_and_wins.wins desc;")
    c.execute(query)
    standings = [(int(row[0]), str(row[1]), int(row[2]), int(row[3]))
                 for row in c.fetchall()]
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    parameter = (winner, loser)
    query = "INSERT INTO matches (winner,loser) VALUES (%s,%s);"
    c.execute(query, parameter)
    db.commit()
    db.close()
              
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    ranking = playerStandings()
    pairs = []
    numplayers = countPlayers()
    numpairs = numplayers / 2

    i = 0
    while i < numpairs:
        player1 = ranking.pop(0)
        player2 = ranking.pop(0)
        pairs.append((player1[0],player1[1],player2[0],player2[1]))
        i = i + 1
        
    return pairs
              

