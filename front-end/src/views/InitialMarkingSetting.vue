<template>
  <div id="initial-marking">
    <div id="initial-marking-header">Configuration</div>
    <div id="initial-marking-input">
      <div id="header-section">
        <div class="number-cell">Number of users</div>
        <div class="multi-cell">Balance</div>
        <div class="function-cell">Function parameters</div>
      </div>
      <div id="input-section">
        <div class="number-cell">
          <input
            type="text"
            placeholder="0"
            v-model="init_marking.NumberOfUser"
            id="number-user"
            class="input-text-form"
          />
        </div>
        <div class="multi-cell">
          <div id="multi-radio-chooses">
            <div class="radio-choose">
              <input
                type="radio"
                name="radio"
                class="radio-buttons"
                value="fixed"
                v-model="init_marking.Balance.type"
              />
              <span>Fixed</span>
            </div>
            <div class="radio-choose">
              <input
                type="radio"
                name="radio"
                class="radio-buttons"
                value="random"
                v-model="init_marking.Balance.type"
              />
              <span>Random</span>
            </div>
            <div class="radio-choose">
              <input
                type="radio"
                name="radio"
                class="radio-buttons"
                value="map"
                v-model="init_marking.Balance.type"
              />
              <span>Map</span>
            </div>
          </div>
          <div id="multi-input-forms">
            <input
              type="text"
              class="input-text-form"
              v-model="init_marking.Balance.fixed"
              id="fixed-input-form"
              placeholder="0"
              v-if="getSelectedRadio == 'fixed'"
            />
            <div id="random-input-form" v-if="getSelectedRadio == 'random'">
              <div id="input-from-range">
                <span>From:</span>
                <input
                  type="text"
                  placeholder="0"
                  v-model="init_marking.Balance.random.from"
                  class="input-text-form"
                />
              </div>
              <div id="input-to-range">
                <span>To:</span>
                <input
                  type="text"
                  placeholder="10"
                  v-model="init_marking.Balance.random.to"
                  class="input-text-form"
                />
              </div>
            </div>
            <input
              type="text"
              v-model="init_marking.Balance.map"
              class="input-text-form"
              id="map-input-form"
              placeholder="0,1,2"
              v-if="getSelectedRadio == 'map'"
            />
          </div>
        </div>
        <div class="function-cell">
          <div id="list-smart-contract">
            <ul class="nav nav-tabs">
              <li
                class="nav-item d-inline-block text-truncate"
                v-for="(item, index) in list_smart_contract"
                :key="item.sid"
              >
                <a
                  class="nav-link"
                  v-on:click="selectSC(item.sid, index)"
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
                      <th style="width: 10 %">#</th>
                      <th>
                        Functions
                        <span>
                    <a-icon id="icon" type="caret-up" />
                    <a-icon id="icon" type="caret-down" />
                  </span>
                      </th>
                      <th style="width: 25%">Arguments</th>
                    </tr>
                  </thead>
                  <tr
                    v-for="(func, index) in init_marking.Smart_contracts[selectedSCIndex].functions"
                    v-bind:key="index"
                    
                  >
                    <td>{{ index + 1 }}</td>
                    <td>{{ func.name }}</td>
                    <td>
                      <div
                        class="input-param-text"
                        @click="setFunctionParam(func.fid)"
                      >
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
                @setArgument="setArgument"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div id="processing-btn">
      <div class="pr-button" @click="routing('save')">Next</div>
      <div class="pr-button" @click="routing('back')">Back</div>
    </div>
  </div>
</template>

