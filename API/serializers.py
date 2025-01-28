from rest_framework import serializers
from .models import Tag, Category, Status, Project
from .models import SocialLink, Experience, Education, AwardAndHonor, Skill, Resume, ResumeData

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
    categories = CategorySerializer(many=True)
    status = StatusSerializer()

    class Meta:
        model = Project
        fields = "__all__"



class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AwardAndHonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardAndHonor
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Resume
        fields = '__all__'

class ResumeDataSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    education = EducationSerializer(many=True)
    awards_and_honors = AwardAndHonorSerializer(many=True)
    skills = SkillSerializer(many=True)
    resumes = ResumeSerializer(many=True)

    class Meta:
        model = ResumeData
        fields = '__all__'