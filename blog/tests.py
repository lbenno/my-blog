from django.test import TestCase
import os
# from django.contrib.sites.models import Site
from django.conf import settings
from django.http import request, response

# Create your tests here.

#def site(request):
 #   return {'SITE_URL': settings.SITE_URL}

#current_site = Site.objects.get_current()
#current_site.domain

def test_detail():
    test = settings
    test1 = {response: response.ResponseHeaders}
    #test2 = {'response': response.JsonResponse}
    return test, test1 #, test2