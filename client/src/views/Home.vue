<template>
  <div>

    <div id='header'>
      <Title/>
      <HeaderArea/>
    </div>

    <Purpose/>

    <section id='speechArea'>

      <div>

        <Speech :title=speechOne></Speech>
        <div>
        </div>
        
      </div>

      <div>

        <Speech :title=speechTwo></Speech>
        <div>
        </div>

      </div>

      <div>

        <Speech :title=speechThree></Speech>
        <div>
        </div>

      </div>

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
  data() {
    return {
      speechOne: 'Gettysburg Address',
      speechTwo: 'I Have a Dream',
      speechThree: 'Military Industrial Complex Speech'
    }
  },
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

#speechArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 2em;
}

</style>
