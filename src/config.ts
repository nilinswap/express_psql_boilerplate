import dotenv from "dotenv"

const intify = (a: string) => {
  a ? parseInt(a) : undefined
}
// I am leading them to .env.test in case of if node_env is test.
dotenv.config({
  path:
    process.env.NODE_ENV !== undefined
      ? `.env.${process.env.NODE_ENV}`
      : `.env`,
})
export const testEnvironmentVariable = process.env.TEST_ENV_VARIABLE
export const connectionString = process.env.CONNECTION_STRING

export const user = process.env.DB_USER
export const password = process.env.DB_PASSWORD
export const database = process.env.DB_DATABASE
export const host = process.env.DB_HOST
export const port = process.env.DB_PORT
  ? parseInt(process.env.DB_PORT)
  : undefined
export const max = process.env.DB_MAX_CLIENT
  ? parseInt(process.env.DB_MAX_CLIENT)
  : undefined
export const idleTimeoutMillis = process.env.DB_IDLE_TIMEOUT
  ? parseInt(process.env.DB_IDLE_TIMEOUT)
  : undefined

export const dbConfig = {
  user: user,
  password: password,
  database: database,
  host: host,
  port: port,
  max: max,
  idleTimeoutMillis: idleTimeoutMillis,
}
