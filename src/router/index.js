import Vue from 'vue'
import Router from 'vue-router'
import editor from '../views/posterEditor/index'
import search from '../views/posterSearcher/index'

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: search,
    meta: { title: 'Home' }
  },
  {
    path: '/editor',
    component: editor,
    meta: { title: 'Editor' }
  },
  {
    path: '/search',
    component: search,
    meta: { title: 'Home' }
  }
]

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: routes
})
