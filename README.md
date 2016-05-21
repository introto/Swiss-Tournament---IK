# SwissTournament
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
3. Download The Swiss Tournament Game from [GitHub](https://github.com/introto/Swiss-Tournament---IK).
4. Extract zipped files to your Vagrant directory
5. Go to terminal and cd to your vagrant directory by entering **cd /fullstack/vagrant/**
6. Type **vagrant up**  and then **vagrant ssh** to log in.
7. Navigate to the tournament folder: /vagrant/swisstournament
8. Setup the PostgreSQL Database by entering **psql**
9. Create the database by running **\i tournament.sql**
10. Your tables and views in the databases should now be setup. Type **\q** to quit psql
11. From here you can run python modules to record game information by entering 


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
