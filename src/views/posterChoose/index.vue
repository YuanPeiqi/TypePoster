<!-- eslint-disable -->
<template>
  <div>
    <el-carousel :height="bannerHeight + 'px'" type="card" interval="4000">
      <el-carousel-item v-for="item in imgwrap" :key="item.url" >
        <!--        <div style="width: 80%">-->
        <img :src="require(item.url)" class="bannerimg">
        <!--        </div>>-->
      </el-carousel-item>
    </el-carousel>
    <el-row>
        <router-link :to="{path:'../search'} ">
      <el-button type="danger" round>BACK</el-button>
        </router-link>
            <router-link :to="{path:'../editor', query:{id:cur_bg}}">
      <el-button type="success" round>CHOOSE</el-button>
            </router-link>
    </el-row>
  </div>
</template>
<script>
export default {
    data() {
        return {
            bannerHeight: 200,
            imgwrap: [
                { url: '../../../template/template1.png' },
                { url: '../../../template/template2.png' },
                { url: '../../../template/template3.png' }  //这里换url没成功，看一下是否换回最初的
                // { url: require('../../../template/template4.png') }
            ]
           // cur_bg: require(this.imgwrap[0].url)
        }
    },
     mounted() {
       this.setSize()
       window.addEventListener('resize', () => {
         this.setSize()
       }, false)
  },
  methods: {
    setSize() {
      this.bannerHeight = document.body.clientWidth / 2.5
    },
    getId(id) {
      this.cur_bg = id
    }
  }
}
</script>
<style>
.bannerimg{
  width: 100%;
  height: inherit;
}
  .el-carousel__item h3 {
    color: rgba(0,0,0,1);
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: -50%;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: rgba(0,0,0,1);
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: rgba(0,0,0,1);
  }

</style>
