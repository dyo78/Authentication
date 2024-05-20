// src/store/index.js

import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      // Define your state variables here
      counter: 0,
    };
  },
  mutations: {
    // Define your mutation functions here
    increment(state) {
      state.counter++;
    },
  },
  actions: {
    // Define your action functions here
    incrementCounter(context) {
      context.commit('increment');
    },
  },
  getters: {
    // Define your getter functions here
    doubledCounter(state) {
      return state.counter * 2;
    },
  },
});

export default store;
