<template>
<div>
  <NavBar></NavBar>
</div>
</template>

<script>
import NavBar from "@/components/NavBar"
export default {
  name: "HomePage",
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  components: {
    NavBar
  }
}
</script>

<style scoped>

</style>