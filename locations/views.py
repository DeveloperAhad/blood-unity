from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from locations.models import Division, District, Upazila, Union

def get_districts(request):
    division_id = request.GET.get('division_id', None)
    if division_id is None:
        return JsonResponse({'districts': []}, safe=False)
    districts = District.objects.filter(division_id=division_id)
    return JsonResponse({'districts': list(districts.values('id', 'name'))}, safe=False)


def get_upazilas(request):
    district_id = request.GET.get('district_id', None)
    if district_id is None:
        return JsonResponse({'upazilas': []}, safe=False)
    upazilas = Upazila.objects.filter(district_id=district_id)
    return JsonResponse({'upazilas': list(upazilas.values('id', 'name'))}, safe=False)


def get_unions(request):
    upazila_id = request.GET.get('upazila_id', None)
    if upazila_id is None:
        return JsonResponse({'unions': []}, safe=False)
    unions = Union.objects.filter(upazila_id=upazila_id)
    return JsonResponse({'unions': list(unions.values('id', 'name'))}, safe=False)