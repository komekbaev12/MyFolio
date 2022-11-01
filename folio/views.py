from django.shortcuts import render
from folio.models import Companies, Services, Projects


def index(request):
    company = Companies.objects.all()
    service = Services.objects.all()
    project = Projects.objects.all()
    context = {
        'company':company,
        'service':service,
        'project':project
    }
    return render(request, 'folio/index.html', context)
def detail(request, pk):
    companylist = Companies.objects.filter(id=pk)
    return render(request,'folio/detail.html', {'companylist' : companylist})