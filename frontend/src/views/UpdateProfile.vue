<template>
  <div>
    <NavBar></NavBar>
    <p v-if="error">{{error}}</p>
    <h1>Update your profile</h1>
    <form v-on:submit.prevent="update">
      <input type="text"  v-model="firstName" placeholder="Enter you first name">
      <input type="text"  v-model="lastName" placeholder="Enter your last name">
      <input type="number"  v-model="phone" placeholder="Enter your phone">
      <input type="email"  v-model="email" placeholder="Enter your email address">
      <input type="text"  v-model="street" placeholder="Enter your street">
      <input type="text"  v-model="city" placeholder="Enter your city">
      <input type="number"  v-model="zipCode" placeholder="Enter your zip code">
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import {getAPI} from "@/axios-api"
import NavBar from "@/components/NavBar"

export default {
  name: "UpdateProfile",
  components: {
    NavBar
  },
  data () {
    return {
      email: '',
      firstName: '',
      lastName: '',
      street: '',
      city: '',
      zipCode: '',
      phone: '',
      error: ''
    }
  },
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  created() {
      getAPI.get('api/profile/' + this.$route.params.id + '/', {headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(response => {
            console.log('Get API has received data')
            this.email = response.data.email
            this.firstName = response.data.first_name
            this.lastName = response.data.last_name
            this.street = response.data.street
            this.zipCode = response.data.zip_code
            this.phone = response.data.phone
          })
          .catch(err => {
            this.error = err.response.data.detail
          })
    },
  methods: {
    update () {
      getAPI.put('api/profile/' + this.$route.params.id + '/', {
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
        street: this.street,
        city: this.city,
        zip_code: this.zipCode,
        phone: this.phone
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            this.$router.push('/profile/' + this.$route.params.id)
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