<template>
  <div class="add-image-widget">
    <div style="font-weight: bold">选择模板</div>
<!--    <div style="display: flex; overflow: auto;max-width: calc(100% - 216px)">-->
<!--      <draggable style="display: flex; overflow: auto;" :animation='300' ghostClass="ghost">-->
<!--        <transition-group style="display: flex; overflow: auto;">-->
<!--        </transition-group>-->
<!--      </draggable>-->
<!--    </div>-->
    <el-row>
      <el-col :span="11" v-for="(poster,index) in this.poster_list" :key="index" :offset="index % 2 > 0 ? 2 : 0">
        <el-card body-style="padding: 3px" shadow="hover" style="margin-top: 20px">
          <div class="middle"
               @mouseenter="mouseenter(index)"
               @mouseleave="mouseleave(index)"
               :style="{backgroundImage: 'url(' + poster.url + ')'}">
            <div class="poster_title" v-if="poster.hover" style="text-align: center">{{poster.description}}</div>
            <div class="close_button">
              <el-button v-if="poster.hover" size="mini" icon="el-icon-close" circle></el-button>
            </div>
            <div class="choose_button">
              <el-button v-if="poster.hover" size="mini" icon="el-icon-s-promotion" circle
                         @click="renderPoster(index)"
              ></el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapActions } from 'poster/poster.vuex'
import { RectWidget, ImageWidget, BackgroundWidget} from '../../widgetConstructor'
import { validateImage } from '@/utils/imageHelpers'
import { uploadActivityImgAssets } from '@/api/activity'
import axios from "axios";
export default {
  data() {
    return {
      poster_list: [
        { url: "http://localhost:5000/get_poster_view/template1.png",
          description: '模板1',
          hover: false,
          data: [
            { type: "background", url: "http://localhost:5000/get_poster_view/template2.png"},
            { type: "img", url: "http://localhost:5000/get_poster_view/template2.png", w: 200, h: 200, x: 100, y: 100 },
            { type: "rect", backgroundColor: "red", w: 200, h: 200, x: 100, y: 100 }
          ]
        },
        { url: "http://localhost:5000/get_poster_view/template2.png", description: '模板2', hover: false },
        { url: "http://localhost:5000/get_poster_view/template3.png", description: '模板3', hover: false },
        { url: "http://localhost:5000/get_poster_view/template4.png", description: '模板4', hover: false },]
    }
  },
  methods: {
    ...mapActions(['addItem', 'addAssistWidget', 'addBackground']),
    renderPoster(index){
      let poster_data = this.poster_list[index].data
      for(let i = 0; i < poster_data.length; i++){
        if(poster_data[i].type === "background") {
          this.urlToBase64(poster_data[i].url).then(res => {
            const src = res
            let temp_bg = new BackgroundWidget({
              wState: {
                src,
                isSolid: false
              }
            })
            this.addBackground(temp_bg)
          })
        }
        else if(poster_data[i].type === "img") {
          this.urlToBase64(poster_data[i].url).then(res => {
            const src = res
            let temp_img = new ImageWidget({ wState: { src }})
            console.log(temp_img)
            temp_img.dragInfo.w = poster_data[i].w
            temp_img.dragInfo.h = poster_data[i].h
            temp_img.dragInfo.x = poster_data[i].x
            temp_img.dragInfo.y = poster_data[i].y
            // 若不设定true则会根据源文件自适应图片大小，我们渲染出来的图片希望可以自己设置宽高，所以将isCopied设为true
            temp_img.isCopied = true
            this.addItem(temp_img)
          })
        }
        else if(poster_data[i].type === "rect") {
          let temp_rect = new RectWidget()
          temp_rect.dragInfo.w = poster_data[i].w
          temp_rect.dragInfo.h = poster_data[i].h
          temp_rect.dragInfo.x = poster_data[i].x
          temp_rect.dragInfo.y = poster_data[i].y
          temp_rect.wState.style.backgroundColor = poster_data[i].backgroundColor
          this.addItem(temp_rect)
        }
      }
    },
    mouseenter (index) {
      this.poster_list[index].hover = true
    },
    mouseleave (index) {
      this.poster_list[index].hover = false
    },
    urlToBase64(url) {
      return new Promise ((resolve,reject) => {
        let image = new Image();
        image.onload = function() {
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
        image.setAttribute("crossOrigin",'Anonymous');
        image.src = url;
        // 图片加载失败的错误处理
        image.onerror = () => {
          reject(new Error('urlToBase64 error'));
      };
    })
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

.middle {
  height: 187px;
  width: 100%;
  background: no-repeat center top;
  background-size: contain;
}

.poster_title{
  width: 100%;
  height: 20px;
  line-height: 20px;
  font-size: 10px;
  color: white;
  background-color: black;
	z-index:999;
  opacity: 0.8;
}

.close_button{
  padding-top: 137px;
  padding-right: 3px;
  float: right;
	z-index:999;
  opacity: 0.8;
}

.choose_button{
  padding-top: 137px;
  padding-left: 3px;
  float: left;
	z-index:999;
  opacity: 0.8;
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
