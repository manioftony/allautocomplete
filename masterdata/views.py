from django.shortcuts import render
from django.http import HttpResponse
from masterdata.models import Profile
import json
# Create your views here.
def home(request):
    return render(request, "index.html", locals())


def profiledata(request):
    # import ipdb;ipdb.set_trace()
    if request.is_ajax():
        qq = request.GET.get('term', '')
        drugs = Profile.objects.filter(name__icontains = qq )[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.pk
            drug_json['label'] = drug.name
            drug_json['value'] = drug.name
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)