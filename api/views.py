from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer, ProductDetailSerializer
from .models import AccountCreationDetails, ProductDetails

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint': '/users/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint': '/users/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single user'
        },
        {
            'Endpoint': '/AuthenticateUser/',
            'method': 'GET',
            'body': None,
            'description': 'Returns success if the user exists'
        },
        {
            'Endpoint': '/CreateUser/',
            'method': 'POST',
            'body': None,
            'description': 'Returns success if the user is created'
        },
        {
            'Endpoint': '/Products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/Products/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product with the specified productId'
        },

    ]

    return Response(routes)


@api_view(['GET'])
def GetUsers(request):
    users=AccountCreationDetails.objects.all()
    serializer= AccountSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetUser(request,key):
    users=AccountCreationDetails.objects.get(UserId=key)
    serializer= AccountSerializer(users,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def AuthenticateUser(request):
    email=request.GET.get('email')
    email=email.replace('%40', '@')

    password = request.GET.get('password')
    account=AccountCreationDetails.objects.get(EmailID=email)
    if account.Password==password:
        #response={'status':'success', 'message': 'Login successful.'}
        serializer= AccountSerializer(account,many=False)
        return Response(serializer.data)
    else:
        response = {'status': 'error', 'message': 'Invalid credentials.'}
        return Response(response)
    

@api_view(['POST'])
def CreateUser(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def GetProducts(request):
    products = ProductDetails.objects.all()
    serializers = ProductDetailSerializer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def GetProduct(request):
    product_id = request.GET.get('product_id')
    
    # Handle URL-encoded characters (%3D)
    product_id = product_id.replace('%3D', '=')
    
    
    products = ProductDetails.objects.get(product_id=product_id)
    serializer = ProductDetailSerializer(products, many=False)
    return Response(serializer.data)
    