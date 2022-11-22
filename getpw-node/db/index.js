const path = require('path')
const sqlite3 = require("sqlite3").verbose()
const dbPath = path.resolve(__dirname, 'passwd.db')

const db = new sqlite3.Database(dbPath, err => {if(err) throw err})

const select = ({ id, name }) => {
  let w = ';'
  if (id) w = `where id = ${id};`
  if (name) w = `where name like '%${name}%';`
  return new Promise((resolve, reject) => {
    db.all(`select * from passwd ${w}`, (err, row) => {
      if (err) reject(err)
      else resolve(row)
    })
  })
}

const addPw = (name, password) => {
  return new Promise((resolve, reject) => {
    db.run(`insert into passwd ("name", "password", "time") values("${name}", "${password}", ${+new Date()})`, (err, row) => {
      if (err) reject(err)
      else resolve(200)
    })
  })
}

const deletePw = (id) => {
  return new Promise(async (resolve, reject) => {
    const data = await select({ id })
    if (data === '[]') {
      resolve(404)
      return
    }
    db.run(`delete from passwd WHERE id = ${id}`, (err, row) => {
      if (err) reject(err)
      else resolve(200)
    })
  })
}
// INSERT INTO "main"."passwd" ("id", "name", "password", "time") VALUES (1, '1', '2', '2022-11-22 11:00:38');
module.exports = {
  select, addPw, deletePw
}
