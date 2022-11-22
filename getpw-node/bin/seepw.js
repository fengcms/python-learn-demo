#!/usr/bin/env node

const { Command } = require('commander')
const { select, deletePw } = require('../db')
const Table = require('cli-table2')
const colors = require('colors')
const dayjs = require('dayjs')

const selectPw = async ({ id, name }) => {
  const res = await select({ id, name })
  if (res.length) {
    const table = new Table({ head: ['ID', '名称', '密码', '创建时间'], wordWrap: true })
    res.forEach(({ id, name, password, time }) => {
      table.push([id, name, password, dayjs(time).format('YYYY-MM-DD HH:mm:ss')])
    })
    console.log(table.toString())
  } else {
    console.log('数据库中暂时还没有存储密码哦！'.green)
  }
  process.exit(0)
}

const deletePassword = async (id) => {
  const res = await deletePw(id)
  if (res === 200) {
    console.log(`ID 为 ${id} 的密码删除成功`.green)
  } else if (res === 404) {
    console.log(`ID 为 ${id} 的密码不存在`.red)
  } else {
    console.log(`ID 为 ${id} 的密码删除失败`.red)
  }
  process.exit(0)
}

if (__filename === process.mainModule.filename) {
  const program = new Command()
  program.version('1.0.0')
    .usage('本程序用来查看和管理数据库中的密码')
    .option('-i, --id <id>', '根据ID查看密码')
    .option('-n, --name <name>', '根据保存的密码名称查询密码（模糊查询）')
    .option('-d, --delete <id>', '删除模式，参数为要删除的密码的ID')
  program.parse()
  const options = program.opts()

  if (options.id) {
    selectPw({ id: options.id })
  } else if (options.name) {
    selectPw({ name: options.name })
  } else if (options.delete) {
    deletePassword(options.delete)
  } else {
    selectPw({})
  }
}
