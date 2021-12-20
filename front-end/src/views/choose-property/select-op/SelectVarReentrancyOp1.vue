<template>
  <div class="container">
    <div class="row">
      <h1 class="text-center">Select variables of the selected function</h1>
    </div>
    <div class="row">
      <div class="table-list">
        <table class="table">
          <thead>
            <tr>
              <th style="width: 10%">#</th>
              <th >
                Global variable
                <span
                  ><a-icon id="icon" type="caret-up" />
                  <a-icon id="icon" type="caret-down" />
                </span>
              </th>
              <th style="width: 15%">Selected</th>
            </tr>
          </thead>
          <tr
            v-for="(func, index) in smart_infor[selectedSCIndex].globalVar"
            v-bind:key="func.fid"
          >
            <td>{{ index + 1 }}</td>
            <td>{{ func.name }}</td>
            <td>
              <input
                type="radio"
                id="one"
                name="globalVar"
                :value="func.name"
              />
            </td>
          </tr>
        </table>
      </div>
    </div>
    <div class="row">
      <div class="function-cell">
        <div id="list-function">
          <ul class="nav nav-tabs">
            <li
              class="nav-item d-inline-block text-truncate"
              v-for="(item, index) in smart_infor[selectedSCIndex].functions"
              :key="item.id"
            >
              <a
                class="nav-link"
                v-on:click="selectFunction(item.fid, index)"
                v-bind:class="{ active: item.fid == selected_func }"
                >{{ item.name }}</a
              >
            </li>
          </ul>
        </div>
        <div id="func-information-table">
          <div id="table-list">
            <table class="table">
              <thead>
                <tr>
                  <th style="width: 10%">#</th>

                  <th>
                    Local variable<span
                      ><a-icon id="icon" type="caret-up" /><a-icon
                        id="icon"
                        type="caret-down"
                    /></span>
                  </th>
                  <th style="width: 15%">Select</th>
                </tr>
              </thead>

              <tr
                v-for="(func, index) in smart_infor[selectedSCIndex].globalVar"
                v-bind:key="func.fid"
              >
                <td>{{ index + 1 }}</td>
                <td>{{ func.name }}</td>
                <td>
                  <input type="radio" id="two" name="ch" :value="func.name" />
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div id="processing-btn">
      <div class="pr-button" @click="routing('next')">Next</div>
      <div class="pr-button" @click="routing('back')">Back</div>
    </div>
  </div>
</template>
<script>
import { GetGloLocArgOfSmartContract } from "../../../services/data";
export default {
  data() {
    return {
      list_smart_contract: [],
      list_function: [],
      functionBySC: [],
      smart_infor: [],
      checkedGlobalVar: "",
      checkedLocalVar: "",
      selectedSCIndex: 0,
      selectedFunctionIndex: 0,
      function_infor: {},
      selected_func: 1,
      selected_smart: 1,
    };
  },

  beforeMount() {
    this.list_smart_contract = this.$store.state.data.data.selectedSc;
    this.setSCInfor();
  },
  computed: {
    getSelectedFunc() {
      return this.function_infor;
    },
    getSelectedSmart() {
      if (this.selected_smart in this.smart_infor) {
        return this.smart_infor[this.selected_smart].SmartContract;
      } else {
        return [];
      }
    },
  },
  methods: {
    selectFunction(fid, index) {
      if (this.selected_func != fid) {
        this.selected_func = fid;
        this.selectedFunctionIndex = index;
        // this.function_infor = this.functionBySC[index].localVar;
      }
    },
    selectSC(sid, index) {
      if (this.selected_smart != sid) {
        this.selected_smart = sid;
        this.selectedSCIndex = index;
        this.functionBySC = this.list_function[index];
      }
    },
    async setSCInfor() {
      for (let i = 0; i < this.list_smart_contract.length; i++) {
        this.smart_infor.push(
          await GetGloLocArgOfSmartContract(this.list_smart_contract[i].sid)
        );
        this.list_function = this.smart_infor.map((item) => item.functions);
      }
    },
    routing(param) {
      if (param == "next") {
        this.$router.push({ name: "Initial" });
      }
      if (param == "back") {
        this.$router.push({ name: "GenaralVulSetting" });
      }
    },
  },
};
</script>
<style scoped>
h1 {
  font-size: 35px;
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif;
}
input {
  margin: 7px;
}
.row {
  margin-top: 5%;
  padding-right: 10px;
}
table {
  width: 100%;
}
table td,
table th {
  padding: 6px;
}
table tr {
  border-bottom: 1px solid #dee2e6;
}
table tr:nth-child(even) {
  background-color: #f2f2f2;
}
table tr:hover {
  background-color: #ddd;
}
table th {
  background-color: #d9edf7;
  color: #3a7694;
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
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
  min-width: 10%;
  margin-right: 3px;
  cursor: pointer;
}

#func-information-table {
  border: black solid 1px;
  padding: 3% 2% 3% 2%;
}

#table-list {
  width: 100%;
  margin: auto;
  height: 300px;
  overflow-y: auto;

}


/* button */
#processing-btn {
  width: 45%;
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