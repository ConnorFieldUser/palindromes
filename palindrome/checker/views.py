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
    banned = ', :!.a'
    for thingy in banned:
        forwards = forwards.replace(thingy, '')
        # print(new_f)
        backwards = backwards.replace(thingy, '')
        # print(new_b)

    if forwards == backwards:
        return True
    else:
        # print(forwards)
        # print(backwards)
        return False


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        text = request.POST.get("text")
        pal_test = pal(text)
        # print(pal_test)
        if pal_test:
            try:
                palindrome = Palindrome.objects.get(text=text)
                return HttpResponseRedirect(reverse("palindrome_detail_view", args=[palindrome.id]))
            except ObjectDoesNotExist:
                #  crete the palendrome in the db
                return HttpResponseRedirect("create_palindrome")
        else:
            return HttpResponseRedirect("fail")


class PalindromeDetailView(DetailView):
    model = Palindrome


class PalindromeCreateView(CreateView):
    model = Palindrome
    fields = ['text']
    success_url = "/"


class FailView(TemplateView):
    template_name = "fail.html"

    def post(self, request):
        text = request.POST.get("text")
        pal_test = pal(text)
        # print(pal_test)
        if pal_test:
            try:
                palindrome = Palindrome.objects.get(text=text)
                return HttpResponseRedirect(reverse("palindrome_detail_view", args=[palindrome.id]))
            except ObjectDoesNotExist:
                #  crete the palendrome in the db
                return HttpResponseRedirect("create_palindrome")
        else:
            return HttpResponseRedirect("fail")
