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

function jawabPertanyaanKualifikasi() {
  const jawab_pertanyaan_kualifikasi = $("#jawab_pertanyaan_kualifikasi");

  $.ajax({
    type: "POST",
    url: "/tes-kualifikasi/pertanyaan/",
    data: jawab_pertanyaan_kualifikasi.serialize(),
  }).done(function (data) {
    jawab_pertanyaan_kualifikasi.trigger("reset");
  });
}
