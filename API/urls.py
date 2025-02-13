from django.urls import path
from .views import *
from .views import serve_media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),

    path("run-migrations/", run_migrations),  # Run this to apply migrations
    path("create-superuser/", create_superuser),  # Run this to create an admin user

    path('api/projects/', ProjectListAPIView.as_view(), name="Project-list"),
    path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name="Project-detail"),
    
    path('api/tags/', TagListAPIView.as_view(), name="Tag-list"),
    path('api/tags/<int:pk>/', TagDetailAPIView.as_view(), name="Tag-detail"),

    path('api/category/', CategoryListAPIView.as_view(), name="Category-list"),
    path('api/category/<int:pk>/', CategoryDetailAPIView.as_view(), name="Category-detail"),

    path('api/status/', StatusListAPIView.as_view(), name="Status-list"),
    path('api/status/<int:pk>/', StatusDetailAPIView.as_view(), name="Status-detail"),


    # FRONTEND daTA 
    path('api/social-links/', SocialLinkAPIView.as_view()),
    path('api/social-links/<int:pk>/', SocialLinkAPIView.as_view()),

    path('api/experiences/', ExperienceAPIView.as_view()),
    path('api/experiences/<int:pk>/', ExperienceAPIView.as_view()),

    path('api/education/', EducationAPIView.as_view()),
    path('api/education/<int:pk>/', EducationAPIView.as_view()),

    path('api/awards-and-honors/', AwardAndHonorAPIView.as_view()),
    path('api/awards-and-honors/<int:pk>/', AwardAndHonorAPIView.as_view()),

    path('api/skills/', SkillAPIView.as_view()),
    path('api/skills/<int:pk>/', SkillAPIView.as_view()),

    path('api/resumes/', ResumeAPIView.as_view()),
    path('api/resumes/<int:pk>/', ResumeAPIView.as_view()),
    
    path('api/resume-data/', ResumeDataAPIView.as_view()),
    path('api/resume-data/<int:pk>/', ResumeDataAPIView.as_view()),

    path('test-media/', serve_media),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
