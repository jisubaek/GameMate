from django.shortcuts import render


def main(request):
    return render(
        request,
        'starting_pages/starting.html'
    )
