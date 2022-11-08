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
            <li><router-link to="cakes">Cakes</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>

</style>