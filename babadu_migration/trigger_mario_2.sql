CREATE OR REPLACE PROCEDURE ubah_status_kualifikasi(IN atlet_id UUID)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Perubahan status atlet non-kualifikasi menjadi kualifikasi
    UPDATE ATLET
    SET World_Rank = (
        SELECT World_Rank
        FROM ATLET_KUALIFIKASI
        WHERE ID_Atlet = atlet_id
    ),
    World_Tour_Rank = (
        SELECT World_Tour_Rank
        FROM ATLET_KUALIFIKASI
        WHERE ID_Atlet = atlet_id
    )
    WHERE ID = atlet_id;

    -- Menghapus riwayat ujian kualifikasi yang pernah diambil
    DELETE FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI
    WHERE ID_Atlet = atlet_id
      AND Hasil_Lulus = FALSE;

    -- Mengupdate total point atlet
    UPDATE ATLET_KUALIFIKASI
    SET Total_Point = Total_Point + 50
    WHERE ID_Atlet = atlet_id;
END;
$$;