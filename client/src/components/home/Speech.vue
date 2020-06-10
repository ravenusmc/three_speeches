<template>
  <div>

    <div id='speechCard'>
      <!-- <hr> -->
      <div>
        <h1>{{ title }}</h1>
        <p><a :href=url>See Speech</a></p>
      </div>
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

#speechCard {
  border-top: 2px solid #BF0D3E;
  border-left: 2px solid #041E42;
  width: 50%;
  padding: 10px;
}

/* hr {
  position: relative;
  left: -45%;
  border-top: 2px solid #041E42;
  width: 10%;
} */

h1 {
  margin-top: 20px;
}

@media only all and (max-width: 900px) {

  #speechCard {
    width: 70%;
    padding: 10px;
  }


}

</style>
