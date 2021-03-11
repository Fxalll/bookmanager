from django.shortcuts import render,redirect
from app01 import models

# Create your views here.
def publisher_list(request):
    all_publishers = models.Publisher.objects.all().order_by('-id')
    return render(request,'publisher_list.html',{'all_publishers': all_publishers})

def publisher_add(request):
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher_add.html',{'error':'请不要留空'})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html',{'error':'出版社名称已存在'})
        models.Publisher.objects.create(name=pub_name)
        return redirect('/publisher_list/')

    return render(request,'publisher_add.html')

def publisher_del(request):
    pk = request.GET.get('pk')
    models.Publisher.objects.get(pk=pk).delete()
    return redirect('/publisher_list/')

def publisher_editor(request):
    pk = request.GET.get('pk')
    pub_obj = models.Publisher.objects.get(pk=pk)


    if request.method == 'GET':
        return render(request,'publisher_editor.html',{'pub_obj':pub_obj})
    else:
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher_add.html',{'error':'请不要留空'})
        pub_obj.name = pub_name
        pub_obj.save()
        return redirect('/publisher_list/')

def book_list(request):
    all_books = models.Book.objects.all().order_by('-id')

    return render(request,'book_list.html',{'all_books': all_books})

def book_add(request):
    all_publisher = models.Publisher.objects.all()
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        if not book_name:
            return render(request, 'book_add.html',{'error':'请不要留空','all_publisher': all_publisher})
        if models.Book.objects.filter(name=book_name):
            return render(request, 'book_add.html',{'error':'书名重复','all_publisher': all_publisher})
        models.Book.objects.create(name=book_name,publisher_id=pub_id)
        return redirect('/book_list/')
    return render(request,'book_add.html',{'all_publisher': all_publisher})

def book_del(request):
    pk = request.GET.get('pk')
    models.Book.objects.get(pk=pk).delete()
    return redirect('/book_list/')

def book_editor(request):
    pk = request.GET.get('pk')
    book_obj = models.Book.objects.get(pk=pk)
    all_publisher = models.Publisher.objects.all()

    if request.method == 'GET':
        return render(request, 'book_editor.html',{'book_obj': book_obj,'all_publisher':all_publisher})
    else:
        book_name = request.POST.get('book_name')
        publisher_id = request.POST.get('publisher_id')
        if not book_name:
            return render(request, 'book_editor.html',{'error':'请不要留空','book_obj': book_obj,'all_publisher':all_publisher})
        book_obj.name = book_name
        book_obj.publisher_id = publisher_id
        book_obj.save()
        return redirect('/book_list/')

def author_list(request):
    all_author = models.Anthor.objects.all().order_by('-id')
    return render(request,'author_list.html',{'all_authors':all_author})

def author_add(request):
    all_books = models.Book.objects.all()
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')
        if not author_name:
            return render(request,'author_add.html',{'error':'请不要留空','all_books':all_books})
        author_obj = models.Anthor.objects.create(name=author_name)
        author_obj.books.set(book_id)
        return redirect('/author_list/')
    return render(request,'author_add.html',{'all_books': all_books})

def author_del(request):
    pk = request.GET.get('pk')
    models.Anthor.objects.get(pk=pk).delete()
    return redirect('/author_list/')

def author_editor(request):
    pk = request.GET.get('pk')
    author_obj = models.Anthor.objects.get(pk=pk)
    all_books = models.Book.objects.all()


    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids')
        if not author_name:
            return render(request, 'author_editor.html',{'error':'请不要留空','author_obj': author_obj,'all_books':all_books})
        author_obj.name = author_name
        author_obj.save()
        author_obj.books.set(book_ids)
        return redirect('/author_list/')

    return render(request, 'author_editor.html',{'author_obj': author_obj,'all_books':all_books})
