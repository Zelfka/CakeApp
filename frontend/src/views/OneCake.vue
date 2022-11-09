<template>
<div>
  <NavBar></NavBar>
  <p v-if="error">{{error}}</p>
  <h1>{{APIData.name}}</h1>
  <p>{{APIData.description}}</p>
  <p>{{APIData.milk_free}}</p>
  <p>{{APIData.eggs_free}}</p>
  <p>{{APIData.price}}</p>
  <img :src="`/img/`+ APIData.img" width=100 height=100 alt="picture">
</div>
</template>

<script>
import {getAPI} from "@/axios-api"
import NavBar from "@/components/NavBar";
import {mapState} from "vuex"
export default {
  name: "OneCake",
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  data() {
    return {
      error: ''
    }
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData']),
  created() {
    getAPI('bake/api/cakes/' + this.$route.params.id + '/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          console.log('Get API has received data')
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