from django.db import models


class Portfolio(models.Model):
    filter_name = models.CharField(max_length=200)
    filter_class = models.CharField(max_length=200)
    title = models.CharField(max_length=200, unique=True) # 프로젝트이름
    slug = models.SlugField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=100)        # 소제목
    lang = models.CharField(max_length=200)             # 사용언어
    dates = models.CharField(max_length=50)             # 제작기간
    content = models.TextField()                        # 프로젝트 설명
    key = models.CharField(max_length=50)        # 프로젝트 유튜브 key
    github_url = models.URLField('Github URL')          # 프로젝트 코드 주소
    photo = models.ImageField(upload_to='portfolio/%Y/%m/%d', default='portfolio/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



