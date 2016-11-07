# from django.shortcuts import render

from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView

from checker.models import Palindrome

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def pal(string):
    forwards = str(string.lower())
    backwards = str(string[::-1].lower())
    banned = ', :!.?'
    for thingy in banned:
        forwards = forwards.replace(thingy, '')
        backwards = backwards.replace(thingy, '')
        if forwards == backwards:
            return True
        else:
            return False


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        text = request.POST.get("text")
        pal_test = pal(text)
        print(pal_test)
        if pal_test:
            try:
                palindrome = Palindrome.objects.get(text=text)
                return HttpResponseRedirect(reverse("palindrome_detail_view", args=[palindrome.id]))
            except ObjectDoesNotExist:
                return HttpResponseRedirect("/")
                #  crete the palendrome in the db
        else:
            return HttpResponseRedirect("/")


class PalindromeDetailView(DetailView):
    model = Palindrome


class PalindromeCreateView(CreateView):
    model = Palindrome
    fields = ['text']
    success_url = "/"
