<template>
  <div>

    <hr>
    <div>
      <h1>{{ title }}</h1>
    </div>


  </div>
</template>

<script>
export default {
  name: "Speech",
  props: ['title']
}
</script>

<style scoped>

hr {
  position: absolute;
  left: 10px;
  border-top: 2px solid #041E42;
  width: 10%;
}

h1 {
  margin-top: 20px;
}

</style>
