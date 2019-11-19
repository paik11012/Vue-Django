<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading</span>
    </div>

    <div v-else class="login-form"> 
      <!-- 에러가 있다면 -->
      <div v-if="errors.length" class="alert alert-danger">  
        <h4>다음 오류를 해결해주세요</h4>
        <hr>
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>

      <div class="form-group">ID
        <input type="text" id="id" class="form-control" placeholder="ID를 입력해주세요" v-model="credentials.username">
        <!-- v-model로 양 방향 바인딩 하기 -->
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <!-- password 별표처리됨 -->
        <input type="password" id="password" class="form-control" placeholder="PASSWORD를 입력해주세요" v-model="credentials.password">
      </div>
      <button class="btn btn-primary" v-on:click="login">Login</button>
    </div>

  </div>
</template>

<script>
import axios from 'axios' // axios설치 후 가져오기

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,  // 서버가 응답할 때까지 spinner 돌리기
      errors: [],
    }
  },
  methods: {
    login() {
      if (this.checkForm() ) {  // true
        this.loading = true
        const SERVER_IP = process.env.VUE_APP_SERVER_IP
        axios.get(SERVER_IP, this.credentials)  // 여기가 중요!!!!!!!!!!!
        .then(response => {
          console.log(response)
          this.loading = false  // 비동기적이기에 두 번 넣어주어야 함
        })
        .catch(error => {
          console.error(error)
          this.loading = false  // 비동기적이기에 두 번 넣어주어야 함
        })
      }
    },
    checkForm() { // 결과적으로 에러 없으면 true 반환
      this.errors = [] // 초기화
      if (!this.credentials.username) {
        this.errors.push('ID를 입력하세요')
      }
      if (this.credentials.password.length < 8) {
        this.errors.push('PASSWORD는 8글자 이상 입력해주세요')
      }
      if (this.errors.length === 0){
        return true
      }
      // 아무것도 없으면 return undefined === falsy한 값
    }
  },
}
</script>

<style>

</style>