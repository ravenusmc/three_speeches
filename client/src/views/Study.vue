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

      <div class='sentimentByLineDiv'>
        <h2 class='center'><span>Current Speech:</span> {{ this.selectedSpeech }}</h2>
        <p class='center'><span>Current Sentence:</span> {{ this.sentence }}</p>
        <div class='dataDivArea'>
          <h4>Sentiment: {{ this.sentenceSentiment }}</h4>
          <h4>Subjectivity: {{ this.sentenceSubjectivity }}</h4>
        </div>
      </div>

      <div>
        <p class='sentenmentByLineParagraph'>
          This section will allow the user to see the sentiment of each sentence
          based on the speech that is selected above. The user will be able to use the
          arrows below and change each sentence as they go through the speech. The sentiment
          ranges from -1 to 1.0. The value of -1 means that the sentence has very negative
          sentiment whereas the 1.0 value means that the sentence is positive. The subjectivity
          value ranges from 0.0 to 1.0. O.0 is very objective and 1.0 is very subjective.
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
        <p class='sentimentChartParagraph'>
          The graph shows the average sentiment of each of the speeches.
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
      'sentence',
      'sentenceIndex',
      'sentenceSentiment',
      'sentenceSubjectivity',
    ]),
  }, // End Computed properties
  methods: {
    ...mapActions([
      'getSentenceAndSentiment',
    ]),
    changeSentenceForward(evt) {
      evt.preventDefault();
      let index = this.sentenceIndex
      let newIndex = index += 1
      // I hard coded the values for the length of the speech's simply because
      // I want to move onto a new project. 
      if (this.selectedSpeech === 'Gettysburg Address' && newIndex > 8) {
        alert('You are at the last sentence.')
      }else if (this.selectedSpeech === 'I have a Dream' && newIndex > 77){
        alert('You are at the last sentence.')
      }else if (this.selectedSpeech === 'Military Industrial Complex Speech' && newIndex > 76){
        alert('You are at the last sentence.')
      }else {
        const payload = {
          speech: this.selectedSpeech,
          index: newIndex,
        };
        this.getSentenceAndSentiment({ payload });
      }
    },
    changeSentenceBackward(evt) {
      evt.preventDefault();
      let index = this.sentenceIndex
      let newIndex = index -= 1
      if (newIndex < 0) {
        alert("You are at the first sentence.")
      }else {
        const payload = {
          speech: this.selectedSpeech,
          index: newIndex,
        };
        this.getSentenceAndSentiment({ payload });
      }
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
  grid-gap: 3em;
  margin-bottom: 50px;
  margin-top: -100px;
}

.sentimentByLineDiv {
  margin-left: 5%;
}

.sentenmentByLineParagraph {
  margin: 0 5% 0 5%;
}

.dataDivArea {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
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

span {
  font-weight: bold;
}

.sentimentSection {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-left: 5%;
  margin-right: 5%;
}

.sentimentDiv {
  margin-right: 10%;
}

/****************
Media Queries
****************/

/* Mobile Screen */
@media only all and (max-width: 900px) {

  .firstGraphArea {
    grid-template-columns: 1fr;
  }

  .sentimentByLine {
    display: grid;
    grid-template-columns: 1fr;
    margin-top: 100px;
  }

  .sentimentSection {
    grid-template-columns: 1fr;
  }

  .sentimentChartParagraph {
    margin-left: 5%;
    margin-right: 5%;
  }

}


</style>
