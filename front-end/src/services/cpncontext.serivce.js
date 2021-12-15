import { BaseService, ErrorWrapper, ResponseWrapper } from "./base";
export class cpncontextService extends BaseService {
    /* Type Object API */
    static getUnity() {
        return 'cpncontext'
    }
    static async GetAllcpncontext() {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/api`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async setDataForCallingTool(context,ltl) {
        try {
            const data = {
                "context":context,
                "ltl": ltl
            }
            console.log('data',data);
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/setDataForCallingTool`, data)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

}