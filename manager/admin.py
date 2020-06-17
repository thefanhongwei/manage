from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.site_header = '儿童体侧资源管理器'
admin.site.site_title = 'BALLLIB'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age','gender' , 'created_time','height','weight','waist','bmi','spine','leg','balance','flexibility','coordinate','user')
    # 文章列表里显示想要显示的字段
    list_per_page = 10
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    #后台数据列表排序方式
    #list_editable 设置默认可编辑字段，在列表里就可以编辑
    #list_editable = ['name','gender']
