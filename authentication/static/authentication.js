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
