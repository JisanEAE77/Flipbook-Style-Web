from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from accounts.models import *
from bookstore.models import *
import math

@login_required
def dashboard(request, *args, **kwargs):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'accounts/dashboard.html', context)

def bookstore(request, *args, **kwargs):
    p = -1
    n = 1
    books = Book.objects.all()
    pages = len(books)
    pages = range(math.ceil(pages/12))
    books = Book.objects.all().order_by('-id')[:12]
    try:
        checknext = Book.objects.all().order_by('-id')[12]
    except:
        n = -1
    context = {
        "books1": books[0:4],
        "books2": books[4:8],
        "books3": books[8:12],
        "title": "Library",
        "prev": p,
        "next": n,
        "pages": pages,
    }
    if request.method == "POST":
        query = request.POST['query']

        if query:
            searchedbooks = list()
            i = 0
            while True:
                if Book.objects.filter(name__icontains=query)[i:i+4]:
                    books = Book.objects.filter(name__icontains=query)[i:i+4]
                    searchedbooks.append(books)
                    i = i + 4
                else:
                    if i == 0:
                        books = Book.objects.filter(name__icontains=query)[i:i+4]
                    break
            context = {
                "books": searchedbooks,
                "title": "Library",
                "prev": p,
                "next": n,
                "pages": pages,
            }
        else:
            context = {
                "error": "No books found for this query....",
                "title": "Library",
                "prev": p,
                "next": n,
                "pages": pages,
            }

        if not books:
            context = {
                "error": "No books found for this query....",
                "title": "Library",
                "prev": p,
                "next": n,
                "pages": pages,
            }
    return render(request, 'accounts/bookstore.html', context)

def blog(request, *args, **kwargs):
    p = -1
    n = 1
    books = Blog.objects.all()
    pages = len(books)
    pages = range(math.ceil(pages/12))
    books = Blog.objects.all().order_by('-id')[:12]
    try:
        checknext = Blog.objects.all().order_by('-id')[12]
    except:
        n = -1
    context = {
        "books1": books[0:4],
        "books2": books[4:8],
        "books3": books[8:12],
        "title": "Blog",
        "prev": p,
        "next": n,
        "pages": pages,
    }
    if request.method == "POST":
        query = request.POST['query']

        if query:
            searchedbooks = list()
            i = 0
            while True:
                if Blog.objects.filter(title__icontains=query)[i:i+4]:
                    books = Blog.objects.filter(title__icontains=query)[i:i+4]
                    searchedbooks.append(books)
                    i = i + 4
                else:
                    if i == 0:
                        books = Blog.objects.filter(title__icontains=query)[i:i+4]
                    break
            context = {
                "books": searchedbooks,
                "title": "Blog",
                "prev": p,
                "next": n,
                "pages": pages,
            }
        else:
            context = {
                "error": "No books found for this query....",
                "title": "Blog",
                "prev": p,
                "next": n,
                "pages": pages,
            }

        if not books:
            context = {
                "error": "No books found for this query....",
                "title": "Blog",
                "prev": p,
                "next": n,
                "pages": pages,
            }
    return render(request, 'accounts/blog.html', context)


def libid(request, id):
    s = id*12
    e = s + 12
    p = id - 1
    n = id + 1
    books = Book.objects.all()
    pages = len(books)
    pages = range(math.ceil(pages/12))
    books = Book.objects.all().order_by('-id')[s:e]
    try:
        checknext = Book.objects.all().order_by('-id')[e]
    except:
        n = -1
    context = {
        "books1": books[0:4],
        "books2": books[4:8],
        "books3": books[8:12],
        "title": "Library",
        "prev": p,
        "next": n,
        "pages": pages,
    }
    if request.method == "POST":
        query = request.POST['query']

        if query:
            searchedbooks = list()
            i = 0
            while True:
                if Book.objects.filter(name__icontains=query)[i:i+4]:
                    books = Book.objects.filter(name__icontains=query)[i:i+4]
                    searchedbooks.append(books)
                    i = i + 4
                else:
                    if i == 0:
                        books = Book.objects.filter(name__icontains=query)[i:i+4]
                    break
            context = {
                "books": searchedbooks,
                "title": "Library",
                "prev": p,
                "next": n,
                "pages": pages,
            }
        else:
            context = {
                "error": "No books found for this query....",
                "title": "Library",
                "prev": p,
                "next": n,
                "pages": pages,
            }

        if not books:
            context = {
                "error": "No books found for this query....",
                "title": "Library",
                "prev": p,
                "next": n,
                "pages": pages,
            }
    return render(request, 'accounts/bookstore.html', context)


