from rest_framework import serializers
from account.models import User
from rest_framework.response import Response
from .models import (
    Category, Subcategory, Course,
    Rating, Enrollment, Instructor,
    Video, VideoPlaylist
)

# ..........................................Course..............................................................

class SubcategorySerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all()) 

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category', 'description', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories', 'label', 'description', 'created_at']


class CourseSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 
            'category', 'subcategory', 'price', 'program_overview', 'brochure_file',
            'thumbnail_image', 'curriculum'
        ]

# .............................................Student................................................................

class RatingSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField() 

    class Meta:
        model = Rating
        fields = ['id', 'course', 'rating', 'comment']

# class EnrollmentSerializer(serializers.ModelSerializer):
#     student = serializers.EmailField(write_only=True)
#     course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())  # Accept course ID input
#     course_detail = CourseSerializer(source='course', read_only=True)  # Serialize course details

#     class Meta:
#         model = Enrollment
#         fields = ['id', 'student', 'course', 'course_detail', 'created_at']
        
   
class EnrollmentSerializer(serializers.ModelSerializer):
    
    # student = serializers.EmailField(source='student.email', read_only=True)
    # course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'created_at']


    # def validate(self, attrs):
      
    #     user = self.context.get('student')
    #     user=User.objects.get(email=user)
    #     print(user.id, "user", request.data)
    #     Enrollment.objects.save(student=user.id)
        
    #     return attrs 
   
# .......................................Instructor............................................................

class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True) 

    class Meta:
        model = Instructor
        fields = [
            'id', 'first_name', 'last_name', 'bio',
            'email', 'hire_date', 'courses'
        ]

class VideoSerializer(serializers.ModelSerializer):
    playlist = serializers.StringRelatedField()  

    class Meta:
        model = Video
        fields = ['id', 'playlist', 'title', 'url']

class VideoPlaylistSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()  
    videos = VideoSerializer(many=True, read_only=True) 

    class Meta:
        model = VideoPlaylist
        fields = ['id', 'teacher', 'title', 'description', 'videos']
