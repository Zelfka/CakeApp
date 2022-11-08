<template>
  <div>
    <NavBar></NavBar>
    <h1>Cakes to come!!</h1>
    <div v-for="cake in APIData" :key="cake.id">
      <p>{{cake.name}}}</p>
    </div>
  </div>
</template>

<script>
import {getAPI} from "@/axios-api";
import NavBar from "@/components/NavBar";
export default {
  name: "CakesList",
  data() {
    return{
      APIData: []
    }
  },
  components: {
    NavBar
  },
  created() {
    getAPI.get('bake/api/cakes/')
        .then(response => {
          console.log('Post API has received data')
          this.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>

<style scoped>

</style>