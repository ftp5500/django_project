from django.shortcuts import render
from django.http import HttpResponse
#مثال لانشاء مصفوفة داخلها قاموس عن الكتاب ومؤلفه والمحتوى وسنة الطبع
posts = [

    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content' :'First post Content',
        'date_posted': ' August 27, 2018'


    },

    {   'author' :'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'First post Content',
        'date_posted': ' Augest 28, 2018'

    }
]


#انشاء وظيفة لفتح صفحة html تحمل blog home
def home(request):

    context = {
        'posts' : posts

    }
   #return HttpResponse('<h1>Blog Home</h1>')
    return render(request , 'blog/home.html',context)
#انشاء وظيفة لفتح صفحة اخرى html تحمل  ولكن مسارها بعد الصفحة السابقةblog about

def about(request):
    return render(request,'blog/about.html' ,{'title':'About'})



