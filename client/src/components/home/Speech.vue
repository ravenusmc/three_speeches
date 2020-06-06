<template>
  <div>

    <hr>
    <div>
      <h1>{{ title }}</h1>
      <p><a :href=url>See Speech</a></p>
    </div>


  </div>
</template>

<script>
export default {
  name: "Speech",
  props: ['title', 'url']
}
</script>

<style scoped>

hr {
  position: relative;
  left: -45%;
  border-top: 2px solid #041E42;
  width: 10%;
}

h1 {
  margin-top: 20px;
}

</style>
