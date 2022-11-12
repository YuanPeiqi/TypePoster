<template>
  <div class="data-backup">
    <el-form size="small">
      <el-form-item label="Enable automatic backup">
        <el-checkbox v-model="autoSave" />
      </el-form-item>
      <el-form-item label="Automatic backup interval">
        <el-select
          v-model="autoSaveDivision"
          placeholder="Please choose"
          :disabled="!autoSave"
        >
          <el-option
            v-for="item in autoSaveDivisionOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
        <div v-if="!autoSaveDivision" style="font-size:12px">
          The system will automatically backup according to your operation
        </div>
      </el-form-item>
      <el-form-item label="Last backup">
        <span>{{ `${lastBackupTime || "Not yet"}` }}</span>
        <span
          v-if="lastBackup"
          class="recover"
          @click="recover(null)"
        >recovery</span>
      </el-form-item>
    </el-form>
    <el-alert
      title="Attention"
      type="warning"
      :closable="false"
      description="The data is saved locally. If you change the browser or clear the cache, the backup data will be lost."
      show-icon
    />
  </div>
</template>

<script>
import { mapState, mapActions } from 'poster/poster.vuex'
export default {
  data() {
    return {
      autoSaveDivisionOptions: [
        {
          label: 'Intelligent backup',
          value: ''
        },
        {
          label: '5 minutes',
          value: 1000 * 60 * 5
        },
        {
          label: '10 minutes',
          value: 1000 * 60 * 10
        },
        {
          label: '20 minutes',
          value: 1000 * 60 * 20
        },
        {
          label: '30 minutes',
          value: 1000 * 60 * 30
        }
      ]
    }
  },
  computed: {
    ...mapState({
      _autoSave: state => state.backup.autoSave,
      _autoSaveDivision: state => state.backup.autoSaveDivision,
      lastBackup: state => state.backup.lastBackup
    }),
    autoSave: {
      get() {
        return this._autoSave
      },
      set(val) {
        this.toggleAutoSave(val)
      }
    },
    autoSaveDivision: {
      get() {
        return this._autoSaveDivision
      },
      set(val) {
        this.changeAutoSaveDivision(val)
      }
    },
    lastBackupTime() {
      if (!this.lastBackup) {
        return null
      }
      return this.$moment(this.lastBackup.createTime).format('MM-DD HH:mm:ss')
    }
  },
  watch: {
    autoSaveDivision: {
      handler(newVal) {}
    }
  },
  methods: {
    ...mapActions({
      toggleAutoSave: 'backup/toggleAutoSave',
      changeAutoSaveDivision: 'backup/changeAutoSaveDivision',
      recover: 'backup/recover'
    })
  }
}
</script>
<style lang="scss" scoped>
.data-backup {
  .recover {
    margin-left: 10px;
    color: $colorTheme;
    cursor: pointer;
  }
}
</style>
