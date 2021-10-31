import Axios from "axios";
import { CheckedService } from "../../../services/listchecked.service";
export default {
    async getListTran({ commit }) {
        try {
            var result = await CheckedService.GetCommonSmartContracts();
            commit('SET_LIST_POSTS',result.data)
            if(result.data.status === 200) {
                commit('SET_LIST_POSTS',result.data)
            }
        } catch(error) {
            console.log("error", error);
        }
    },

    setid({commit},data) {
        console.log("action setid")
        commit('SET_ID',data)
    }, 

    async setlistcheck({ commit},data) {
        try {
            var result = await Axios.get('http://127.0.0.1:8000/select-sc/checkreentrancydetail/?id='+data);
            commit('SET_LIST_CHECK',result.data)
            if(result.data.status === 200) {
                commit('SET_LIST_CHECK',result.data)
            }
        } catch(error) {
            console.log("error", error);
        }
    },

    async setListSmartContract({commit}) {
        try {
            console.log("setListSmartContract");
            var result = await Axios.get('http://127.0.0.1:8000/smartconstract/select-smart-contract/');
            console.log('result',result);
            commit('SET_LIST_SMART_CONTRACT',result.data)
            if(result.data.status === 200) {
                commit('SET_LIST_SMART_CONTRACT',result.data)
            }
            console.log("setListSmartContract");
        } catch(error) {
            console.log("error", error);
        }
    },

    // async setListLTLTemplate({commit}) {
    //     try {
    //         console.log("setListLTLTemplate");
    //         var result = await Axios.get('http://127.0.0.1:8000/ltltemplate/api/');
    //         console.log('result',result);
    //         commit('SET_LIST_LTL_TEMPLATE',result.data)
    //         if(result.data.status === 200) {
    //             commit('SET_LIST_LTL_TEMPLATE',result.data)
    //         }
    //         console.log("setListLTLTemplate");
    //     } catch(error) {
    //         console.log("error", error);
    //     }
    // }
}