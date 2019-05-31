<template>
  <div class="home">
    <el-upload
      class="upload-box"
      :drag="true"
      action="/upimg"
      :show-file-list="false"
      :on-success="onSuccess"
      >
      <div class="c">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </div>
    </el-upload>
    <div class="btns">
      <el-button-group>
        <el-button type="primary" id="mdbtn" size="mini" @click="copyStr(mdPath)">复制 MDCODE</el-button>
        <el-button type="primary" size="mini" @click="copyStr(githubPath)">复制 GITHUB URL</el-button>
        <el-button type="primary" size="mini" @click="copyStr(imgPath)">复制图片相对路径</el-button>
        <el-button type="primary" size="mini" @click="copyStr(localPath)">复制本地绝对路径</el-button>
      </el-button-group>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      imgPath: '',
      mdPath: '',
      githubPath: '',
      prePath: '',
      localPath: ''
    }
  },
  methods: {
    onSuccess (res) {
      if (res.status === 0) {
        let fix = 'https://raw.githubusercontent.com/fengcms/articles/master/image'
        let local = '/Users/fungleo/Documents/Blog/articles/image'
        let path = res.data.path
        let mdPath = `![](${fix}${path})`
        this.imgPath = path
        this.mdPath = mdPath
        this.githubPath = fix + path
        this.localPath = local + path
        setTimeout(() => document.getElementById('mdbtn').click(), 500)
      } else {
        this.$message.error(res.data)
      }
    },
    copyStr (str) {
      if (str === '') {
        this.$message.error('内容为空，不能复制')
        return
      }
      let oInput = document.createElement('input')
      oInput.value = str
      document.body.appendChild(oInput)
      oInput.focus()
      oInput.select()
      try {
        var successful = document.execCommand('copy', false, null)
        console.log(successful)
        var msg = successful ? '成功复制到剪贴板' : '该浏览器不支持点击复制到剪贴板111'
        this.$message.success(msg)
      } catch (err) {
        this.$message.success('该浏览器不支持点击复制到剪贴板')
      }
      oInput.parentNode.removeChild(oInput)
    }
  }
}
</script>

<style lang="scss">
@import "./Home.scss";
</style>
