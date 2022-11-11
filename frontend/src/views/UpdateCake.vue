<template>
  <div>
    <NavBar></NavBar>
    <p v-if="error">{{error}}</p>
    <h1>Change details of the cake</h1>
    <form v-on:submit.prevent="updateCake">
      <input type="text" required v-model="name" placeholder="name of the cake">
      <textarea required v-model="description" placeholder="description"></textarea>
      <label for="egg">Egg free:</label>
      <input type="checkbox" v-model="eggFree" id="egg">
       <label for="egg">Milk free:</label>
      <input type="checkbox" v-model="milkFree" id="milk">
      <input type="number" required v-model="price" placeholder="price">
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar"
import {getAPI} from "@/axios-api"

export default {
  name: "UpdateCake",
   onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  components: {
    NavBar
  },
  data(){
    return {
      name: '',
      description: '',
      eggFree: '',
      milkFree: '',
      price: '',
      error: ''
    }
  },
  created() {
    getAPI.get('bake/api/cakes/update/' + this.$route.params.id + '/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          this.name = response.data.name
          this.description = response.data.description
          this.milkFree = response.data.milk_free
          this.eggFree = response.data.eggs_free
          this.price = response.data.price
          console.log('GET API has received data')
        })
        .catch(err => {
          this.error = err.response.data.detail
        })
  },
  methods: {
    updateCake() {
      getAPI.put('bake/api/cakes/update/'  + this.$route.params.id + '/', {
        name: this.name,
        description: this.description,
        eggs_free: this.eggFree,
        milk_free: this.milkFree,
        price: this.price
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('PUT API has received data')
            this.$router.push('/cakes')
          })
          .catch(err => {
            if(err.response.data){
              this.error = err.response.data.detail
            } else {
              this.$router.push('/')
            }
          })
    }
  }
}
</script>

<style scoped>

</style>