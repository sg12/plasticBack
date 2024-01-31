from apps.accounts.yasg import doc_review_update, doc_review_create


def auto_doc(func):
    def wrapper(request, *args, **kwargs):
        method = request.method
        decorator = None

        if method == 'GET':
            if len(kwargs) > 0:
                decorator = None
            else:
                decorator = ""
        elif method == 'POST':
            decorator = ""
        elif method in ['PUT', 'PATCH']:
            decorator = ""
        elif method == 'DELETE':
            decorator = ""

        if decorator:
            return decorator(func(request, *args, **kwargs))

        return func(request, *args, **kwargs)
    return wrapper
