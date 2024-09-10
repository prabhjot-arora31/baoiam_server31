from django.db import models
from django.conf import settings



# .......................................Instructor.........................................................

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# ..........................................Course...............................................................

class Category(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    program_overview = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # New price field
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    Instructor = models.ForeignKey('Instructor', related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    brochure_file = models.FileField(upload_to='brochures/', blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    curriculum = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title



# .............................................Student................................................................


class Rating(models.Model):
    course = models.ForeignKey(Course, related_name='ratings', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating {self.rating} for {self.course.title}"

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', related_name='enrollments', on_delete=models.CASCADE)  # Correct related_name
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')  

    def __str__(self):
        return f"{self.student.email} - {self.course.title}"

class Video(models.Model):
    playlist = models.ForeignKey('VideoPlaylist', related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField() 

    def __str__(self):
        return self.title

class VideoPlaylist(models.Model):
    instructor = models.ForeignKey(Instructor, related_name='playlists', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
