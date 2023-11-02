from rest_framework import serializers
from home.models import Person, Color
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
            if data['username']:
                if User.objects.filter(username=data['username']).exists():
                    raise serializers.ValidationError("Username already exists")
                
            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError("email already exists")
                
            return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        print(validated_data)
        return validated_data
    

class LoginSerializer(serializers.Serializer):
    # email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name', 'id']

class PeopleSerializer(serializers.ModelSerializer):
    # color = ColorSerializer()
    # color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1
        # fields = ['name', 'age']
        # exclude = ['name']

    # def validate_age(self, age):
    #     if age < 18:
    #         raise serializers.ValidationError("Age must be greater than 18")
    #     return age

    # def validate_name(self, name):
    #     special_characters = "~!@#$%^&*()_+|:<>?`-=[]\;',./"
    #     if any(c in special_characters for c in name):
    #         raise serializers.ValidationError("Name must not contain special characters")
    #     return name

    def get_color_info(self, obj):
        if obj.color is not None:
            color_obj = Color.objects.get(id=obj.color.id)
            return {'color_name': color_obj.color_name, 'hex_code': '#000000'}
        else:
            return {'color_name': None, 'hex_code': None}
        
        # color_obj = Color.objects.get(id = obj.color.id)

        # return ({'color_name' : color_obj.color_name, 'hex_code' : '#000000'})

    def validate(self, data):
        special_characters = "~!@#$%^&*()_+|:<>?`-=[]\;',./"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name must not contain special characters")


        # if data['age'] < 18:
        #     raise serializers.ValidationError("Age must be greater than 18")
        return data