<template>
  <div>

    <div class='imageArea'>
      <div class='navBarArea'>
        <router-link class='linkFix' to="/">Home</router-link>
        <router-link class='linkFix' to="/study">Study</router-link>
        <router-link class='linkFix' to="/about">About</router-link>
      </div>
      <router-view/>
      <img src="../../assets/images/headerImage.jpg" alt="">
    </div>

  </div>
</template>

<script>
</script>

<style scoped>

.navBarArea {
  font-size: 25px;
  text-align: right;
  padding: 10px;
}

img {
  height: 500px;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

</style>
