from django.shortcuts import render

# Create your views here.
def list_atlet(request):
    dummy_list_atlet = {
        "list_atlet": [
            {
                "nama_lengkap": "Aegon Targaryen",
                "email": "aegon@got.com",
                "world_rank": "#1",
            },
            {
                "nama_lengkap": "Daenerys Targaryen",
                "email": "daenerys@got.com",
                "world_rank": "#16",
            },
            {
                "nama_lengkap": "Eugenius Mario Situmorang",
                "email": "eugeniusms@gmail.com",
                "world_rank": "#1182",
            },
            {
                "nama_lengkap": "Tyrion Lannister",
                "email": "tyrion@got.com",
                "world_rank": "#2126",
            },
            {
                "nama_lengkap": "Peokra Mokra",
                "email": "peokramokra@gmail.com",
                "world_rank": "#5432",
            },
        ]
    }
    return render(request, 'list_atlet.html', dummy_list_atlet)