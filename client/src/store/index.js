import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    selectedSpeech: 'Gettysburg Address',
    sentence: 'Four score and seven years ago our fathers brought forth on this continent a new nation conceived in Liberty and dedicated to the proposition that all men are created equal',
    // The sentence index will be used to move back and forth in a speech.
    sentenceIndex: 0,
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
    sentenceSentiment: 0.375,
    sentenceSubjectivity: 0.575,
  },

  getters: {
    wordCountChartData: state => state.wordCountChartData,
    sentimentChartData: state => state.sentimentChartData,
    selectedSpeech: state => state.selectedSpeech,
    sentence: state => state.sentence,
    sentenceIndex: state => state.sentenceIndex,
    sentenceSentiment: state => state.sentenceSentiment,
    sentenceSubjectivity: state => state.sentenceSubjectivity,
  },

  actions: {

    fireActions: ({ dispatch }, payload) => {
      dispatch('setSelectedSpeech', { payload });
      dispatch('setSelectedSentence', { payload });
      dispatch('fetchWordCountChartData', { payload });
    },

    setSelectedSpeech: ({ commit }, { payload }) => {
      let data = payload.payload.speech
      commit('setSpeech', data);
    },

    // The purpose of this action is to set the first sentence on the sentiment
    // and subjectivity section when the speech is changed.
    setSelectedSentence: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/getSelectedSentenceData';
      axios.post(path, payload)
      .then((res) => {
        commit('setSentence', res.data)
      });
    },

    fetchWordCountChartData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/getWordCountData';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b[1] - a[1]);
        commit('setWordCountChartData', res.data);
        // Here I'm resetting the count for the index value when each speech
        // changes.
        let data = 0
        commit('setSentenceIndex', data)
      });
    },

    getSentenceAndSentiment: ({ commit}, { payload }) => {
      const path = 'http://localhost:5000/getSentenceAndSentiment';
      axios.post(path, payload)
      .then((res) => {
        commit('setSentence', res.data[0])
        commit('setSentenceIndex', res.data[1])
        commit('setSentenceSentiment', res.data[2])
        commit('setSentenceSubjectivity', res.data[3])
      });
    },

  },

  mutations: {

    setSpeech(state, data) {
      state.selectedSpeech = data
    },

    setWordCountChartData(state, data) {
      state.wordCountChartData = data;
    },

    setSentence(state, data) {
      state.sentence = data;
    },

    setSentenceIndex(state, data) {
      state.sentenceIndex = data;
    },

    setSentenceSentiment(state, data) {
      state.sentenceSentiment = data;
    },

    setSentenceSubjectivity(state, data) {
      state.sentenceSubjectivity = data;
    }

  },


})
