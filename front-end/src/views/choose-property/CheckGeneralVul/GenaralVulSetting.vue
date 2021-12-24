<template>
  <div class="container">
    <div id="header">General Vulnerability Setting</div>
    <div class="row">
      <div class="col-2">Vulnerability</div>
      <div class="col-9">
        <select
          name="lteid"
          class="form-select"
          @change="changeid($event.target.value)"
          v-model="select"
        >
          <option v-for="item in listTemplates" :key="item" :value="item.name">
            {{ item.name }}
          </option>
        </select>
      </div>
    </div>
    <div class="row">
      <div class="col-2">Description</div>
      <div class="col-10">
        <textarea
          name=""
          id=""
          cols="30"
          rows="5"
          class="form-control"
          v-model="ltlConfig.params.description"
        >
        </textarea>
      </div>
    </div>
    <div id="btn-group">
      <button class="btn btn-primary-outline btn-sm" @click="routing('add')">Next</button>
      <button
        class="btn btn-primary-outline btn-sm"
        type="button"
        @click="routing('back')"
      >
        Back
      </button>
    </div>
  </div>
</template>

<script>
import { GetAllltltemplates } from "../../../services/data";
import { analyseLTLCode } from "../../../mixins/text-parser.js";
export default {
  data: function () {
    return {
      selectVariable: false,
      select_variable_value: "",
      select_variable_id: "",
      select_variable_type: "",
      selected_template: "",
      ltlcode: "abc",
      listTemplates: [],
      select: "interger_overflow_underflow",

      ltlConfig: {
        type: "general",
        params: {
          id: "iou",
          name: "under_over_flow",
          inputs: {
            min_threshold: "",
            max_threshold: "",
            selected_variable: "",
          },
          description: "",
        },
      },
    };
  },
  mounted() {
    this.initData();
    this.updateContent(1, this.ltlcode);
  },
  watch: {
    selected_template: function (val) {
      if (val == "interger_overflow_underflow") {
        this.updateContent(1, this.ltlcode);
      } else {
        this.updateContent(1, "");
      }
    },
    ltlcode: function (newVal) {
      this.updateContent(1, newVal);
    },
  },
  computed: {
    isSelectVariable() {
      return this.selectVariable;
    },
    getSelectVariableValue() {
      return this.select_variable_value;
    },
    getVariableType() {
      return this.select_variable_type;
    },
  },
  methods: {
    async initData() {
      this.listTemplates = await GetAllltltemplates();
      this.ltlcode = this.listTemplates[0].formula;
      this.ltlConfig.params.description = this.listTemplates[0].description;
    },
    changeid(value) {
      const data = this.listTemplates.find((i) => {
        return i.lteid == value;
      });
      this.ltlcode = data.formula;
      this.description = data.description;
    },
    routing(param) {
      /* let ltl_content = this.getNodeValue() ltl content se duoc gui ve phia backend*/
      if (param == "add") {
        this.$store.commit("SetLtlConfig", this.ltlConfig);
        this.$store.commit("SetSelectedTemplate", this.select);
        if (this.select == "interger_overflow_underflow") {
          this.$router.push({ name: "ChooseElementOfSmartContract" });
        } else if (this.select == "reetrancy") {
          this.$router.push({ name: "SelectFuncReentrancyOp1" });
        } else if (this.select == "self_destruction") {
          this.$router.push({ name: "SelectFuncSD" });
        } else if (this.select == "timestamp_dependence") {
          this.$router.push({ name: "SelectFuncTimeStampSkipEmpty" });
        }
      }
      if (param == "back") {
        this.$router.push({ name: "CSPSettingType" });
      }
    },
    updateSelection(new_value) {
      if (new_value != "") {
        let elemnet = document.getElementById(this.select_variable_id);
        elemnet.innerText = new_value;
      }
      this.select_variable_id = "";
      this.select_variable_value = "";
      this.select_variable_type = "";
      this.selectVariable = false;
    },
    openSelectTable(id, value, type) {
      this.select_variable_value = value.substring(1, value.length - 1);
      this.select_variable_id = id;
      if (type != "") {
        this.select_variable_type = type;
      } else {
        this.select_variable_type = "var";
      }
      this.selectVariable = true;
    },
    removeSelectVarEventListener() {
      var userSelection = document.getElementsByClassName("select-variable");
      var self = this;
      for (var i = 0; i < userSelection.length; i++) {
        (function (index) {
          userSelection[index].removeEventListener("click", function (event) {
            self.openSelectTable(
              event.target.id,
              event.target.innerHTML,
              event.target.type
            );
          });
        })(i);
      }
    },
    addSelectVarEventListener() {
      var userSelection = document.getElementsByClassName("select-variable");
      var self = this;
      for (var i = 0; i < userSelection.length; i++) {
        (function (index) {
          userSelection[index].setAttribute("id", "select_var_" + i);
          userSelection[index].addEventListener("click", function (event) {
            self.openSelectTable(
              event.target.id,
              event.target.innerHTML,
              event.target.type
            );
          });
        })(i);
      }
    },
    updateContent(pos, value) {
      let result_element = document.getElementById("highlighting-content");
      this.removeSelectVarEventListener();
      result_element.innerHTML = analyseLTLCode(value);
      this.setCursor(pos);
      this.addSelectVarEventListener();
    },
    getNodeValue() {
      let result_element = document.getElementById("highlighting-content");
      let childs = result_element.childNodes;
      let all_text = [];
      for (let i = 0; i < childs.length; ++i) {
        if (childs[i]) {
          if (childs[i].nodeType != 3) {
            let value = childs[i].innerHTML;
            all_text.push(value);
          } else {
            all_text.push(childs[i].data);
          }
        }
      }
      return all_text
        .join("")
        .replace(/&amp;/g, "&")
        .replace(/&lt;/g, "<")
        .replace(/&gt;/g, ">");
    },
    updateInput() {
      let value = this.getNodeValue();
      let pos = this.getCursorPos();
      if (value.length == 0 && pos == 0) {
        value = " ";
        pos = 1;
      }
      this.updateContent(pos, value);
    },
    keyEnter() {
      let value = this.getNodeValue();
      let pos = this.getCursorPos();
      value = value.substring(0, pos) + "\n " + value.substring(pos, value.length);
      this.updateContent(pos + 1, value);
    },
    keyTab() {
      let value = this.getNodeValue();
      let pos = this.getCursorPos();
      value = value.substring(0, pos) + "\t" + value.substring(pos, value.length);
      this.updateContent(pos + 1, value);
    },
    getCursorPos() {
      let selection = window.getSelection();
      let range = selection.getRangeAt(0);
      range.setStartBefore(document.getElementById("highlighting-content").parentNode);
      let pos = range.toString().split("").length;
      range.collapse(false);
      return pos;
    },
    setCursor(pos) {
      pos += 1;
      let selection = window.getSelection();
      for (let position = 1; position < pos; position++) {
        selection.modify("move", "right", "character");
      }
    },
  },
};
</script>

