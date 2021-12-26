<template>
  <div class="container-fluid">
    <div class="row"><h1 class="text-center">Configuration</h1></div>
    <div class="row">
      <div class="col-md-3">Type</div>
      <div class="col-md-7">
        <div id="multi-radio-chooses">
          <div class="radio-choose">
            <input
              type="radio"
              name="radio"
              class="radio-buttons"
              value="fixed"
              v-model="init_marking.balance.type"
            />
            <span>Fixed</span>
          </div>
          <div class="radio-choose">
            <input
              type="radio"
              name="radio"
              class="radio-buttons"
              value="random"
              v-model="init_marking.balance.type"
            />
            <span>Random</span>
          </div>
          <div class="radio-choose">
            <input
              type="radio"
              name="radio"
              class="radio-buttons"
              value="map"
              v-model="init_marking.balance.type"
            />
            <span>Map</span>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">User parameters</div>
      <div class="col-md-7">
        <div id="table-list">
          <table class="table">
            <thead>
              <tr>
                <th style="width: 15%">#</th>
                <th>Users</th>
                <th style="width: 25%">Balance</th>
              </tr>
            </thead>
            <tr v-for="(func, index) in dataUserTable" v-bind:key="func.fid">
              <td>{{ index + 1 }}</td>
              <td>{{ func.name }}</td>
              <td>{{ func.balance }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">Function parameters</div>
      <div class="col-md-7">
        <div id="list-smart-contract">
          <ul class="nav nav-tabs">
            <li
              class="nav-item d-inline-block text-truncate"
              v-for="item in list_smart_contract"
              :key="item.id"
            >
              <a
                class="nav-link"
                v-on:click="selectSC(item.sid)"
                v-bind:class="{ active: item.sid == selected_sc }"
                >{{ item.name }}</a
              >
            </li>
          </ul>
        </div>
        <div id="sm-information-table">
          <div v-if="function_cell_selection == 'function'">
            <div id="table-list">
              <table class="table">
                <thead>
                  <tr>
                    <th style="width: 10%">#</th>
                    <th>Functions</th>
                    <th style="width: 25%">Arguments</th>
                  </tr>
                </thead>
                <tr v-for="(func, index) in func" v-bind:key="index">
                  <td>{{ index + 1 }}</td>
                  <td>{{ func.name }}</td>
                  <td>
                    <div class="input-param-text" @click="setFunctionParam(func.fid)">
                      Input Params
                    </div>
                  </td>
                </tr>
              </table>
            </div>
          </div>
          <div v-if="function_cell_selection == 'params'">
            <function-table
              :list_argument="getFunctionArgument"
              @changeSelected="changeSelected"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="buttonGroup">
      <button type="button" class="btn btn-outline-primary" @click="routing('back')">
        Back
      </button>
    </div>
  </div>
</template>

<script>
import FunctionTableResult from "./initmarking/FunctionTableResult.vue";
export default {
  components: {
    "function-table": FunctionTableResult,
  },
  data() {
    return {
      userParam: [],
      radio_seleted: "fixed",
      function_cell_selected: "function",
      list_smart_contract: [],
      smart_contract_infors: {},
      selected_sc: null,
      selected_function: null,
      functionSC: [],
      func: {},
      init_marking: {},
      dataUserTable: [],
    };
  },
  beforeMount() {
    this.list_smart_contract = this.$store.state.data.data.selectedSc;
    this.init_marking = this.$store.state.data.data.initialMarkingInfor;
    this.getFuntionSC();

    this.setUserParam();
    if (this.list_smart_contract.length > 0) {
      this.selected_sc = this.list_smart_contract[0].sid;
    }
  },
  watch: {
    init_marking: {
      handler(val) {
        this.$store.commit("SetInitialMarking", val);
      },
      deep: true,
    },
  },
  computed: {
    getSelectedRadio() {
      return this.init_marking.Balance.type;
    },
    getSelectedScFunc() {
      if (this.selected_sc in this.smart_contract_infors) {
        return this.smart_contract_infors[this.selected_sc];
      } else {
        return [];
      }
    },
    function_cell_selection() {
      return this.function_cell_selected;
    },
    getFunctionArgument() {
      return this.selected_function;
    },
  },
  methods: {
    getDataTable() {
      if (this.init_marking.balance.type === "fixed")
        return this.init_marking.balance.fixed;
      else if (this.init_marking.balance.type === "random")
        return (
          Math.floor(
            Math.random() *
              (parseInt(this.init_marking.balance.random.to) -
                parseInt(this.init_marking.balance.random.from) +
                1)
          ) + parseInt(this.init_marking.balance.random.from)
        );
    },
    setUserParam() {
      for (let i = 1; i <= this.init_marking.NumberOfUser; i++) {
        if (!this.init_marking.balance.map) {
          this.dataUserTable.push({
            name: "User" + i,
            balance: this.getDataTable(),
          });
        } else {
          this.dataUserTable.push({
            name: "User" + i,
            balance: this.init_marking.balance.map.split(",")[i - 1],
          });
        }
      }
    },
    changeSelected(value) {
      this.function_cell_selected = value;
    },
    getFuntionSC() {
      this.func = this.init_marking.smart_contract[0].functions;
    },
    selectSC(sid) {
      if (this.selected_sc != sid) {
        this.selected_sc = sid;
      }
    },

    routing(param) {
      if (param == "save") {
        this.$store.commit("SetInitialMarking", this.init_marking);
        this.$router.push({ name: "CheckSmartContract" });
        this.$store.commit("setIndex", 5);
      }
      if (param == "back") {
        this.$router.push({ name: "CheckSmartContract" });
        this.$store.commit("setIndex", 4);
      }
    },
    setFunctionParam(funct) {
      this.function_cell_selected = "params";
      for (let i = 0; i < this.func.length; i++) {
        if (this.func[i].fid === funct) this.selected_function = this.func[i];
      }
    },
  },
};
</script>
<style scoped>
.container-fluid {
  color: black;
}
h1 {
  font-weight: bold;
}
.row {
  margin-top: 2%;
  padding-right: 10px;
  margin-bottom: 3%;
}
.col-md-3 {
  padding-left: 13%;
  font-size: 18px;
}
/* function */
table {
  width: 100%;
}
table td,
table th {
  padding: 6px;
}
table td {
  padding: 10px;
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

#table-list {
  width: 100%;
  margin: auto;
  font-size: 0.9em;
  height: 240px;
  overflow-y: auto;
}
.input-param-text {
  padding: 2px;
}
.input-param-text:hover {
  color: red;
  text-decoration: underline red wavy;
}

/* radio button */
#multi-radio-chooses {
  display: flex;
}

.radio-choose {
  flex-basis: 20%;
  height: 20px;
  margin-bottom: 20px;
}

.radio-choose span {
  font-size: 14px;
}

.radio-choose input {
  height: 11px;
}

#fixed-input-form {
  width: 60%;
}

#map-input-form {
  width: 60%;
}

#random-input-form {
  width: 60%;
  display: flex;
  justify-content: space-between;
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

#sm-information-table {
  border: black solid 1px;
  padding: 3% 2% 3% 2%;
}

/* button */
.buttonGroup {
  padding-top: 2%;
  display: flex;
  width: 60%;
  justify-content: space-around;
  margin: 0 auto;
  padding-bottom: 2%;
}
</style>
