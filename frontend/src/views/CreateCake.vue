<template>
<div>
  <NavBar></NavBar>
  <p v-if="error">{{error}}</p>
  <h1>Add new cake</h1>
  <form v-on:submit.prevent="createCake">
    <input type="text" required v-model="name" placeholder="name of the cake">
    <textarea required v-model="description" placeholder="description"></textarea>
    <label for="egg">Egg free:</label>
    <input type="checkbox" v-model="eggFree" id="egg">
     <label for="egg">Milk free:</label>
    <input type="checkbox" v-model="milkFree" id="milk">
    <input type="number" required v-model="price" placeholder="price">
    <button type="submit">Add cake</button>
  </form>
</div>
</template>

<script>
import {getAPI} from "@/axios-api"
import NavBar from "@/components/NavBar"
export default {
  name: "CreateCake",
   onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  data () {
    return {
      name:'',
      description: '',
      eggFree: false,
      milkFree: false,
      price: 0,
      error: ''
    }
  },
  components: {
    NavBar
  },
  methods: {
    createCake(){
      getAPI.post('bake/api/cakes/', {
          name: this.name,
          description: this.description,
          milk_free: this.milkFree,
          eggs_free: this.eggFree,
          price: this.price
      }, { headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('POST API has received data')
            this.$router.push('/cakes')
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