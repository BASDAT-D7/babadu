CREATE OR REPLACE FUNCTION mario_cek_atlet_pernah_ikut_ujian()
RETURNS TRIGGER AS $$
DECLARE last_world_rank integer;
BEGIN
    IF EXISTS (SELECT * FROM atlet_kualifikasi WHERE id_atlet=NEW.id_atlet) THEN
        RAISE EXCEPTION 'Atlet sudah lulus ujian kualifikasi';
    ELSE
        IF EXISTS (SELECT * FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet=NEW.id_atlet AND tahun=NEW.tahun AND batch=NEW.batch AND tanggal=NEW.tanggal) THEN
            RAISE EXCEPTION 'Atlet sudah pernah mengikuti ujian kualifikasi';
        ELSE
            IF (NEW.hasil_lulus='1') THEN
                DELETE FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet=NEW.id_atlet;
                DELETE FROM atlet_non_kualifikasi WHERE id_atlet=NEW.id_atlet;

                SELECT COUNT(*) INTO last_world_rank
                FROM atlet_kualifikasi;
                last_world_rank := last_world_rank + 1;
                
                INSERT INTO atlet_kualifikasi VALUES (NEW.id_atlet, last_world_rank, last_world_rank);
                UPDATE atlet SET world_rank = ak.world_rank FROM atlet_kualifikasi ak WHERE atlet.id = ak.id_atlet;

                IF EXISTS (SELECT * FROM point_history WHERE id_atlet=NEW.id_atlet AND minggu_ke=EXTRACT(WEEK FROM NEW.tanggal) AND bulan=TO_CHAR(NEW.tanggal, 'Month') AND tahun=EXTRACT(YEAR FROM NEW.tanggal)) THEN
                    UPDATE point_history SET total_point=total_point+50 WHERE id_atlet=NEW.id_atlet AND minggu_ke=EXTRACT(WEEK FROM NEW.tanggal) AND bulan=TO_CHAR(NEW.tanggal, 'Month') AND tahun=EXTRACT(YEAR FROM NEW.tanggal);
                ELSE
                    INSERT INTO point_history VALUES (NEW.id_atlet, EXTRACT(WEEK FROM NEW.tanggal), TO_CHAR(NEW.tanggal, 'Month'), EXTRACT(YEAR FROM NEW.tanggal), 50);
                END IF;

                RETURN NULL;
            ELSE
                RETURN NEW;
            END IF;
        END IF;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER mario_cek_atlet_pernah_ikut_ujian
BEFORE INSERT ON atlet_nonkualifikasi_ujian_kualifikasi
FOR EACH ROW
EXECUTE PROCEDURE mario_cek_atlet_pernah_ikut_ujian();