const path = require('path')
const sqlite3 = require("sqlite3").verbose()
const dbPath = path.resolve(__dirname, 'passwd.db')

const db = new sqlite3.Database(dbPath, err => {if(err) throw err})

const selectAll = () => {
  return new Promise((resolve, reject) => {
    db.all(`select * from passwd`, (err, row) => {
      if (err) reject(err)
      else resolve(JSON.stringify(row))
    })
  })
}

const addPw = (name, password) => {
  return new Promise((resolve, reject) => {
    db.run(`insert into passwd ("name", "password") values("${name}", "${password}")`, (err, row) => {
      if (err) reject(err)
      else resolve(200)
    })
  })
}
// INSERT INTO "main"."passwd" ("id", "name", "password", "time") VALUES (1, '1', '2', '2022-11-22 11:00:38');
module.exports = {
  selectAll, addPw
}
