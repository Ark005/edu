class SearchSerializer:
    def serialize(self,rezult):
        item_list_serialized = []
        for qs in rezult:
            for i in qs:
                item_serialized = {
                    'name': i.name,
                    'link': i.get_absolute_url()
                }
                if hasattr(i, "get_search_description"):
                    item_serialized["description"] = i.get_search_description()
                item_list_serialized.append(item_serialized)
        return item_list_serialized
    
    def song_serialize(self,rezult):
        song_list_serialized = []
        for i in rezult:
           song_serialized = {
               'name': i.name,
               'slug': i.slug,
               'singer': i.singer,
               'author': i.author
           }
           song_list_serialized.append(song_serialized)
        print (song_list_serialized)
        return song_list_serialized
    
