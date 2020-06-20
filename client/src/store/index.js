import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    wordCountChartData: []
  },

  getters: {
    wordCountChartData: state => state.wordCountChartData,
  },

  actions: {

    fetchWordCountChartData: ({ commit }, { payload }) => {
      console.log(payload)
      const path = 'http://localhost:5000/getWordCountData';
      axios.post(path, payload)
      .then((res) => {
        console.log(res.data)
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
