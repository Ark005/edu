from django.apps import apps
from core.apps import CoreConfig


class SearchManager:
    def search(self, search_str: str):
        modellist = self.get_models()
        return self._search(modellist, search_str)

    def get_models(self):
        return apps.get_app_config('core').get_models()

    def _search(self, modellist, field_value):
        result_list = []
        for model in modellist:
            if hasattr(model, 'get_search_field'):
                search_field = model.get_search_field()
                search_kwargs = {search_field: field_value}
                result = model.objects.filter(**search_kwargs)
                if result:
                    result_list.append(result)
        return result_list
