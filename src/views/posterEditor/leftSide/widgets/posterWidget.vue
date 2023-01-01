<!-- eslint-disable -->
<template>
  <div style="height: 100%; width: 100%">
    <el-dialog
        :modal-append-to-body='false'
        :visible.sync="blendDialogVisible"
        center
        title="模板混合"
        width="30%">
      <div style="width: 100%; height: 600px; display: flex; justify-content: center; align-items: center;">
        <div style="background-color: black; width: 80%; height: 600px;">
          hh
        </div>
      </div>
      <div style="width: 100%; height: 60px; display: flex; justify-content: center; align-items: center;">
        <el-slider
            v-model="alpha"
            :step="25"
            show-stops
            style="width: 60%">
        </el-slider>
      </div>
      <div style="width: 100%; height: 60px; display: flex; justify-content: center; align-items: center;">
        <el-button @click="blendDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="blendDialogVisible = false">确 定</el-button>
      </div>
    </el-dialog>
    <div style="margin-left: 15px; margin-top: 15px; font-weight: bold">选择模板</div>
    <div class="poster-choose-widget">
      <el-row>
        <draggable v-model="poster_list" :options="posterOptions" style="padding: 2%">
          <el-col v-for="(poster, index) in this.poster_list" :key="poster.id" :span="12">
            <el-card body-style="padding: 3px" shadow="hover" style="width: 150px; margin: 5px 5px">
              <div :style="{backgroundImage: 'url(' + poster.preview + ')'}"
                   class="poster-view"
                   @mouseenter="mouseenter(index)"
                   @mouseleave="mouseleave(index)"
              >
                <transition name="plus-icon">
                  <div v-if="poster.hover" class="poster_title">{{ poster.description }}</div>
                </transition>
                <transition name="plus-icon">
                  <div v-if="poster.hover" class="poster_mask">
                    <div class="close_button">
                      <el-button v-if="poster.hover" circle icon="el-icon-close" size="mini" @click="removeTemplate(index)"></el-button>
                    </div>
                    <div class="choose_button">
                      <el-button v-if="poster.hover" circle icon="el-icon-s-promotion" size="mini" @click="chooseTemplate(index)"></el-button>
                    </div>
                  </div>
                </transition>
              </div>
            </el-card>
          </el-col>
        </draggable>
      </el-row>
    </div>
    <div style="padding: 15px; font-weight: bold; position: relative">请选择两套模板
      <el-button round size="mini"
                 style="font-weight: bold; font-size: 15px; position: absolute; background-color: #dcdee0;
                 color: #54616c; border-color: #dcdee0; vertical-align: middle; right: 15px; top: 8px"
                 @click="blendTemplate">
        混合
      </el-button>
    </div>
    <div style="height: calc(28% - 78px); width: 100%; display: flex;">
      <div style="height: 100%; width: 50%; background: rgba(212,212,212,0.34); padding: 2%">
        <draggable v-model="blender1" :options="blenderOptions" style="height: 100%; width: 100%; border: 3px dashed #9099a4;
                        border-radius: 4px; display: flex; padding: 1%; overflow: hidden"
                   @change="blender1.splice(1)">
          <el-card v-for="poster in this.blender1" :key="poster.id"
                   body-style="padding: 3px" shadow="hover" style="height: 195px; min-width: 100%">
            <div :style="{backgroundImage: 'url(' + poster.preview + ')'}"
                 class="poster-view"
            ></div>
          </el-card>
        </draggable>
      </div>
      <div style="height: 100%; width: 50%; background: rgba(212,212,212,0.34); padding: 2%">
        <draggable v-model="blender2" :options="blenderOptions" style="height: 100%; width: 100%; border: 3px dashed #9099a4;
                        border-radius: 4px; display: flex; padding: 1%; overflow: hidden"
                   @change="blender2.splice(1)">
          <el-card v-for="poster in this.blender2" :key="poster.id"
                   body-style="padding: 3px" shadow="hover" style="height: 195px; min-width: 100%">
            <div :style="{backgroundImage: 'url(' + poster.preview + ')'}"
                 class="poster-view"
            ></div>
          </el-card>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import {mapActions} from 'poster/poster.vuex'
import {BackgroundWidget, ImageWidget, RectWidget, TextWidget} from '../../widgetConstructor'
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  data() {
    return {
      user: 'test_user',
      blendDialogVisible: false,
      alpha: 0,
      poster_list: this.$store.state.poster_list,
      blender1: [],
      blender2: [],
      posterOptions: {
        group: {name: 'poster', pull: 'clone', put: false},
        animation: 300,
        ghostClass: "ghost",
      },
      blenderOptions: {
        group: {name: 'blender', pull: 'clone', put: true},
        ghostClass: "ghost",
      },
    }
  },
  methods: {
    ...mapActions(['addItem', 'addAssistWidget', 'addBackground', 'removeAllAssistWidgets', 'removeBackground', 'removeAllItems']),
    renderPoster(index) {
      this.removeAllAssistWidgets()
      this.removeAllItems()
      this.removeBackground()
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
        } else if (poster_data[i].type === "text" || poster_data[i].type === "title") {
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
    },
    removeTemplate(index) {
      this.$confirm(`确认移除 "${this.poster_list[index].description}" 吗`, '移除海报模板', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'info'
      }).then(() => {
        this.$message({
          type: 'success',
          message: `成功移除 "${this.poster_list[index].description}"`
        });
        this.poster_list = this.poster_list.filter(i => i.id !== this.poster_list[index].id)
      }).catch(action => {
        this.$message({
          type: action === 'cancel' ? 'info' : 'error',
          message: action === 'cancel' ? '已取消' : '移除海报出错，请重新操作'
        });
      });
    },
    blendTemplate() {
      this.blendDialogVisible = true;
    }
  }
}
</script>
<style lang="scss" scoped>
.poster-choose-widget {
  width: 100%;
  height: 72%;
  box-sizing: border-box;
  overflow-y: auto;

  .add-image {
    width: 100%;
  }
}

.blender {
  border: 3px dashed #9099a4;
  border-radius: 4px;
  width: 48%;
  height: 190px;
  background: white no-repeat center top;
  background-size: contain;
}

.poster-view {
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
