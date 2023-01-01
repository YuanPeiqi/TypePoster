<!-- eslint-disable -->
<template>
  <div>
    <div class="header">
      <el-row>
        <el-col :span="1">
          <div style="width: 60px; height: 60px; margin-top: 10px">
            <el-image :src="require('../../assets/logo.png')"></el-image>
          </div>
        </el-col>
        <el-col :span="18">
          <span style="font-weight: bolder; color: #546E7A; font-size: 40px; height: 80px;line-height: 80px">Type</span>
          <span style="font-weight: bolder; color: rgba(244, 67, 54, 0.85); font-size: 40px; height: 80px;line-height: 80px">Poster</span>
        </el-col>
        <el-col :span="5">
          <el-button class="top-button" round style="background-color: #dcdee0; color: #54616c; border-color: #dcdee0">注册</el-button>
          <el-button class="top-button" style="color: #54616c" type="text">登录</el-button>
        </el-col>
      </el-row>
    </div>
    <div class="card">
      <el-radio-group v-model="language" style="margin-bottom: 20px; margin-left: 15px">
        <el-radio-button :label="true">中文</el-radio-button>
        <el-radio-button :label="false">English</el-radio-button>
      </el-radio-group>
      <el-form v-if="language" ref="chineseForm" :model="form" :rules="chineseRules" label-width="100px">
        <el-form-item label="报告主题" prop="title">
          <el-input v-model="form.title" maxlength="30" show-word-limit type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="报告地点" prop="location">
          <el-select v-model="form.location" clearable filterable placeholder="请选择报告地点" style="width: 400px">
            <el-option
                v-for="item in chineseLocation"
                :key="item"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="报告时间" prop="time">
          <el-col :span="8">
            <el-date-picker
                v-model="form.date"
                :picker-options="this.$store.state.pickerOptions"
                placeholder="选择日期"
                format="yyyy-MM-dd"
                value-format="yyyy-MM-dd"
                type="date">
            </el-date-picker>
          </el-col>
          <el-col :span="11">
            <el-time-picker
                v-model="form.time"
                end-placeholder="结束时间"
                is-range
                placeholder="选择时间范围"
                range-separator="至"
                start-placeholder="开始时间"
                format="HH:mm"
                value-format="HH:mm"
            >
            </el-time-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="报告人" prop="reporter">
          <el-input v-model="form.reporter"></el-input>
        </el-form-item>
        <el-form-item label="邀请人">
          <el-input v-model="form.inviter"></el-input>
        </el-form-item>
        <el-form-item label="报告摘要" prop="abstract">
          <el-input v-model="form.abstract" maxlength="260" show-word-limit type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="报告人简介" prop="introduction">
          <el-input v-model="form.introduction" maxlength="260" show-word-limit type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="线上会议号">
          <el-input v-model="form.meeting_num"></el-input>
        </el-form-item>
<!--        <el-form-item label="报告人照片">-->
<!--          <el-upload-->
<!--              :before-upload="beforeAvatarSuccess"-->
<!--              :on-success="handleAvatarSuccess"-->
<!--              :show-file-list="false"-->
<!--              action="https://jsonplaceholder.typicode.com/posts/"-->
<!--              class="upload-demo"-->
<!--              list-type="picture">-->
<!--            <el-button size="small" type="primary">点击上传</el-button>-->
<!--            <div slot="tip" class="el-upload__tip">只能上传<b>jpg/png</b>文件，且不超过<b>500kb</b></div>-->
<!--          </el-upload>-->
<!--        </el-form-item>-->
        <el-form-item>
          <el-button :loading="loading"
                     icon="el-icon-magic-stick"
                     round
                     style="font-weight: bold;"
                     type="primary"
                     @click="submitForm('chineseForm')">
            {{ loading ? '生成中，请稍候...' : '立即生成' }}
          </el-button>
        </el-form-item>
      </el-form>
      <el-form v-else ref="englishForm" :model="form" :rules="englishRules" label-width="100px">
        <el-form-item label="Title" prop="title">
          <el-input v-model="form.title" maxlength="120" show-word-limit type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="Location" prop="location">
          <el-select v-model="form.location" clearable filterable placeholder="Please choose location" style="width: 400px">
            <el-option
                v-for="item in englishLocation"
                :key="item"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Time" prop="time">
          <el-col :span="11">
            <el-date-picker
                v-model="form.time"
                end-placeholder="End"
                format="yyyy-MM-dd HH:mm"
                range-separator="to"
                start-placeholder="Start"
                type="datetimerange"
                value-format="yyyy-MM-dd HH:mm">
            </el-date-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="Reporter" prop="reporter">
          <el-input v-model="form.reporter"></el-input>
        </el-form-item>
        <el-form-item label="Inviter">
          <el-input v-model="form.inviter"></el-input>
        </el-form-item>
        <el-form-item label="Abstract" prop="abstract">
          <el-input v-model="form.abstract" maxlength="600" show-word-limit type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="Intro" prop="introduction">
          <el-input v-model="form.introduction" maxlength="600" show-word-limit type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="Online">
          <el-input v-model="form.meeting_num"></el-input>
        </el-form-item>
        <el-form-item label="Photo">
          <el-upload
              :before-remove="beforeRemove"
              :file-list="fileList"
              :on-exceed="handleExceed"
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              action="https://jsonplaceholder.typicode.com/posts/">
            <el-button size="small" type="primary">upload</el-button>
            <div slot="tip" class="el-upload__tip">Only <b>jpg/png</b> files with size less than <b>500kb</b> can be uploaded</div>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button icon="el-icon-magic-stick"
                     round
                     style="font-weight: bold;"
                     type="primary"
                     @click="submitForm('englishForm')">
            Generate Now
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

