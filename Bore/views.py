from django.shortcuts import render, redirect
from urllib.parse import urlencode
import requests
from django.http.response import HttpResponse
from .forms import Activity, NumberTriviaForm
from django.core.cache import caches

def ActivityFormView(request):
    actvity = ""
    form = Activity()
    if request.method == "POST":
        form = Activity(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            field_label = list(form.fields.keys())
            type = form.cleaned_data.get("type")
            participant = form.cleaned_data.get("participant", None)
            accessibility = form.cleaned_data.get("accessibility", None)
            price = form.cleaned_data.get("price",None)
            activity_filter = [type,participant, accessibility, price]
            #print(type)
            query = {}
            for i, x in enumerate(activity_filter):
                #print(field_label[i])
                if x is not None and x != "":
                    #print(x)
                    query[str(field_label[i])] = x
            #print(query)
            base_url = "http://www.boredapi.com/api/activity/"
            query = urlencode(query)
            full_url = f"{base_url}?{query}"
            print(full_url)
            response = requests.get(full_url, "json")
            actvity = response.json()
            print(actvity)

    context = {
        "form":form,
        "activity":actvity
    }
    return render(request, "activityform.html", context)


def NumberFormView(request):
    form = NumberTriviaForm()
    text = ""
    if request.method == "POST":
        form = NumberTriviaForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data.get("type")
            number = form.cleaned_data.get("number")
            url = f"http://numbersapi.com/{number}/{type}"
            response = requests.get(url, 'json')

            text = response.json()["text"]

    context = {
        "form":form,
        "text":text
    }
    return render(request, "numberform.html", context)

def Home(request):
    return render(request, "home.html" )
