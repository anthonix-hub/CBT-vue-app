import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// import App from './App.vue'
import geoApp from './GeoApp.vue'

import vuetify from './plugins/vuetify'
import Vuetify from 'vuetify/lib'
// import router from './router'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Vuetify)

// new Vue({
// router,
//   render: h => h(App)
// }).$mount('#app')
new Vue({
  vuetify,
  render: h => h(geoApp)
}).$mount('#geoApp')
