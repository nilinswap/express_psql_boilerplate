export const authware = async (req: any, res: any, next: any) => {
  try {
    console.log("req.cookies", req.cookies)
    if (req.isAuthenticated()) {
      console.log("guy's trusted")
      next()
    } else {
      res.status(401).json({
        message: "tresspassing attempted",
        status: "failure",
      })
    }
  } catch (err) {
    next(err)
  }
}
