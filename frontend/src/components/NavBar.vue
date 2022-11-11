<template>
  <div class="nav-bar">
    <nav>
      <div class="container">
        <router-link :to="'/'">
           <img src="../assets/fox.png" width="200" height="200">
        </router-link>
        <div>
          <ul>
            <li><router-link :to="'/'">Home</router-link></li>
            <li v-if="accessToken != null"><router-link to="/logout">Logout</router-link></li>
            <li v-if="accessToken != null"><router-link :to="'/profile/' + this.$store.state.id">Profile</router-link></li>
            <li v-if="accessToken != null"><router-link :to="'/cakes/'">Cakes</router-link></li>
            <li v-if="accessToken != null"><router-link :to="'/order'">Basket</router-link></li>
            <li v-if="accessToken != null && admin !== false"><router-link :to="'/cakes/admin/add'">Add new cake</router-link></li>
            <li v-if="accessToken  == null"><router-link to="/login">Login</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import {mapState} from "vuex"

export default {
  name: "NavBar",
  computed: mapState(['accessToken', "admin"])
}
</script>

<style scoped>

</style>