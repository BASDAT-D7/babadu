from django.shortcuts import render

# Create your views here.
def hasil_pertandingan(request):
    dummy_hasil_pertandingan = {
        'event': {
            "nama_event": "Badminton Open",
            "total_hadiah": "Rp 5.000.000",
            "tanggal_mulai": "12-04-2023",
            "tanggal_selesai": "15-04-2023",
            "kategori": "S200",
            "kapasitas_terisi": 3,
            "kapasitas_total": 8,
            "nama_stadium": "Gelora Bung Karno",
            "negara": "Indonesia"
        },
        'daftar_tahap': [
            {
                "nama_tahap": "Juara 1",
                "daftar_tim": [
                    "A"
                ]
            },
            {
                "nama_tahap": "Juara 2",
                "daftar_tim": [
                    "G"
                ]
            },
            {
                "nama_tahap": "Juara 3",
                "daftar_tim": [
                    "D"
                ]
            },
            {
                "nama_tahap": "Semifinal",
                "daftar_tim": [
                    "E"
                ]
            },
            {
                "nama_tahap": "Perempat Final",
                "daftar_tim": [
                    "C", "F", "B", "H"
                ]
            }
        ]
    }
    return render(request, 'hasil_pertandingan.html', dummy_hasil_pertandingan)