from django.shortcuts import render
# from .models import Profile, Skill, Experience, Education

def index(request):
    # profile = Profile.objects.first()
    # skills = Skill.objects.all()
    # experiences = Experience.objects.all()
    # educations = Education.objects.all()
    return render(request, 'portfolio_app/index.html')
    # , {
    #     'profile': profile,
    #     'skills': skills,
    #     'experiences': experiences,
    #     'educations': educations,
    # })
