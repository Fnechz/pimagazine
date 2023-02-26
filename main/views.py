# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Category,Comment
import requests

def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:3]
    three_categories=Category.objects.all()[0:3]
    return render(request,'home1.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

# All News
def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html',{
        'all_news':all_news
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        # email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            # email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted but in moderation mode.')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments
    })

# Fetch all category
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })

# Fetch guide category
def guide_category(request):
    #news=News.objects.all()
    guide_cat=Category.objects.all().filter(title='guides').first()
    guide_id = guide_cat.id
    guide_news=News.objects.filter(category=guide_id)
    return render(request,'guides.html',{
        'guide_news': guide_news,
    })

# Fetch about Pi page
def about(request):
    return render(request, 'about.html', {})

# Fetch Learn page
def learn(request):
    return render(request, 'learn.html', {})

def jobs(request):
    return render(request, 'jobs.html', {})

def events(request):
    return render(request, 'events.html', {})

def press(request):
    return render(request, 'press.html', {})

def mine(request):
    return render(request, 'mine.html', {})

# Fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

#implement pi backend

# #@user_blueprint.route("/user/<string:username>", methods=['GET','POST'])
# def app_user(request):
#     """
#     Route displaying a user's profile page.
#     """
#     if request.method == 'POST':
#         try:
#             try:
#                 content = request.json
#                 try:
#                     if content['user_name']:
#                         print('Log: received data for user Pi Network Username: ' + str(content['user_name']))
#                         verifyWithPi(content)
#                 except:
#                     pass
#                 try:
#                     if str(content['action']) == 'approve' or str(content['action']) == 'complete':
#                         verifyPayments(content)
#                 except:
#                     pass
#             except:
#                 pass
#         except:
#             print('Error during VerifyWithPi-Routine')
#     return render(request, 'user.html')
    

# def verifyWithPi(content):
#     """
#     Verifies the Pi Network data the user sent with the backend-API
#     User-content: [user_token, user_name, user_roles]
#     """
#     baseURL = 'https://api.minepi.com'
#     user_name = content['user_name']
#     authentication = 'Bearer ' + content['user_token']
#     auth_bearer = {'Authorization':authentication}
#     request_verification = requests.get(baseURL + '/v2/me', headers = auth_bearer)
#     server_data = eval(request_verification.text)
#     print(server_data)
#     # if server_data['username'] == content['user_name']:
#     #     app_user = AppUser.query.filter_by(username=current_user.username).first()
#     #     app_user.pi_username = server_data['username']
#     #     print('Log: found roles are ' + str(server_data['roles']))
#     #     if server_data['roles'][0] == 'moderator':
#     #         app_user.moderator = True
#     #     db.session.commit()

# def verifyPayments(content):
#     """
#     Verifies the Pi Network data the user sent with the backend-API
#     User-content: [user_token, user_name, user_roles]
#     """
#     baseURL = 'https://api.minepi.com'
#     authentication = 'Key ' + 'iv7u2qkyzand5pziejizuqpbojkittuxplwbduyxuzeynpxmrlqdttdccwgmlhyr'
#     header = {'Authorization': authentication}
#     if str(content['action']) == 'approve':
#         url = baseURL + '/v2/payments/' + content['paymentId'] + '/approve'
#         data = {}
#     if str(content['action']) == 'complete':
#         url = baseURL + '/v2/payments/' + content['paymentId'] + '/complete'
#         data = {'txid': content['txid']}

#     request_payment = requests.post(url, json=data, headers=header)