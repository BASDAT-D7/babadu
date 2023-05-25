-- TRIGGER & STORED PROCEDURE

-- DESCRIPTION 1
-- Ketika seorang atlet mengikuti ujian
-- kualifikasi, perlu dilakukan pengecekan apakah
-- ia sudah pernah mengikuti ujian kualifikasi
-- yang ia pilih tersebut atau tidak. Jika sudah
-- pernah (terlepas dari hasil yang ia dapatkan),
-- tampilkan pesan error.

CREATE OR REPLACE FUNCTION mario_cek_atlet_pernah_ikut_ujian()
RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (SELECT * FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet=NEW.id_atlet AND tahun=NEW.tahun AND batch=NEW.batch AND tanggal=NEW.tanggal) THEN
		RAISE EXCEPTION 'Atlet sudah pernah mengikuti ujian kualifikasi';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER mario_cek_atlet_pernah_ikut_ujian
BEFORE INSERT ON atlet_nonkualifikasi_ujian_kualifikasi
FOR EACH ROW
EXECUTE PROCEDURE mario_cek_atlet_pernah_ikut_ujian();
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2023', '1', 'Jakarta', '2023-02-26', '0');
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '2023', '1', 'Jakarta', '2023-02-26', '1');
DELETE FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet='d7bbec6c-01f4-4cc1-89b8-2be2b0cba371' AND tahun='2023' AND batch='1' AND tanggal='2023-02-26';
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2022', '2', 'Bogor', '2022-06-10', '0');
DELETE FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet='2e0d9f03-3158-4e4a-a928-1e0a6c838d42' AND tahun='2022' AND batch='2' AND tanggal='2022-06-10';
DROP TRIGGER IF EXISTS mario_cek_atlet_pernah_ikut_ujian ON atlet_nonkualifikasi_ujian_kualifikasi;
DROP FUNCTION IF EXISTS mario_cek_atlet_pernah_ikut_ujian;

