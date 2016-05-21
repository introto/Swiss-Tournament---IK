-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Delete any old tournamment database
DROP DATABASE IF EXISTS tournament;

-- Creates the Database
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Creates a table containing the players, id and name
CREATE TABLE  players (id SERIAL primary key, 
						name TEXT );

-- Creates a table of matches, and the winners and losers
CREATE TABLE matches (matchid SERIAL,
						winner INTEGER 
							references players(id),
						loser INTEGER 
							references players(id));

-- Creates A VIEW FOR number of wins, by joining players and match tables
CREATE VIEW number_of_wins AS
	SELECT players.id, count(matches.winner) AS wins
	FROM players left join matches
	ON players.id = matches.winner
	GROUP BY players.id;

-- Creates A VIEW FOR number of losses, by joining players and match tables this is a useless table 
CREATE VIEW number_of_losses AS
	SELECT players.id, count(matches.loser) AS losses
	FROM players left join matches
	ON players.id = matches.loser
	GROUP BY players.id;

-- Creates A View for the number of matches, by counting the matches played
CREATE VIEW number_of_matches AS
	SELECT players.id, 
		count (combine) AS nummatches
	FROM players left join 
		(SELECT winner as combine FROM matches
		UNION ALL 
		SELECT loser FROM matches) AS combine 
	ON players.id = combine
	GROUP BY players.id;

-- Creates A VIEW for the number of wins and the number of matches for each player. 
CREATE VIEW matches_and_wins AS
	SELECT number_of_matches.id, number_of_wins.wins, number_of_matches.nummatches AS matches
	FROM number_of_matches, number_of_wins
	WHERE number_of_matches.id = number_of_wins.id

