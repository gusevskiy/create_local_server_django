from django.core.paginator import Paginator

QUANTITY_POSTS = 9


def get_paginated_objects(queryset, request):
    paginator = Paginator(queryset, QUANTITY_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {"page_obj": page_obj}


