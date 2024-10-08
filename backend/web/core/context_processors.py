from core.models import Category, SuperCategory


def navbar_categories(request=None) -> dict:
    data = {
        "navbar_categories": Category.objects.filter(is_disabled=False).exclude(short_name__isnull=True).order_by("name"),
        "navbar_supercategories": SuperCategory.objects.all()
    }
    return data
