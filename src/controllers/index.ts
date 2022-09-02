import { testEnvironmentVariable } from "../config"
import { getCart, addCart } from "./cart"
import { getUser, registerUser, loginUser } from "./user"
import { getArtifact } from "./artifact"
import { getOrder } from "./order"
import { checkout } from "./checkout"

export const testenv = (req: any, res: any) => {
  res.status(200).json({ message: testEnvironmentVariable })
}

export {
  getCart,
  getUser,
  getArtifact,
  getOrder,
  registerUser,
  loginUser,
  addCart,
  checkout,
}
