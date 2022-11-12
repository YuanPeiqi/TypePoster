<template>
  <div class="add-text-widget">
    <ul>
      <li
        v-for="(item, index) in presuppositionTextList"
        :key="index"
        class="presupposition-item"
        :style="item.style"
        @click="addText(item)"
      >
        {{ `Add ${item.text}` }}
      </li>
    </ul>
    <el-button
      class="add-text"
      size="mini"
      type="plain"
      @click="addText(null)"
    >Add a text box</el-button>
  </div>
</template>

<script>
import { mapActions } from 'poster/poster.vuex'
import { TextWidget } from '../../widgetConstructor'

export default {
  data() {
    return {
      presuppositionTextList: [
        {
          text: 'Title',
          style: {
            fontSize: '24px'
          }
        },
        {
          text: 'Subtitle',
          style: {
            fontSize: '18px'
          }
        },
        {
          text: 'Content',
          style: {
            fontSize: '14px'
          }
        },
        {
          text: 'Bold Text',
          style: {
            fontSize: '14px',
            fontWeight: 'bold'
          }
        },
        {
          text: 'Italic Text',
          style: {
            fontSize: '14px',
            fontStyle: 'italic'
          }
        }
      ]
    }
  },
  methods: {
    ...mapActions(['addItem']),
    addText(item) {
      if (item) {
        this.addItem(
          new TextWidget({
            wState: item
          })
        )
      } else {
        this.addItem(new TextWidget())
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.add-text-widget {
  width: 100%;
  box-sizing: border-box;
  padding: 10px;
  .presupposition-item {
    padding: 12px 0 !important;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
    cursor: pointer;
    &:hover {
      color: $colorTheme !important;
    }
  }
  .add-text {
    width: 100%;
    margin-top: 20px;
    color: #606266;
  }
}
</style>
