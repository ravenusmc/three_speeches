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
    ]

  },

  getters: {
    wordCountChartData: state => state.wordCountChartData,
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