def blogid(request, id):
    s = id*12
    e = s + 12
    p = id - 1
    n = id + 1
    books = Blog.objects.all()
    pages = len(books)
    pages = range(math.ceil(pages/12))
    books = Blog.objects.all().order_by('-id')[s:e]
    try:
        checknext = Blog.objects.all().order_by('-id')[e]
    except:
        n = -1
    context = {
        "books1": books[0:4],
        "books2": books[4:8],
        "books3": books[8:12],
        "title": "Blog",
        "prev": p,
        "next": n,
        "pages": pages,
    }
    if request.method == "POST":
        query = request.POST['query']

        if query:
            searchedbooks = list()
            i = 0
            while True:
                if Blog.objects.filter(title__icontains=query)[i:i+4]:
                    books = Blog.objects.filter(title__icontains=query)[i:i+4]
                    searchedbooks.append(books)
                    i = i + 4
                else:
                    if i == 0:
                        books = Blog.objects.filter(title__icontains=query)[i:i+4]
                    break
            context = {
                "books": searchedbooks,
                "title": "Blog",
                "prev": p,
                "next": n,
                "pages": pages,
            }
        else:
            context = {
                "error": "No books found for this query....",
                "title": "Blog",
                "prev": p,
                "next": n,
                "pages": pages,
            }

        if not books:
            context = {
                "error": "No books found for this query....",
                "title": "Blog",
                "prev": p,
                "next": n,
                "pages": pages,
            }
    return render(request, 'accounts/blog.html', context)

def cart(request, *args, **kwargs):
    total = 0
    print(kwargs)
    if kwargs:
        bookid = kwargs['bid']
        book = Book.objects.get(id=bookid)

    userid = request.user.id
    user = User(id=userid)
    userlibrary = Library.objects.get(username=user)
    
    if kwargs:
        userlibrary.cart.add(book.id)
        userlibrary.save()
    

    return redirect('/#page/11')

def wishlist(request, *args, **kwargs):
    print(kwargs)
    if kwargs:
        bookid = kwargs['bid']
        book = Book.objects.get(id=bookid)

    userid = request.user.id
    user = User(id=userid)
    userlibrary = Library.objects.get(username=user)
    if kwargs:
        userlibrary.wishlist.add(book.id)
        userlibrary.save()
    return redirect('/#page/11')

def wishtocart(request, *args, **kwargs):
    print(kwargs)
    if kwargs:
        bookid = kwargs['bid']
        book = Book.objects.get(id=bookid)

    userid = request.user.id
    user = User(id=userid)
    userlibrary = Library.objects.get(username=user)
    if kwargs:
        userlibrary.wishlist.remove(book.id)
        userlibrary.cart.add(book.id)
        userlibrary.save()
    return redirect(cart)

def rcart(request, bid):
    total = 0
    book = Book.objects.get(id=bid)
    print(book)
    userid = request.user.id
    user = User(id=userid)
    userlibrary = Library.objects.get(username=user)
    userlibrary.cart.remove(book.id)
    userlibrary.save()

    return redirect('/#page/11')

def index(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, 'flipbook/index.html', context)

def page5(request):
    return render(request, 'flipbook/pages/page5.html')

def page6(request):
    
    return render(request, 'flipbook/pages/page6.html')

def page7(request):
    books = Book.objects.all().order_by('-id')[:20]
    n = len(books)
    context = {
        "books": books,
        "n": n,
    }
    return render(request, 'flipbook/pages/page7.html', context)

def library(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'flipbook/library.html', context)

def page8(request):
    subs = Subscription.objects.all()
    context = {
        "subs": subs,
    }
    return render(request, 'flipbook/pages/page8.html', context)

def page9(request):
    blogs = Blog.objects.all().order_by('-id')[:20]
    n = len(blogs)
    context = {
        "blogs": blogs,
        "n": n,
    }
    return render(request, 'flipbook/pages/page9.html', context)

def page10(request):
    return render(request, 'flipbook/pages/page10.html')

def page11(request):
    total = 0

    userid = request.user.id
    user = User(id=userid)
    userlibrary = Library.objects.get(username=user)
    
    for book in userlibrary.cart.all():
        total += book.price

    context = {
        "books": userlibrary.cart.all(),
        "total": total,
        "books2": userlibrary.wishlist.all()
    }
    return render(request, 'flipbook/pages/page11.html', context)

def page12(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'flipbook/pages/page12.html', context)

def signup(request):
    context = {}
    form1 = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form1.is_valid():
            user = form1.save()

            try:
                registered_user = User.objects.get(id=user.id)
                Library.objects.create(username=registered_user, subsciption="unsubscribed")
                
            except:
                print("Error occured")

            login(request,user)
            return redirect('/#page/11')
            
    context['form1']=form1
    return render(request, 'registration/sign-up.html', context)