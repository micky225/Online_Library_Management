from django.db import models

# Create your models here.

class Book(models.Model):
    CHOICES=(
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )

    BOOK_GENRE=(
        ('Fairytales','Fairytales'),
        ('Historical Fiction', 'Historical Fiction'),
        ('Poetry','Poetry'),
        ('Picture Books','Picture Books'),
        

    )
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.CharField(max_length=50, choices=CHOICES)
    front_page = models.ImageField()
    description = models.CharField(max_length=200)
    summary = models.TextField()
    book_genre = models.CharField(max_length=50, choices=BOOK_GENRE)
    book_code = models.CharField(max_length=50, unique=True)
    edition = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    copies = models.IntegerField()
    published_date = models.DateField()
    published_in = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    


    def __str__(self):
        return self.name
    


    @property
    def imageUrl(self):
        try:
            url = self.front_page.url
        except:
            url = ''
        return url


        