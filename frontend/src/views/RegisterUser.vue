<template>
<div>
  <p v-if="error">{{error}}</p>
  <form v-on:submit.prevent="register">
    <input type="text" placeholder="Enter your username" required v-model="username">
    <input type="email" placeholder="Enter your e-mail address" required v-model="email">
    <input type="password" placeholder="Enter your password" required v-model="password">
    <input type="password" placeholder="Password confirmation" required v-model="password2">
    <button type="submit">Register</button>
  </form>
</div>
</template>

<script>
import {getAPI} from "@/axios-api";
export default {
  name: "RegisterUser",
  data(){
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      error: ''
    }
  },
  methods: {
    register(){
      getAPI.post('api/register/', {
        username: this.username,
        email: this.email,
        password: this.password,
        password2: this.password2
      })
          .then(() => {
            this.$router.push('login')
          })
          .catch(err => {
            console.log(err)
            this.error = err.response.data.detail
          })
    }
  }
}
</script>

<style scoped>

</style>