from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from adminapp.models import Status
from adminapp.models import Blog

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get("fullName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        status = request.POST.get("status")
        image = request.FILES.get("image")  # Use square brackets to access request.FILES

        # Validate password match
        if password != confirm:
            messages.error(request, 'Passwords do not match.')
            return redirect('index')

        # Create a new user instance
        try:
            # Save the Status instance
            data = Status(name=name, email=email, password=password, status=status, image=image)
            data.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('index')

    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        status = request.POST.get("status")
        if status == 'admin':
            details = Status.objects.filter(email=email, password=password, status='admin')
            if details:
                request.session['email'] = email
                return redirect('adminhome')

        else:
            details = Status.objects.filter(email=email, password=password, status=status)
            if details:
                request.session['email'] = email
                return redirect('cus_emp')

    return render(request, 'login_page.html')

def adminhome(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)
        all_users = Status.objects.exclude(status='admin')

    return render(request, 'admin/home_admin.html',{'user':user, 'all_users':all_users})

def adminprofile(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)

    return render(request, 'admin/adminprofile.html',{'user':user})

def custable(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)
        cusdata = Status.objects.filter(status='Customer')

    return render(request, 'admin/cusemptable.html',{'user':user, 'all_users':cusdata})

def emptable(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)
        all_users = Status.objects.filter(status='Employee')

    return render(request, 'admin/cusemptable.html',{'user':user, 'all_users':all_users})


def cus_emp(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)

    return render(request, 'cus_emp.html',{'user':user})

def blog(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog = Blog(title=title,content=content)
        blog.save()
        return redirect('blogshow')
    else:
        return render(request, 'admin/blog.html')

    return render(request, 'admin/blog.html',{'user':user})

def blogshow(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)
        blog = Blog.objects.all()
    return render(request, 'admin/blogshow.html',{'user':user, 'blog':blog})

def blogedit(request, id):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)
        blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog.title = title
        blog.content =content
        blog.save()
        return redirect('blogshow')
    else:
        return render(request,"admin/blogedit.html",{'user':user, 'blog':blog})

    return render(request, "admin/blogedit.html",{'user':user, 'blog':blog})

def blogdelete(request, id):
    if 'email' in request.session:
        email = request.session['email']
        user = Status.objects.get(email=email)
        blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        blog.delete()
        return redirect('blogshow')
    else:
        return render(request, "admin/blogdelete.html", {'user': user, 'blog': blog})

    return render(request, "admin/blogdelete.html",{'user':user, 'blog':blog})



def logout(request):
    if 'email' in request.session:
        # Remove email from session
        del request.session['email']
        request.session.flush()
        messages.success(request, 'You have successfully logged out.')

    return redirect('login')

