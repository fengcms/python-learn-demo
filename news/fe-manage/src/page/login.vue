<template>
  <div>
    <input type="text" v-model="account"> <br>
    <input type="text" v-model="password"> <br>
    <input type="text" v-model="new_password"> <br>
    <input type="button" @click='onSubmit' value="提交">
    <input type="button" @click='logout' value="退出">
    <input type="button" @click='getList' value="获取文章列表">
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
      password: '123456',
      new_password: '1445667'
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
        sort: '-id'
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
      this.$api.delete('article/4', {love: 1}, r => {
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
    }
  }
}
</script>
