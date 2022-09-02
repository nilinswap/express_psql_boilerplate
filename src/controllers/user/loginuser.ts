import { userModel, cartModel } from "../../common"
import { ICart } from "../../models/mongo/cartSchema"

const util = require("util")

interface ReqBody {
  email: string
  password: string
}

export const loginUser = async (req: any, res: any) => {
  try {
    const { email, password }: ReqBody = req.body
    const clause = util.format("WHERE email='%s'", email)
    const data = await userModel.select("*", clause)
    const rows = data.rows
    const user = rows[0]
    console.log("req.cookies lu", req.cookies)
    var res_cart: Array<string> = []

    const cart: ICart | null = await cartModel.findOne({ user_id: user.id })
    if (cart) {
      res_cart = cart.artifacts
      console.log("cart ke", res_cart)
    }
    res.status(200).json({
      data: {
        user: user,
        cart: res_cart,
      },
      status: "success",
    })
  } catch (err) {
    res.status(500).json({ status: "failure" })
  }
}
