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
    caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    cocoa cream chocolate fruit milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour sugar cocoa cream chocolate chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk fruit caramel eggs milk fruit caramel eggs
    oil sugar cocoa cream chocolate chocolate fruit caramel eggs milk flour chocolate fruit caramel eggs milk flour fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk fruit caramel eggs milk fruit caramel eggs oil milk eggs
  </p>
    <div class="box">
      <p class="error" v-if="error">{{error}}</p>
      <p class="success" v-else-if="success">{{success}}</p>
      <div v-else>
        <h1> {{username}}'s basket</h1>
        <p><span class="left">Created:</span> {{getFormattedDate(APIData.created)}}</p>
        <div v-for="cake in cakes" :key="cake.id">
          <p>{{cake.name}}: {{cake.price}} CZK</p>
          <button v-on:click="remove(cake.id)">-</button>
        </div>
        <p>Number of cakes: {{APIData.sum_cakes}}</p>
        <p class="price">Total: {{APIData.total_price}} CZK</p>
        <form v-on:submit.prevent="sendOrder">
          <div>
            <label for="date">Pick a day:</label>
            <input type="date" required :min="new Date().toISOString().split('T')[0]" v-model="date" id="date">
          </div>
          <div>
            <label for="detail">Details:</label>
          <input type="text" v-model="details" placeholder="Any details you would like add to your order?" id="'detail">
          </div>
          <button class="button" type="submit"><span>Send order</span></button>
        </form>
      </div>
    </div>

  </div>
</template>

<script>
import NavBar from "@/components/NavBar"
import {getAPI} from "@/axios-api"
import {mapState} from "vuex"
import moment from "moment"
export default {
  name: "UserOrder",
   onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  data (){
    return {
      error: '',
      success: '',
      cakes: [],
      username: '',
      date: '',
      details: ''
    }
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('order/api/orders/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          this.$store.state.APIData = response.data
          this.cakes = response.data.cakes
          this.username = response.data.user.username
          console.log('GET API has received data')
        })
        .catch(err => {
          this.error = err.response.data.detail
        })
  },
  methods: {
    sendOrder(){
      getAPI.put('order/api/orders/', {
        date: this.date,
        details: this.details
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(response => {
            this.success = response.data.detail
            console.log('PUT API has received data')
            this.$router.push('/cakes')
          })
          .catch(err => {
            this.error = err.response.data.detail
          })
    },
    remove(id) {
      getAPI.delete('order/api/orders/' + id + '/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('DELETE API has received data')
            this.$router.go(0)
          })
          .catch(err => (
              console.log(err)
          ))
    },
     getFormattedDate: function (date){
        return moment(date, 'YYYY-MM-DD').format('MMMM Do YYYY');
      },
  }
}
</script>

<style scoped>
#container{
  width: 100%;
  min-height: 105%;
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
.success{
  text-align: center;
  color: green;
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
  padding-bottom: 2%;
}
form{
  text-align: left;
  width: 80%;
  margin: auto;
}
label {
  display: inline-block;
  width: 30%;
  font-size: medium;
}
input{
  width: 60%;
  background-color: inherit;
  font-family: 'Bad Script', cursive;
  color: white;
  border: 0;
  border-bottom: 1px solid white;
  font-size: medium;
  margin-bottom: 3%;
}
.price{
  color: #dd9add;
}
.button {
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

.button span {
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

.button:hover span {
 color: #dd9add;
}

.button::before {
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

.button::after {
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

.button span::before {
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
button{
  vertical-align: middle;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 0;
  color: black;
  font-size: xx-large;
  background: rgb(221,154,221);
  background: radial-gradient(circle, rgba(221,154,221,1) 0%, rgba(249,250,251,1) 45%, rgba(0,0,0,1) 100%);
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
}
button:hover{
  color: white;
  cursor: pointer;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
}
.left{
  display: inline-block;
  width: 10%;
  text-align: left;
}
</style>