<!-- eslint-disable -->
<template>
  <div class="add-image-widget">
    <div style="margin-left: 15px; font-weight: bold">选择模板</div>
    <el-row>
      <draggable :animation='300' ghostClass="ghost">
        <transition-group>
          <el-col v-for="(poster, index) in this.poster_list" :key="poster" :offset="1" :span="11">
            <el-card body-style="padding: 3px" shadow="hover" style="margin-top: 20px">
              <div :style="{backgroundImage: 'url(' + poster.preview + ')'}"
                   class="middle"
                   @mouseenter="mouseenter(index)"
                   @mouseleave="mouseleave(index)">
                <transition name="plus-icon">
                  <div v-if="poster.hover" class="poster_title">{{ poster.description }}</div>
                </transition>
                <transition name="plus-icon">
                  <div v-if="poster.hover" class="poster_mask">
                    <div class="close_button">
                      <el-button v-if="poster.hover" circle icon="el-icon-close" size="mini"></el-button>
                    </div>
                    <div class="choose_button">
                      <el-button v-if="poster.hover" circle icon="el-icon-s-promotion" size="mini"
                                 @click="chooseTemplate(index)"
                      ></el-button>
                    </div>
                  </div>
                </transition>
              </div>
            </el-card>
          </el-col>
        </transition-group>
      </draggable>
    </el-row>
  </div>
</template>

<script>
/* eslint-disable */
import {mapActions} from 'poster/poster.vuex'
import {RectWidget, ImageWidget, BackgroundWidget, TextWidget} from '../../widgetConstructor'
import draggable from "vuedraggable";
import {validateImage} from '@/utils/imageHelpers'
import {uploadActivityImgAssets} from '@/api/activity'
import axios from "axios";

