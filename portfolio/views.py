from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Achievement, Certification, Education, Experience, Profile, Project, Skill


def shared_context():
    return {'profile': Profile.objects.first(), 'skills': Skill.objects.all()}


def home(request):
    context = shared_context()
    context.update({'projects': Project.objects.filter(is_featured=True)[:3], 'certifications': Certification.objects.all()[:3]})
    return render(request, 'home.html', context)


def about(request):
    context = shared_context()
    context['education'] = Education.objects.all()
    context['experience'] = Experience.objects.all()
    context['achievements'] = Achievement.objects.all()
    return render(request, 'about.html', context)


def projects(request):
    context = shared_context()
    context['projects'] = Project.objects.all()
    return render(request, 'projects.html', context)


def project_detail(request, slug):
    context = shared_context()
    context['project'] = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', context)


def resume(request):
    context = shared_context()
    context.update({'education': Education.objects.all(), 'experience': Experience.objects.all(), 'certifications': Certification.objects.all(), 'achievements': Achievement.objects.all()})
    return render(request, 'resume.html', context)


def contact(request):
    context = shared_context()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            profile = context['profile']
            if profile and profile.email:
                send_mail(f'Portfolio contact: {contact_message.subject}', contact_message.message, None, [profile.email], fail_silently=True)
            messages.success(request, 'Thanks for reaching out. Your message is on its way.')
            return redirect(f'{reverse("contact")}#contact-form')
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)


def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')


def sitemap(request):
    return render(request, 'sitemap.xml', content_type='application/xml')