import { BaseService, ErrorWrapper, ResponseWrapper } from "./base";
export default class CheckService extends BaseService {
    static getUnity() {
        return '/smartconstract'
    }

    static async callToolsCheckContext(id, nameCt, contentCt, descriptionCt, ctidCt) {
        const paraData = {
            cid: id,
            name: nameCt,
            content: contentCt,
            description: descriptionCt,
            ctid: ctidCt
        }
        try {
            const response = await this.request({ auth: true }).post('', paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async callDCNTools(tName, tXml) {
        const paraData = {
            toolname: tName,
            xml: tXml
        };
        try {
            const response = await this.request({ auth: true }).post('/tools/', paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async callUnfoldingTools(tName, tcontext_PATH_xml, tltl_PATH_json,initialMarkingInfor) {
        const paraData = {
            name: tName,
            "context_PATH.xml": tcontext_PATH_xml,
            "ltl_PATH.json": tltl_PATH_json,
            "initialMarkingInfor.json": initialMarkingInfor
        };
        try {
            const response = await this.request({ auth: true }).post('/tools/', paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    static async getFileToDownload() {

        try {
            const response = await this.request({ auth: true }).get('/tools/')
            console.log("RES-------------",response)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async callToolLTL(tName) {
        const paraData = {
            toolname: tName
            
        };
        try {
            const response = await this.request({ auth: true }).post('/tools/', paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async callHelenaTools(tName) {
        const paraData = {
            name: tName
        };
        try {
            const response = await this.request({ auth: true }).post('/tools/', paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
}