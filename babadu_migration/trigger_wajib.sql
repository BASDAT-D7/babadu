CREATE OR REPLACE FUNCTION cek_email_exist()
RETURNS trigger AS
$$
BEGIN
	IF EXISTS (SELECT email FROM member WHERE email=NEW.email) THEN
		RAISE EXCEPTION 'Email sudah ada!';
	ELSE
		RETURN NEW;
	END IF;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION register_atlet()
RETURNS trigger AS
$$
BEGIN
	INSERT INTO atlet_non_kualifikasi VALUES (NEW.id);
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER cek_email_exist
BEFORE INSERT ON member
FOR EACH ROW 
EXECUTE PROCEDURE cek_email_exist();

CREATE TRIGGER register_atlet
AFTER INSERT ON atlet
FOR EACH ROW 
EXECUTE PROCEDURE register_atlet();