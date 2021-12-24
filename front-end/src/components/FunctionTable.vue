<template>
  <div class="container">
    <div class="header">
      <div class="title">
        <h1>Select a function of the smart contract</h1>
      </div>
    </div>
    <div class="function_cell">
      <div id="list-function">
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
      <div id="func-information-table">
        <div id="table-list">
          <table class="table">
            <thead>
              <th style="width: 10%">#</th>
              <th>Function</th>
              <th style="width: 15%">Selected</th>
            </thead>
            <tr
              v-for="(func, index) in smart_infor[selectedSCIndex].functions"
              v-bind:key="func.fid"
            >
              <td>{{ index + 1 }}</td>
              <td>{{ func.name }}</td>
              <td>
                <input
                  type="radio"
                  id="one"
                  name="ch"
                  :value="func.name"
                  v-model="selected_variable"
                />
              </td>
            </tr>
          </table>
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
import { GetGloLocArgOfSmartContract } from "../services/data";
export default {
  data() {
    return {
      list_smart_contract: [],
      smart_infor: [],
      selectedSCIndex: 0,
      selected_smart: 0,
      selected_variable: "",
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
        this.$store.commit("setVarSelected", this.selected_variable);
        document.getElementById("selection-table").style.display = "none";
      }
      if (param == "back") {
        document.getElementById("selection-table").style.display = "none";
      }
    },
  },
};
</script>
<style scoped>
.title {
  padding-top: 8%;
  margin-bottom: 5%;
  text-align: center;
}
.title h1 {
  font-size: 35px;
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif;
}
/* tab link */
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
  padding: 4% 3% 4% 3%;
}

/* table */
#table-list {
  overflow-y: auto;
  height: 300px;
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
