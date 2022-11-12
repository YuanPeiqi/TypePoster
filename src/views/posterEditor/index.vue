<!-- eslint-disable -->
<template>
  <div class="poster-editor" :class="{ 'init-loading': initLoading }">
    <div class="header">
      <el-row>
        <el-col :span="1">
          <div style="width: 60px; height: 60px; margin-top: 10px"><el-image :src="require('../../assets/logo.png')"></el-image></div>
        </el-col>
        <el-col :span="18">
          <span style="font-weight: bolder; color: #546E7A; font-size: 40px; height: 80px;line-height: 80px">Type</span>
          <span style="font-weight: bolder; color: rgba(244, 67, 54, 0.85); font-size: 40px; height: 80px;line-height: 80px">Poster</span>
        </el-col>
        <el-col :span="5">
          <el-button class="top-button" type="info" icon="el-icon-back" round>Back</el-button>
        </el-col>
      </el-row>
    </div>
    <div class="base">
      <left-side />
      <main-component ref="main" />
      <extend-side-bar />
      <control-component />
    </div>
    <transition name="el-zoom-in-top">
      <layer-panel v-show="layerPanelOpened" />
    </transition>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from './poster.vuex'
import controlComponent from './control/index'
import mainComponent from './main/index'
import leftSide from './leftSide/index'
import extendSideBar from './extendSideBar'
import layerPanel from './extendSideBar/layerPanel'
import store from '@/store'
import posterModule from './vuexModule/poster'
import PubSub from 'pubsub-js'

const DELETE_KEY = 8 // delete
const COPY_KEY = 67 // c
const PASTE_KEY = 86 // v
const LAYER_PANEL_KEY = 76 // l
const REFERENCE_LINE_KEY = 72 // h
const UNDO_KEY = 90 // z
const BACKUP_KEY = 83 // s
const SELECT_ALL_KEY = 65 // a

export default {
  components: {
    controlComponent,
    mainComponent,
    leftSide,
    extendSideBar,
    layerPanel
  },
  data() {
    return {
      text: '',
      initLoading: false,
      collapse: true
    }
  },
  computed: {
    ...mapState([
      'posterItems',
      'layerPanelOpened',
      'activeItems',
      'copiedWidgets',
      'referenceLineOpened',
      'isUnsavedState'
    ]),
    ...mapGetters(['activeItemIds'])
  },
  beforeRouteLeave(to, from, next) {
    if (this.isUnsavedState) {
      const answer = window.confirm(
        'The current page is not saved. Exiting will discard all changes. Do you want to continue?'
      )
      if (answer) {
        next()
      } else {
        next(false)
      }
    } else {
      next()
    }
  },
  beforeCreate() {
    if (!store.hasModule('poster')) {
      /** 注册poster-vuex模块 */
      store.registerModule('poster', posterModule)
    }
  },
  async created() {
    this.initLoading = true
    // if (!store.hasModule('poster')) return
    const loading = this.$loading({
      lock: true,
      text: 'Initializing',
      spinner: 'el-icon-loading',
      background: 'rgba(255, 255, 255, 0.6)'
    })
    await this.resetState()
    const configData = JSON.parse(localStorage.getItem('configData'))
    if (configData) {
      await this.updatePageConfig(configData)
    }
    loading.close()
    this.initLoading = false
    // 订阅
    PubSub.subscribe('saveFunc', (event, data) => {
      this.$setGlobalState({
        imgData: data.imgData,
        configData: data.configData
      })
    })
  },
  async mounted() {
    document.addEventListener('keydown', this.keydownHandle)
    this.body = document.body
    this.mainPanelRef = this.$refs.main.$refs.mainPanel
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.keydownHandle)
    this.killAutoSaveTask()
  },
  methods: {
    ...mapActions([
      'replacePosterItems',
      'replaceActiveItems',
      'pasteWidget',
      'copyWidget',
      'setLayerPanel',
      'setReferenceLineVisible',
      'resetState',
      'updatePageConfig'
    ]),
    ...mapActions({
      undo: 'history/undo',
      redo: 'history/redo',
      backupInit: 'backup/init',
      killAutoSaveTask: 'backup/killAutoSaveTask',
      backupInvoker: 'backup/invoker'
    }),
    keydownHandle(e) {
      if (e.target !== this.body) {
        return
      }
      const keyCode = e.keyCode
      const ctrl = e.ctrlKey || e.metaKey
      const shift = e.shiftKey
      switch (true) {
        case keyCode === DELETE_KEY:
          if (this.activeItemIds.length > 0) {
            this.replacePosterItems(
              this.posterItems.filter(
                (item) => !this.activeItemIds.includes(item.id)
              )
            )
          }
          break
        case keyCode === PASTE_KEY && ctrl:
          if (this.copiedWidgets) {
            this.pasteWidget()
          }
          break
        case keyCode === COPY_KEY && ctrl:
          if (this.activeItems.length > 0) {
            // const copiedWidgets = []
            // const widgetRefs = this.mainPanelRef.$refs
            // this.activeItemIds.forEach((itemId) => {
            // const widgetRef = widgetRefs[itemId][0]
            // copiedWidgets.push(getCopyData(widgetRef.item, widgetRef._self))
            // })
            const copiedWidgets = [...this.activeItems].map((item) => {
              item._copyFrom = 'command'
              return item
            })
            this.copyWidget(copiedWidgets)
          }
          break
        case keyCode === LAYER_PANEL_KEY && ctrl:
          e.preventDefault()
          this.setLayerPanel(!this.layerPanelOpened)
          break
        case keyCode === REFERENCE_LINE_KEY && ctrl:
          e.preventDefault()
          this.setReferenceLineVisible(!this.referenceLineOpened)
          break
        case keyCode === UNDO_KEY && ctrl && shift:
          this.redo()
          break
        case keyCode === UNDO_KEY && ctrl:
          this.undo()
          break
        case keyCode === BACKUP_KEY && ctrl:
          e.preventDefault()
          this.backupInvoker()
          break
        case keyCode === SELECT_ALL_KEY:
          e.preventDefault()
          this.replaceActiveItems(this.posterItems)
          break
        default:
          break
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.header{
  .title{
    margin-left: 30px;
    height: 80px;
    line-height: 80px;
    font-size: 40px;
    font-weight: bolder;
    color: white
  }
  position:relative;
  z-index: 999;
  box-shadow: 0 0 4px rgba(8, 10, 12, 0.5) !important;
  background-color: #ffffff;
  height: 80px;
  padding: 0 30px;
}
.poster-editor {
  width: 100%;
  min-width: 900px;
  height: 100%;
  background-color: #fff;
  position: fixed;
  &.init-loading {
    filter: blur(6px);
  }
  .base {
    width: 100%;
    height: calc(100% - 80px);
    position: relative;
    display: flex;
  }
  .left-side {
    height: 100%;
  }
  .poster-editor-main {
    flex: 1;
    height: 100%;
    box-sizing: border-box;
  }
  .extend-side-bar {
    width: 50px;
    height: 100%;
    border-left: 1px solid $colorBorder;
  }
  .poster-editor-control {
    width: 250px;
    height: 100%;
    box-sizing: border-box;
    border-left: 1px solid $colorBorder;
  }
}
.top-button{
  margin-top: 20px;
  margin-left: 30px;
  font-weight: bold;
  font-size: 15px;
  float: right
}
</style>
