const util = require("util")
import { userModel } from "../../common"

export const getUser = async (req: any, res: any) => {
  try {
    const user_id: string = req.query.uid
    if (typeof user_id === "undefined") {
      return res.status(400).json({ error: "bad request" })
    }
    const clause = util.format("WHERE id=%s", user_id)
    const data = await userModel.select("*", clause)

    res.status(200).json({
      data: {
        user: data.rows,
      },
    })
  } catch (err) {
    res.status(200).json({ products: err.stack })
  }
}
