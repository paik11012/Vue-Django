서버 django

프론트 vue js

request & response structure



장고 인증: 세션 + 쿠키

장고가 사용자 확인 하고 세션 생성, 세션 발급

브라우저에게 쿠키 주기(쿠기에는 세션id가 있다)



## Json web token 이용한 인증 시스템 구현

결론: 서버가 하는 일이 줄어든다. 서버는 세션을 사용하지 않는다. 유저 정보를 따로 기록하지 않는다.

동시 접속수 몇 만명이 되면 그 데이터를 서버가 기록하기 힘들다. 한 명 요청당 몇만 개의 세션을 비교해야하기 때문에 힘들다. 서버가 부담스럽다.

따라서 이 부담을 서버 말고 클라이언트에게 주자. 

**JWT등장**

어떤 처리를 하는가: 사용자가 서버에게 로그인 보냄, 서버가 확인하고 Secret key로 토큰 발행(JWT) 

client는 서버가 암호화해서 준 jwt를 지닌다. 

내가 가진 시크릿키로 복호화가 가능한지 확인하고 맞으면 인증!

인증 유효기간을 짧게 준다! 

## 

URL이랑 연결하기



장고 깔고

```
 django-admin startapp todo-back .
 vue create todo-front
 rm -rf .git
```

총 두개 프로젝트 생김



vue router: url별로 어떤 컴포넌트를 사용자에게 렌더링해서 보여줄 지 결정하는 라이브러리

```
vue ui  # 프로젝트 매니저 띄우기(vue에서 제공)
플러그인-vue router설치
```

views에서는 main.js에서 router-index.js기본으로 가져온다



views = page 전체 레이아웃 틀을 만들었다. 

```
http://localhost:8080/about
```

vue에서 사용되는 컴포넌트들은(유튜브에서 사용된 것) components에 저장하기

app.vue

```vue
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      <!-- 특이한 것 존재!  -->
    </div>
    <router-view/>
  </div>
</template>
```

home 클릭 - index.js에서 어디로 갈 지 찾기 - home 찾았다 - 어떤 컴포넌트? home - router view에서 보여주기

### 기억 

vue-router: 어떤 컴포넌트 렌더링해! index.js에서 const routes 구성(회원가입, 로그인 등등 가능) 그러나 여기 작성되는  component는 view폴더 내에 있어야 한다



## login path

npm i bootstrap bootstrap-vue

main.js

```
import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
```

### css등록

loginform.vue

```vue
<template>
  <div class="login-div">
    <div class="form-group">
      <label for="id">ID</label>
      <input type="text" id="id" class="form-control" placeholder="ID를 입력해주세요" v-model="credentials.username">
      <!-- v-model로 양 방향 바인딩 하기 -->
    </div>
    <div class="form-group">
      <label for="password">PASSWORD</label>
      <!-- password 별표처리됨 -->
      <input type="password" id="password" class="form-control" placeholder="PASSWORD를 입력해주세요" v-model="credentials.password">
    </div>
    <button class="btn btn-primary">Login</button>

  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
}
</script>

<style>

</style>
```

package.json -> console.log 찍을 수 있게 바꾸자

```json
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "rules": {
        "no-console":"off"
    },
```





## 로그인 요청 보내기 axios

axios 설치

```
npm i axios
```



### front, back 둘 다 실행시 Access to XMLHttpRequest at 'http://127.0.0.1:8000/' from origin 'http://localhost:8081' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.  오류

뷰 //  장고(유저, 투두 등 정보 지님, 우리만 쓰는 서버)

근데 이상한 놈이 나타나서 장고에게 유저 정보 내놔라고 요구하는 중. 그래서 위에 오류가 나타난다.

장고 측에서 이상한 놈(뷰)를 화이트리스트로 처리해야 한다

```
https://developer.mozilla.org/ko/docs/Web/HTTP/Access_control_CORS
```

cors란?



## 화이트 리스트 처리

todos앱 만들고 등록

```
pip install djangorestframework
pip install djangorestframework-jwt
pip install django-cors-headers
```

각각 등록

  'rest_framework',  'corsheaders',

 http://jpadilla.github.io/django-rest-framework-jwt/ 

setting.py

```python
#  jwt 관련 셋팅
REST_FRAMEWORK = {   # 로그인 여부 확인해주는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (  # 인증 여부 확인하는 클래스
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    # 토큰을 암호화할 시크릿 키 등록, 절대 외부 노출 금지
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,  # 다시 토큰 새로고침해서 받아가는것 가능(2주 짧다, 대신 자주 갱신)
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # 토큰 유효기간 일주일, 원래는 5분
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.time(days=28),  # 28일마다 토큰이 갱신(유효기간 연장시)
    # 토큰 두 개 발행. 하나는 access토큰=접근가능, refresh토큰(access토큰을 발행하기 위한 토큰)=access토큰 발행시 이용
    
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:8080",  # 뷰 서버
#     "http://localhost:8081", 
# ]
```

토큰 받아갈 수 있게 셋팅하기

urls.py

```python
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api-token-auth/', botain_jwt_token),
    path('admin/', admin.site.urls),
]
```

todos-models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 장고에서는 강력히 커스텀 유저를 사용하라고 권장함
class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
```

settings.py 

AUTH_USER_MODEL = 'todos.User'



## 세션스토리지 이용하기

프론트엔드

npm install vue session

main.js

```
import VueSession from 'vue-session'
Vue.use(VueSession)
```

## 로그아웃 만들기

```vue
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login/">Login</router-link> |
      <a @click.prevent="logout" href="/logout">Logout</a>
      <!-- prevent를 사용하는 이유는 herf로 리다이렉트를 방지하기 위함 -->

    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import router from '@/router'
export default {
  name: 'App',
  methods: {
    logout() {
      this.$session.destroy()
      router.push('/login/')
    }
  }
}
</script>
```



## 로그인 되어 있을때만 로그아웃 보이도록, 반대도 가능 (조건부 렌더링)

 