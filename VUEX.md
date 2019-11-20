## VUEX

 https://vuex.vuejs.org/kr/ 

```
Vuex는 Vue.js 애플리케이션에 대한 상태 관리 패턴 + 라이브러리 입니다. 애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할을 하며 예측 가능한 방식으로 상태를 변경할 수 있습니다. 또한 Vue의 공식 devtools 확장 프로그램과 통합되어 설정 시간이 필요 없는 디버깅 및 상태 스냅 샷 내보내기/가져오기와 같은 고급 기능을 제공합니다

데이터값을 모두 바라볼 수 있는 새로운 가상공간 창출
```

view = component

actions = methods

state = data, 모든 컴포넌트에서 쉽게 셰어 가능(jwt)

mutation = state만 바꾸는 함수

![vuex](C:\Users\student\development\Vue_Django\vuex.png)

action에 로그인 정의

mutation발생 = 로딩을 true로 바꾸는 것 -> state 로딩값 바뀜 -> 로그인 요청 -> 기다림 -> jwt 셋팅 -> 로딩 다시 false로

