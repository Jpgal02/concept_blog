from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# 글의 분류(일상, 유머, 정보)
class Category(models.Model):
    name=models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex.일상)")
    def __str__(self):
        return self.name

COUNTRY_CHOICES=[
    ("미확인","미확인"),
    ("가능", "가능"),
    ("불가능", "불가능"),
    ("조건부가능", "조건부가능"),
]

THESIS_CHOICES=[
    ("유", "유"),
    ("무", "무"),
]

PATENT_CHOICES=[
    ("유", "유"),
    ("무", "무"),
]

REWARD_CHOICES=[
    ("유", "유"),
    ("무", "무"),
]


# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="컨셉명")
    tentative_title = models.CharField(max_length=200, blank=True, verbose_name="가칭명")
    inci_name=models.CharField(max_length=200, verbose_name="INCI명")
    ingredient = models.CharField(max_length=200, verbose_name="국문명")
    title_image=models.ImageField(verbose_name="대표 이미지", upload_to='title_images/', blank=True, null=True, default='default_image.jpg')
    export_china=models.CharField(max_length=6, choices=COUNTRY_CHOICES , verbose_name="중국수출여부")
    thesis=models.CharField(max_length=2, choices=THESIS_CHOICES, verbose_name="논문 유/무")
    patent=models.CharField(max_length=2, choices=PATENT_CHOICES, verbose_name="특허 유/무")
    reward=models.CharField(max_length=2, choices=REWARD_CHOICES, verbose_name="수상 유/무")
    thesis_name=models.CharField(max_length=100, blank=True, verbose_name="논문명")
    patent_number=models.CharField(max_length=50, blank=True, verbose_name="특허 번호")
    reward_name=models.CharField(max_length=100, blank=True, verbose_name="수상명")
    efficacy_image=models.ImageField(verbose_name="효능/임상 이미지", upload_to='efficacy_images/', blank=True, null=True, default='default_image.jpg')
    content = models.TextField(verbose_name="주요 내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자") #유저가삭제되면내용삭제
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="생성일자")
    updateDate = models.DateTimeField(auto_now_add=True, verbose_name="수정일자")
    #하나의 글을 여러가지의 분류에 해당될 수 있다. (ex. 정보, 유머), 하나의 분류에는 여러가지 글이 포함될 수 있죠.(정보 카테고리에 글 10개)
    #다대다 관계
    category = models.ManyToManyField(Category, help_text='글의 분류를 설정하세요.', verbose_name="효능 카테고리")
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True, verbose_name="북마크")
   
    def  __str__(self):
        return self.title
    
    #1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.pk)]) 
    # 내용이 300자 넘는가
    def is_content_more300(self):
        return len(self.content) > 300
    # 300자 만큼 잘라서. 내용 받는 코드 작성
    def get_content_under300(self):
        return self.content[:300]

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%s'%(self.post.title, self.name)