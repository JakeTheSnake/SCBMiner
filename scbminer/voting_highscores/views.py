from django.shortcuts import render
from voting_highscores.services import get_region_highscores

def highscores(request):
    highscores = list(get_region_highscores().items())
    context = {
        'highscores': sorted([(year, (result_list[0], result_list[1])) for (year, result_list) in highscores])
    }
    return render(request, 'index.html', context)

