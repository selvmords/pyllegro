from django.db import models


# Create your models here.
class Article(models.Model):
    # pole 150 znakow
    # pole nie moze byc puste
    # mozna stworzyc pole o tym samym tytule
    title = models.CharField(max_length=64, blank=False, unique=False)
    # x
    content = models.TextField(default="")
    # brak roku = 2023
    year = models.PositiveIntegerField(default=2023)
    # img
    imgThumb = models.ImageField(upload_to="media_img", null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
