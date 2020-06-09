<template>
  <div>

    <div id='header'>
      <Title/>
      <HeaderArea/>
    </div>

    <hr>

    <Purpose/>

    <hr>

    <section id='speechArea'>

      <div id='speechDiv'>

        <Speech
          class='speechArea'
          :title=speechOne
          :url=urlGettysburg>
        </Speech>

        <div class='imageDiv'>
          <img class='imageOne' src="../assets/images/wall.jpg" alt="Vietnam Wall">
        </div>

      </div>

      <div id='speechDiv'>

        <Speech
          class='speechArea'
          :title=speechTwo
          :url=urlDream>
        </Speech>

        <div class='imageDiv'>
          <img class='imageOne' src="../assets/images/dream.jpg" alt="I have a dream image">
        </div>

      </div>

      <div id='speechDiv'>

        <Speech
          class='speechArea'
          :title=speechThree
          :url=urlMilitary>
        </Speech>

        <div class='imageDiv'>
          <img class='imageOne' src="../assets/images/military.jpg" alt="Military image">
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
      speechThree: 'Military Industrial Complex Speech',
      urlGettysburg: 'https://en.wikipedia.org/wiki/Gettysburg_Address#:~:text=The%20Gettysburg%20Address%20is%20a,armies%20defeated%20those%20of%20the',
      urlDream: 'https://www.americanrhetoric.com/speeches/mlkihaveadream.htm',
      urlMilitary: 'https://avalon.law.yale.edu/20th_century/eisenhower001.asp',
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
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 2em;
  margin-top: 50px;
}

#speechDiv {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.speechArea {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.imageDiv {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.imageOne {
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 300px;
  width: 60%;
}


</style>
