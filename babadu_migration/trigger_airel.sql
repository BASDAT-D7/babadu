CREATE OR REPLACE FUNCTION cek_latih_atlet()
RETURNS trigger AS
$$
Declare dilatih atlet_pelatih.id_pelatih%TYPE;
DECLARE count_pelatih integer;
BEGIN
	SELECT COUNT(*) INTO count_pelatih
	FROM atlet_pelatih
	WHERE id_atlet = NEW.id_atlet
	GROUP BY id_atlet;

	SELECT id_pelatih INTO dilatih
	FROM atlet_pelatih
	WHERE id_atlet = NEW.id_atlet AND id_pelatih = NEW.id_pelatih;

	IF found THEN
		RAISE EXCEPTION 'Atlet sudah dilatih!';
	ELSE
		IF (count_pelatih >= 2) THEN
			UPDATE atlet_pelatih
			SET id_pelatih = NEW.id_pelatih
			WHERE id_atlet = NEW.id_atlet AND id_pelatih IN 
				(SELECT id_pelatih
				FROM atlet_pelatih
				WHERE id_atlet = NEW.id_atlet
				LIMIT 1);
			RETURN NULL;
		ELSE
			RETURN NEW;
		END IF;
	END IF;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER cek_latih_atlet
BEFORE INSERT ON atlet_pelatih
FOR EACH ROW 
EXECUTE PROCEDURE cek_latih_atlet();