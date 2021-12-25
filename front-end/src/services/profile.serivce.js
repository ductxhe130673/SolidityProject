import { BaseService, ErrorWrapper, ResponseWrapper } from "./base";
export class ProfileService extends BaseService {
    /* Type Object API */
    static getUnity() {
            return 'auth'
        }
        /*---------Get All Of Row In Context Table---------- */
        /*
         * Using baseSerivce(axios) to send request to BackEnd
         * return a type ResponseWrapper having data of Backend
         */

    /*---------Get Contact By ID--------- */
    static async GetAccountById(id) {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/getcontactbyaid?id= ${id}`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    static async GetAvatarById(id) {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/getavatarbyaid?id= ${id}`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

}