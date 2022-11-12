<template>
  <div class="rect-control">
    <el-collapse v-model="activeNames">
      <el-collapse-item name="borderAndBackground">
        <template #title>
          <div class="header">Border & Background</div>
        </template>
        <setting-content>
          <setting-item label="Background color">
            <el-color-picker v-model="inBackgroundColor" size="small" />
          </setting-item>
          <setting-item label="Border color & width">
            <el-color-picker v-model="inBorderColor" size="small" />
            <el-input-number v-model="inBorderWidth" style="margin-left: 5px" size="small" controls-position="right" min="0" />
          </setting-item>
          <setting-item label="Border style">
            <el-select v-model="inBorderStyle" size="small">
              <el-option
                v-for="item in borderStyleList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </setting-item>
          <setting-item label="Upper left radian">
            <el-slider
              v-model="inBorderTopLeftRadius"
              style="width:100%"
              @input="borderRadiusInput('tl')"
              @change="borderRadiusChange"
            />
          </setting-item>
          <setting-item label="Upper right radian">
            <el-slider
              v-model="inBorderTopRightRadius"
              style="width:100%"
              @input="borderRadiusInput('tr')"
              @change="borderRadiusChange"
            />
          </setting-item>
          <setting-item label="Lower left radian">
            <el-slider
              v-model="inBorderBottomLeftRadius"
              style="width:100%"
              @input="borderRadiusInput('bl')"
              @change="borderRadiusChange"
            />
          </setting-item>
          <setting-item label="Lower right radian">
            <el-slider
              v-model="inBorderBottomRightRadius"
              style="width:100%"
              @input="borderRadiusInput('br')"
              @change="borderRadiusChange"
            />
          </setting-item>
        </setting-content>
      </el-collapse-item>
      <el-collapse-item name="position">
        <template #title>
          <div class="header">
            Position
          </div>
        </template>
        <position-control :drag-info="dragInfo" />
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import { commonMixin } from './common/mixins'

export default {
  mixins: [commonMixin],
  data() {
    return {
      activeNames: ['position', 'borderAndBackground'],
      borderStyleList: [
        { label: 'solid', value: 'solid' },
        { label: 'dashed', value: 'dashed' },
        { label: 'double', value: 'double' },
        { label: 'dotted', value: 'dotted' }
      ],
      borderRadiusInit: {}
    }
  },
  computed: {
    inBorderColor: {
      get() {
        return this.style.borderColor
      },
      set(val) {
        this.updateStyle('borderColor', val)
      }
    },
    inBorderWidth: {
      get() {
        return parseInt(this.style.borderWidth)
      },
      set(val) {
        this.updateStyle('borderWidth', val + 'px')
      }
    },
    inBorderStyle: {
      get() {
        return this.style.borderStyle
      },
      set(val) {
        this.updateStyle('borderStyle', val)
      }
    },
    inBackgroundColor: {
      get() {
        return this.style.backgroundColor
      },
      set(val) {
        this.updateStyle('backgroundColor', val)
      }
    },
    inBorderTopLeftRadius: {
      get() {
        return parseInt(this.style.borderTopLeftRadius)
      },
      set(val) {
        this.updateStyle('borderTopLeftRadius', val + '%', false /** no pushHistory */)
      }
    },
    inBorderTopRightRadius: {
      get() {
        return parseInt(this.style.borderTopRightRadius)
      },
      set(val) {
        this.updateStyle(
          'borderTopRightRadius',
          val + '%',
          false /** no pushHistory */
        )
      }
    },
    inBorderBottomLeftRadius: {
      get() {
        return parseInt(this.style.borderBottomLeftRadius)
      },
      set(val) {
        this.updateStyle(
          'borderBottomLeftRadius',
          val + '%',
          false /** no pushHistory */
        )
      }
    },
    inBorderBottomRightRadius: {
      get() {
        return parseInt(this.style.borderBottomRightRadius)
      },
      set(val) {
        this.updateStyle(
          'borderBottomRightRadius',
          val + '%',
          false /** no pushHistory */
        )
      }
    }
  },
  methods: {
    borderRadiusInput(flag) {
      // el-slider初始化时会派发input事件
      // 所以在初始化时候忽略该事件
      // 防止往撤销的历史栈里添加数据
      if (!this.borderRadiusInit[flag]) {
        this.borderRadiusInit[flag] = true
        return
      }
      if (!this.borderRadiusDragging) {
        this.borderRadiusDragging = true
        this.pushHistory()
      }
    },
    borderRadiusChange() {
      this.borderRadiusDragging = false
    }
  }
}
</script>
<style lang="scss" scoped>
.rect-control {
  width: 100%;
  .header {
    box-sizing: border-box;
    padding: 0 20px;
    /* border-style: dashed; */
  }
}
</style>
