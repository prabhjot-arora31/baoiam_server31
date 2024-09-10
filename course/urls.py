from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    
   
    CategoryViewSet, SubcategoryViewSet,
    
    CourseListCreateView, CourseDetailView,
   
    enrollment_list, 
    

    RatingListCreateView, RatingDetailView,
    InstructorListCreateView, InstructorDetailView,
    VideoListCreateView, VideoDetailView,
    VideoPlaylistListCreateView, VideoPlaylistDetailView
)


router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)



urlpatterns = [
  
    # Category Subcategory URLs
    path('', include(router.urls)),


    # Course URLs
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),


    # Enrollment URLs
    path('enrollments/', enrollment_list),


# .........................................................to be completed....................................................................
    # Rating URLs
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),

    # Instructor URLs
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),

    # Video URLs
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),

    # Video Playlist URLs
    path('playlists/', VideoPlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', VideoPlaylistDetailView.as_view(), name='playlist-detail'),
]
