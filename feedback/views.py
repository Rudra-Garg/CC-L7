from django.shortcuts import render, redirect

from .forms import FeedbackForm
from .models import Feedback


def home(request):
    return render(request, 'home.html')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})
