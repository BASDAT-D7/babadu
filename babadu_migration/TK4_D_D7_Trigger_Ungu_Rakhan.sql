CREATE or REPLACE FUNCTION peserta_unenroll_event()
RETURNS trigger AS
$$ 
DECLARE
tgl_event DATE; 
current_date DATE := CURRENT_DATE;
BEGIN
SELECT tgl_mulai INTO tgl_event
FROM EVENT E
WHERE E.nama_event =  OLD.nama_event AND E.tahun = OLD.tahun;

IF tgl_event <= current_date THEN
 RAISE EXCEPTION 'Error: tidak bisa unenroll dari event yang telah berlalu.';

END IF;
RETURN OLD;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER peserta_unenroll_event
BEFORE DELETE ON PESERTA_MENDAFTAR_EVENT
FOR EACH ROW 
EXECUTE FUNCTION peserta_unenroll_event();