export default {
  components: {
    draggable,
  },
  data() {
    return {
      poster_list: [
        {
          preview: "http://localhost:5000/get_poster_view/template0.png",
          description: '模板1',
          hover: false,
          data: [
            {type: "background", opacity: 0.5, url: "http://localhost:5000/get_image/bg.png"},
            {type: "rect", backgroundColor: '#FFFFFF', opacity: 0.6, w: 646, h: 427, x: 17, y: 463},
            {type: "rect", backgroundColor: '#FFFFFF', opacity: 0.6, w: 485, h: 212, x: 178, y: 213},
            {type: "rect", backgroundColor: '#000000', opacity: 1, w: 612, h: 4, x: 34, y: 671},
            {type: "img", url: "http://localhost:5000/get_image/department_logo.png", w: 265, h: 55, x: 390, y: 17},
            {type: "img", url: "http://localhost:5000/get_image/school_logo.png", w: 212, h: 55, x: 17, y: 17},
            {type: "img", url: "http://localhost:5000/get_image/photo.png", w: 140, h: 212, x: 17, y: 214},
            {type: "img", url: "http://localhost:5000/get_image/qrcode.png", w: 106, h: 106, x: 542, y: 300},
            {
              type: "text", content: "文字到海报的端到端生成, 测试一下文字长度会不会超出海报",
              font: {
                fontSize: '32px',
                color: '#2D5960',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '158%'
              },
              w: 560, h: 120, x: 60, y: 76
            },
            {
              type: "text", content: "时间:",
              font: {
                fontSize: '18px',
                color: '#2D5960',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 70, h: 35, x: 184, y: 225
            },
            {
              type: "text", content: "2022年11月16日(周三) 9:30-11:30",
              font: {
                fontSize: '18px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 295, h: 35, x: 238, y: 225
            },
            {
              type: "text", content: "地点:",
              font: {
                fontSize: '18px',
                color: '#2D5960',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 70, h: 35, x: 184, y: 260
            },
            {
              type: "text", content: "第一科研楼报告厅",
              font: {
                fontSize: '18px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 166, h: 35, x: 238, y: 260
            },
            {
              type: "text", content: "报告人:",
              font: {
                fontSize: '18px',
                color: '#2D5960',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 80, h: 35, x: 184, y: 295
            },
            {
              type: "text", content: "陈明 副教授/杜克大学",
              font: {
                fontSize: '18px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 200, h: 35, x: 256, y: 295
            },
            {
              type: "text", content: "邀请人:",
              font: {
                fontSize: '18px',
                color: '#2D5960',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 80, h: 35, x: 184, y: 330
            },
            {
              type: "text", content: "原佩琦 学术垃圾/南方科技大学",
              font: {
                fontSize: '18px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 270, h: 35, x: 256, y: 330
            },
            {
              type: "text", content: "腾讯会议号:",
              font: {
                fontSize: '18px',
                color: '#2D5960',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 116, h: 35, x: 184, y: 365
            },
            {
              type: "text", content: "123-456-789",
              font: {
                fontSize: '18px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 200, h: 35, x: 290, y: 365
            },
            {
              type: "text", content: "Abstract:",
              font: {
                fontSize: '19px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '100%'
              },
              w: 118, h: 50, x: 25, y: 465
            },
            {
              type: "text", content: "About the speaker:",
              font: {
                fontSize: '19px',
                color: '#000000',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '158%'
              },
              w: 208, h: 50, x: 25, y: 678
            },
            {
              type: "text",
              content: "We present a novel method for blending hierarchical layouts with semantic labels. The core of our method is a hierarchical structure correspondence algorithm, which recursively finds optimal substructure correspondences, achieving a globally optimal correspondence between a pair of hierarchical layouts. This correspondence is consistent with the structures of both layouts, allowing us to define the union of the layouts’ structures. The resulting compound structure helps extract intermediate layout structures, from which blended layouts can be generated via an optimization approach.",
              font: {
                fontSize: '16px',
                fontFamily: '"Times New Roman",Georgia,Serif',
                color: '#595959',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '135%'
              },
              w: 625,
              h: 170,
              x: 26,
              y: 489
            },
            {
              type: "text",
              content: "We present a novel method for blending hierarchical layouts with semantic labels. The core of our method is a hierarchical structure correspondence algorithm, which recursively finds optimal substructure correspondences, achieving a globally optimal correspondence between a pair of hierarchical layouts. This correspondence is consistent with the structures of both layouts, allowing us to define the union of the layouts’ structures. The resulting compound structure helps extract intermediate layout structures, from which blended layouts can be generated via an optimization approach.",
              font: {
                fontSize: '16px',
                fontFamily: '"Times New Roman",Georgia,Serif',
                color: '#595959',
                fontWeight: 'bold',
                textAlign: 'left',
                fontStyle: '',
                letterSpacing: 0,
                lineHeight: '135%'
              },
              w: 625,
              h: 170,
              x: 26,
              y: 708
            },
          ]
        },
        {preview: "http://localhost:5000/get_poster_view/template1.png", description: '模板2', hover: false, data: []},
        {preview: "http://localhost:5000/get_poster_view/template2.png", description: '模板3', hover: false, data: []},
        {preview: "http://localhost:5000/get_poster_view/template3.png", description: '模板4', hover: false, data: []},
        {preview: "http://localhost:5000/get_poster_view/template4.png", description: '模板4', hover: false, data: []}]
    }
  },
  methods: {
    ...mapActions(['addItem', 'addAssistWidget', 'addBackground']),
    renderPoster(index) {
      let poster_data = this.poster_list[index].data
      for (let i = 0; i < poster_data.length; i++) {
        if (poster_data[i].type === "background") {
          this.urlToBase64(poster_data[i].url).then(res => {
            const src = res
            let temp_bg = new BackgroundWidget({
              wState: {
                src,
                opacity: poster_data[i].opacity,
                isSolid: false
              }
            })
            this.addBackground(temp_bg)
          })
        } else if (poster_data[i].type === "img") {
          this.urlToBase64(poster_data[i].url).then(res => {
            const src = res
            let temp_img = new ImageWidget({wState: {src}})
            temp_img.dragInfo.w = poster_data[i].w
            temp_img.dragInfo.h = poster_data[i].h
            temp_img.dragInfo.x = poster_data[i].x
            temp_img.dragInfo.y = poster_data[i].y
            // 若不设定true则会根据源文件自适应图片大小，我们渲染出来的图片希望可以自己设置宽高，所以将isCopied设为true
            temp_img.isCopied = true
            this.addItem(temp_img)
          })
        } else if (poster_data[i].type === "rect") {
          let temp_rect = new RectWidget()
          temp_rect.dragInfo.w = poster_data[i].w
          temp_rect.dragInfo.h = poster_data[i].h
          temp_rect.dragInfo.x = poster_data[i].x
          temp_rect.dragInfo.y = poster_data[i].y
          temp_rect.wState.style.backgroundColor = poster_data[i].backgroundColor
          temp_rect.wState.style.opacity = poster_data[i].opacity
          this.addItem(temp_rect)
        } else if (poster_data[i].type === "text") {
          let temp_text = new TextWidget(
              {
                wState: {
                  text: poster_data[i].content,
                  style: poster_data[i].font
                }
              })
          temp_text.dragInfo.w = poster_data[i].w
          temp_text.dragInfo.h = poster_data[i].h
          temp_text.dragInfo.x = poster_data[i].x
          temp_text.dragInfo.y = poster_data[i].y
          // console.log(temp_text)
          temp_text.isCopied = true
          this.addItem(temp_text)
        }
      }
    },
    mouseenter(index) {
      this.poster_list[index].hover = true
    },
    mouseleave(index) {
      this.poster_list[index].hover = false
    },
    urlToBase64(url) {
      return new Promise((resolve, reject) => {
        let image = new Image();
        image.onload = function () {
          let canvas = document.createElement('canvas');
          canvas.width = this.naturalWidth;
          canvas.height = this.naturalHeight;
          // 将图片插入画布并开始绘制
          canvas.getContext('2d').drawImage(image, 0, 0);
          // result
          let result = canvas.toDataURL('image/png')
          resolve(result);
        };
        // CORS 策略，会存在跨域问题https://stackoverflow.com/questions/20424279/canvas-todataurl-securityerror
        image.setAttribute("crossOrigin", 'Anonymous');
        image.src = url;
        // 图片加载失败的错误处理
        image.onerror = () => {
          reject(new Error('urlToBase64 error'));
        };
      })
    },
    chooseTemplate(index) {
      this.$confirm(`确认切换到海报 "${this.poster_list[index].description}" 吗`, '选择海报模板', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'info'
      }).then(() => {
        this.$message({
          type: 'success',
          message: `已切换至 "${this.poster_list[index].description}"`
        });
        this.renderPoster(index)
      }).catch(action => {
        this.$message({
          type: action === 'cancel' ? 'info' : 'error',
          message: action === 'cancel' ? '已取消' : '渲染海报出错，请选择其它模板'
        });
      });
    }
  }
}
</script>
<style lang="scss" scoped>
.add-image-widget {
  width: 100%;
  box-sizing: border-box;
  padding-right: 15px;
  padding-top: 15px;
  padding-bottom: 15px;

  .add-image {
    width: 100%;
  }
}

.middle {
  height: 187px;
  width: 100%;
  background: no-repeat center top;
  background-size: contain;
}

.poster_title {
  width: 100%;
  height: 20px;
  line-height: 20px;
  font-size: 10px;
  color: white;
  text-align: center;
  background-color: black;
  z-index: 999;
  opacity: 0.8;
}

.poster_mask {
  width: 100%;
  height: calc(100% - 20px);
  background-color: rgba(0, 0, 0, 0.2);
  z-index: 998;
}

.close_button {
  padding-top: 137px;
  padding-right: 3px;
  float: right;
  z-index: 999;
}

.choose_button {
  padding-top: 137px;
  padding-left: 3px;
  float: left;
  z-index: 999;
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

.plus-icon-enter-active {
  transition: opacity .5s;
}

.plus-icon-enter {
  opacity: 0;
}

.plus-icon-leave-active {
  transition: opacity .5s;
}

.plus-icon-leave-to {
  opacity: 0;
}

</style>
