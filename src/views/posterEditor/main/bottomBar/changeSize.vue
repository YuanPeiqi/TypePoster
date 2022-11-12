<template>
  <div class="change-size">
    <div class="item" title="Please enter the canvas width">
      <span class="label">Width</span>
      <el-input-number
        v-model.number="width"
        style="width:120px"
        controls-position="right"
        size="mini"
      />
    </div>
    <div class="item" title="Please enter the canvas height">
      <span class="label">Height</span>
      <el-input-number
        v-model.number="height"
        style="width:120px"
        controls-position="right"
        size="mini"
      />
    </div>
    <el-button size="mini" @click="save">Commit</el-button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'poster/poster.vuex'
export default {
  data() {
    return {
      width: 0,
      height: 0
    }
  },
  computed: {
    ...mapState({
      canvasWidth: (state) => state.canvasSize.width,
      canvasHeight: (state) => state.canvasSize.height
    })
  },
  created() {
    this.width = this.canvasWidth
    this.height = this.canvasHeight
  },
  methods: {
    ...mapActions(['setCanvasSize', 'seekBackgroundSize']),
    save() {
      if (!(this.width && this.height)) {
        return
      }
      this.setCanvasSize({ width: this.width, height: this.height })
      this.seekBackgroundSize()
    }
  }
}
</script>
<style lang="scss" scoped>
.change-size {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.item {
  margin-bottom: 20px;
  .label {
    padding-right: 10px;
  }
}
</style>
