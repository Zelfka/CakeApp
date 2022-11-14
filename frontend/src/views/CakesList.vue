<template>
  <div id="container">
    <NavBar></NavBar>
      <p class="background">eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel cocoa
    eggs milk flour oil fruit caramel eggs milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel cocoa
    cake eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    cake eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream  eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar oil sugar cocoa cream chocolate fruit caramel eggs milk milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel

  </p>
    <h1>KAMA Cakes</h1>
    <p v-if="error" class="error">{{error}}</p>
    <div class="cakes">
      <div v-for="item in pageOfItems" :key="item.id" class="cakeList">
      <div class="cake">
        <h3>{{item.name}}</h3>
        <p>{{item.description}}</p>
        <p>Price: {{item.price}} CZK</p>
        <router-link :to="'/cakes/' + item.id"><img :src="`/img/`+ item.img" alt="picture"></router-link>
        <button v-on:click="add(item.id)">+</button>
        <button v-if="admin === true" id="button"><router-link :to="'/cakes/admin/update/' + item.id">&#9998;</router-link></button>
      </div>
      </div>
      <div class="page">
          <jw-pagination :pageSize=6 :items="APIData" @changePage="onChangePage"></jw-pagination>
        </div>
    </div>
  </div>
</template>

<script>
import {getAPI} from "@/axios-api"
import {mapState} from 'vuex'
import NavBar from "@/components/NavBar"
export default {
  name: "CakesList",
  onIdle () {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  data(){
    return {
      error: '',
      pageOfItems: []
    }
  },
  components: {
    NavBar
  },
  computed: mapState(['APIData', 'admin']),
  created() {
    getAPI.get('bake/api/cakes/', {headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          console.log('Get API has received data')
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  },
  methods: {
    add(id) {
      getAPI.post('order/api/orders/', {
        cake_id: id
      }, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(() => {
            console.log('POST API has received data')
            this.$router.go(0)
          })
          .catch((err) => {
            this.error = err.response.data.detail
          } )
    },
    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    }
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
.cakeList{
  width: 30%;
  text-align: center;
  display: inline-block;
  margin-bottom: 20px;
  margin-right: 1.5%;
  margin-left: 1.5%;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  background: #232526;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #414345, #232526);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #414345, #232526); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  padding-bottom: 10px;
}
.cakes{
  width: 90%;
  margin: auto;

}
img{
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px;
  width: 150px;
  height: 100px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  border-radius: 2px;
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
.background{
  margin-top: 60px;
  position: absolute;
  color: #715e74;
  z-index: -1;
  text-align: justify;
  top: 10%;
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
a{
  text-decoration: none;
  color: black;
  vertical-align: middle;
}
a:hover{
  color: white;
}
#button{
  background-color: lightseagreen;
  transform: scaleX(-1);
  margin-left: 5px;
}
.page{
  text-align: center;
}
</style>