const { Command } = require('commander')
const { sum } = require('lodash')
const colors = require('colors')
const clipboard = require('node-clipboardy')

const { shuffle, randint, choice } = require('../utils')
const { addPw } = require('../db')
const cutLength = (length,level) => {
  // 算法比较复杂，简化来说，就是已知数组长度，和数组内数字的和
  // 求一个随机的数组，满足上面的两个条件
  const res = []
  const arr = level === 1 ? [] : level === 3 ? [3, 2] : [4, 3, 2]
  arr.forEach(i => {
    res.push(randint(1, length - sum(res) - i + 1))
  })

  res.push(length - sum(res))

  // 因为第一位生成大数字的几率高于后面的几位，
  // 所以在得到结果后，随机排序一下,以期待更随机一些
  return shuffle(res)
}

const makePassword = (dists, arr) => {
  res = []
  // # 根据字典和数组，循环生成密码
  ;[...new Array(arr.length)].forEach((_, i) => {
    ;[...new Array(arr[i])].forEach((_, j) => {
      res.push(choice(dists[i]))
    })
  })
  return shuffle(res).join('')
}

const getPassword = (length, level) => {
  const arr = cutLength(length,level)
  // 制造字典
  const str1 = '01'
  const str2 = '23456789'
  const str3 = 'abcdefghijkmnpqrstuvwxyz'
  const str4 = 'ABCDEFGHJKMNPQRSTUVWXYZ'
  const str5 = '_@!,.:;-=+/?'

  const dists = {
    1: [str1 + str2],
    3: [str2, str3, str4],
    4: [str2, str3, str4, str5]
  }
  // 生成密码
  return makePassword(dists[level], arr)
}

const returnPassword = async (passwd, name) => {
  clipboard.writeSync(passwd)
  console.log('↓ 新密码已为您创建 ↓'.green)
  console.log(passwd.red)
  console.log('提示：密码已经复制到剪切板')
  if (name) {
    const res = await addPw(name, passwd)
    if (res === 200) console.log('密码已经保存到数据库中'.green)
  }
  process.exit(0)
}

if (__filename === process.mainModule.filename) {
  let length = 8
  let level = 3
  const program = new Command()

  program.version('1.0.0')
    .usage('本程序用来生成简单或复杂的密码。')
    .argument('[length]', '设置密码的长度(默认 8)')
    .option('-n, --name <name>', '为您要保存到数据库的密码设置一个名字。')
    .option('-s, --simple', '密码由纯数字构成')
    .option('-c, --commonly', '密码由数字加大小写字母构成（默认）')
    .option('-d, --difficult', '密码由数字大小写字母以及英文标点符号构成')
    .action((sl) => {
      l = Number(sl)
      if (sl && isNaN(l)) {
        console.log('密码长度必须为数字'.red)
        process.exit(0)
      } else if (l > 255 || l < 4) {
        console.log('错误：密码的长度只能在4-255位之间'.red)
        process.exit(0)
      } else if (sl) {
        length = l
      }
    })
  program.parse()
  const options = program.opts()
  if (options.simple) level = 1
  if (options.difficult) level = 4

  const pw = getPassword(length, level)
  // console.log(pw, options, length)
  returnPassword(pw, options.name)
}
