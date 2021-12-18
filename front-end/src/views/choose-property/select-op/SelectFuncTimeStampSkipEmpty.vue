<template>
  <div class="container">
    <div class="row">
      <h1 class="text-center">Select functions of the smart contracts</h1>
    </div>
    <div class="row">
      <div id="list-smart-contract">
        <ul class="nav nav-tabs">
          <li
            class="nav-item d-inline-block text-truncate"
            v-for="(item, index) in list_smart_contract"
            :key="item.id"
          >
            <a
              class="nav-link"
              v-on:click="selectSC(item.sid, index)"
              v-bind:class="{ active: item.sid == selected_smart }"
              >{{ item.name }}</a
            >
          </li>
        </ul>
      </div>
      <div id="sm-information-table">
        <table class="table table-sm">
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
            <th>Select</th>
          </tr>
          <tr
            v-for="(func, index) in smart_infor[selectedSCIndex].functions"
            v-bind:key="func.fid"
          >
            <td>{{ index + 1 }}</td>
            <td>{{ func.name }}</td>
            <td>
              <input class="form-check-input" type="radio" value="func.name" />
            </td>
          </tr>
        </table>
      </div>
    </div>
    <div id="action">
      <div
        type="button"
        class="btn btn-outline-primary"
        @click="routing('next')"
      >
        Next
      </div>
      <div type="button" class="btn btn-outline-primary" @click="routing('back')">
        Back
      </div>
    </div>
  </div>
</template>
<script>
import { GetGloLocArgOfSmartContract } from "../../../services/data";
export default {
  data() {
    return {
      list_smart_contract: [],
      smart_infor: [],
      selectedSCIndex: 0,
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
    selectSC(sid, index) {
      if (this.selected_smart != sid) {
        this.selected_smart = sid;
        this.selectedSCIndex = index;
      }
    },
    async setSCInfor() {
      for (let i = 0; i < this.list_smart_contract.length; i++) {
        this.smart_infor.push(
          await GetGloLocArgOfSmartContract(this.list_smart_contract[i].sid)
        );
      }
    },
    routing(param) {
      if (param == "next") {
        this.$router.push({ name: "SelectVarReentrancyOp1" });
      }
      if (param == "back") {
        this.$router.push({ name: "GenaralVulSetting" });
      }
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
