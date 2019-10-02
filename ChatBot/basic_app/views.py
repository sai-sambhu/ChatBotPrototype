from django.shortcuts import render
from django.views.generic import TemplateView
from basic_app.models import StudentBotUser
# Create your views here.

 

class IndexView(TemplateView):
    template_name = 'index.html'

#user=User.objects.get_or_create(first_name='sai'+str(st[0]),last_name='reddy'+'1',email='saisambhuprasad@gmail.com')

        
    
def CHATBOT(request):
    my_dict={'Question_list':['Enter your Name','Enter your Email','Enter your Phone Number']}
    
    if request.method=="POST":
           print("sai")
           ChatString = request.POST["Chat"]
           ChatString=ChatString.split("\t")
           print(ChatString)
           
           user=StudentBotUser.objects.get_or_create(first_name=str(ChatString[1]),email=ChatString[2],phone_number=ChatString[3])
           my_dict={'message':'Your Information is stored'}
           return render(request,'index.html',context=my_dict)
    return render(request,'Chatbot.html',context=my_dict)
    pass   
           
       