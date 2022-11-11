<template>
  <div>
    <NavBar></NavBar>
    <p v-if="error">{{error}}</p>
    <p v-if="success">{{success}}</p>
    <h1>Orders:</h1>
      <form v-on:submit.prevent="filter">
      <input type="text" v-model="username" placeholder="Search orders by username">
      <input type="text" v-model="name" placeholder="Search orders by cake">
        <select v-model="orderState">
          <option>Open</option>
          <option>Closed</option>
        </select>
      <input type="date" v-model="date">
      <button type="submit">Search</button>
    </form>
    <div v-for="order in APIData" :key="order.id">
      <p>{{order.id}}</p>
      <p>{{order.created}}</p>
      <p>{{order.booked_date}}</p>
      <p>{{order.sum_cakes}}</p>
      <p>{{order.total_price}}</p>
      <p>{{order.details}}</p>
      <p>{{order.state}}</p>
      <div v-for="cake in order.cakes" :key="cake.id">
        <p>{{cake.name}}</p>
        <p>{{cake.price}}</p>
      </div>
      <button v-if="order.state === 'Open'" v-on:click="closeOrder(order.id)">Close order</button>
      <button v-on:click="deleteOrder(order.id)">Delete order</button>
    </div>
  </div>
</template>
<script>
import NavBar from "@/components/NavBar"
import {mapState} from "vuex"
import {getAPI} from "@/axios-api";
export default {
  name: "ALLOrders",
  components: {NavBar},
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  data () {
    return {
      error: '',
      success: '',
      name: '',
      date: '',
      username: '',
      orderState: ''
    }
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('order/api/admin/orders/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          console.log('GET API has received data')
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          this.error = err.response.data.detail
        })
  },
  methods: {
    filter(){
      getAPI.post('order/api/admin/orders/', {
        name: this.name,
        date: this.date,
        username: this.username,
        order_state: this.orderState
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(response => {
            console.log('POST API has received data')
            this.$store.state.APIData = response.data
          })
          .catch(err => {
            this.error = err.response.data.detail
          })
    },
    closeOrder(id) {
      getAPI.put('order/api/admin/orders/', {
        order_id: id
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('PUT API has received data')
            this.$router.go(0)
          })
          .catch(err => {
            this.error = err.response.data.detail
          })
    },
    deleteOrder(id) {
      getAPI.delete('order/api/admin/orders/' + id + '/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('Delete API has received data')
            this.success = 'Order with id' + id + ' was successfully deleted'
            this.$router.go(0)
          })
          .catch(err => {
            this.error = err.response.data.detail
          })
    }
  }
}
</script>

<style scoped>

</style>