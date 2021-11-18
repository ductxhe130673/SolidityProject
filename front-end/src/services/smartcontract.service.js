import { BaseService, ErrorWrapper, ResponseWrapper } from "./base";
export class SmartContractsService extends BaseService {
    static getUnity() {
        return '/smartconstract'
    }

    static async GetCommonSmartContracts() {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/api?type=common`)
            console.log(response)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async GetPrivateSmartContracts() {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/api?type=private`)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    static async GetPendingSmartContracts() {
        try {
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/api?type=pending`)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    /*---------Create New Smartcontract--------- */
    static async CreateSmartContracts(id, sc_name, option, content, createdDate) {
        console.log('createdDate',createdDate);
        try {
            const paraData = {
                "id": id,
                "name": sc_name,
                "createdDate": createdDate,
                "type": option,
                "content": content,
                "aid":"1"
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/select-smart-contract`, paraData)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    /*---------get smart contract by Id--------- */
    static async GetSmartContractById(id) {
        const smartContractById = await this.request({ auth: true }).get(`${this.getUnity()}/scbyid?id=${id}`)
        console.log('smartContractById',smartContractById);
        try {
            return new ResponseWrapper(smartContractById)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    /*---------Update Smartcontract--------- */
    static async UpdateSmartContracts(id, sc_name, code, description, option) {
        console.log('description',description);
        // const smartContractById = await this.request({ auth: true }).get(`${this.getUnity()}/scbyid?id=${id}`)
        try {
            const paraData = {
                "id": id,
                "name": sc_name,
                // "date_modified": smartContractById.data.date_modified,
                "content": code,
                "description": description,
                "type": option,
                "aid":1
                
            }
            console.log('paraData',paraData)
            const response = await this.request({ auth: true }).put(`${this.getUnity()}/select-smart-contract`, paraData)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
      /*---------Acccept Pendind Smartcontract--------- */
      static async AcceptPendingSmartContracts(id, sc_name, code) {
        try {
            const paraData = {
                "id": id,
                "name": sc_name,
                //"date_modified": smartContractById.data.date_modified,
                "content": code,
                "type": "common",
                "aid":1
            }
            console.log(paraData)
            const response = await this.request({ auth: true }).put(`${this.getUnity()}/select-smart-contract`, paraData)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    /*---------Refuse Pendind Smartcontract--------- */
        static async RefusePendingSmartContracts(id, sc_name, code) {
        try {
            const paraData = {
                "id": id,
                "name": sc_name,
                //"date_modified": smartContractById.data.date_modified,
                "content": code,
                "type": "private",
                "aid":1
            }
            console.log(paraData)
            const response = await this.request({ auth: true }).put(`${this.getUnity()}/select-smart-contract`, paraData)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    /*---------Delete Smartcontract--------- */
    static async DeleteSmartContracts(id) {
        try {
            const response = await this.request({ auth: true }).delete(`${this.getUnity()}/select-smart-contract?id=${id}`)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    /*---------Get GlobalVariable,Argument,Localvariable--------- */
    static async getArguLocalGlobalVar(id) {
        try {
            
            const response = await this.request({ auth: true }).get(`${this.getUnity()}/getvariablefunctionargu?id=${id}`)
            // const data = {
            //     content: response.data.data,
            //     headers: response.headers['']
            // }
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

}