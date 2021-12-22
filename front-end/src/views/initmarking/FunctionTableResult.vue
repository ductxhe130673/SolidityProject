<template>
  <div>
    <div id="params-setting-header">
      <span id="return-arrow" class="material-icons" @click="existParamTable">
        keyboard_backspace
      </span>
      <span id="ps-function-name">Function: {{ own_list_argument.name }}</span>
    </div>
    <div id="params-setting-input">
      <div id="sender-value-section">
        <span>Sender value</span>
        <input type="text" placeholder="0" v-model="own_list_argument.sender" />
      </div>
      <div id="table-params">
        <table class="table">
          <thead>
            <tr>
              <th style="width: 10%">#</th>
              <th>
                Parameters
                <span>
                  <a-icon id="icon" type="caret-up" />
                  <a-icon id="icon" type="caret-down" />
                </span>
              </th>
              <th style="width: 25%">Range</th>
            </tr>
          </thead>
          <tr
            v-for="(param, key) in own_list_argument.argument"
            v-bind:key="key"
          >
            <td>{{ param.id }}</td>
            <td>{{ param.name }}</td>
            <td><input type="text" v-model="param.value" /></td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["list_argument"],
  data() {
    return {
      function_cell_selected: "function",
      own_list_argument: {},
    };
  },
  beforeMount() {
    this.own_list_argument = this.list_argument;
  },
  methods: {
    setArgument() {
      this.$emit("setArgument", this.own_list_argument.argument);
    },
    existParamTable() {
      this.$emit("changeInitMarking", this.own_list_argument);
      this.setArgument();
      this.$emit("changeSelected", "function");
    },
  },
  computed: {},
};
</script>

<style scoped>
#params-setting-header {
  display: flex;
  height: 30px;
  vertical-align: middle;
}

#params-setting-header span {
  margin-right: 20px;
}
#ps-function-name {
  font-weight: bold;
}
#return-arrow {
  cursor: pointer;
  color: rgb(38, 38, 192);
  font-size: 26px;
}

#return-arrow:hover {
  color: rgb(81, 81, 231);
}

#params-setting-input {
  height: 270px;
  border: 1px solid black;
  padding-left: 4%;
  padding-right: 4%;
}

#sender-value-section {
  margin-top: 10px;
  margin-bottom: 10px;
}

#sender-value-section span {
  font-size: 14px;
}
#sender-value-section input {
  width: 80px;
  height: 25px;
  margin-left: 10px;
  margin-right: 10px;
  border: 1px solid grey;
}

/* table */
#table-params {
  margin: auto;
  font-size: 0.9em;
  height: 240px;
  overflow-y: auto;
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
table input{
  border: 1px solid grey;
  width: 50%;
}
</style>
