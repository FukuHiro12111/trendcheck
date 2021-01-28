from django.db import models

class News(models.Model):
    title = models.CharField()
    link = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)

    # クラスオブジェクトを文字列で返すメソッド
    def __str__(self):
        return self.title
