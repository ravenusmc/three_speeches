<template>
  <div>
    <Navbar />
    <Header />
    <section class='firstGraphArea'>
      <FilterArea />
    </section>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/generic/Navbar.vue';
import Header from '@/components/study/Header.vue';
import FilterArea from '@/components/study/FilterArea.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'About',
  components: {
    Navbar,
    Header,
    FilterArea,
    Footer,
  }
}

</script>

<style scoped>

.firstGraphArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

</style>
