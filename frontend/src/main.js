// import Vue from 'vue'
// import App from './App.vue'
// import axios from 'axios'
// import VueAxios from 'vue-axios'

// Vue.config.productionTip = false
// Vue.use(VueAxios, axios)

// new Vue({
//   render: h => h(App),
// }).$mount('#app')

import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import App from './App.vue';

// VueAxiosとaxiosをVueに登録
Vue.use(VueAxios, axios);

// Vueインスタンスを作成してマウント
new Vue({
  render: h => h(App),
}).$mount('#app');
