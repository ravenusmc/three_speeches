<template>
  <div>
    <!-- <div>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view/>
  </div>
</template>

<style>
.center {
  text-align: center;
}

.fontSizeHeadings {
  font-size: 55px;
}

.linkFix {
  text-decoration: none;
  color: #BF0D3E;
  margin-right: 15px;
}

.linkFix:hover {
  color: #041E42;
}

.blueColor {
  color: #041E42;
}

.redColor {
  color: #BF0D3E;
}

button {
  margin-top: 30px;
  width: 10%;
  background-color: #BF0D3E;
  border-color: #BF0D3E;
  color: white;
  border-radius: 5px;
}

button:hover {
  background-color: #041E42;
  border-color: #041E42;
}

</style>
