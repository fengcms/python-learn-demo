<template>
  <div>
    <input type="text" v-model="account"> <br>
    <input type="text" v-model="password"> <br>
    <input type="text" v-model="new_password"> <br>
    <input type="button" @click='onSubmit' value="提交">
    <input type="button" @click='logout' value="退出">
    <input type="button" @click='getList' value="获取文章列表">
    <input type="button" @click='search' value="搜索文章列表">
    <input type="button" @click='del' value="删除数据">
    <input type="button" @click='put' value="修改数据">
    <input type="button" @click='post' value="添加数据">
    <input type="button" @click='postMore' value="添加多条数据">
    <input type="button" @click='get' value="获取单条数据">
    <input type="button" @click='getSite' value="获取站点信息">
    <input type="button" @click='postSite' value="更新站点信息">
    <input type="button" @click='putManages' value="更新管理员密码"><br>
    <input type="file" @change='upload'>
  </div>
</template>
<script>
import Rsa from '@/tool/rsa'
export default {
  data () {
    return {
      account: 'admin',
      password: '123456',
      new_password: '1445667',
      img: ''
    }
  },
  created () {
    this.getList()
  },
  methods: {
    getList () {
      this.$api.get('article', {
        page: 0,
        pagesize: 10,
        sort: '-channel_id,id'
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    search () {
      this.$api.get('article', {
        'title-like': '猪'
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    onSubmit () {
      let pw = Rsa(this.password)
      console.log(pw)
      this.$api.post('login', {
        account: this.account,
        password: pw
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    logout () {
      this.$api.get('logout', {
        api_use_store: false
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    del () {
      this.$api.delete('article/38', {love: 1}, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    put () {
      this.$api.put('article/37', {
        title: '我爱你',
        content: '我爱你的内容'
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    get () {
      this.$api.get('article/37', null, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    post () {
      this.$api.post('article', {
        title: '猪八戒',
        channel_id: 2,
        content: '我爱你的内容'
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    postMore () {
      this.$api.post('article', {
        batch_additon: [{
          title: '猪八戒',
          channel_id: 2,
          content: '我爱你的内容'
        }, {
          title: '孙悟空',
          channel_id: 1,
          content: '我爱你的内容'
        }]
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    getSite () {
      this.$api.get('site', null, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    postSite () {
      this.$api.post('site', {
        name: '文章系统'
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    putManages () {
      let pw = Rsa(this.password)
      let npw = Rsa(this.new_password)
      this.$api.put('manages', {
        account: this.account,
        old_password: pw,
        new_password: npw
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    upload (e) {
      let v = this
      var xhr = new XMLHttpRequest()
      xhr.withCredentials = true
      xhr.open('POST', this.$api.root() + 'upload')
      xhr.onload = function () {
        if (xhr.status === 200) {
          let r = JSON.parse(this.responseText)
          if (r.code === 0) {
            v.imgUrl = r.data.url
            v.$emit('input', v.imgUrl)
            v.progress = null
          } else {
            v.progress = null
            window.alert(r.msg)
          }
        // 上传成功
        } else {
        // 处理其他情况
        }
      }
      xhr.onerror = function () {
        // 处理错误
      }
      xhr.upload.onprogress = function (e) {
        // 上传进度
        if (e.lengthComputable) {
          v.progress = ~~(e.loaded / e.total)
        }
      }
      let fd = new FormData()
      fd.append('file', e.target.files[0])
      // 添加参数和触发上传
      xhr.send(fd)
    }
  }
}
</script>
