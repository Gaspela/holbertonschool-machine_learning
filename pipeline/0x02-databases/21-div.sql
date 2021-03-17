-- Safe divide
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
    RETURNS FLOAT
    BEGIN
        SET @ans = 0;
        IF b <> 0 THEN
            set @ans = a/b;
        END IF;
        RETURN @ans;
    END //
DELIMITER ;