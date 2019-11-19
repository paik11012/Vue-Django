<template>
  <div class="todo-input">
    <form class="input-group mb-3" @submit.prevent="onSubmit">
      <!-- 실제 제출은 막아서 리다이렉트 방지, spa이기 때문 -->
      <input v-model="title" type="text" class="form-control">
      <button type="submit" class="btn btn-success">Add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    onSubmit() {
      this.$emit('createTodo', this.title)  // emit은 컴포넌트가 이벤트를 발생하게 하는 함수
      this.title = ''
    }
  }
}
</script>

<style>

</style>