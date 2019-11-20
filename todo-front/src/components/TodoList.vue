<template>
  <div class="todo-list">

    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between mb-1" >
        <span>{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="btn btn-delete">Delete</button>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'  // 요청 보낼 때는 엑시오스 가져오기

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  computed: {
    options() {
      return this.$store.getters.options
    }
  },

  methods: {
    deleteTodo(todo) {  // 현재 선택된 투두
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, this.options)  // 위 대신 여기 부분 추가함
      .then(response => {
        console.log(response)
        const idx = this.todos.indexOf(todo)
        if (idx > -1){
          this.todos.splice(idx, 1)
        }
      })
      .catch(error => {
        console.error(error)
      })
    }
  }
}
</script>

<style>

</style>