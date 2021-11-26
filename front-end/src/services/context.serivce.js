import { BaseService, ErrorWrapper, ResponseWrapper } from "./base";
export class ContextService extends BaseService {
    /* Type Object API */
    static getUnity() {
            return 'cpncontext'
        }
        /*---------Get All Of Row In Context Table---------- */
        /*
         * Using baseSerivce(axios) to send request to BackEnd
         * return a type ResponseWrapper having data of Backend
         */
    static async GetAllContext() {
            try {
                const response = await this.request({ auth: true }).get(`${this.getUnity()}/api`) // ->  http://127.0.0.1:8000/context/api/
                return new ResponseWrapper(response, response.data)
            } catch (error) {
                const message = error.response.data ? error.response.data.error : error.response.statusText
                throw new ErrorWrapper(error, message)
            }
        }
        /* ------------- Create A Context In Database------------ */
    static async CreateContext(name, dateFormat, option, description, content) {
        // console.log('ct_name, content, description, option',name, option, description, content);
            try {
                const paraData = {
                    "name": name,
                    "createdDate": dateFormat,
                    "context_type": option,
                    "description": description,
                    "content": content,
                    "aid": "1"
                }
                const response = await this.request({ auth: true }).post(`${this.getUnity()}/api`, paraData)
                return new ResponseWrapper(response, response.data)
            } catch (error) {
                const message = error.response.data ? error.response.data.error : error.response.statusText
                throw new ErrorWrapper(error, message)
            }
        }
        /*---------Delete Context--------- */
    static async DeleteContext(id) {
            try {
                console.log(id)
                const response = await this.request({ auth: true }).delete(`${this.getUnity()}/api?cid=${id}`)
                return new ResponseWrapper(response, response.data)
            } catch (error) {
                const message = error.response.data ? error.response.data.error : error.response.statusText
                throw new ErrorWrapper(error, message)
            }
        }
        /*---------Update Context--------- */
    static async UpdateContext(id, ct_name, dateFormat, option, description, content) {
            // const ContextById = await this.request({ auth: true }).get(`${this.getUnity()}/cpncontextbyid?cid=${id}`)
            // console.log(ContextById,ct_name,ct_description)
            try {
                const paraData = {
                    "cid": id,
                    "name": ct_name,
                    "createdDate" : dateFormat,
                    "context_type": option,
                    "description": description,
                    "content": content,
                    "aid": "1"
                }
                const response = await this.request({ auth: true }).put(`${this.getUnity()}/api`, paraData)
                console.log(response.data);
                return new ResponseWrapper(response, response.data)
            } catch (error) {
                const message = error.response.data ? error.response.data.error : error.response.statusText
                console.log(error)
                throw new ErrorWrapper(error, message)

            }
        }
        /*---------Get Context By ID--------- */
    static async GetContextById(id) {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/cpncontextbyid?cid=${id}`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
}