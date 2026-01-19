from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def list_books(request):
    return Response([
{'id': 1, 'title': 'Clean Architecture', 'price': 20.5}
])