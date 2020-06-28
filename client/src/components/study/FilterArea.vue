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
      'fireActions',
    ]),
    submitSelection(evt) {
      evt.preventDefault();
      const payload = {
        speech: this.speech,
      };
      this.fireActions({ payload });
    },
  }
}
</script>

<style scoped>

section {
  margin-top: 50px;
  height: 500px;
}

form {
  margin-top: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

select {
  width: 275px;
}

@media only all and (max-width: 900px) {

  section {
    margin-top: -100px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 300px;
  }

  form {
    display: flex;
    justify-content: center;
    align-items: center;
  }

}

</style>
