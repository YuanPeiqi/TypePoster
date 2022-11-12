<!-- eslint-disable -->
<template>
  <div>
    <div class="header">
      <el-row>
        <el-col :span="1">
          <div style="width: 60px; height: 60px; margin-top: 10px"><el-image :src="require('../../assets/logo.png')"></el-image></div>
        </el-col>
        <el-col :span="18">
          <span style="font-weight: bolder; color: #546E7A; font-size: 40px; height: 80px;line-height: 80px">Type</span>
          <span style="font-weight: bolder; color: rgba(244, 67, 54, 0.85); font-size: 40px; height: 80px;line-height: 80px">Poster</span>
        </el-col>
        <el-col :span="5">
          <el-button class="top-button" style="background-color: #dcdee0; color: #54616c; border-color: #dcdee0" round>注册</el-button>
          <el-button class="top-button" type="text" style="color: #54616c">登录</el-button>
        </el-col>
      </el-row>
    </div>
    <div class="card">
    <el-form ref="form" :model="form" label-width="100px">
      <el-form-item label="报告主题">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="报告地点">
        <el-select v-model="form.location" placeholder="请选择报告地点">
        </el-select>
      </el-form-item>
      <el-form-item label="报告时间">
        <el-col :span="11">
          <el-date-picker
              v-model="form.time"
              type="datetimerange"
              range-separator="至"
              start-placeholder="开始时间"
              end-placeholder="结束时间"
              format="yyyy-MM-dd HH:mm"
              value-format="yyyy-MM-dd HH:mm">
          </el-date-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="报告人">
        <el-input v-model="form.reporter"></el-input>
      </el-form-item>
      <el-form-item label="邀请人">
        <el-input v-model="form.inviter"></el-input>
      </el-form-item>
      <el-form-item label="报告摘要">
        <el-input type="textarea" v-model="form.abstract"></el-input>
      </el-form-item>
      <el-form-item label="讲者简介">
        <el-input type="textarea" v-model="form.introduction"></el-input>
      </el-form-item>
      <el-form-item label="线上会议号">
        <el-input v-model="form.meeting_num"></el-input>
      </el-form-item>
      <el-form-item label="报告人照片">
        <el-upload
          class="upload-demo"
          action="https://jsonplaceholder.typicode.com/posts/"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :before-remove="beforeRemove"
          multiple
          :limit="3"
          :on-exceed="handleExceed"
          :file-list="fileList">
          <el-button size="mini" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button style="font-weight: bold;"
                   icon="el-icon-magic-stick"
                   type="primary"
                   @click="onSubmit"
                   round>
          立即生成
        </el-button>
      </el-form-item>
    </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      form: {
        title: '',
        location: '',
        time: '',
        reporter: '',
        inviter: '',
        abstract: '',
        introduction: '',
        meeting_num: ''
      }
    }
  },
  methods: {
    onSubmit() {
      console.log(this.form)
      axios.get('http://localhost:5000/submit_poster_info', {
        params: this.form
      }).then((resp) => {
        console.log(resp.data)
      })
    }
  }
}
</script>

<style scoped>
.header{
  box-shadow: 0 0 4px rgba(8, 10, 12, 0.07) !important;
  height: 80px;
  width: 100%;
  padding: 0 200px;
}
.card{
  padding: 1.25rem;
  background-clip: border-box;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  position: relative;
  width: 50%;
  left: 25%;
  margin-top: 50px;
}
.top-button{
  margin-top: 20px;
  margin-left: 30px;
  font-weight: bold;
  font-size: 15px;
  float: right
}
</style>
