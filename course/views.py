from rest_framework import generics, viewsets, status
from account.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from rest_framework.generics import ListAPIView

from .models import (
    Category, Subcategory, Course,
    Rating, Enrollment, Instructor,
    Video, VideoPlaylist
)
from .serializers import (
    CategorySerializer, SubcategorySerializer, CourseSerializer,
    RatingSerializer, EnrollmentSerializer, InstructorSerializer,
    VideoSerializer, VideoPlaylistSerializer
)

# category

class CategoryViewSet(viewsets.ModelViewSet):
    
        permission_classes = [IsAdminOrReadOnly]
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
    
class SubcategoryViewSet(viewsets.ModelViewSet):
    
        permission_classes = [IsAdminOrReadOnly]
        queryset = Subcategory.objects.all()
        serializer_class = SubcategorySerializer


# course

class CourseListCreateView(generics.ListCreateAPIView):
    
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    # filter_backends = [SearchFilter]
    # search_fields = ['title', 'subcategory']
    
    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category', None)
        subcategory = self.request.query_params.get('subcategory', None)
        search = self.request.query_params.get('search', None)

        try:
            if category:
               queryset = queryset.filter(category_id=category)
            
            if subcategory:
               queryset = queryset.filter(subcategory_id=subcategory)

            if search:
               queryset = queryset.filter(title__icontains=search)
            
        except Exception as e:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        return queryset
    
    

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    # filter_backends = [SearchFilter]
    # search_fields = ['subcategory']
    
   
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def enrollment_list(request):
    
    if request.method == 'GET':
        try: 
           enrollments = Enrollment.objects.filter(student=request.user)
           courses = [enrollment.course for enrollment in enrollments]
           serializer = CourseSerializer(courses, many=True)
           return Response(serializer.data)
       
        except User.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   
    elif request.method == 'POST':
        
        user=User.objects.get(email=request.user).id
        request.data['student']=user
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# .............................................Student................................................................

class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



# Instructor

class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoPlaylistListCreateView(generics.ListCreateAPIView):
    queryset = VideoPlaylist.objects.all()
    serializer_class = VideoPlaylistSerializer

class VideoPlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoPlaylist.objects.all()
    serializer_class = VideoPlaylistSerializer
