<template>
  <div class="home"></div>
</template>

<script>
import router from '@/router'
export default {
  name: 'Home',
  methods: {
    checkLoggedIn(){  // 사용자 로그인 유무 확인해 로그인이 아니면 로그인 페이지로 보낸다 
      // 1. 세션을 시작하고 
      this.$session.start()
      //2. jwt가 있는지 확인 - boolean 반환
      if (!this.$session.has('jwt')) { 
        // jwt 없으면 로그인 페이지
        router.push('/login/')
      }
    }
  },
  // vue가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn()
  }

}
</script>

<style>

</style>