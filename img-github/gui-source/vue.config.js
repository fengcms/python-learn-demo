module.exports = {
  baseUrl: '/gui/',
  devServer: {
    proxy: {
      '/upimg': {
        target: 'http://localhost:7000', // 你接口的域名
        secure: false,
        changeOrigin: false
      }
    }
  }
}
