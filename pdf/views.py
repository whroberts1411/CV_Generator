
from django.shortcuts import redirect, render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import io
from weasyprint import HTML, CSS
from django.template.loader import render_to_string

#------------------------------------------------------------------------------
def index(request):
    """ Display the site's start page - it just has a bit of information
        about how to use the site.  """

    return render(request, 'pdf/index.html')

#------------------------------------------------------------------------------
def accept(request):
    """ Get the cv data entered by the user on the screen, and store
        it on the database.  """

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        mobile = request.POST.get('mobile','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous_work','')
        skills = request.POST.get('skills','')

        profile = Profile(name=name,email=email,phone=phone, mobile=mobile,
                        summary=summary,degree=degree,school=school,
                        university=university,previous_work=previous_work,
                        skills=skills)
        profile.save()

    return render(request, 'pdf/accept.html')

#------------------------------------------------------------------------------
def cv(request, id):
    """ Populate the CV template, convert it to a pdf format and download
        it to the user's machine (or display a dialogue box, depending on the
        way the browser has been configured)   """

    from django.conf import settings
    css = str(settings.BASE_DIR) + '/static/' + 'style.css'

    profile = Profile.objects.get(pk=id)
    fullname = profile.name.replace(' ','_')
    filename = fullname + '_CV.pdf'

    html_string = render_to_string('pdf/cv.html',{'profile':profile})
    html = HTML(string=html_string)
    pdf = html.write_pdf(stylesheets=[CSS(css),
    'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css'])
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    return response

#------------------------------------------------------------------------------
def list(request):
    """ Display a list of all users, with the option to download their cv. """

    profiles = Profile.objects.all().order_by('name')
    return render(request, 'pdf/list.html', {'profiles':profiles})

#------------------------------------------------------------------------------
def update(request, id):
    """ Update the cv that has been requested. """

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        mobile = request.POST.get('mobile','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous_work','')
        skills = request.POST.get('skills','')

        profile = Profile.objects.filter(id=id).update(name=name,
                        email=email,phone=phone, mobile=mobile,
                        summary=summary,degree=degree,school=school,
                        university=university,previous_work=previous_work,
                        skills=skills)
        profiles = Profile.objects.all()
        return render(request, 'pdf/list.html', {'profiles':profiles})

    cv = Profile.objects.get(id=id)
    return render(request, 'pdf/update.html', {'cv':cv})

#-------------------------------------------------------------------------------