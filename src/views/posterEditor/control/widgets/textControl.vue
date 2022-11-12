<template>
  <div class="text-control">
    <el-collapse v-model="activeNames">
      <el-collapse-item name="text">
        <template #title>
          <div class="header">
            Text
          </div>
        </template>
        <setting-content>
          <setting-item label="Color & font size">
            <el-color-picker v-model="inColor" size="small" />
            <input v-model.number="inFontSize" min="0" type="number">
          </setting-item>
          <setting-item label="Alignment">
            <radio-group v-model="inTextAlign" :list="textAlignList">
              <template #left>
                <i class="icon-align-left" />
              </template>
              <template #center>
                <i class="icon-align-center" />
              </template>
              <template #right>
                <i class="icon-align-right" />
              </template>
            </radio-group>
          </setting-item>
          <setting-item label="Line height">
            <input v-model.number="inLineHeight" min="0" type="number">
          </setting-item>
          <setting-item label="Letter spacing">
            <input v-model.number="inLetterSpacing" min="0" type="number">
          </setting-item>
          <setting-item label="Format">
            <radio-group v-model="inTextFormat" :list="textFotmatList" />
          </setting-item>
        </setting-content>
      </el-collapse-item>
      <el-collapse-item name="borderAndBackground">
        <template #title>
          <div class="header">Border & background</div>
        </template>
        <setting-content>
          <setting-item label="Background color">
            <el-color-picker v-model="inBackgroundColor" size="small" />
          </setting-item>
          <setting-item label="Padding">
            <input v-model.number="inPadding" min="0" type="number">
          </setting-item>
          <setting-item label="Border color & width">
            <el-color-picker v-model="inBorderColor" size="small" />
            <input v-model.number="inBorderWidth" min="0" type="number">
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
      activeNames: ['text', 'position', 'borderAndBackground'],
      textAlignList: [
        { label: 'left', value: 'left' },
        { label: 'center', value: 'center' },
        { label: 'right', value: 'right' }
      ],
      textFotmatList: [
        { label: 'bold', value: 'bold' },
        { label: 'italic', value: 'italic' },
        { label: 'line', value: 'line-through' }
      ],
      borderStyleList: [
        { label: 'solid', value: 'solid' },
        { label: 'dashed', value: 'dashed' },
        { label: 'double', value: 'double' },
        { label: 'dotted', value: 'dotted' }
      ]
    }
  },
  computed: {
    inColor: {
      get() {
        return this.style.color
      },
      set(val) {
        this.updateStyle('color', val)
      }
    },
    inFontSize: {
      get() {
        return parseInt(this.style.fontSize)
      },
      set(val) {
        this.updateStyle('fontSize', val + 'px')
      }
    },
    inPadding: {
      get() {
        return parseInt(this.style.padding)
      },
      set(val) {
        this.updateStyle('padding', val + 'px')
      }
    },
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
    inLineHeight: {
      get() {
        return parseInt(this.style.lineHeight)
      },
      set(val) {
        this.updateStyle('lineHeight', val + '%')
      }
    },
    inLetterSpacing: {
      get() {
        return parseInt(this.style.letterSpacing)
      },
      set(val) {
        this.updateStyle('letterSpacing', val + 'px')
      }
    },
    inTextAlign: {
      get() {
        return this.style.textAlign
      },
      set(val) {
        this.updateStyle('textAlign', val)
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
    inTextFormat: {
      get() {
        const result = []
        if (this.style.fontWeight === 'bold') {
          result.push('bold')
        }
        if (this.style.fontStyle === 'italic') {
          result.push('italic')
        }
        if (this.style.textDecoration === 'line-through') {
          result.push('line-through')
        }
        return result
      },
      set(list) {
        const operation = list._operation
        const value = list._value
        const newValue = operation === 'add' ? value : ''
        if (value === 'bold') {
          this.updateStyle('fontWeight', newValue)
        } else if (value === 'italic') {
          this.updateStyle('fontStyle', newValue)
        } else if (value === 'line-through') {
          this.updateStyle('textDecoration', newValue)
        }
      }
    }
  },
  methods: {}
}
</script>
<style lang="scss" scoped>
.text-control {
  width: 100%;
  .header {
    box-sizing: border-box;
    padding: 0 20px;
    /* border-style: dashed; */
  }
}
</style>
