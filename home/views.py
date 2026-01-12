from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from blog.models import Post
from .forms import ContactForm


def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)

def home(request):
    # Get latest blog posts
    latest_posts = Post.objects.filter(status='published').order_by('-published_date')[:3]

     # My introduction
    intro = {
        'title': 'Prosper O. Popoola',
        'tagline': 'Transforming business needs into technical solutions',
        'description': 'Expert in requirements analysis, business process reengineering, process optimization, and stakeholder management.',
        'highlights': [
            'IT Service Delivery & Management',
            'Process Improvement & Optimization',
            'Stakeholder Management',
            'Business Process Re-engineering',
        ]
    }

    context = {
        'intro': intro,
        'latest_posts': latest_posts,
    }
    return render(request, 'home/index.html', context)

def about(request):
    professional_summary = {
        'title': 'Business Analyst',
        'summary': 'Results-driven Business Analyst with 5+ years of experience in...',
        'skills': [
            'Requirements Gathering & Analysis',
            'Process Modeling & Optimization',
            'Stakeholder Management',
            'Agile/Scrum Methodologies',
            'Data Analysis & Visualization',
            'UML & BPMN',
            'JIRA, Confluence, Visio',
            'IT Operation, Network Design and Management',
        ],

    }
    return render(request, 'home/about.html' , {'summary':professional_summary})

def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Format the email
            email_message = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}

            Message:
            {message}
            """

            # Send email (for now, just print to console)
            try:
                send_mail(
                    subject=f'Portfolio Contact: {subject}',
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['email@popoola.org.ng'],  # Change to your email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully! I\'ll get back to you soon.')
                return redirect('contact')
            except Exception as e:
                print(f"Email error:{e}")
                messages.error(request, "There was an error sending your message, try again later")

    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})