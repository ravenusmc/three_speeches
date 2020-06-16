<template>
  <div>
    <Navbar />
    <FilterArea />
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/generic/Navbar.vue';
import FilterArea from '@/components/study/FilterArea.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'About',
  components: {
    Navbar,
    FilterArea,
    Footer,
  }
}

</script>

<style scoped>
</style>
