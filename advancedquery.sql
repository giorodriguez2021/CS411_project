CREATE OR REPLACE FUNCTION
test(x_pts real, x_ast real, x_reb real, x_blk real, x_stl real, x_gp real, normalize boolean) 
RETURNS TABLE(f1 int, f2 varchar(150), f3 int, f4 int, f5 int, f6 int, f7 int, f8 int, f9 int, f0 real)
AS $$
    DECLARE
        avg_pts real;
        avg_ast real;
        avg_reb real;
        avg_blk real;
        avg_stl real;
        avg_gp real;
        sd_pts real;
        sd_ast real;
        sd_reb real;
        sd_blk real;
        sd_stl real;
        sd_gp real;
        mul_pts real;
        mul_ast real;
        mul_reb real;
        mul_blk real;
        mul_stl real;
        mul_gp real;
    BEGIN
        DROP VIEW Player;
        CREATE VIEW Player AS SELECT player_id,points as pts,assists as ast,rebounds as reb,blocks as blk,steals as stl,games_played as gp,team_id,playername FROM nba_app_Player;
        sd_pts := 1;
        sd_ast := 1;
        sd_reb := 1;
        sd_blk := 1;
        sd_stl := 1;
        sd_gp := 1;
        mul_pts := 1;
        mul_ast := 1;
        mul_reb := 1;
        mul_blk := 1;
        mul_stl := 1;
        mul_gp := 1;
        IF normalize THEN
            SELECT avg(pts) INTO avg_pts FROM Player;
            SELECT avg(ast) INTO avg_ast FROM Player;
            SELECT avg(reb) INTO avg_reb FROM Player;
            SELECT avg(blk) INTO avg_blk FROM Player;
            SELECT avg(stl) INTO avg_stl FROM Player;
            SELECT avg(gp) INTO avg_gp FROM Player;
            SELECT sqrt(sum((pts-avg_pts)^2)/count(pts)) INTO avg_pts FROM Player;
            SELECT sqrt(sum((ast-avg_ast)^2)/count(ast)) INTO avg_ast FROM Player;
            SELECT sqrt(sum((reb-avg_reb)^2)/count(reb)) INTO avg_reb FROM Player;
            SELECT sqrt(sum((blk-avg_blk)^2)/count(blk)) INTO avg_blk FROM Player;
            SELECT sqrt(sum((stl-avg_stl)^2)/count(stl)) INTO avg_stl FROM Player;
            SELECT sqrt(sum((gp-avg_gp)^2)/count(gp)) INTO avg_gp FROM Player;
        END IF;
        IF x_pts IS NULL THEN
            mul_pts := 0;
            x_pts := 0;
        END IF;
        IF x_ast IS NULL THEN
            mul_ast := 0;
            x_ast := 0;
        END IF;
        IF x_reb IS NULL THEN
            mul_reb := 0;
            x_reb := 0;
        END IF;
        IF x_blk IS NULL THEN
            mul_blk := 0;
            x_blk := 0;
        END IF;
        IF x_stl IS NULL THEN
            mul_stl := 0;
            x_stl := 0;
        END IF;
        IF x_gp IS NULL THEN
            mul_gp := 0;
            x_gp := 0;
        END IF;
        RETURN QUERY SELECT player_id,playername,pts,ast,reb,blk,stl,gp,team_id,CAST (sqrt(mul_pts*((x_pts-pts)/sd_pts)^2+mul_ast*((x_ast-ast)/sd_ast)^2+mul_reb*((x_reb-reb)/sd_reb)^2+mul_blk*((x_blk-blk)/sd_blk)^2+mul_stl*((x_stl-stl)/sd_stl)^2+mul_gp*((x_gp-gp)/sd_gp)^2) AS real) AS edist
        FROM Player ORDER BY edist;
    END;
$$
LANGUAGE plpgsql;
