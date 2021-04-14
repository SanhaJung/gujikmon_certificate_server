from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User  
import requests         


#카카오 유저 저장 및 확인
@api_view(['POST'])
def kakao_account(request):
    account_token = json.loads(request.body)
    access_token = account_token.get('access_token')
    # refresh_token = account_token.get('refresh_token')
    # post request
    # 유저 정보 가져오기
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()

    if User.objects.filter(social_login_id = profile_json['id']).exists(): #기존에 소셜로그인을 했었는지 확인
        user_info          = User.objects.get(social_login_id=profile_json['id'])
        # encoded_jwt        = jwt.encode({'id': user_info.id}, "secret", algorithm='HS256') # jwt토큰 발행
        json_list={
            'access_token' :access_token,
            'refresh_token' : refresh_token,
            'user_email'    : user_info.email,
            'user_pk'      : user_info.id
        }
        return Response(json_list)        
    else:
        new_user_info = User(
                social_login_id = profile_json['id'],
                platform          = "kakao",
                email           = profile_json['kakao_account'].get('email', None),
                cofavorate =[]
            )
        new_user_info.save()
        json_list={
            'access_token' : access_token,
            'refresh_token' : refresh_token,
            'user_email'    : new_user_info.email,
            'user_pk'      : new_user_info.id,
        }
        return Response(json_list)  

#구글 유저 저장 및 확인 
@api_view(['POST'])
def google_account(request):
    account_token = json.loads(request.body)
    # access_token = account_token.get('access_token')
    # refresh_token = account_token.get('refresh_token')
    id_token = access_token.get('id_token')

    url   = 'https://oauth2.googleapis.com/tokeninfo?id_token=' # 토큰을 이용해서 회원의 정보를 확인하기 위한 gogle api주소
    response = requests.get(url+id_token) #구글에 id_token을 보내 디코딩 요청
    google_account = response.json() # 유저의 정보를 json화해서 변수에 저장
    # print(google_account)

    if User.objects.filter(social_login_id= google_account['sub']).exists():
        user_info = User.objects.get(social_login_id=google_account['sub'])
        # encoded_jwt = jwt.encode({'id': google_account["sub"]}, "secret", algorithm='HS256')
        email =google_account.get('email',None)
        
        json_list={
            'access_token'  : access_token,
            'refresh_token' : refresh_token,
            'user_email'    : email,
            'user_pk'       : user_info.id
        }

        return Response(json_list)
    else:
        new_user_info = User( # 처음으로 소셜로그인을 했을 경우 회원으 정보를 저장(email이 없을 수도 있다 하여, 있으면 저장하고, 없으면 None으로 표기)
                social_login_id = google_account['sub'],
                platform          = "google",
                email           = google_account.get('email', None),
                cofavorate =[]
            )
        new_user_info.save() # DB에 저장
        # encoded_jwt  = jwt.encode({'id': new_user_info.id}, "secret", algorithm='HS256') # jwt토큰 발행
        
        json_list={
            'access_token' : access_token,
            'refresh_token': refresh_token,
            'user_email'   : new_user_info.email,
            'user_pk'      : new_user_info.id
        }

        return Response(json_list)