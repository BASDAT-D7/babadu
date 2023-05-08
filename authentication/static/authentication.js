function login() {
  const login = $("#login");

  $.ajax({
    type: "POST",
    url: "/authentication/login/",
    data: login.serialize(),
  }).done(function (data) {
    login.trigger("reset");
  });
}

function registerAtlet() {
  const register_atlet = $("#register_atlet");

  $.ajax({
    type: "POST",
    url: "/authentication/register/atlet/",
    data: register_atlet.serialize(),
  }).done(function (data) {
    register_atlet.trigger("reset");
  });
}

function registerPelatih() {
  const register_pelatih = $("#register_pelatih");

  $.ajax({
    type: "POST",
    url: "/authentication/register/pelatih/",
    data: register_pelatih.serialize(),
  }).done(function (data) {
    register_pelatih.trigger("reset");
  });
}

function registerUmpire() {
  const register_umpire = $("#register_umpire");

  $.ajax({
    type: "POST",
    url: "/authentication/register/umpire/",
    data: register_umpire.serialize(),
  }).done(function (data) {
    register_umpire.trigger("reset");
  });
}