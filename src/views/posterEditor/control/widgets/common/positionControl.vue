<template>
  <setting-content>
    <setting-item label="Width">
      <input v-model.number="dragInfo.w" type="number">
    </setting-item>
    <setting-item label="Height">
      <input v-model.number="dragInfo.h" type="number">
    </setting-item>
    <setting-item label="Top">
      <input v-model.number="dragInfo.y" type="number">
    </setting-item>
    <setting-item label="Left">
      <input v-model.number="dragInfo.x" type="number">
    </setting-item>
    <setting-item label="Rotation">
      <input v-model.number="dragInfo.rotateZ" type="number">
    </setting-item>
  </setting-content>
</template>

<script>
import { settingContent, settingItem } from 'poster/commonUI'
export default {
  components: { settingContent, settingItem },
  props: {
    dragInfo: {
      type: Object,
      default() {
        return {}
      },
      require: true
    }
  },
  data() {
    return {}
  },
  methods: {}
}
</script>
<style lang="scss" scoped></style>
