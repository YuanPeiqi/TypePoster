<template>
  <div class="add-text-widget">
    <el-input
      v-model="text"
      type="textarea"
      :rows="3"
      placeholder="Please describe the poster in your mind..."
      style="margin-bottom: 10px"
    />
    <el-button
      class="add-text"
      size="mini"
      type="plain"
      @click="addRect"
    >Get posters</el-button>
  </div>
</template>

<script>
import { mapActions } from 'poster/poster.vuex'
import { DrawRectWidget } from '../../widgetConstructor'
export default {
  data() {
    return {
      text: '',
      recommendList: []
    }
  },
  methods: {
    ...mapActions(['addAssistWidget']),
    addRect() {
      this.addAssistWidget(new DrawRectWidget())
    }
  }
}
</script>
<style lang="scss" scoped>
.add-text-widget {
  width: 100%;
  box-sizing: border-box;
  padding: 10px;
  .add-text {
    width: 100%;
    color: #606266;
  }
}
</style>
