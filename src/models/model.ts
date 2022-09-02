import { pool } from "./pool"
import util from "util"

class Model {
  pool: any
  table: string
  idQuery: string
  constructor(table: string) {
    this.pool = pool
    this.table = table
    this.idQuery = `SELECT * FROM $1 WHERE id='$2'`
    this.pool.on(
      "error",
      (err: any, client: any) => `Error, ${err}, on idle client${client}`
    )
  }

  async select(columns: string, clause: string) {
    let query = `SELECT ${columns} FROM ${this.table} `
    if (clause) query += clause
    console.log("query", query)
    return this.pool.query(query)
  }

  async insert(columns: string, values: string) {
    let query = `INSERT INTO ${this.table} ` + columns + ` VALUES ` + values
    console.log("query", query)
    return this.pool.query(query)
  }

  async findOne(column: string, value: string) {
    let query = util.format(
      `SELECT * FROM %s WHERE %s='%s'`,
      this.table,
      column,
      value
    )
    console.log("query", query)
    return this.pool.query(query)
  }
}
export default Model
