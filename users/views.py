from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User #user 모델 불러오기
from django.contrib.auth import authenticate, login as loginsession
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        # 여기에서 get은 request.Post로 온 데이터 안에있는 것중에서 키값이 username인것을 get해라 
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        # print(username, password, passwordcheck) 위 3가지 값들이 잘 가져와 졌는지 확인
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password) # create를 사용하면 비밀번호 자동 해싱 된다.
            return HttpResponse("회원가입 완료!")
        else:
            return HttpResponse("비밀번호 확인이 틀렸습니다.")
    else:
        return HttpResponse("이상한거")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # authenticate는 인증만 하는 것(진짜 있는 user인지), 없으면 none값 반환
        # login은 아이디와 패스워드로 로그인 세션을 만들어준다.(실제 로그인 과정을 실행)
        if user:
            loginsession(request, user)
            # 원래는 login을 import한거지만 함수명과 같이 오류가 생길수도 있어 import부분에서 as loginsession으로 이름을 변경해줌
            return redirect('users:user')
        else:
            return HttpResponse("로그인 실패")
        
def user(request):
    return HttpResponse(request.user)

def profile(request, username):
    # user = User.objects.get(username=username) 이것 대신 아래 404를 사용하면 이상한 아이디를 주소창에 쳤을 때 이상한 오류창이 아니라 404창이 뜬다.
    # 예쁜 404창을 만드려면 debug를 false로 해주자!
    user = get_object_or_404(User, username=username)
    # for article in user.article_set.all():
        # 유저가 작성한 모든 글을 불러올 때
        # print(article)
    context = {
        'user': user
    }
    # html에서 context안에 들어있는 데이터를 이용할 수 있다.
    return render(request, 'profile.html', context)

def logout_view(request):
    logout(request)