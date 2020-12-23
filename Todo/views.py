from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth import authenticate, login

# def classes(request):
#     conn=pymysql.connect(host='127.0.0.1',
#                          port=3306,
#                          user='root',
#                          passwd='wbt62803683')
#     cursor=conn.cursor()
#     cursor.execute('select id, title form class')
#     class_list=cursor.fetchall()
#     cursor.close()
#     conn.close()
#
#
# def login(request):
#     if request.method=="GET":
#         print(request.method)
#         return render(request,'./templates/login.html')
#     else:
#         print(request.method)
#         u=request.POST.get('user')
#         print(u)
#         p=request.POST.get('pwd')
#         print(p)
#         if u=='root' and p=='123123':
#             return redirect("/index/")
#             # return render(request, './templates/index.html')
#         else:
#             return  render(request,'./templates/login.html',{'msg':'userID or password fault'})

def index(request):
    """
    index page
    :param request:
    :return:
    """
    return render(request, './templates/index.html')

def postLogin(request):
    """

    :param request:
    :return:
    """
    user_name=request.POST.get('user')
    password=request.POST.get('password')
    user_obj = authenticate(username=user_name, password=password)
    if user_obj:
        login(request, user_obj)
    try:
        user = FirebaseAuth.sign_in_with_email_and_password(user_name, password)
    except:
        message="Invalid email or password"
        return render(request, 'ToDoer/index.html', {"message":message})

    session_id=user['idToken']
    request.session['uid']=str(session_id)
    id_token=request.session['uid']
    session_token = FirebaseAuth.get_account_info(id_token)

    localID = session_token['users'][0]['localId']
    username= database.child('users').child(localID).child('details').child('Firstname').get().val()
    surname= database.child('users').child(localID).child('details').child('Surname').get().val()
    email= database.child('users').child(localID).child('details').child('email').get().val()
    timestamps = database.child('users').child(localID).child('Tasks').shallow().get().val()

    if timestamps != None:
        comb_toDoList, comb_doneList = loadTasksFromDB(timestamps, localID)
        return render(request, 'ToDoer/welcome.html', {"username":username, "todo_list":comb_toDoList, "done_list":comb_doneList, "uid":localID, "surname":surname, "email":email})

    else:
        return render(request, 'ToDoer/welcome.html', {"username":username, "uid":localID, "surname":surname, "email":email})
