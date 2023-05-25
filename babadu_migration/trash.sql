-- TESTS
-- 1. Atlet pernah mengikuti ujian kualifikasi yang dipilih
-- Expectation: Error
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2023', '1', 'Jakarta', '2023-02-26', '0');
-- 2. Atlet belum pernah mengikuti ujian kualifikasi
-- Expectation: Success
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '2023', '1', 'Jakarta', '2023-02-26', '1');
DELETE FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet='d7bbec6c-01f4-4cc1-89b8-2be2b0cba371' AND tahun='2023' AND batch='1' AND tanggal='2023-02-26';
-- 3. Atlet pernah mengikuti ujian kualifikasi, tetapi bukan yang dipilih
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2022', '2', 'Bogor', '2022-06-10', '0');
DELETE FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet='2e0d9f03-3158-4e4a-a928-1e0a6c838d42' AND tahun='2022' AND batch='2' AND tanggal='2022-06-10';
-- Expectation: Success
-- 4. Atlet lulus ujian kualifikasi
INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi VALUES ('75011b5f-723e-4b11-8314-80656c46c346', '2022', '2', 'Bogor', '2022-06-10', '1');
DELETE FROM atlet_nonkualifikasi_ujian_kualifikasi WHERE id_atlet='75011b5f-723e-4b11-8314-80656c46c346' AND tahun='2022' AND batch='2' AND tanggal='2022-06-10';

-- RESET
DROP TRIGGER IF EXISTS mario_cek_atlet_pernah_ikut_ujian ON atlet_nonkualifikasi_ujian_kualifikasi;
DROP FUNCTION IF EXISTS mario_cek_atlet_pernah_ikut_ujian;

