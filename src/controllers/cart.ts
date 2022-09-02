import Model from "../models/model"
import mongoose from "mongoose"
import { cartModel } from "../common"
import { ICart } from "../models/mongo/cartSchema"
const util = require("util")

export const getCart = async (req: any, res: any) => {
  try {
    const user_id: string = req.user.rows[0].id
    var db_cart: ICart | null = await cartModel.findOne({ user_id: user_id })
    if (db_cart) {
      res.status(200).json({
        artifacts: db_cart.artifacts,
      })
    }
  } catch (err) {
    res.status(200).json({ products: err.stack })
  }
}

export const addCart = async (req: any, res: any) => {
  try {
    var cs_cart: Array<string> = req.body.artifacts
    const user_id: string = req.user.rows[0].id
    var db_cart: ICart | null = await cartModel.findOne({ user_id: user_id })

    if (db_cart) {
      cs_cart.concat(db_cart.artifacts)
      db_cart.artifacts = cs_cart
      await db_cart.save() //remove this await here
    } else {
      db_cart = new cartModel({
        user_id: user_id,
        artifacts: cs_cart,
      })
      await db_cart.save()
    }
    res.status(200).json({
      artifacts: db_cart.artifacts,
    })
  } catch (err) {
    res.status(200).json({ products: err.stack })
  }
}
