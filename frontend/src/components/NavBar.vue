<template>
  <div class="nav-bar">
    <nav>
      <div class="container">
        <a href="#">
           <img src="../assets/fox.png" width="200" height="200">
        </a>
        <button type="button">Push me</button>
        <div>
          <ul>
            <li><router-link :to="'/'">Home</router-link></li>
            <li v-if="accessToken != null"><router-link to="logout">Logout</router-link></li>
            <li v-if="accessToken == null"><router-link to="login">Login</router-link></li>
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
  computed: mapState(['accessToken'])
}
</script>

<style scoped>

</style>