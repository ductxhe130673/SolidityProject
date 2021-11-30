<template>
  <div>
    <div class="container">
      <div class="header">
        <div class="title">
          <h1>Select Variables Of Smart Contract</h1>
        </div>
      </div>
      <div class="smart-cell">
        <div id="list-smart">
          <ul class="nav nav-tabs">
            <li
              class="nav-item d-inline-block text-truncate"
              v-for="item in list_smart_contract"
              :key="item.id"
            >
              <a
                class="nav-link"
                v-on:click="selected_smart = item.id"
                v-bind:class="{ active: item.id == selected_smart }"
                >{{ item.name }}</a
              >
            </li>
          </ul>
        </div>
        <div id="Information-table">
          <div id="table-list">
            <div class="table-row" id="header-row">
              <div class="table-cell header-cell first-cell">
                #
                <span>
                  <a-icon id="icon" type="caret-up" />
                  <a-icon id="icon" type="caret-down" />
                </span>
              </div>
              <div class="table-cell header-cell second-cell">
                Global variables
                <span>
                  <a-icon id="icon" type="caret-up" />
                  <a-icon id="icon" type="caret-down" />
                </span>
              </div>
              <div class="table-cell header-cell third-cell">Selected</div>
            </div>
            <div
              class="table-row"
              v-for="(func, index) in getSelectedSmart"
              v-bind:key="func.fid"
              :class="{ even_row: index % 2 == 0 }"
            >
              <div class="table-cell first-cell">{{ index + 1 }}</div>
              <div class="table-cell second-cell">{{ func.name }}</div>
              <div class="table-cell third-cell">
                <input
                  type="radio"
                  id="one"
                  name="ch"
                  v-model="checkedNames"
                  :value="data"
                />
              </div>
            </div>
          </div>

          <div class="function">
            <div id="list-function">
              <ul class="nav nav-tabs">
                <li
                  class="nav-item d-inline-block text-truncate"
                  v-for="item in list_function"
                  :key="item.id"
                >
                  <a
                    class="nav-link"
                    v-on:click="selected_func = item.id"
                    v-bind:class="{ active: item.id == selected_func }"
                    >{{ item.name }}</a
                  >
                </li>
              </ul>
            </div>
            <div id="Func-table">
              <div id="table-list">
                <div class="table-row" id="header-row">
                  <div class="table-cell header-cell first-cell">
                    #
                    <span>
                      <a-icon id="icon" type="caret-up" />
                      <a-icon id="icon" type="caret-down" />
                    </span>
                  </div>
                  <div class="table-cell header-cell second-cell">
                    Local variables
                    <span>
                      <a-icon id="icon" type="caret-up" />
                      <a-icon id="icon" type="caret-down" />
                    </span>
                  </div>
                  <div class="table-cell header-cell third-cell">Selected</div>
                </div>
                <div
                  class="table-row"
                  v-for="(func, index) in getSelectedFunc"
                  v-bind:key="func.fid"
                  :class="{ even_row: index % 2 == 0 }"
                >
                  <div class="table-cell first-cell">{{ index + 1 }}</div>
                  <div class="table-cell second-cell">{{ func.name }}</div>
                  <div class="table-cell third-cell">
                    <input
                      type="radio"
                      id="one"
                      name="ch"
                      v-model="checkedNames"
                      :value="data"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="processing-btn">
        <div class="pr-button" @click="routing('next')">Next</div>
        <div class="pr-button" @click="routing('back')">Back</div>
      </div>
    </div>
  </div>
</template>
<script>
import { GetGloLocArgOfSmartContract } from "../../../services/data";
export default {
  data() {
    return {
      // function_cell_selected: "function"
      list_smart_contract: [],
      list_function: [],
      smart_infor: [],
      function_infor: {
        1: {
          name: "Function 1",
          functions: [
            {
              fid: 1,
              name: "LV1",
            },
            {
              fid: 2,
              name: "LV2",
            },
            {
              fid: 3,
              name: "LV3",
            },
            {
              fid: 4,
              name: "LV4",
            },
          ],
        },
      },
      selected_func: 1,
      selected_smart: 1,
    };
  },
  mounted() {
    this.setSCInfor();
    this.list_smart_contract = this.$store.state.data.data.selectedSc;
  },
  methods: {
    routing(param) {
      if (param == "next") {
        this.$router.push({ name: "Initial" });
      }
      if (param == "back") {
        this.$router.push({ name: "GenaralVulSetting" });
      }
    },
    getData(sid) {
      return GetGloLocArgOfSmartContract(sid);
    },
    async setSCInfor() {
      for (let i = 0; i < this.list_smart_contract.length; i++) {
        this.smart_infor[i] = await this.getData(this.list_smart_contract[i].sid);
      }
      console.log("this.smart_infor", this.smart_infor);
    },
  },
  computed: {
    getSelectedFunc() {
      if (this.selected_func in this.function_infor) {
        return this.function_infor[this.selected_func].functions;
      } else {
        return [];
      }
    },
    getSelectedSmart() {
      if (this.selected_smart in this.smart_infor) {
        return this.smart_infor[this.selected_smart].SmartContract;
      } else {
        return [];
      }
    },
  },
};
</script>

<style scoped>
.title {
  text-align: center;
  margin-top: 5%;
}
.title h1 {
  font-size: 35px;
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif;
}
table span {
  float: right;
  display: block;
}
#icon {
  display: block;
  height: 8px;
}
.nav-item .active {
  color: white;
  background-color: #383838;
  border: grey;
}
.nav-link {
  color: #383838;
  border: grey solid;
  border-bottom: none;
}
.nav-item {
  width: 20%;
  margin-right: 3px;
  cursor: pointer;
}

#Information-table {
  border: 1px black solid;
  padding: 3% 2% 3% 2%;
}
#Func-table {
  border: 1px black solid;
  padding: 5% 4% 5% 4%;
}
.smart-cell {
  margin-top: 50px;
}
.function {
  margin-top: 50px;
}
#table-list {
  width: 100%;
  margin: auto;
  font-size: 0.9em;
  height: 300px;
  overflow-y: auto;
  border-radius: 4px;
  border: 1px solid black;
  background: rgb(241, 240, 240);
}

.table-row {
  display: flex;
  height: 50px;
  border: 1px solid #ddd;
}
#header-row {
  background-color: rgb(196, 194, 194);
  font-weight: bold;
}

#table-list span {
  float: right;
  margin: 0 20% 0 0;
  padding: 0;
  font-size: 100%;
}
.even_row {
  background-color: rgb(226, 224, 224);
}
.table-cell {
  padding-top: 10px;
  font-size: 15px;
}
.first-cell {
  flex-basis: 10%;
  padding-left: 5px;
}
.second-cell {
  flex-basis: 60%;
}
.third-cell {
  flex-basis: 30%;
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
