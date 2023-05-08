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

function register_atlet() {
  const register_umpire = $("#register_umpire");

  $.ajax({
    type: "POST",
    url: "/authentication/register/umpire/",
    data: register_umpire.serialize(),
  }).done(function (data) {
    register_umpire.trigger("reset");
  });
}

function register_umpire() {
  const register_umpire = $("#register_umpire");

  $.ajax({
    type: "POST",
    url: "/authentication/register/umpire/",
    data: register_umpire.serialize(),
  }).done(function (data) {
    register_umpire.trigger("reset");
  });
}