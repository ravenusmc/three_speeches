<template>
  <div>

    <section>

      <form @submit="submitSelection">
        <h3>Select Speech</h3>
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
import { mapActions } from 'vuex';

export default {
  name: "filterArea",
  data() {
    return {
      speech: 'Gettysburg Address',
      speeches: ['Gettysburg Address', 'I have a Dream', 'Military Industrial Complex Speech'],
    };
  },
  methods: {
    ...mapActions([
      'fetchWordCountChartData',
    ]),
    submitSelection(evt) {
      evt.preventDefault();
      const payload = {
        speech: this.speech,
      };
      this.fetchWordCountChartData({ payload });
    },
  }
}
</script>

<style scoped>

section {
  margin-top: 50px;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

select {
  width: 43%;
}

</style>
