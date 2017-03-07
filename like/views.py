from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def create_update_like(request, post_pk, like):
    pass
