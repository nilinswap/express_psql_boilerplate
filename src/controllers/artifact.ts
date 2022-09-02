import Model from "../models/model";
const util = require('util'); 

const artifactModel = new Model("core_artifact");
export const 
getArtifact = async (req: any, res: any) => {
  try {
    const artifact_id: string = req.query.afid
    if (typeof(artifact_id) === "undefined"){
        return res.status(400).json({error:"bad request"})
    }
    const clause = util.format("where id=%s", artifact_id)
    const data = await artifactModel.select("*", clause); //wrapper over select which returns the element itself instead of singleton array.
    res.status(200).json({
      data: {  
        artifacts: data.rows,
      }
    });
  } catch (err) {
    res.status(200).json({ artifact: err.stack });
  }

};