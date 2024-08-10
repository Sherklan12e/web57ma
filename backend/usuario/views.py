from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Rating,Comment
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'usuarios/profile/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating_range'] = range(1, 6)  # Generar un rango de 1 a 5
        return context
        
@login_required
def rate_profile(request, slug, rating_value):
    profile = get_object_or_404(Profile, slug=slug)
    rating, created = Rating.objects.get_or_create(user=request.user, profile=profile, defaults={'value': rating_value})
    if not created:
        rating.value = rating_value
        rating.save()
    profile.update_average_rating()
    return redirect('profile-detail', slug=profile.slug)

@login_required
def comment_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content').order_by(-'created_at')
        Comment.objects.create(user=request.user, profile=profile, content=content)
    return redirect('profile-detail', slug=profile.slug)