<template>
  <div>
    <NavBar></NavBar>
    <h1>My order:</h1>
    <p v-if="error">{{error}}</p>
    <div v-else>
      <div v-for="cake in APIData" :key="cake.id">
      <p>{{cake.name}}</p>
      <p>{{cake.description}}</p>
      <p>{{cake.price}}</p>
      <img :src="`/img/`+ cake.img" width=100 height=100 alt="picture">
    </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar"
import {getAPI} from "@/axios-api"
import {mapState} from "vuex"
export default {
  name: "CakesByOrder",
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  components: {
    NavBar
  },
  data() {
    return {
      error: ''
    }
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('bake/api/cakes/order/' + this.$route.params.order_id + '/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          this.error = err.response.data.detail
        })
  }
}
</script>

<style scoped>

</style>