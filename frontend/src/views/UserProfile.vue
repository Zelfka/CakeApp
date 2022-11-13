<template>
  <div id="container">
    <NavBar></NavBar>
    <p class="background">eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel cocoa
    eggs milk flour oil fruit caramel eggs milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel cocoa
   milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    cake eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream  eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour sugar cocoa cream chocolate chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk fruit caramel eggs milk fruit caramel eggs
    oil sugar cocoa cream chocolate chocolate fruit caramel eggs milk flour chocolate fruit caramel eggs milk flour fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk fruit caramel eggs milk fruit caramel eggs oil milk
  </p>
    <div class="box">
        <h1 v-if="APIData.username">{{APIData.username}}'s profile</h1>
        <p class="error" v-if="error">{{error}}</p>
        <div v-if="APIData.username" class="center">
           <ul>
              <li v-if="APIData.username"><span class="profile">Username:</span>{{APIData.username}}</li>
              <li v-else><span class="profile">Username:</span>N/A</li>
              <li v-if="APIData.first_name"><span class="profile">First name:</span>{{APIData.first_name}}</li>
              <li v-else><span class="profile">First name:</span>N/A</li>
              <li v-if="APIData.last_name"><span class="profile">Last name:</span>{{APIData.last_name}}</li>
              <li v-else><span class="profile">Last name:</span>N/A</li>
              <li v-if="APIData.email"><span class="profile">E-mail:</span>{{APIData.email}}</li>
              <li v-else><span class="profile">E-mail:</span>N/A</li>
              <li v-if="APIData.phone"><span class="profile">Phone number:</span>{{APIData.phone}}</li>
              <li v-else><span class="profile">Phone number:</span>N/A</li>
              <li v-if="APIData.street"><span class="profile">Street:</span>{{APIData.street}}</li>
              <li v-else><span class="profile">Street:</span>N/A</li>
              <li v-if="APIData.city"><span class="profile">City:</span>{{APIData.city}}</li>
              <li v-else><span class="profile">City:</span>N/A</li>
              <li v-if="APIData.zip_code"><span class="profile">Zip code:</span>{{APIData.zip_code}}</li>
              <li v-else><span class="profile">Zip code:</span>N/A</li>
          </ul>
          <button><span><router-link :to="this.$store.state.id + '/update'">Update</router-link></span></button>
        </div>

    </div>
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
#container{
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
  background: #232526;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #414345, #232526);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #414345, #232526); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
h1,h3 {
  text-align: center;
  font-weight: lighter;
}
.error{
  text-align: center;
  color: darkred;
  background-color: black;
  z-index: unset;
  position: unset;
  font-weight: bold;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  font-size: large;
}
.box {
  padding-top: 1%;
  width: 30%;
  margin-left: auto;
  margin-right: auto;
  height: 80%;
  margin-top: 2%;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  background: #232526;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #414345, #232526);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #414345, #232526); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
.profile{
  display: inline-block;
  width: 30%;
}
.center{
  width: 80%;
  margin: auto;
}
li{
  list-style-type: none;
}
a{
  text-decoration: none;
  color: white;
}
a:hover{
  color: #dd9add;
}
button {
  margin-top: 20px;
  margin-left: 30%;
  font-family: 'Bad Script', cursive;
  position: relative;
  text-decoration: none;
  font-size: 20px;
  letter-spacing: 5px;
  line-height: 48px;
  width: 160px;
  height: 55px;
}

button span {
  font-family: 'Bad Script', cursive;
   position: absolute;
   display: flex;
   justify-content: center;
   top: 4px;
   right: 4px;
   bottom: 4px;
   left: 4px;
   text-align: center;
   background: #2E2E2E;
   color: rgba(255, 255, 255, 0.781);
   transition: 0.5s;
   z-index: 1;
}

button:hover span {
 color: #dd9add;
}

button::before {
 content: '';
 position: absolute;
 width: 100%;
 height: 100%;
 top: 0;
 left: 0;
 background-size: 400%;
 opacity: 0;
 transition: 0.5s;
 background: linear-gradient(90deg, rgba(255,255,255,1) 0%, rgba(221,154,221,1) 51%, rgba(255,255,255,1) 100%);
}

button::after {
 content: '';
 position: absolute;
 width: 100%;
 height: 100%;
 top: 0;
 left: 0;
 background-size: 400%;
 transition: 0.5s;
 background: linear-gradient(90deg, rgba(255,255,255,1) 0%, rgba(221,154,221,1) 51%, rgba(255,255,255,1) 100%);
}

button span::before {
 content: '';
 position: absolute;
 top: 0;
 left: 0;
 width: 100%;
 height: 50%;
 background: rgba(255,255,255,0.1);
}
.background{
  position: absolute;
  color: dimgray;
  z-index: -1;
  text-align: justify;
}
</style>