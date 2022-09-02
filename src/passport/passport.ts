import bcrypt from "bcrypt"
import { userModel } from "../common"
import passport from "passport"
import Strategy from "passport-local"

const LocalStrategy = Strategy.Strategy

passport.serializeUser((user: any, done) => {
  done(null, user.id)
})

passport.deserializeUser((id: any, done) => {
  console.log(
    "deserializing userModel.idQuery",
    userModel.idQuery,
    userModel.table
  )
  userModel
    .findOne("id", id)
    .then(user => done(undefined, user))
    .catch(err => {
      done(err, undefined)
    })
})

// Local Strategy
passport.use(
  new LocalStrategy({ usernameField: "email" }, (email, password, done) => {
    // Match User
    userModel
      .findOne("email", email)
      .then(user => {
        // Create new User
        user = user.rows[0]
        if (!user) {
          console.log("wrong credentials: wrong email")
          done(null, false, { message: "wrong credentials." })
        } else {
          // Match password
          bcrypt.compare(password, user.password, (err, isMatch) => {
            if (err) throw err

            if (isMatch) {
              return done(null, user)
            } else {
              console.log("wrong credentials: wrong password")
              return done(null, false, { message: "wrong credentials" })
            }
          })
        }
      })
      .catch(err => {
        return done(null, false, { message: err })
      })
  })
)

export default passport
