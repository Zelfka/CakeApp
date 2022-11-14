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
      <h1>Update your profile</h1>
       <p class="error" v-if="error">{{error}}</p>
        <form v-on:submit.prevent="update">
          <div class="input">
            <label for="name">First name:</label>
            <input type="text"  v-model="firstName" placeholder="Enter you first name" id="name">
          </div>
          <div class="input">
            <label for="lastName">Last name:</label>
            <input type="text"  v-model="lastName" placeholder="Enter your last name" id="lastName">
          </div>
          <div class="input">
            <label for="phone">Phone number:</label>
            <input type="tel"  v-model="phone" placeholder="+420 777 777 777" id="phone">
          </div>
          <div class="input">
            <label for="e_mail">E-mail address:</label>
            <input type="email"  v-model="email" placeholder="Enter your email address" id="e_mail">
          </div>
          <div class="input">
            <label for="address">Street and street number:</label>
            <input type="text"  v-model="street" placeholder="Enter your street and street number" id="address">
          </div>
          <div>
            <label for="city">City:</label>
            <input type="text"  v-model="city" placeholder="Enter your city" id="city">
          </div>
          <div class="input">
            <label for="zip">Zip code:</label>
             <input type="number"  v-model="zipCode" placeholder="Enter your zip code" id="zip">
          </div>
          <button type="submit"><span>Update</span></button>
        </form>
    </div>
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
            console.log('PUT API has received data')
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
#container{
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
  background: #232526;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #414345, #232526);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #414345, #232526); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
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
  width: 620px;
  padding-top: 1%;
  margin-top: 2%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  background: #232526;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #414345, #232526);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #414345, #232526); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  height: 80%;
}
h1,h3 {
  text-align: center;
  font-weight: lighter;
}
form{
  text-align: left;
  width: 80%;
  margin: auto;
}
label {
  display: inline-block;
  width: 50%;
  font-size: medium;
}
input{
  width: 40%;
  background-color: inherit;
  font-family: 'Bad Script', cursive;
  color: white;
  border: 0;
  border-bottom: 1px solid white;
  font-size: medium;
  margin-bottom: 3%;
}
button {
  margin-top: 40px;
  margin-left: 33%;
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