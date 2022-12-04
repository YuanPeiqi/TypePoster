<template>
  <div class="add-image-widget">
    <div style="font-weight: bold">选择模板</div>
    <el-row>
      <el-col :span="11" v-for="(o, index) in 4" :key="o" :offset="index % 2 > 0 ? 2 : 0">
        <el-card :body-style="{ padding: '0px' }" shadow="hover" style="margin-top: 20px">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <span>好吃的汉堡</span>
            <div class="bottom clearfix">
<!--              <time class="time">{{ currentDate }}</time>-->
              <el-button type="text" class="button">操作按钮</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapActions } from 'poster/poster.vuex'
import { ImageWidget } from '../../widgetConstructor'
import { validateImage } from '@/utils/imageHelpers'
import { uploadActivityImgAssets } from '@/api/activity'
export default {
  data() {
    return {}
  },
  methods: {
    ...mapActions(['addItem']),
    selectImgHandler() {
      this.$refs.input.click()
    },
    async selectImg({ currentTarget: inputNode }) {
      try {
        const file = inputNode.files
        const imgFile = file && file[0]
        await validateImage(imgFile)
        const src = await uploadActivityImgAssets(imgFile)
        this.addImage({ src })
      } catch (e) {
        console.error(e)
      } finally {
        inputNode.value = ''
      }
    },
    addImage({ src }) {
      this.addItem(new ImageWidget({ wState: { src }}))
    }
  }
}
</script>
<style lang="scss" scoped>
.add-image-widget {
  width: 100%;
  box-sizing: border-box;
  padding: 15px;
  .add-image {
    width: 100%;
  }
}

  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }
  .image {
    width: 100%;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
</style>
