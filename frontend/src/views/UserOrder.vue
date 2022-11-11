<template>
  <div>
    <NavBar></NavBar>
    <p v-if="error">{{error}}</p>
    <p v-else-if="success">{{success}}</p>
    <div v-else>
      <h1> {{username}}'s basket:</h1>
    <p>Created: {{APIData.created}}</p>
    <div v-for="cake in cakes" :key="cake.id">
      <p>{{cake.name}}</p>
      <p>{{cake.description}}</p>
      <p>{{cake.price}}</p>
      <button v-on:click="remove(cake.id)">Remove</button>
    </div>
    <p>Number of cakes: {{APIData.sum_cakes}}</p>
    <p>Total: {{APIData.total_price}} CZK</p>
    <form v-on:submit.prevent="sendOrder">
      <label for="date">Pick a day:</label>
      <input type="date" required :min="new Date().toISOString().split('T')[0]" v-model="date" id="date">
      <label for="detail">Details:</label>
      <input type="text" v-model="details" placeholder="Any details you would like add to your order?" id="'detail">
      <button type="submit">Send order</button>
    </form>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar"
import {getAPI} from "@/axios-api"
import {mapState} from "vuex"
export default {
  name: "UserOrder",
   onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  data (){
    return {
      error: '',
      success: '',
      cakes: [],
      username: '',
      date: '',
      details: ''
    }
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('order/api/orders/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          this.$store.state.APIData = response.data
          this.cakes = response.data.cakes
          this.username = response.data.user.username
          console.log('GET API has received data')
        })
        .catch(err => {
          this.error = err.response.data.detail
        })
  },
  methods: {
    sendOrder(){
      getAPI.put('order/api/orders/', {
        date: this.date,
        details: this.details
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(response => {
            this.success = response.data.detail
            console.log('PUT API has received data')
            this.$router.go(0)
          })
          .catch(err => {
            this.error = err.response.data.detail
          })
    },
    remove(id) {
      getAPI.delete('order/api/orders/' + id + '/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('DELETE API has received data')
            this.$router.go(0)
          })
          .catch(err => (
              console.log(err)
          ))
    }
  }
}
</script>

<style scoped>

</style>