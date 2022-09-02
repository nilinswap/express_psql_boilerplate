import express from "express"
import {
  testenv,
  getCart,
  getArtifact,
  getOrder,
  registerUser,
  addCart,
  checkout,
  loginUser,
} from "../controllers"
import { authware } from "../middleware"
import passport from "../passport/passport"

const indexRouter = express.Router()
indexRouter.get("/", testenv)

//cart
indexRouter.get("/cart", authware, getCart)

indexRouter.post("/cart", authware, addCart)

//artifact
indexRouter.get("/artifact", authware, getArtifact)

indexRouter.post("/artifact", authware, getArtifact)

//order
indexRouter.get("/order", authware, getOrder)

//checkout
indexRouter.get("/checkout", authware, checkout)

//auth
indexRouter.post(
  "/register",
  (req, res, next) => {
    registerUser(req, res)
  },
  passport.authenticate("register")
)

indexRouter.post("/login", passport.authenticate("local"), loginUser)
// NOTE: we don't need redirection params in passport here because we use csr on frontend. we will handle redirection on frontend.

export default indexRouter
