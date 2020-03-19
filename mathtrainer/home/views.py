from django.shortcuts import render
from users.models import CustomUser as User

# Create your views here.
def start_view(request):
    template_name = 'train.html' # ernsthaft? erm warte mal

    return render(request, template_name, {})

def scoreboard(request):
    template_name = 'scoreboard.html'

    users = User.objects.all().order_by('xp').reverse()
    if (len(users) >= 10):
        users = users[0:9]
    
    users = list(users)
    print(users)

    return render(request, template_name, {"users": users })
