import { orderModel } from "../common"
const util = require("util")

export const getOrder = async (req: any, res: any) => {
  try {
    const user_id: string = req.user.id
    if (typeof user_id === "undefined") {
      return res.status(400).json({ error: "bad request" })
    }
    const clause = util.format("WHERE buyer_id=%s", user_id)
    const data = await orderModel.select("*", clause)
    res.status(200).json({
      data: {
        orders: data.rows,
      },
    })
  } catch (err) {
    res.status(200).json({ error: err.stack })
  } finally {
    console.log("finally")
  }
}
