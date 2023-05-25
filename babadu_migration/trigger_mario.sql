-- TRIGGER & STORED PROCEDURE

-- Ketika seorang atlet mengikuti ujian
-- kualifikasi, perlu dilakukan pengecekan apakah
-- ia sudah pernah mengikuti ujian kualifikasi
-- yang ia pilih tersebut atau tidak. Jika sudah
-- pernah (terlepas dari hasil yang ia dapatkan),
-- tampilkan pesan error.

CREATE OR REPLACE FUNCTION mario_cek_atlet_pernah_ikut_ujian()
RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (SELECT * FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet=NEW.id_atlet) THEN
		RAISE EXCEPTION 'Atlet sudah pernah mengikuti ujian kualifikasi';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER mario_cek_atlet_pernah_ikut_ujian
BEFORE INSERT ON atlet_nonkualifikasi_ujian_kualifikasi
FOR EACH ROW
EXECUTE PROCEDURE mario_cek_atlet_pernah_ikut_ujian();

-- TEST

INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2023', '1', 'Jakarta', '2023-02-26', '1');