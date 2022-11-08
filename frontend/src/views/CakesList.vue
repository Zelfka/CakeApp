<template>
  <div>
    <NavBar></NavBar>
    <h1>Cakes to come!!</h1>
    <div v-for="cake in APIData" :key="cake.id">
      <p>{{cake.name}}</p>
    </div>
  </div>
</template>

<script>
import {getAPI} from "@/axios-api"
import {mapState} from 'vuex'
import NavBar from "@/components/NavBar"
export default {
  name: "CakesList",
  components: {
    NavBar
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('bake/api/cakes/', {headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          console.log('Post API has received data')
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