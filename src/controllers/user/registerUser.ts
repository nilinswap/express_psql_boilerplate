import { userModel } from "../../common"
import bcrypt from "bcrypt"
const util = require("util")

interface ReqBody {
  email: string
  first_name: string
  last_name: string
  password: string
}

export const registerUser = async (req: any, res: any) => {
  try {
    console.dir(req.body)
    var { email, first_name, last_name, password }: ReqBody = req.body
    password = await bcrypt
      .genSalt(10)
      .then((salt: any) => bcrypt.hash(password, salt))
      .catch((err: any) => {
        console.log("bcrypt error")
        throw err
      })

    const columns = `(email, first_name, last_name, password, phone)`
    const values = util.format(
      `('%s', '%s', '%s', '%s', '0000000000')`,
      email,
      first_name,
      last_name,
      password
    )
    const data = await userModel.insert(columns, values)
    res.status(200).json({
      data: {
        row_count: data.rowCount,
      },
      status: "success",
    })
  } catch (err) {
    // res.status(200).json({ status: "failure"});
    throw err
  }
}
