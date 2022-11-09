<template>
  <div>
    <NavBar></NavBar>
    <h1 v-if="APIData.username">{{APIData.username}}'s profile</h1>
    <p v-if="error">{{error}}</p>
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