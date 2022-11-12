<template>
  <div class="nav-bar">
    <nav>
      <div class="container">
        <div class="routes">
          <ul>
              <li><router-link :to="'/'">Home</router-link></li>
              <li v-if="accessToken != null"><router-link to="/logout">Logout</router-link></li>
              <li v-if="accessToken != null"><router-link :to="'/profile/' + this.$store.state.id">Profile</router-link></li>
              <li v-if="accessToken != null"><router-link :to="'/cakes/'">Cakes</router-link></li>
              <li v-if="accessToken != null"><router-link :to="'/order'">Basket</router-link></li>
               <li v-if="accessToken != null && admin !== false"><router-link :to="'/cakes/admin/add'">Add new cake</router-link></li>
               <li v-if="accessToken != null && admin !== false"><router-link :to="'/order/admin'">Manage orders</router-link></li>
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
.container{
  background: rgb(35,37,38);
  background: linear-gradient(0deg, rgba(35,37,38,1) 0%, rgba(65,67,69,1) 51%, rgba(35,37,38,1) 100%);
}

li{
  display: inline-block;
}
ul{
  display: flex;
  justify-content: space-between;
  padding: 20px 40px 20px 40px;
  margin: 0;
}
a{
  text-decoration: none;
  color: white;
  letter-spacing: 5px;
}
a:hover{
  color: #dd9add;
}
.routes{
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
}
</style>