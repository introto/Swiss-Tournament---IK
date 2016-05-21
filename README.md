# Swiss-Tournament---IK
Swiss Tournament Game

By Inderjit Kanwal

version 1.05   05/21/2106

What is it?
-----------

The Swiss Tournament Game is a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament. The Swiss tournament system for pairing up players in each round ensures that players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible. This game assumes a even number of players and does not account for ties in a match. 

The Latest Version
------------------
The latest version was released on May 21, 2016.


Installation
------------

1. Download Vagrant from vagrantup.com. 
2. To install Vagrant on your machine please see this [tutorial](https://www.udacity.com/wiki/ud197/install-vagrant) for more instruction using Vagrants. 
2. Download The Swiss Tournament Game from [GitHub](https://github.com/introto/Swiss-Tournament---IK).
3. Extract zipped files to your Vagrant directory
4. Go to termindal and cd to your vagrant directory/
5. Type **vagrant up**  and then **vagrant ssh** to log in.
6. Navigate to the tournamnet folder: /swiss

From the terminal, cd to your /vagrant directory.
Type vagrant up to launch the virtual machine. Then type vagrant ssh to log in.
In the VM, cd to the /tournament folder.
Setup the PostgreSQL database with the command, psql -f tournament.sql


psql => \i tournament.sql

Modules
------------

Connect
Meant to connect to the database. Already set up for you.

deleteMatches
Remove all the matches records from the database.

deletePlayers
Remove all the player records from the database.

countPlayers
Returns the number of players currently registered

registerPlayer -- Adds a player to the tournament database.

playerStandings --
Returns a list of the players and their win records, sorted by wins. You can use the player standings table created in your .sql file for reference.

reportMatch
This is to simply populate the matches table and record the winner and loser as (winner,loser) in the insert statement.

swissPairings
Returns a list of pairs of players for the next round of a match. Here all we are doing is the pairing of alternate players from the player standings table, zipping them up and appending them to a list with values:
(id1, name1, id2, name2)


What's included
--------
  Swiss-Tournament---IK
  
  -> tournament.py
  
  -> tournament_test.py
  
  -> tournament.sql
  
  -> README.md


Contacts
--------

If you notice any bugs or have any questions please contact me at ikanwal@gmail.com. 


Copyright
--------

Copyright (c) 2016 Inder Kanwal

You can redistribute it and/or modify the game as needed.

Swiss Tournament is distributed in the hope that it will be useful, but without any warranty or guarantee.
