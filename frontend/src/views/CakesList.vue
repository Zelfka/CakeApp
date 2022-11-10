<template>
  <div>
    <NavBar></NavBar>
    <h1>Best cakes ever</h1>
    <div v-for="cake in APIData" :key="cake.id">
      <p>{{cake.name}}</p>
      <p>{{cake.description}}</p>
      <p>{{cake.price}}</p>
      <button v-if="admin === true"><router-link :to="'/cakes/admin/update/' + cake.id">Update</router-link></button>
      <button v-on:click="add(cake.id)">Add to basket</button>
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
  data(){
    return {
      error: ''
    }
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData', 'admin']),
  created() {
    getAPI.get('bake/api/cakes/', {headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          console.log('Get API has received data')
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  },
  methods: {
    add(id) {
      getAPI.post('order/api/orders/', {
        cake_id: id
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            this.$router.go(0)
          })
          .catch((err) => {
            this.error = err.response.data.detail
          } )
    }
  }
}
</script>

<style scoped>

</style>