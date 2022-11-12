<template>
<div id="container">
  <p>eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel cocoa
    eggs milk flour oil fruit caramel eggs milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel cocoa
    cake eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream  eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    fruit caramel eggs milk flour oil sugar cocoa fruit caramel eggs milk flour oil milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel
    eggs milk flour sugar cocoa cream chocolate fruit caramel cream eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk flour oil sugar cocoa cream chocolate fruit caramel eggs milk fruit caramel eggs milk fruit caramel eggs

  </p>
  <button id="left"><span><router-link to="register">Register</router-link></span></button>
  <button id="right"><span><router-link to="login">Login</router-link></span></button>
  <div class="headers">
    <h1> Welcome to KAMA Cakes!</h1>
    <h3>Baking cakes is one of my biggest hobbies and here is a collection of my cakes which I have created so far. </h3>
    <h3>Would you like to order such a yummy cake as well?</h3>
    <h3>Please login or register!</h3>
  </div>
  <div class="pic"></div>
</div>
</template>

<script>
export default {
  name: "HomePage",
}
</script>

<style scoped>
@keyframes blink {
  0%{
    background-image: url("../assets/IMG_0106.jpg");
    background-size: cover;
  }
  15%{
    background-image: url("../assets/IMG_1658.jpg");
    background-size: cover;
  }
  30%{
    background-image: url("../assets/IMG_2455.jpg");
    background-size: cover;
  }
  42%{
    background-image: url("../assets/IMG_1866.jpg");
    background-size: cover;
  }
  58%{
    background-image: url("../assets/IMG_2933.jpg");
    background-size: cover;
  }
  70%{
    background-image: url("../assets/IMG_0190.jpg");
    background-size: cover;
  }
  85%{
    background-image: url("../assets/IMG_4185.jpg");
    background-size: cover;
  }
  100%{
    background-image: url("../assets/IMG_4583.jpg");
    background-size: cover;
  }
}
@-webkit-keyframes blink {
   0%{
    background-image: url("../assets/IMG_0106.jpg");
    background-size: cover;
  }
  15%{
    background-image: url("../assets/IMG_1658.jpg");
    background-size: cover;
  }
  30%{
    background-image: url("../assets/IMG_2455.jpg");
    background-size: cover;
  }
  42%{
    background-image: url("../assets/IMG_1866.jpg");
    background-size: cover;
  }
  58%{
    background-image: url("../assets/IMG_2933.jpg");
    background-size: cover;
  }
  70%{
    background-image: url("../assets/IMG_0190.jpg");
    background-size: cover;
  }
  85%{
    background-image: url("../assets/IMG_4185.jpg");
    background-size: cover;
  }
  100%{
    background-image: url("../assets/IMG_4583.jpg");
    background-size: cover;
  }
}
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
.pic{
  width: 600px;
  height: 400px;
  animation: blink 20s infinite;
  -webkit-animation: blink 20s infinite;
  margin: auto;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  border-radius: 3px;
}
button {
  margin-top: 20px;
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
#right{
  margin-top: 20px;
  position: absolute;
  right: 20px;
}
#left{
  position: absolute;
  left: 20px;
}
a{
  text-decoration: none;
  color: white;
}
p{
  top: 31%;
  position: absolute;
  color: dimgray;
  z-index: -1;
  text-align: justify;
}
.headers{
  margin-bottom: 85px;
}
a:hover{
  color: #dd9add;
}
</style>