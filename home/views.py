from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer, LoginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        
        print(serializer.data)
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        print(user)
        if not user:
            return Response({
                'status' : False,
                'message' : 'Invalid credentials',
            }, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            'status' : True,
            'message' : 'User logged in successfully',
            'token' : str(token)
        },
        status=status.HTTP_200_OK)

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({
            'status' : True,
            'message' : 'User created successfully'
        },
        status=status.HTTP_201_CREATED)

class PersonAPI(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
        # return Response({'message' : 'This is a get request'})
    
    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        # return Response({'message' : 'This is a post request'})
    
    def put(self, request):
        data = request.data
        refObj = Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(instance=refObj , data=request.data)
        # serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        # return Response({'message' : 'This is a put request'})
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        # return Response({'message' : 'This is a patch request'})
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'msg': 'Data deleted successfully'})   
        # return Response({'message' : 'This is a delete request'})


@api_view(['GET', 'POST'])
def index(request):
    courses = {
            'course_name' : 'Python',
            'learn' : ['Django', 'Flask', 'REST API', 'Machine Learning', 'Data Science'],
            'courser_provider' : 'Udemy'
            }
    if request.method == 'GET':
        print(request.GET.get('search'))
        print("GET method")
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print('*****')
        print(data)
        print('*****')
        print("POST method")
        return Response(courses)

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({'message' : 'success'})
    
    return Response(serializer.errors)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        refObj = Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(instance=refObj , data=request.data)
        # serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'msg': 'Data deleted successfully'}) 

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search is not None:
            queryset = queryset.filter(name__startswith=search)
        serializer = PeopleSerializer(queryset, many=True)
        return Response({'status': 200, 'data' : serializer.data})