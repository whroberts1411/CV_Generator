from django.shortcuts import redirect, render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

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
    """ Format the cv details for the requested individual for conversion
        to a pdf document. Download it to the caller's PC when done. """

    profile = Profile.objects.get(pk=id)
    fullname = profile.name.replace(' ','_')
    filename = fullname + '_CV.pdf'

    template = loader.get_template('pdf/cv.html')
    html = template.render({'profile':profile})
    options = {
        'enable-local-file-access': None,
        'page-size':'A4',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
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