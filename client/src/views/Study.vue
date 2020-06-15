<template>
  <div>
    <Navbar />

    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/generic/Navbar.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'About',
  components: {
    Navbar,
    Footer,
  }
}

</script>

<style scoped>
</style>
