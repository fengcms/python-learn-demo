<template>
  <div>
    <input type="text" v-model="account"> <br>
    <input type="text" v-model="password"> <br>
    <input type="button" @click='onSubmit' value="提交">
    <input type="button" @click='logout' value="退出">
    <input type="button" @click='del' value="删除数据">
    <input type="button" @click='put' value="修改数据">
    <input type="button" @click='post' value="添加数据">
    <input type="button" @click='get' value="获取单条数据">
    <input type="button" @click='getSite' value="获取站点信息">
    <input type="button" @click='postSite' value="更新站点信息">
    <input type="button" @click='putManages' value="更新管理员密码">
  </div>
</template>
<script>
import Rsa from '@/tool/rsa'
export default {
  data () {
    return {
      account: 'admin',
      password: '123456'
    }
  },
  created () {
    this.$api.get('article', null, r => {
      console.log(r)
    }, e => {
      console.log(e)
    })
  },
  methods: {
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
      this.$api.delete('article/4', null, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    put () {
      this.$api.put('article/17', {
        title: '我爱你',
        content: '我爱你的内容'
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    get () {
      this.$api.get('article/17', null, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    },
    post () {
      this.$api.post('article', {
        title: '我爱你',
        channel_id: 2,
        content: '我爱你的内容'
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
      this.$api.put('manages', {
        account: this.account,
        password: pw
      }, r => {
        console.log(r)
      }, e => {
        console.log(e)
      })
    }
  }
}
</script>
