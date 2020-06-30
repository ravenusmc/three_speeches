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

    <section class='sentimentByLine'>

      <div>
        <h2 class='center'>Current Speech: {{ this.selectedSpeech }}</h2>
        <h4 class='center'>Current Sentence:</h4>
        <h4>Sentiment: </h4>
      </div>

      <div>
        <p>
          This section will allow the user to see the sentiment of each sentence
          based on the speech that is selected above. The user will be able to use the
          arrows below and change each sentence as they go through the speech.
          <div class='changeSentenceArea'>
            <form class='upArrow' @submit="changeSentenceForward">
              <button><i class="fa fa-arrow-circle-up fa-3x" aria-hidden="true"></i></button>
            </form>
            <form class='downArrow' @submit="changeSentenceBackward">
              <button><i class="fa fa-arrow-circle-down fa-3x" aria-hidden="true"></i></button>
            </form>
          </div>
        </p>
      </div>


    </section>

    <hr>

    <section class='sentimentSection'>

      <div>
        <GraphCard
         :typeOne='typeOne'
         :data='sentimentChartData'
         :options='chartOptionsTwo'>
        </GraphCard>
      </div>

      <div class='sentimentDiv'>
        <h2 class='center'>Analysis</h2>
        <p>
          The graph on the left shows the average sentiment of each of the speeches.
          The method that I used to do this is that I went line by line, got the sentiment
          and then averaged the sentiment values. I find it interesting that the Gettysburg
          Address shows the greatest positive sentiment with the military
          Industrial Complex Speech the lowest. Part of me would have thought that the
          I Have a Dream Speech would have the greatest postive sentiment. Maybe it's
          because the speech talks about what can be - what we can reach to in the
          future. The Gettysburg Address on the other hand talks about a new birth
          of freedom. It's almost as if the U.S. is being reborn and that is always
          an optimistic idea. Finally, the military industrial speech is a warning.
          It's not about hope but a warning of what can become of the U.S. if Eisenhower's
          words are not followed.
        </p>
      </div>

    </section>

    <Footer/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
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
        colors:['#BF0D3E'],
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
      chartOptionsTwo: {
        title: 'Average Sentiment of the Speeches',
        legend: { position: 'top' },
        colors:['#BF0D3E'],
        height: 500,
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
      'sentimentChartData',
      'selectedSpeech',
    ]),
  }, // End Computed properties
  methods: {
    ...mapActions([
      'getSentenceAndSentiment',
    ]),
    changeSentenceForward(evt) {
      evt.preventDefault();
      const payload = {
        speech: this.selectedSpeech,
      };
      this.getSentenceAndSentiment({ payload });
    },
    changeSentenceBackward(evt) {
      console.log(this.selectedSpeech)
      evt.preventDefault();
      console.log('Backw')
    }
  }
}

</script>

<style scoped>

.firstGraphArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

/****************
This is the CSS for the change sentiment by line area
****************/

.sentimentByLine {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border: 2px solid red;
}

.changeSentenceArea {
  display: flex;
  justify-content: center;
  align-items: center;
}

.upArrow {
  margin-right: 10px;
}

.downArrow {
  margin-left: 10px;
}


/****************
This is the CSS for the sentiment area
****************/

.sentimentSection {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.sentimentDiv {
  margin-right: 10%;
}

/****************
Media Queries
****************/
@media only all and (max-width: 900px) {

  .firstGraphArea {
    grid-template-columns: 1fr;
  }

}


</style>
