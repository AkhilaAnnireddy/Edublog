from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .forms import StudentSignUpForm, FacultySignUpForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from decorators import faculty_required
from posts.models import Post
from django.db.models import Count
def register(request):
    return render(request, 'accounts/register.html')

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class faculty_register(CreateView):
    model = User
    form_class = FacultySignUpForm
    template_name = 'accounts/faculty_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def updateprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.faculty)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile',request.user.username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.faculty)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/updateprofile.html', context)

@login_required
def profile(request,username):
    user1=get_object_or_404(User,username=username)
    posts=Post.objects.filter(user=user1)
    total_posts=posts.count()
    no_likes=user1.posts.aggregate(total_likes=Count('likes'))['total_likes']
    equal=0
    if user1.username==request.user.username:
        equal=1
    return render(request,'accounts/profile.html',{'posts':posts,'equal':equal,'user1':user1,'total_posts':total_posts,'no_likes':no_likes})
