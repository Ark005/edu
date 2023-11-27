def song_detail_view(request: HttpRequest, slug: str):
   
    object_list = get_object_list(slug)
    if object_list == False: 
        return HttpResponse(status=404)
    return render(request, template_name='core/author_details.html', context={'song_list': object_list})