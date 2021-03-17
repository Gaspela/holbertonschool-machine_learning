--  Email validation to sent
DELIMITER / / CREATE TRIGGER transaction__ BEFORE
INSERT
,
UPDATE
    ON users FOR EACH ROW BEGIN
UPDATE
    users
SET
    valid_email = 0
WHERE
    NEW.email <> OLD.email;

END / / DELIMITER;