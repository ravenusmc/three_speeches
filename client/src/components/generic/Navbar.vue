<template>
  <div>

    <!-- BootStrap Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light backgroundColor">
      <a class="navbar-brand fontColor" href="#">3 Speeches</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#"><router-link class='fontColor' to="/">Home</router-link></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><router-link class='fontColor' to="/study">Study</router-link></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><router-link class='fontColor' to="/about">About</router-link></a>
          </li>
        </ul>
      </div>
    </nav>
    <!-- End BootStrap Navbar -->

  </div>
</template>

<script>

export default {

}

</script>

<style scoped>

.backgroundColor {
  background-color: #041E42 !important;
}

.fontColor {
  color: white !important;
}

</style>