let checkIntro = (rule, value, callback) => {
  let word = ['千人计划', '长江学者']
  if (!value) {
    return callback(new Error('介绍不能为空'));
  }
  setTimeout(() => {
    for (let i in word) {
      console.log(value.includes(word[i]));
      if (value.includes(word[i])) {
        callback(new Error('不能包含敏感词' + word[i]));
      }
    }
    callback();
  }, 200);
};
export default {
  data() {
    return {
      // sensitiveWordNotice: false,
      loading: false,
      language: true,
      chineseLocation: ['第一科研楼报告厅', '图书馆102会议室', '工学院南楼551会议室'],
      englishLocation: ['Lecture Hall of 1st Scientific Research Building', 'Conference Room 102, Library'],
      form: {
        userid: 'test_user',
        title: '',
        location: '',
        date: '',
        time: '',
        datetime: '',
        reporter: '',
        inviter: '',
        abstract: '',
        introduction: '',
        meeting_num: '',
        photo: '',
      },
      chineseRules: {
        title: [
          {required: true, message: '请输入报告主题', trigger: 'blur'}
        ],
        location: [
          {required: true, message: '请选择报告地点', trigger: 'change'}
        ],
        time: [
          {required: true, message: '请选择报告时间', trigger: 'blur'}
        ],
        reporter: [
          {required: true, message: '请填写报告人姓名', trigger: 'blur'}
        ],
        abstract: [
          {required: true, message: '请填写报告摘要', trigger: 'blur'}
        ],
        introduction: [
          {validator: checkIntro, trigger: 'blur'},
          {required: true, message: '请填写报告人简介', trigger: 'blur'}
        ],
      },
      englishRules: {
        title: [
          {required: true, message: 'Please enter the title', trigger: 'blur'}
        ],
        location: [
          {required: true, message: 'Please choose a location', trigger: 'change'}
        ],
        time: [
          {required: true, message: 'Please choose the report time', trigger: 'blur'}
        ],
        reporter: [
          {required: true, message: 'Please enter the reporter\'s name', trigger: 'blur'}
        ],
        abstract: [
          {required: true, message: 'Please enter the abstraction', trigger: 'blur'}
        ],
        introduction: [
          {required: true, message: 'Please enter the introduction to reporter', trigger: 'blur'}
        ],
        photo: [
          {required: true, message: 'Please upload the photo', trigger: 'change'}
        ]
      }
    }
  },
  created() {
  },
  methods: {
    submitForm(formName) {
      if (this.form.time !== '' || this.form.time !== null) {
        this.form.datetime = `${this.form.date} ${this.form.time[0]}-${this.form.time[1]}`
      }
      this.$store.state.info_form = this.form
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.loading = true
          axios.get('http://localhost:5000/submit_poster_info', {
            params: this.$store.state.info_form
          }).then((resp) => {
            this.loading = false
            this.$store.commit('setPosterList', resp.data)
            this.$router.push('editor')
          })
        } else {
          console.log('error submit!!');
          return false;
        }
      })
    },
    handleAvatarSuccess(res, file) {
      this.form.photo = URL.createObjectURL(file.raw)
    },
    beforeAvatarSuccess(file) {
      //验证图片格式大小信息
      console.log(file)
      const isJPG = file.type === 'image/jpeg' || file.type === 'image/png';
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isJPG) {
        this.$message.error('上传图片只能是 JPG 或 PNG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传图片大小不能超过 2MB!');
      }
      //图片格式大小信息没问题 执行上传图片的方法
      return isJPG && isLt2M;
    }
  }
}
</script>

<style scoped>
.header {
  box-shadow: 0 0 4px rgba(8, 10, 12, 0.07) !important;
  height: 80px;
  width: 100%;
  padding: 0 200px;
}

.card {
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

.top-button {
  margin-top: 20px;
  margin-left: 30px;
  font-weight: bold;
  font-size: 15px;
  float: right
}
</style>
