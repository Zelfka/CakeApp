<template>
  <div>
    <NavBar></NavBar>
    <h1 v-if="APIData.username">{{APIData.username}}'s profile</h1>
    <p v-if="error">{{error}}</p>
    <ul>
      <li v-if="APIData.username"><span>Username:</span>{{APIData.username}}</li>
      <li v-else><span>Username:</span>N/A</li>
      <li v-if="APIData.first_name"><span>First name:</span>{{APIData.first_name}}</li>
      <li v-else><span>First name:</span>N/A</li>
      <li v-if="APIData.last_name"><span>Last name:</span>{{APIData.last_name}}</li>
      <li v-else><span>Last name:</span>N/A</li>
      <li v-if="APIData.email"><span>E-mail:</span>{{APIData.email}}</li>
      <li v-else><span>E-mail:</span>N/A</li>
      <li v-if="APIData.phone"><span>Phone number:</span>{{APIData.phone}}</li>
      <li v-else><span>Phone number:</span>N/A</li>
      <li v-if="APIData.street"><span>Street:</span>{{APIData.street}}</li>
      <li v-else><span>Street:</span>N/A</li>
      <li v-if="APIData.city"><span>City:</span>{{APIData.city}}</li>
      <li v-else><span>City:</span>N/A</li>
      <li v-if="APIData.zip_code"><span>Zip code:</span>{{APIData.zip_code}}</li>
      <li v-else><span>Zip code:</span>N/A</li>
    </ul>
    <button><router-link :to="this.$store.state.id + '/update'">Update profile</router-link></button>
  </div>
</template>

<script>
import {getAPI} from "@/axios-api"
import {mapState} from 'vuex'
import NavBar from "@/components/NavBar"

export default {
  name: "UserProfile",
  data () {
    return {
      error: ''
    }
  },
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('api/profile/' + this.$route.params.id + '/', {headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
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