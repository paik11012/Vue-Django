import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  // 앱의 상태(data)
  state: {
    token: null,
  },
  // computed
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false  //  삼항연산자 이용
    },
    options(state) {
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state) {
      return state.token ? jwtDecode(state.token).user_id : null  // null안되게 체크, 있을 때만 앞에것 없으면 null return
    }
  },
  // state를 변경하는 함수
  mutations: {
    setToken(state, token){  // 토큰 상태를 변경할 함수
      state.token = token
    }
  },
  // methods
  actions: {
    login(context, token) {
      context.commit('setToken', token) // 위 mutation 실행해 status를 변경하겠다
    },
    logout(context) {
      context.commit('setToken', null)
    }
  },
})
