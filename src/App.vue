<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script>
import 'element-ui/lib/theme-chalk/index.css'
import '@/styles/index.scss' // global css
import '@/styles/element-variables.scss'
import store from './store'

export default {
  store
}
</script>
<style lang="scss">
</style>

