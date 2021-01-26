from rest_framework import serializers

from providers.models import Employee, Title, Clinic
from providers.custom_serializer_fields import SlugRelatedFieldCreate


class TitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Title
        fields = ("name",)


    def create(self, validated_data):
        title, _ = Title.objects.update_or_create(
            name=validated_data['name']
        )
        return title


class ClinicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clinic
        fields = ("name",)

    def create(self, validated_data):
        clinic, _ = Clinic.objects.update_or_create(
            name=validated_data['name']
        )
        return clinic



class EmployeeSerializer(serializers.ModelSerializer):

    name_given = serializers.CharField(source="given_name")    
    name_family = serializers.CharField(source="family_name")    
    title = SlugRelatedFieldCreate(slug_field='name', queryset=Title.objects.all())
    clinic = SlugRelatedFieldCreate(slug_field='name', queryset=Clinic.objects.all())

    class Meta:
        model = Employee
        fields = ("name_given", "name_family", "title", "clinic")

    def create(self, validated_data):
        employee, _ = Employee.objects.update_or_create(
            given_name=validated_data['given_name'],
            family_name=validated_data['family_name'],
            title=validated_data['title'],
            clinic=validated_data['clinic'],
        )
        return employee
