<template>
  <div>

    <section>

      <form @submit="submitYears">
        <select v-model="speech" name="speech">
           <option v-for="speech in speeches" v-bind:key="speech" :value="speech">
             {{ speech }}
           </option>
        </select>
        <button>Submit</button>
      </form>

    </section>

  </div>
</template>

<script>
//import { mapActions } from 'vuex';

export default {
  name: "filterArea",
  data() {
    return {
      speech: 'Gettysburg Address',
      speeches: ['Gettysburg Address', 'I have a Dream', 'Military Industrial Complex Speech'],
    };
  },
  methods: {
    submitYears(evt) {
      evt.preventDefault();
      // const payload = {
      //   question: this.question,
      //   answer: this.answer,
      //   sex: this.sex,
      // };
      // this.fetchMapData({ payload });
    },
  }
}
</script>

<style scoped>
</style>
