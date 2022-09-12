import Vue from 'vue'
import VueRouter from 'vue-router'
import GeoApp from '../views/GeoApp.vue'
import App from '../views/App.vue'

Vue.use(VueRouter)

// export default new VueRouter({
//   routes: [
//     {
//       path: '/',
//       name: 'App',
//       component: App
//     }
//   ]
// })

const routes = [
  {
    path: 'App',
    name: 'App',
    component: App
  },
  {
    path: 'GeoApp',
    name: 'GeoApp',
    component: GeoApp
  }
]

const router = new VueRouter({
  mode: 'history',
  base: ProcessingInstruction.env.BASE_URL,
  routes
})
export default router
