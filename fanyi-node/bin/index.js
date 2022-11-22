#!/usr/bin/env node
const { Command } = require('commander')
const readline = require('readline')
const axios = require('axios')
const crypto = require('crypto')
const Table = require('cli-table2')
const clipboard = require('node-clipboardy')
const { APPID, APPKey } = require('./config')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const errorExit = () => {
  console.error('\033[1;31m请求发生错误，请稍后再试\033[4;0m\n')
  rl.close()
  process.exit(0)
}

const exitFanyi = () => {
  console.log('\n\033[0m很高兴为您服务')
  rl.close()
  process.exit(0)
}

const uuid = () => {
  const s = []
  const hexDigits = "0123456789abcdef";
  for (let i = 0; i < 36; i++) {
    s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1)
  }
  s[14] = "4"
  s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1)
  s[8] = s[13] = s[18] = s[23] = "-";

  return s.join("")
}

const showRes = (word, res) => {
  const translation = res.translation

  if (translation) {
    console.log('\n\033[1;36m简单结果\033[35m 该结果会自动复制到剪切板\033[0m')
    const table = new Table({ head: ['原词', word], wordWrap: true })

    res['translation'].forEach(i => {
      table.push(['结果', i])
      clipboard.writeSync(i)
    })
    console.log(table.toString())
  }

  const basic = res.basic
  if (basic) {
    const wfs = basic.wfs
    if (wfs) {
      console.log('\n\033[1;36m有道词典\033[0m')
      const table = new Table({ head: ['演化', '结果'], wordWrap: true })
      wfs.forEach(i => {
        table.push([i.wf.name, i.wf.value])
      })
      console.log(table.toString())
    }
    const exps = basic.explains
    if (exps) {
      console.log('\n\033[1;36m示例\033[0m')
      exps.forEach((item, index) => {
        console.log((index + 1) + '. ' + item + '\n')
      })
    }
  }

  const web = res.web
  if (web) {
    console.log('\n\033[1;36m网络释义\033[0m')
    const table = new Table({ head: ['相关词汇', '翻译'], wordWrap: true })
    web.forEach(i => {
      table.push([i.key, i.value.join(', ')])
    })
    console.log(table.toString())
  }
  console.log('\n')
}

const fanyi = async (word, goNext) => {
  const baseUrl = 'https://openapi.youdao.com/api'
  const salt = uuid()
  const curtime = String(~~(+(new Date()) / 1000))
  const signStr = APPID + word + salt + curtime + APPKey
  const sign = crypto.createHash('sha256').update(signStr).digest('hex')
  const params = {
    q: word,
    appKey: APPID,
    salt,
    from: 'auto',
    to: 'auto',
    sign,
    signType: 'v3',
    curtime
  }
  try {
    const res = await axios.get(baseUrl, { params })
    if (res.status === 200) {
      showRes(word, res.data)
      if (goNext) {
        inputWord(false)
      } else {
        process.exit(0)
      }
    } else {
      errorExit()
    }
  } catch (e) {
    errorExit()
  }
}



const inputWord = (isFirst) => {
  if (isFirst) {
    console.log('\n\033[1;36m英汉互译词典\033[0m by FungLeo')
    console.log('\033[35mTip：退出程序请输入 \033[1;31mexit\033[4;0m\n')
  }
  rl.question('请输入要翻译的内容：', (w) => {
    if (w === 'exit') {
      exitFanyi()
    } else {
      fanyi(w, true)
    }
  })
}

const program = new Command()

program.version('1.0.0')
  .usage(' [待翻译词语]')
  .argument('[word]', '需要翻译的单词')
  .action((word) => {
    if (word) {
      fanyi(word, false)
    } else {
      inputWord(true)
    }
  })
program.parse();

// var options = program.opts()
