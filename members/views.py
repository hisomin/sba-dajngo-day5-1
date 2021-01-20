from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def my_test(req):
    return HttpResponse("<h2>Test</h2>")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']
        #username == exit
        # h2 로  나가기를 출력
        if username == 'exit' :
            return HttpResponse('나가기')
        elif username == 'codingon' :
            return render(req, 'login.html')

        #my_username 이 그 외의 경우는 
            return HttpResponse("안녕갑세요  "+username)

            member = Members(username=my_username, user_email=my_email)

            member.save() #db에 저장? save가 뭔지?
            res_data={}
            res_data['res'] ="등록성공"
            print('\n\n\n\n\n\n\n\n\n')
            print(res_data) # 터미널 창 확인
            return render(req, 'index.html',res_data)

