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
      <h1>Change details of the cake</h1>
      <p class="error" v-if="error">{{error}}</p>
      <form v-on:submit.prevent="updateCake">
        <div class="input">
          <label for="name">Name:</label>
          <input type="text" required v-model="name" placeholder="name of the cake" id="name">
        </div>
        <div id="desc">
          <label for="desc" >Description:</label>
           <textarea required v-model="description" placeholder="Change description of the cake"></textarea>
        </div>
        <div class="input" >
          <label for="egg">Egg free:</label>

            <span class="checkmark"><input type="checkbox" v-model="eggFree" id="egg"></span>
        </div>
        <div class="input">
          <label for="milk">Milk free:</label>

          <span class="checkmark"><input type="checkbox" v-model="milkFree" id="milk"></span>
        </div>
        <div class="input">
          <label for="price">Price (CZK):</label>
          <input type="number" required v-model="price" placeholder="Change price">
        </div>
        <button type="submit"><span>Update</span></button>
      </form>
    </div>
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
#container{
  width: 100%;
  min-height: 100%;
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
  width: 40%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 2%;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  background: #232526;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #414345, #232526);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #414345, #232526); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  padding-bottom: 2%;
}
form{
  text-align: left;
  width: 70%;
  margin: auto;
}
label {
  display: inline-block;
  width: 40%;
  font-size: medium;
}
input{
  width: 50%;
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
textarea{
  width: 50%;
  background-color: inherit;
  font-family: 'Bad Script', cursive;
  color: white;
  border: 0;
  border-bottom: 1px solid white;
  font-size: medium;
  margin-top: 3%;
  margin-bottom: 3%;
  display: inline-block;
}
#desc{
    display: flex;
    align-items: center;
    height: 50px;
    margin-bottom: 5%;
}
.input{
  margin-bottom: 5%;
  position: relative;
}

</style>