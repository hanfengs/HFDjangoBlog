from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 100)
    pud_date = models.DateTimeField()

    add_i = models.CharField(max_length = 100, default = '+')

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 200)
    book = models.ForeignKey(Book)
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期

    def __str__(self):
        return self.title

    # class Article(models.Model) :
    #     title = models.CharField(max_length = 100)  #博客题目
    #     category = models.CharField(max_length = 50, blank = True)  #博客标签
    #     date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    #     content = models.TextField(blank = True, null = True)  #博客文章正文
    #     book = models.ForeignKey(Book)
    #
    #     def __unicode__(self) :
    #         return self.title

        # class Meta:  #按时间下降排序
        #     ordering = ['-date_time']
