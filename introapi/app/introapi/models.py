from django.db import models


class User(models.Model):
    intra_id = models.CharField(max_length=50)
    favorite_language = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50)
    favorite_color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'intra_id:{self.intra_id} favorite_language:{self.favorite_language} favorite_food:{self.favorite_food} favorite_color:{self.favorite_color}'
