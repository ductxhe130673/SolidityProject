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
    static async CreateSmartContracts(id, sc_name, option, content, createdDate, description) {
            console.log('createdDate', createdDate);
            try {
                const paraData = {
                    "id": id,
                    "name": sc_name,
                    "createdDate": createdDate,
                    "type": option,
                    "content": content,
                    "description": description,
                    "aid": "1"
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
        console.log('smartContractById', smartContractById);
        try {
            return new ResponseWrapper(smartContractById)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    /*---------Update Smartcontract--------- */
    static async UpdateSmartContracts(id, sc_name, code, description, option) {
            console.log('description', description);
            // const smartContractById = await this.request({ auth: true }).get(`${this.getUnity()}/scbyid?id=${id}`)
            try {
                const paraData = {
                    "id": id,
                    "name": sc_name,
                    // "date_modified": smartContractById.data.date_modified,
                    "content": code,
                    "description": description,
                    "type": option,
                    "aid": 1

                }
                console.log('paraData', paraData)
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
                    "aid": 1
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
                    "aid": 1
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

    /*---------createNewInitialMarking--------- */

    static async createNewInitialMarking(numberUser, type) {
            try {
                const paraData = {
                    "num_user": numberUser,
                    "IM_type": type
                }
                const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewinitialmarking`, paraData)
                return new ResponseWrapper(response, response.data)
            } catch (error) {
                const message = error.response.data ? error.response.data.error : error.response.statusText
                throw new ErrorWrapper(error, message)
            }
        }
        /*---------createNewInitialMarking--------- */

    static async createNewBalance(balanceType, blfrom, blto, blvalue, blrange) {
        try {
            const paraData = {
                "balanceType": balanceType,
                "blfrom": blfrom,
                "blto": blto,
                "blvalue": blvalue,
                "blrange": blrange,
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewbalance`, paraData)

            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    static async addNewIMFunction(fun_name, sender_from, sender_to) {
        try {
            const paraData = {
                "fun_name ": fun_name,
                "sender_from ": sender_from,
                "sender_to ": sender_to,
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewimfunction`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
    static async addNewIMArgument(arg_name, IMfrom, IMto) {
        try {
            const paraData = {
                "arg_name ": arg_name,
                "IMfrom ": IMfrom,
                "IMto ": IMto,
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewimargument`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async addNewLNAFile(hcpnfile, propfile) {
        try {
            const paraData = {
                "hcpnfile ": hcpnfile,
                "propfile ": propfile,
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewlnafile`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async addNewCheckedBatchSC(aid, lteid, cid, noSC, status, LTLformula, result) {
        try {
            const paraData = {
                "aid": aid,
                "lteid": lteid,
                "cid": cid,
                "noSC": noSC,
                "status": status,
                "LTLformula": LTLformula,
                "result": result,
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewcheckedbatchsc`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }

    static async addNewCheckedSmartContractDetail(sid) {
        try {
            const paraData = {
                "sid": sid
            }
            const response = await this.request({ auth: true }).post(`${this.getUnity()}/addnewcheckedsmartcontractdetail`, paraData)
            return new ResponseWrapper(response, response.data)
        } catch (error) {
            const message = error.response.data ? error.response.data.error : error.response.statusText
            throw new ErrorWrapper(error, message)
        }
    }
}