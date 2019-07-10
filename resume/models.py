from django.db import models

# Create your models here.
class Project(models.Model):

    project_name = models.CharField(
        max_length=300,
        default='None'
        )
    title = models.CharField(
        max_length=300,
        default='None'
        )
    framework = models.CharField(
        max_length=300,
        default='None'
        )
    languages = models.CharField(
        max_length=300,
        default='None'
        )
    description = models.TextField(
        max_length=1000,
        default='None'
        )
    image = models.ImageField(
        upload_to='images/project_images',
        default='None'
        )
    carousel_image1 = models.ImageField(
        upload_to='images/project_images',
        default='None'
        )
    carousel_image2 = models.ImageField(
        upload_to='images/project_images',
        default='None'
        )
    carousel_image3 = models.ImageField(
        upload_to='images/project_images',
        default='None'
        )
    carouselTitle = models.CharField(
        max_length=300,
        default='None'
        )
    video = models.FileField(
        upload_to='videos/project_videos',
        default='None'
        )
    project_url = models.URLField(
        max_length=500,
        default='None'
        )
    github_url = models.URLField(
        max_length=500,
        default='None'
        )

    def __str__(self):
        
        return self.framework


class Blog(models.Model):
    blog_title = models.CharField(
        max_length=500
        )
    description = models.TextField(
        max_length=1000
        )
    pub_date = models.DateField()
    image = models.ImageField(
        upload_to='images/blog_images',
        default='None'
        )
    
    def __str__(self):
        return self.blog_title



class ResumeHardCopy(models.Model):
    title = 'resume'
    CV= models.FileField(
        upload_to='pdf/hard_copy_CV',
        default='None'
        )
    coverletter = models.FileField(
        upload_to='pdf/hard_copy_cover_letter',
        default='None'
        )

    def __str__(self):
        return self.title
