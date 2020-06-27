import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    wordCountChartData: [
      ["Word", "Count"],
      ["we", 10],
      ["nation", 5],
      ["dedicated", 4],
      ["great", 3],
      ["dead", 3],
      ["they", 3],
      ["us", 3],
      ["people", 3]
    ],
    sentimentChartData: [
      ['Speech', 'Sentiment'],
      ['Gettysburg Address', 0.1521518759018759],
      ['I have a Dream', 0.11747201520935695],
      ['Military Industrial Complex Speech', 0.0981414680197148]
    ],

  },

  getters: {
    wordCountChartData: state => state.wordCountChartData,
    sentimentChartData: state => state.sentimentChartData,
  },

  actions: {

    fetchWordCountChartData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/getWordCountData';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b[1] - a[1]);
        commit('setWordCountChartData', res.data);
      });
    }

  },

  mutations: {

    setWordCountChartData(state, data) {
      state.wordCountChartData = data;
    },

  },


})
