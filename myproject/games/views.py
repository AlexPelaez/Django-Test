from django.shortcuts import render

# Create your views here.
def view_titles(request):
    user = request.user
    args = {'user': user}
    return render(request, 'games/titles.html', args)
    