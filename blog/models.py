from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()  # 문자열의 길이 제한 없음
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # author: 추후 작성

    def __str__(self):
        return f'[{self.pk}]{self.title}'