<script>
import { GetGloLocArgOfSmartContract } from "../services/data";
import FunctionTable from "./initmarking/FunctionTable.vue";
export default {
  components: {
    "function-table": FunctionTable,
  },
  data() {
    return {
      radio_seleted: "fixed",
      function_cell_selected: "function",
      list_smart_contract: [],
      smart_contract_infors: this.$store.state.data.data.selectedSCInfor,
      selected_sc: null, //sc selected
      selected_function: null, //function selected
      selectedSCIndex: 0,
      init_marking: {},
    };
  },
  beforeMount() {
    this.list_smart_contract = this.$store.state.data.data.selectedSc;
    this.getFuntionSC(this.list_smart_contract[0].sid);
    // this.initInitialMarkingHolder();

    if (this.list_smart_contract.length > 0) {
      this.selected_sc = this.list_smart_contract[0].sid;
    }
  },
  mounted() {
    this.setSCInfor();
    this.init_marking = this.$store.state.data.data.initialMarkingInfor;
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

    function_cell_selection() {
      return this.function_cell_selected;
    },
    getFunctionArgument() {
      return this.selected_function;
    },
  },
  methods: {
    setArgument(arg) {
      this.selected_function.argument = arg;
    },
    changeSelected(value) {
      this.function_cell_selected = value;
    },

    getFuntionSC(sid) {
      return GetGloLocArgOfSmartContract(sid);
      // console.log("fun.functions", fun);
    },
    selectSC(sid, index) {
      if (this.selected_sc != sid) {
        this.selected_sc = sid;
        this.selectedSCIndex = index;
      }
    },
    async setSCInfor() {
      for (let i = 0; i < this.list_smart_contract.length; i++) {
        this.init_marking.Smart_contracts[i] = await this.getFuntionSC(
          this.list_smart_contract[i].sid
        );
      }
    },
    // updateInitMarking(val) {
    //   this.function_cell_selected = "function";
    //   this.selected_function = null;
    //   this.init_marking.Funtion_params[this.selected_sc].functions[
    //     this.selected_function
    //   ] = val;
    // },
    routing(param) {
      if (param == "save") {
        if (
          !this.init_marking.NumberOfUser ||
          !this.init_marking.Balance.type
        ) {
          alert("You must to input all field!!!");
        } else if (
          this.init_marking.Balance.type === "fixed" &&
          !this.init_marking.Balance.fixed
        ) {
          alert("You must to input balance fixed!!!");
        } else if (
          (this.init_marking.Balance.type === "random" &&
            !this.init_marking.Balance.random.from) ||
          (this.init_marking.Balance.type === "random" &&
            !this.init_marking.Balance.random.to)
        ) {
          alert("You must to input balance random!!!");
        } else if (
          this.init_marking.Balance.type === "map" &&
          !this.init_marking.Balance.map
        ) {
          alert("You must to input balance map!!!");
        } else if (
          this.init_marking.Balance.type === "random" &&
          this.init_marking.Balance.random.from >=
            this.init_marking.Balance.random.to
        ) {
          alert("From must be smaller than To");
        } else {
          this.$store.commit("SetInitialMarking", this.init_marking);
          this.$router.push({ name: "CheckSmartContract" });
          this.$store.commit("setIndex", 5);
        }
      }
      if (param == "back") {
        this.$router.push({ name: "LTLCheckOption" });
        this.$store.commit("setIndex", 4);
      }
    },
    setFunctionParam(funct) {
      this.function_cell_selected = "params";
      this.selected_function = this.init_marking.Smart_contracts[
        this.selectedSCIndex
      ].functions.find((item) => {
        return item.fid === funct;
      });
    },
  },
};
</script>
<style scoped>

input {
  border: 1px solid gray;
}
#initial-marking {
  height: 100%;
  width: 100%;
  min-width: 900px;
  color: black;
}

#initial-marking-header {
  height: 60px;
  padding-top: 10px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}
#initial-marking-input {
  width: 60%;
  margin-left: 20%;
  display: flex;
  justify-content: space-between;
}

#header-section {
  flex-basis: 20%;
}

#input-section {
  flex-basis: 80%;
}

.number-cell {
  height: 40px;
  margin-top: 20px;
}

.multi-cell {
  height: 100px;
  margin-top: 20px;
}

.function-cell {
  margin-top: 20px;
}

#number-user {
  width: 100%;
}

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
  border: 1px;
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
  border: 1px black solid;
  padding: 3% 2% 3% 2%;
}

/* function */
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

#table-list {
  width: 100%;
  margin: auto;
  font-size: 0.9em;
  height: 240px;
  overflow-y: auto;
}

.input-param-text {
  color: rgb(42, 42, 214);
  cursor: pointer;
}
.input-param-text:hover {
  color: rgb(78, 78, 243);
}

/* Button */
#ssc-button {
  width: 60%;
  height: 80px;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.button-style {
  background-color: #ffffff;
  border: 0;
  border-radius: 0.5rem;
  box-sizing: border-box;
  color: #111827;
  font-family: "Inter var", ui-sans-serif, system-ui, -apple-system, system-ui,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif,
    "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 0.875rem;
  font-weight: 600;
  line-height: 1.25rem;
  padding: 0.75rem 1rem;
  text-align: center;
  text-decoration: none #d1d5db solid;
  text-decoration-thickness: auto;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1), 0 2px 3px 0 rgba(0, 0, 0, 0.06);
  cursor: pointer;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-style:hover {
  background-color: rgb(249, 250, 251);
}

.button-style:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.button-style:focus-visible {
  box-shadow: none;
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
