# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Game


def game_recommendation(request):
    if request.method == 'POST':
        # 추천 질문 처리 로직
        question1_answer = request.POST.get('question1')
        question2_answer = request.POST.get('question2')


        # 추천 게임 생성 로직
        recommended_games = Game.objects.filter(peoplenum=question1_answer, playrule=question2_answer)[:2]

        games = []

        for game in recommended_games:
            game_data = {
                'title1': game.title1,
                'title2': game.title2,
                'title3': game.title3,
                'comment': game.comment
            }
            games.append(game_data)

        return JsonResponse({'games': games})
    else:
        return render(request, 'question.html')