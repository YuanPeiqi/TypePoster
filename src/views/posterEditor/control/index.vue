<template>
  <div class="poster-editor-control poster-editor_deactivated-ignore" :class="{ collapsed :collapse}">
    <portal-target name="widgetControl" class="control-target" />
    <widget-composition-control />
  </div>
</template>

<script>
import widgetCompositionControl from './widgets/widgetCompositionControl'
export default {
  components: { widgetCompositionControl },
  data() {
    return {
      collapse: false
    }
  },
  methods: {}
}
</script>
<style lang="scss" scoped>
.poster-editor-control {
  width: 100%;
  height: 100%;
  position: relative;
  .control-target {
    width: 100%;
    height: 100%;
    overflow-y: auto;
    //overflow-y: scroll;
  }
  &.collapsed {
    width: 0;
  }
}
</style>
