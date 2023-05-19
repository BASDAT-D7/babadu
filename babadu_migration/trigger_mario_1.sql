CREATE OR REPLACE FUNCTION cek_ujian_kualifikasi()
RETURNS TRIGGER AS
$$
DECLARE
    atlet_status VARCHAR(20);
BEGIN
    -- Pengecekan apakah atlet sudah pernah mengikuti ujian kualifikasi yang dipilih
    SELECT CASE
        WHEN EXISTS (
            SELECT 1
            FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI
            WHERE ID_Atlet = NEW.ID_Atlet
              AND Tahun = NEW.Tahun
              AND Batch = NEW.Batch
              AND Tempat = NEW.Tempat
              AND Tanggal = NEW.Tanggal
        ) THEN 'Error: Atlet sudah pernah mengikuti ujian kualifikasi tersebut'
        ELSE NULL
    END INTO atlet_status;

    IF atlet_status IS NOT NULL THEN
        RAISE EXCEPTION '%', atlet_status; -- Memperbaiki exception yang dilempar
    END IF;

    -- Pengecekan apakah atlet non-kualifikasi lulus ujian kualifikasi
    IF EXISTS (
        SELECT 1
        FROM ATLET_NON_KUALIFIKASI
        WHERE ID_Atlet = NEW.ID_Atlet
    ) THEN
        IF NEW.Hasil_Lulus THEN
            -- Perubahan status atlet non-kualifikasi menjadi kualifikasi
            UPDATE ATLET
            SET World_Rank = (
                SELECT World_Rank
                FROM ATLET_KUALIFIKASI
                WHERE ID_Atlet = NEW.ID_Atlet
            ),
            World_Tour_Rank = (
                SELECT World_Tour_Rank
                FROM ATLET_KUALIFIKASI
                WHERE ID_Atlet = NEW.ID_Atlet
            )
            WHERE ID = NEW.ID_Atlet;

            -- Menghapus riwayat ujian kualifikasi yang pernah diambil
            DELETE FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI
            WHERE ID_Atlet = NEW.ID_Atlet
              AND Hasil_Lulus = FALSE;

            -- Mengupdate total point atlet
            UPDATE POINT_HISTORY
            SET Total_Point = Total_Point + 50
            WHERE ID_Atlet = NEW.ID_Atlet
              AND Minggu_Ke = EXTRACT(WEEK FROM NEW.Tanggal) -- Menyesuaikan dengan minggu yang tepat
              AND Bulan = TO_CHAR(NEW.Tanggal, 'Month')
              AND Tahun = EXTRACT(YEAR FROM NEW.Tanggal);
        ELSE
            -- Hanya menyimpan data ujian kualifikasi yang diambil
            RETURN NEW;
        END IF;
    ELSE
        -- Atlet kualifikasi yang mengambil ujian kualifikasi kembali
        RETURN NULL;
    END IF;

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;
