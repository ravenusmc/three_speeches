<template>
  <div>

    <div id='header'>
      <Title/>
      <HeaderArea/>
    </div>

    <Purpose/>

  </div>
</template>

<script>
import Title from '@/components/home/Title.vue';
import HeaderArea from '@/components/home/HeaderArea.vue';
import Purpose from '@/components/home/Purpose.vue';

export default {
  name: 'Home',
  components: {
    Title,
    HeaderArea,
    Purpose,
  }
}

</script>

<style scoped>

#header {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

</style>
