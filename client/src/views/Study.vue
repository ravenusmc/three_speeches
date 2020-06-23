<template>
  <div>
    <Navbar />

    <Header />

    <section class='firstGraphArea'>
      <FilterArea />
      <GraphCard
       :typeOne='typeOne'
       :data='wordCountChartData'
       :options='chartOptionsOne'>
      </GraphCard>
    </section>

    <hr>

    <section class='sentimentSection'>

      <div>
      </div>

      <div>
        <h2 class='center'>Analysis</h2>
        <p>
          The graph on the left shows the average sentiment of each of the speeches.
          The method that I used to do this is that I went line by line, got the sentiment
          and then averaged the sentiment values.
        </p>
      </div>

    </section>

    <Footer/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Navbar from '@/components/generic/Navbar.vue';
import Header from '@/components/study/Header.vue';
import FilterArea from '@/components/study/FilterArea.vue';
import GraphCard from '@/components/charts/GraphCard.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'About',
  components: {
    Navbar,
    Header,
    FilterArea,
    GraphCard,
    Footer,
  },
  data() {
    return {
      typeOne: 'BarChart',
      chartOptionsOne: {
        title: 'Word Count by Speech',
        legend: { position: 'top' },
        colors:['#05ce78'],
        height: 500,
        animation:{
         duration: 1000,
         easing: 'linear',
       },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    }
  },
  computed: {
  ...mapGetters([
    'wordCountChartData',
  ]),
}, // End Computed properties
}

</script>

<style scoped>

.firstGraphArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.sentimentSection {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

@media only all and (max-width: 900px) {

  .firstGraphArea {
    grid-template-columns: 1fr;
  }

}


</style>
