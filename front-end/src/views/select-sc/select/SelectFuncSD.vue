<template>
  <div class="container">
    <div class="row">
      <h1 class="text-center">Select functions of the smart contracts</h1>
    </div>
    <div class="row">
      <div class="function-cell">
        <div id="list-smart-contract">
          <ul class="nav nav-tabs">
            <li
              class="nav-item d-inline-block text-truncate"
              v-for="item in list_smart_contract"
              :key="item.id"
            >
              <a
                class="nav-link"
                v-on:click="selected_sc = item.id"
                v-bind:class="{ active: item.id == selected_sc }"
                >{{ item.name }}</a
              >
            </li>
          </ul>
        </div>
        <div id="sm-information-table">
          <div v-if="function_cell_selection == 'function'">
            <table class="table table-sm">
              <thead>
                <tr>
                  <th>
                    #
                    <span
                      ><a-icon id="icon" type="caret-up" />
                      <a-icon id="icon" type="caret-down" />
                    </span>
                  </th>

                  <th>
                    Functions<span
                      ><a-icon id="icon" type="caret-up" /><a-icon
                        id="icon"
                        type="caret-down"
                    /></span>
                  </th>
                  <th>
                    Select<span
                      ><a-icon id="icon" type="caret-up" /><a-icon
                        id="icon"
                        type="caret-down"
                    /></span>
                  </th>
                </tr>
              </thead>
              <tr v-for="(func, index) in getSelectedSc" v-bind:key="func.fid">
                <td>{{ index + 1 }}</td>
                <td>{{ func.name }}</td>
                <td>
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                  />
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div id="action">
      <div type="button" class="btn btn-outline-primary" @click="funtionNext()">
        Next
      </div>
      <div type="button" class="btn btn-outline-primary" @click="funtionNext()"  v-if="list_smart_contract.length == 1">
        Select another smart contract
      </div>
      <div
        type="button"
        class="btn btn-outline-primary"
        @click="routing('back')"
      >
        Back
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      function_cell_selected: "function",
      list_smart_contract: [
        { name: "Smart I", id: 1 },
        { name: "Smart II", id: 2 },
        { name: "Smart III", id: 3 },
        { name: "Smart IV", id: 4 },
      ],
      smart_contract_infors: {
        1: {
          name: "smart I",
          functions: [
            {
              fid: 3,
              name: "bidding",
              argument: [
                {
                  id: 1,
                  name: "biddingTime",
                  vartype: "state",
                  type: "uint",
                  value: 1,
                  fid: 3,
                },
                {
                  id: 2,
                  name: "revealTime",
                  vartype: "local",
                  type: "uint",
                  value: 3,
                  fid: 3,
                },
              ],
              localVar: [],
            },
            {
              fid: 4,
              name: "reveal",
              argument: [
                {
                  id: 4,
                  name: "blindedBid",
                  vartype: "local",
                  type: "bytes32",
                  value: 7,
                  fid: 4,
                },
              ],
              localVar: [],
            },
            {
              fid: 5,
              name: "claimReward",
              argument: [],
              localVar: [
                {
                  id: 2,
                  name: "length",
                  vartype: "public",
                  type: "unit",
                  value: "bids[msg.sender].length",
                },
                {
                  id: 3,
                  name: "refund",
                  vartype: "public",
                  type: "unit",
                  value: "+= bid.deposit",
                },
                {
                  id: 4,
                  name: "bid",
                  vartype: "public",
                  type: "var",
                  value: "bids[msg.sender][i]",
                },
                {
                  id: 5,
                  name: "(value,fake,secret)",
                  vartype: "public",
                  type: "var",
                  value: "(_values[i], _fake[i], _secret[i])",
                },
              ],
            },
            {
              fid: 6,
              name: "playAround",
              argument: [
                {
                  id: 8,
                  name: "bidder",
                  vartype: "local",
                  type: "address",
                  value: 4,
                  fid: 6,
                },
                {
                  id: 9,
                  name: "value",
                  vartype: "state",
                  type: "uint",
                  value: 6,
                  fid: 6,
                },
              ],
              localVar: [],
            },
          ],
          globalVar: [
            {
              id: 1,
              name: "beneficiary",
              vartype: "address",
              type: "public",
              value: "",
            },
            {
              id: 2,
              name: "auctionStart",
              vartype: "uint",
              type: "public",
              value: "",
            },
            {
              id: 3,
              name: "biddingEnd",
              vartype: "uint",
              type: "public",
              value: "",
            },
            {
              id: 4,
              name: "revealEnd",
              vartype: "uint",
              type: "public",
              value: "",
            },
            {
              id: 5,
              name: "ended",
              vartype: "bool",
              type: "public",
              value: "",
            },
            {
              id: 6,
              name: "highestBidder",
              vartype: "address",
              type: "public",
              value: "",
            },
            {
              id: 7,
              name: "highestBid",
              vartype: "uint",
              type: "public",
              value: "",
            },
          ],
        },
      },
      selected_sc: 1,
      selected_function: null,
     
    };
  },
  methods: {
    setFunctionParam(func) {
      this.function_cell_selected = "params";
      this.selected_function = func;
    },
    
  },
  
  computed: {
    getSelectedSc() {
      if (this.selected_sc in this.smart_contract_infors) {
        return this.smart_contract_infors[this.selected_sc].functions;
      } else {
        return [];
      }
    },
    function_cell_selection() {
      return this.function_cell_selected;
    },
  },
};
</script>

<style scoped>
input {
  margin: 7px;
}
.row {
  margin-top: 2%;
  padding-right: 10px;
}
/* button */
#action {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 70%;
}
/* table  */
table {
  width: 100%;
  border-collapse: collapse;
}
table td,
table th {
  border: 1px solid #ddd;
  padding: 6px;
}
table tr:nth-child(even) {
  background-color: #f2f2f2;
}

table tr:hover {
  background-color: #ddd;
}

table th {
  background-color: #d9edf7;
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  color: black;
  text-indent: inherit;
}

table span {
  float: right;
  display: block;
}
#icon {
  display: block;
  height: 8px;
}

button {
  margin-right: 5px;
  margin-top: 5px;
}
/* function */
.function-cell {
  margin-top: 20px;
}
.nav-item .active {
  color: black;
  background-color: #d9edf7;
}
.nav-link {
  color: black;
  border: black solid 1px;
  border-bottom: none;
}
.nav-item {
  width: 10%;
  margin-right: 3px;
  cursor: pointer;
}

#sm-information-table {
  border: black solid 1px;
  padding: 3% 2% 3% 2%;
}

/* button */
#processing-btn {
  width: 60%;
  height: 120px;
  margin-left: 25%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#processing-btn .pr-button {
  cursor: pointer;
  width: 20%;
  height: 30px;
  border: 1px solid #2196f3;
  text-align: center;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  padding-top: 4px;
  border-radius: 4px;
}
#processing-btn .pr-button:hover {
  background-color: #1079cf;
  color: white;
}
.btn {
  margin: 0 3%;
}
</style>