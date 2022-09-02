import logger from "morgan"
import express from "express"
import cookieParser from "cookie-parser"
import indexRouter from "./routes/index"
import session from "express-session"
import passport from "./passport/passport"
const MongoStore = require("connect-mongo")(session)
import mongoose from "mongoose"
import cors from "cors"

const MONGO_URI = "mongodb://127.0.0.1:27017/tutorial_social_login"

mongoose
  .connect(MONGO_URI, { useNewUrlParser: true })
  .then(res => console.log(`MongoDB connected ${MONGO_URI}`))
  .catch(err => console.log(err))

const app = express()
app.use(logger("dev"))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(
  cors({
    origin: "http://localhost:1234",
    credentials: true,
  })
)
// Express Session
app.use(
  session({
    secret: "very secret this is",
    resave: false,
    saveUninitialized: true,
    store: new MongoStore({ mongooseConnection: mongoose.connection }),
    cookie: { httpOnly: false },
  })
)

app.use(passport.initialize())
app.use(passport.session())

app.use(cookieParser())

app.use("/api", indexRouter)

export default app
