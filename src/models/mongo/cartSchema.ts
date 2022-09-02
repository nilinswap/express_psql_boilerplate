// import mongoose from "mongoose"

import { Schema, Document } from "mongoose"

export interface ICart extends Document {
  user_id: string
  artifacts: Array<string>
}

const CartSchema: Schema = new Schema({
  user_id: {
    type: String,
    required: true,
  },
  artifacts: {
    type: [String],
  },
})

export default CartSchema
