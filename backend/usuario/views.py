from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Rating,Comment
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import ProfileForm
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
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-detail', slug=profile.slug)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'usuarios/profile/edit.html', {'form': form})

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
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, profile=profile, content=content)
    return redirect('profile-detail', slug=profile.slug)

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment.content = content
        comment.save()
        return redirect('profile-detail', slug=comment.profile.slug)
    return render(request, 'usuarios/profile/editcome.html', {'comment': comment})
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    profile_slug = comment.profile.slug
    if request.method == 'POST':
        comment.delete()
        return redirect('profile-detail', slug=profile_slug)
    return render(request, 'usuarios/profile/deletecome.html', {'comment': comment})
