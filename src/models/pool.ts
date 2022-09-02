import { Pool } from "pg"
import dotenv from "dotenv"
import { dbConfig } from "../config"
dotenv.config()

export const pool: any = new Pool(dbConfig)
