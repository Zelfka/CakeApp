<template>
<div>
  <div>
    <h1>Log In!</h1>
    <p v-if="incorrectAuth">Incorrect username or password</p>
    <form v-on:submit.prevent="login">
      <input type="text" placeholder="Enter your username" v-model="username">
      <input type="password" placeholder="Enter you password" v-model="password">
      <button type="submit">Submit</button>
    </form>
  </div>
</div>
</template>

<script>
export default {
  name: "LogIn",
  data(){
    return{
      username: '',
      password: '',
      incorrectAuth: false
    }
  },
  methods:{
    login(){
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      })
          .then(() => {
            this.$router.push({name: 'cakes'})
          })
          .catch(err => {
            console.log(err)
            this.incorrectAuth = true
          })
    }
  }
}
</script>

<style scoped>

</style>