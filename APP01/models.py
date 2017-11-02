from django.db import models

# Create your models here.


class Survery(models.Model):
    """
    问卷
    """
    name = models.CharField(verbose_name="调查问卷名称", max_length=128, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name=u"问卷创建日期")


class SurveryItem(models.Model):
    """
    问卷选项
    """
    name = models.CharField(u"调查问题", max_length=255, help_text=u"此处填写需要调查的问题...")
    date = models.DateField(auto_now_add=True)
    answer_type_choices = (('single', "单选"),
                           ('score', "打分"),
                           ('suggestion', "建议"),
                           )
    answer_type = models.CharField(u"问题类型", choices=answer_type_choices, default='score', max_length=32)


class SurveryChoices(models.Model):
    """
    问卷选项答案
    """
    question = models.ForeignKey(SurveryItem, verbose_name='问题')
    content = models.CharField(verbose_name='答案内容', max_length=256)
    points = models.IntegerField(verbose_name='分值', )


class SurveryRecord(models.Model):
    """
    问卷记录
    """
    survery = models.ForeignKey(Survery, verbose_name="问卷")
    survery_item = models.ForeignKey(verbose_name="调查项", to='SurveryItem')

    score = models.IntegerField(verbose_name="评分", blank=True, null=True)
    single = models.ForeignKey(verbose_name='单选', to='SurveryChoices', blank=True, null=True)

    suggestion = models.TextField(verbose_name="建议", max_length=1024, blank=True, null=True)

    date =models.DateTimeField(verbose_name="答题日期", auto_now_add=True)