<style scoped>
.container {
color: black;
}
#con-setting {
  width: 70%;
}
#header {
  margin-top: 2%;
  text-align: center;
  font-size: 35px;
  font-weight: bold;
}
.row {
  margin-top: 20px;
  margin-bottom: 5%;
}
.col-2 {
  font-size: 20px;
}
textarea {
  height: auto;
}
#btn-group {
  /* width: 100%; */
  padding-bottom: 5%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 25px;
  margin-bottom: 15px;
}
button {
  margin: auto;
  cursor: pointer;
  width: 15%;
  height: 2%;
  border: 1px solid #2196f3;
  text-align: center;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  padding: 4px 3px;
  border-radius: 4px;
  cursor: pointer;
}
#highlighting-content {
  margin: 10px;
  padding: 10px;
  border: 0;
  width: calc(100% - 32px);
  height: 150px;
  background-color: #f6f6f6;
  font-size: 15pt;
  font-family: normal normal 1em/1.2em monospace;
  line-height: 20pt;
  overflow: auto;
  white-space: pre;
}
#selection-table {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.5);
  transition: opacity 0.3s;
}
#selection-table-b2 {
  position: absolute;
  height: 550px;
  width: 1000px;
  border-radius: 10px;
  top: 60px;
  left: calc(50% - 500px);
  background-color: white;
}
</style>
