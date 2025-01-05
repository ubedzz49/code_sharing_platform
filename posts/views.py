from .models import Post,Soln
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .forms import SolnForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    soln=Soln.objects.all()
    return render(request,'index.html',{'soln': soln})

def sol(request,pk):
    sol=Soln.objects.get(id=pk)
    return render(request,'sol.html',{'sol':sol})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm_password')  # Changed to match HTML

        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'signup.html')


def user_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,'invalid credintials')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form' : form})

def logout_view(request):
  logout(request)
  return redirect('index')



@login_required
def submit_solution(request):
    if request.method == 'POST':
        form = SolnForm(request.POST)
        if form.is_valid():
            # Save the form but don't commit yet (so we can modify the "posted_by" field)
            solution = form.save(commit=False)
            solution.posted_by = request.user.username  # Set the "posted_by" field to the current user's username
            solution.save()  # Save the solution
            return redirect('index')  # Redirect after successful form submission (replace with your success URL)
    else:
        form = SolnForm()
    
    return render(request, 'submit_solution.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.utils import timezone

@login_required
def chat(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            message = Message.objects.create(user=request.user, content=message_content, timestamp=timezone.now())
            message.save()
            return redirect('chat')

    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat.html', {'messages': messages})
