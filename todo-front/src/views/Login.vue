<template>
  <div>
    <h1>Login Page</h1>
    <br>
    <br>
    <br>
    <!-- 3 컴포넌트 사용 -->
    <LoginForm />
  </div>
</template>

<script>
// 1 컴포넌트 호출
import LoginForm from '@/components/LoginForm'
export default {
  name: 'Login',
  components: {
    LoginForm  // 2 컴포넌트 등록
  }
}
</script>

<style>

</style>