<template>
  <div>
    <NavBar></NavBar>
    <h1>Best cakes ever</h1>
    <div v-for="cake in APIData" :key="cake.id">
      <p>{{cake.name}}</p>
<!--      <img :src="`/img/fox.ad5cb41c.png`" width=100 height=100 alt="picture">-->
<!--      <img src="../assets/fox.png"   width=100 height=100 alt="picture">-->
      <p>{{cake.description}}</p>
      <router-link :to="'/cakes/' + cake.id"><img :src="`/img/`+ cake.img" width=100 height=100 alt="picture"></router-link>
    </div>
  </div>
</template>

<script>
import {getAPI} from "@/axios-api"
import {mapState} from 'vuex'
import NavBar from "@/components/NavBar"
export default {
  name: "CakesList",
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('bake/api/cakes/', {headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          console.log('Get API has received data')
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>

<style scoped>

</style>