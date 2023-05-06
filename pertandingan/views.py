from django.shortcuts import render

# Create your views here.
def perempat_final(request):
    dummy_perempat_final = {
        'daftar_perempat_final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'B',
                'skor_tim_1': 21,
                'skor_tim_2': 19
            },
            {
                'id': 2,
                'tim_1': 'C',
                'tim_2': 'D',
                'skor_tim_1': 15,
                'skor_tim_2': 21
            },
            {
                'id': 3,
                'tim_1': 'E',
                'tim_2': 'F',
                'skor_tim_1': 21,
                'skor_tim_2': 13
            },
            {
                'id': 4,
                'tim_1': 'G',
                'tim_2': 'H',
                'skor_tim_1': 21,
                'skor_tim_2': 17
            }
        ]
    }           
    return render(request, 'pertandingan_perempat_final.html', dummy_perempat_final)

def semifinal(request):
    return render(request, 'pertandingan_semifinal.html')

def final(request):
    return render(request, 'pertandingan_final.html')