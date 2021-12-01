import { BaseService, ErrorWrapper, ResponseWrapper } from "./base";
export class ltltemplateService extends BaseService {
    /* Type Object API */
    static getUnity() {
        return 'ltltemplate'
    }
    static async GetAllltltemplates() {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/api`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    static async GetLtltemplteById(id) {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/ltltemplatebyid?lteid=${id}`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }

    }

    /*---------Create New LTLTemplate--------- */
    static async CreateLTLTemplate(name, formula, description, date) {
        console.log('name, formula, description,date', name, formula, description, date);
        try {
            const paraData = {
                "name": name,
                "formula": formula,
                "description": description,
                "template_type": "test",
                "createdDate": date, // hard code, chua fix trong database,chuyen thanh ham getdate ben js
                //"createdDate": createdDate,
                "aid": "1"
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/api`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    /*---------Update LTLTemplate--------- */
    static async UpdateLtlTemplate(id, name, description, fomular, date) {
        try {
            const paraData = {
                "lteid": id,
                "name": name,
                "formula": fomular, // fix cung
                "description": description,
                "createdDate": date, // fix cung
                "template_type": "test", // fix cung
                "aid": "1" // fix cung
            }

            const response = await this.request({ auth: true }).put(`${this.getUnity()}/api`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            console.log(error)
            throw new ErrorWrapper(error, message)

        }
    }

    /*---------Delete LTLTemplate--------- */
    static async DeleteLtlTemplate(id) {
        console.log('id', id);
        try {
            const response = await this.request({ auth: true }).delete(`${this.getUnity()}/api?lteid=${id}`)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
}