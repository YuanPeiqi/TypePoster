import Vue from 'vue'
import Router from 'vue-router'
import editor from '../views/posterEditor/index'
import search from '../views/posterSearcher/index'
import choose from '../views/posterChoose/index'

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: search,
    meta: { title: 'Editor' }
  },
  {
    path: '/editor',
    component: editor,
    meta: { title: 'Editor' }
  },
  {
    path: '/choose',
    component: choose,
    meta: { title: 'Choose' }
  },
  {
    path: '/search',
    component: search,
    meta: { title: 'Search Page' }
  }
]

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: routes
})
