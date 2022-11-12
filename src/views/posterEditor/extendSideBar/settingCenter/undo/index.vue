<template>
  <div class="undo">
    <el-form size="small">
      <el-form-item label="Limit on #undo/redo">
        <el-input v-model.number="maxHistoryStackLength" type="number" />
      </el-form-item>
    </el-form>
    <el-alert
      title="Tips"
      type="info"
      :closable="false"
      description="Try lowering this property, if the editor is stuck."
      show-icon
    />
  </div>
</template>

<script>
import { mapState, mapActions } from 'poster/poster.vuex'
export default {
  data() {
    return {}
  },
  computed: {
    ...mapState({
      maxHistory: state => state.history.maxHistoryStackLength
    }),
    maxHistoryStackLength: {
      get() {
        return this.maxHistory
      },
      set(val) {
        this.setMaxHistory(val)
      }
    }
  },
  methods: {
    ...mapActions({
      setMaxHistory: 'history/setMaxHistory'
    })
  }
}
</script>
<style lang="scss" scoped>
.el-input {
  width: 200px;
}
</style>
