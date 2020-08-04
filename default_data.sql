/*
DELETE FROM nba_app_OnTeam;
DELETE FROM nba_app_Game;
DELETE FROM nba_app_PlayerStats;
DELETE FROM nba_app_Player;
DELETE FROM nba_app_Team;

INSERT INTO nba_app_Player VALUES
    (0, 'Aa'),
    (1, 'B'),
    (2, 'C'),
    (3, 'D');

INSERT INTO nba_app_Team VALUES
    (0,'Good Team'),
    (1,'Bad Team');

INSERT INTO nba_app_OnTeam VALUES
    (0,0,0),
    (1,1,0),
    (2,2,1),
    (3,3,1);

INSERT INTO nba_app_Game VALUES
    (0,99,-2,0,1),
    (1,0,12345,1,0);

INSERT INTO nba_app_PlayerStats VALUES
    (0,1,2,3,4),
    (1,1234,4321,9,9999),
    (2,0,0,0,0),
    (3,0,0,0,-2);
*/

DELETE FROM nba_app_Team;
DELETE FROM nba_app_Player;
DELETE FROM nba_app_Game;

INSERT INTO nba_app_Team(team_id,teamname) VALUES
    (0,'Team0'),
    (1,'Team1');

INSERT INTO nba_app_Player(player_id,playername,team_id,points,assists,rebounds,blocks,steals) VALUES
    (0,'P0',0,1,2,3,4,5),
    (1,'P1',0,2,4,6,8,10),
    (2,'P2',1,0,0,0,0,0),
    (3,'P3',1,-1,-1,-1,-1,-1);
