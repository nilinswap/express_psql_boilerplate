import Model from "../models/model";
const util = require('util'); 

const paymentModel = new Model("core_payment");
export const getPayment = async (req: any, res: any) => {
  try {
    const payment_id: string = req.query.pymtid
    if (typeof(payment_id) === "undefined"){
        return res.status(400).json({error:"bad request"})
    }
    const clause = util.format("where id=%s", payment_id)
    const data = await paymentModel.select("*", clause);
    res.status(200).json({
        data:{
          payments: data.rows,
        }
    });
  } catch (err) {
    res.status(200).json({ products: err.stack });
  }
};