<template>
  <div class="home">
    <h1>Todo</h1>
    <!-- props 이용해서 특정 데이터 넘기기 -->
    <TodoInput @createTodo="createTodo" />
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import axios from 'axios' // third party
import router from '@/router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
// import jwtDecode from 'jwt-decode' // jwt의 payload값을 해석해서 보여주는 라이브러리
import { mapGetters } from 'vuex'  // import vuex from 'vuex'; vuex.mapGetters

export default {
  name: 'Home',
  data() {
    return {
      todos:[]
    }
  },
  computed: {  // getters 한번에 가져오기 import { mapGetters } from 'vuex' 원래 하나씩 뽑음
    ...mapGetters([  // spread operator 점점점
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  components: {
    TodoList,
    TodoInput
  },
  methods: {
    checkLoggedIn(){  // 사용자 로그인 유무 확인해 로그인이 아니면 로그인 페이지로 보낸다 
      // 1. 세션을 시작하고 
      // this.$session.start()
      //2. jwt가 있는지 확인 - boolean 반환
      // if (!this.$session.has('jwt')) { 
        // jwt 없으면 로그인 페이지
      if (!this.isLoggedIn) {
        router.push('/login/')
      }
    },
    // 우리가 만든 장고 API서버로 todos를 달라는 요청을 보낸 뒤 todos data에 할당하는 함수
    getTodo() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const userId = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      axios.get(`${SERVER_IP}/api/v1/users/${this.userId}/`, this.options)
      .then(response => {
        this.todos = response.data.todo_set // vue가 todo data를 가질 수 있게 되었다
      })
      .catch(error => {
        console.error(error)
      })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const userId = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const data = {
        title,
        user: this.userId
      }
      axios.post(`${SERVER_IP}/api/v1/todos/`, data, this.options)
      .then(response => {
        this.todos.push(response.data)
      })
      .catch(error => {
        console.error(error)
      })
    }
  },
  // vue가 화면에 그려지면 실행하는 함수
  mounted() {
    if (this.isLoggedIn) {
      this.checkLoggedIn()
      this.getTodo()
    }
  },
  watch: {
    isLoggedIn() {
      this.getTodo()
    }
  }
}
</script>

<style>

</style>