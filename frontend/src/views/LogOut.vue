<template>
<div>
  <h1>Bye bye</h1>
  <button><router-link to="login">Back to login?</router-link></button>
</div>
</template>

<script>
export default {
  name: "LogOut",
  created(){
      this.$store.dispatch('userLogout')
  }
}

</script>

<style scoped>

</style>