# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Game


def game_recommendation(request):
    if request.method == 'POST':
        # 추천 질문 처리 로직
        question1_answer = request.POST.get('question1')
        question2_answer = request.POST.get('question2')
        # 추가 질문들...

        # 추천 게임 생성 로직
        recommended_games = Game.objects.filter(peoplenum=question1_answer, playrule=question2_answer)[:3]

        games = [{'name': game.name} for game in recommended_games]

        return JsonResponse({'games': games})
    else:
        return render(request, 'question.html')