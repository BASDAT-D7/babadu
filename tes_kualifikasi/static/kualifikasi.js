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
