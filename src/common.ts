import Model from "./models/model"
export const userModel = new Model("core_user")
export const orderModel = new Model("core_order")

import mongoose from "mongoose"
import CartSchema from "./models/mongo/cartSchema"
import { ICart } from "./models/mongo/cartSchema"
export const cartModel: mongoose.Model<ICart> = mongoose.model<ICart>(
  "Cart",
  CartSchema
)
