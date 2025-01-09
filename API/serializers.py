from rest_framework import serializers
from .models import Tag, Category, Status, Project

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    categories = TagSerializer(many=True)
    status = TagSerializer()

    class Meta:
        model = Project
        fields = "__all__"



class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"