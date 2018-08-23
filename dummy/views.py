# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import Learning
from .serializer import learningSerializer
# Create your views here.
def fetchWords(request,language,level):
    if request.method=='GET':
        resp={"language":language,"difficulty":level}
        words = []
        resp.update({"words":words})
        lean = Learning.objects.create(language=language,difficulty=level,words=words,category="xyz")
        lean.save()
        obj=Learning.objects.filter(language='marathi')
        serializer=learningSerializer(obj,many=True)
        return JsonResponse(serializer.data,safe=False)