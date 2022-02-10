from goproduct.models import Go_category


def menu_categories(request):
    categories = Go_category.objects.all()

    return {'menu_categories': categories}
