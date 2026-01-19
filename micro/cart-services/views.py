from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def add_to_cart(request):
    return Response({'message': 'Book added to cart'})