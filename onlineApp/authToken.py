from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def getToken(Token):
    token = Token.objects.get_or_create(user = 'root',password='1234')
    return Response({'token':token.key})