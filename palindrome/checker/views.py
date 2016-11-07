# from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from checker.models import Palindrome

from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        text = request.POST.get("text")
        palindrome = Palindrome.objects.get(text=text)
        print(palindrome)
        return HttpResponseRedirect(reverse("palindrome_detail_view", args=[palindrome.id]))
        # return HttpResponseRedirect(reverse("child_detail_view", args=[child.id]))

    # def pal():
    #     string = input("Type here: ")
    #     forwards = str(string.lower())
    #     backwards = str(string[::-1].lower())
    #     banned = ', :!.?'
    #     for thingy in banned:
    #         forwards = forwards.replace(thingy, '')
    #         backwards = backwards.replace(thingy, '')
    #     if forwards == backwards:
    #         return('Your phrase: ' + string + ', is a palindrome!')
    #     else:
    #         return('Your phrase: ' + string + ', is not a palindrome')


class PalindromeDetailView(DetailView):
    model = Palindrome
