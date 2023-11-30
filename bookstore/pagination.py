from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def pagination(page, limit, form, serializer):
    paginator = Paginator(form, limit)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    ser = serializer(data, many=True)
    
    result = {
        'current_page': data.number,
        'limit': limit,
        'pages': paginator.num_pages,
        'data': ser.data,
    }
    return result