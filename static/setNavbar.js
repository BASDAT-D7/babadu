function setNavbar(is_authenticated) {
  if (is_authenticated) {
    var userRole = getCookie("user_role");
    if (userRole == "ATLET") {
      // NAVBAR ATLET
      return `<div class="flex justify-between bg-black/50 backdrop-blur-sm text-white font-poppins items-center py-4 px-8 cursor-pointer top-0 z-50 w-full fixed border-b-[1px] border-white/20">
                <div class="flex gap-5 font-semibold text-bluebright text-xl">
                    Babadu.D7
                </div>  
                <div class="flex gap-5 items-center">
                    <button class="hover:text-blue"><a href="/">Dashboard</a></button>
                    <div class="dropdown">
                      <button class="hover:text-blue">Ujian Kualifikasi</button>
                      <div class="dropdown-content">
                        <a href="/tes-kualifikasi">List Ujian Kualifikasi</a>
                        <a href="/riwayat-ujian-kualifikasi">Riwayat Ujian Kualifikasi</a>
                      </div>
                    </div>
                    <div class="dropdown">
                      <button class="hover:text-blue">Event</button>
                      <div class="dropdown-content">
                        <a href="/daftar-event">Daftar Event</a>
                        <a href="/enrolled-event">Enrolled Event</a>
                      </div>
                    </div>
                    <div class="dropdown">
                      <button class="hover:text-blue">Sponsor</button>
                      <div class="dropdown-content">
                        <a href="/daftar-sponsor">Daftar Sponsor</a>
                        <a href="/list-sponsor">List Sponsor</a>
                      </div>
                    </div>
                    <a href="/authentication/logout/">
                        <button class="border-2 border-redbright text-redbright rounded-xl py-2 px-4 hover:bg-redbright hover:text-black duration-200">Logout</button>
                    </a>
                </div>
            </div>
            `;
    } else if (userRole == "PELATIH") {
      // NAVBAR PELATIH
      return `<div class="flex justify-between bg-black/50 backdrop-blur-sm text-white font-poppins items-center py-4 px-8 cursor-pointer top-0 z-50 w-full fixed border-b-[1px] border-white/20">
                    <div class="flex gap-5 font-semibold text-bluebright text-xl">
                        Babadu.D7
                    </div>  
                    <div class="flex gap-5">
                        <button class="hover:text-blue"><a href="/">Dashboard</a></button>
                        <button class="hover:text-blue"><a href="/daftar-atlet">Daftar Atlet</a></button>
                        <button class="hover:text-blue"><a href="/list-atlet">List Atlet</a></button>
                        <a href="/authentication/logout/">
                            <button class="border-2 border-redbright text-redbright rounded-xl py-2 px-4 hover:bg-redbright hover:text-black duration-200">Logout</button>
                        </a>
                    </div>
                </div>`;
    } else {
      // NAVBAR UMPIRE
      return `<div class="flex justify-between bg-black/50 backdrop-blur-sm text-white font-poppins items-center py-4 px-8 cursor-pointer top-0 z-50 w-full fixed border-b-[1px] border-white/20">
                <div class="flex gap-5 font-semibold text-bluebright text-xl">
                    Babadu.D7
                </div>  
                <div class="flex gap-5">
                    <button class="hover:text-blue"><a href="/">Dashboard</a></button>
                    <button class="hover:text-blue"><a href="/daftar-atlet">Daftar Atlet</a></button>
                    <button class="hover:text-blue"><a href="/lihat-event">Lihat Event</a></button>
                    <button class="hover:text-blue"><a href="/hasil-pertandingan">Hasil Pertandingan</a></button>
                    <a href="/authentication/logout/">
                        <button class="border-2 border-redbright text-redbright rounded-xl py-2 px-4 hover:bg-redbright hover:text-black duration-200">Logout</button>
                    </a>
                </div>
            </div>`;
    }
  } else {
    // NAVBAR GUEST
    return `<div class="flex justify-between bg-black/50 backdrop-blur-sm text-white font-poppins items-center py-4 px-8 cursor-pointer top-0 z-50 w-full fixed border-b-[1px] border-white/20">
                <div class="flex gap-5 font-semibold text-bluebright text-xl">
                    Babadu.D7
                </div>  
                <div class="flex gap-5">
                    <button class="hover:text-blue"><a href="/">Dashboard</a></button>
                    <button class="hover:text-blue"><a href="/daftar-atlet">Daftar Atlet</a></button>
                    <button class="hover:text-blue"><a href="/lihat-event">Lihat Event</a></button>
                    <button class="hover:text-blue"><a href="/hasil-pertandingan">Hasil Pertandingan</a></button>
                    <a href="/authentication/">
                        <button class="border-2 border-green text-green rounded-xl py-2 px-4 hover:bg-green hover:text-black duration-200">Login</button>
                    </a>
                </div>
            </div>`;
  }
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
