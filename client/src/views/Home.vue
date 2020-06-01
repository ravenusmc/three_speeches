<template>
  <div>

    <div id='header'>
      <Title/>
      <HeaderArea/>
    </div>

    <Purpose/>

    <section>
      <Speech></Speech>
    </section>

    <Footer/>

  </div>
</template>

<script>
import Title from '@/components/home/Title.vue';
import HeaderArea from '@/components/home/HeaderArea.vue';
import Purpose from '@/components/home/Purpose.vue';
import Speech from '@/components/home/Speech.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'Home',
  components: {
    Title,
    HeaderArea,
    Purpose,
    Speech,
    Footer,
  }
}

</script>

<style scoped>

#header {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

</style>
