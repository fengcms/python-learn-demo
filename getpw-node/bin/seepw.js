const { selectAll, addData } = require('../db')

const seeAllPw = async () => {
  const res = await selectAll()
  console.table(res)
}

const addPw = async (name, pw) => {
  const res = await addData(name, pw)
  if (res === 200) console.log('新增成功')
}

if (__filename === process.mainModule.filename) {
  addPw('fungleo', '123456')
  // let length = 8
  // let level = 3
  // const program = new Command()

  // program.version('1.0.0')
  //   .usage('本程序用来生成简单或复杂的密码。')
  //   .argument('[length]', '设置密码的长度(默认 8)')
  //   .option('-n, --name <name>', '为您要保存到数据库的密码设置一个名字。')
  //   .option('-s, --simple', '密码由纯数字构成')
  //   .option('-c, --commonly', '密码由数字加大小写字母构成（默认）')
  //   .option('-d, --difficult', '密码由数字大小写字母以及英文标点符号构成')
  //   .action((sl) => {
  //     l = Number(sl)
  //     if (sl && isNaN(l)) {
  //       console.log('密码长度必须为数字'.red)
  //       process.exit(0)
  //     } else if (l > 255 || l < 4) {
  //       console.log('错误：密码的长度只能在4-255位之间'.red)
  //       process.exit(0)
  //     } else if (sl) {
  //       length = l
  //     }
  //   })
  // program.parse()
  // const options = program.opts()

}
