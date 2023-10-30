from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer


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


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
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