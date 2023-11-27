from django.views.generic import View
from django.http.response import HttpResponse
from core.src.search_manager import SearchManager
from core.serializers.search_serializer import SearchSerializer
import json
from django.shortcuts import render

class SearchView(View):
    def get(self,request):
        search_query = request.GET.get('search')
        if search_query:
            result = SearchManager().search(search_query)
            response_data = SearchSerializer().serialize(result)
            return render (request,template_name='core/search.html',context={'search_data':response_data})
        else:
            return render (request,template_name='core/search.html')
    
        
