
from .models import Article
from django.shortcuts import get_object_or_404, render


import json

def index(request):
    allarticle = Article.objects.all()
    #把查询出来的分类封装到上下文里
    context = {
            'allarticle': allarticle,
        }
    return render(request, 'index.html', context)#把上下文传到index.html页面


#以下功能待开发
#列表页
def olist(request,lid):
    allarticle=Article.objects.filter(article_id=lid)#获取通过URL传进来的lid，然后筛选出对应学生信息
    context = {'allarticle': allarticle}
    return render(request, 'list.html', context)


def detail(request, sid):
    article = get_object_or_404(Article, pk=sid)
    data = Article.objects.filter( pk=sid).values_list('bmi','flexibility','coordinate')

    newlist = list(data)
    context={
        'article': article, "data": data,
        'newlist' : json.dumps(*newlist)
        }


    return render(request, 'detail.html', context)
# 搜索页
def search(request):
    pass
# 关于我们
def about(request):
    pass