function buatDataKualifikasi() {
  const buat_data_kualifikasi = $("#buat_data_kualifikasi");

  $.ajax({
    type: "POST",
    url: "/tes-kualifikasi/",
    data: buat_data_kualifikasi.serialize(),
  }).done(function (data) {
    buat_data_kualifikasi.trigger("reset");
  });
}

function jawabPertanyaanKualifikasi(tahun, batch, tempat, tanggal) {
  const jawab_pertanyaan_kualifikasi = $("#jawab_pertanyaan_kualifikasi");

  console.log("TEST");

  $.ajax({
    type: "POST",
    url: `/tes-kualifikasi/pertanyaan/${tahun}/${batch}/${tempat}/${tanggal}/`,
    data: jawab_pertanyaan_kualifikasi.serialize(),
  }).done(function (data) {
    jawab_pertanyaan_kualifikasi.trigger("reset");
  });
}
