from django.contrib.auth.views import login_required
from django.shortcuts import render


@login_required
def tmp_home(request):
    return render(request, "pages/home.html")
