<template>
  <div>

    <div id='header'>
      <Title/>
      <HeaderArea/>
    </div>

  </div>
</template>

<script>
import Title from '@/components/home/Title.vue';
import HeaderArea from '@/components/home/HeaderArea.vue';

export default {
  name: 'Home',
  components: {
    Title,
    HeaderArea,
  }
}

</script>

<style scoped>

#header {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

</style>
