<template>
    <div class="container">
      <div class="header">
        <div class="title">
          <h1>Select variables of the selected function</h1>
        </div>
      </div>
    <div class="row">
      <table class="table table-striped table-hover table-sm">
        <thead class="table-inside">
          <tr>
            <th style="width: 10%" scope="col">#
              <span><a-icon id="icon" type="caret-up" />
              <a-icon id="icon" type="caret-down"/>
              </span>
            </th>
            <th style="width: 60%" scope="col">Global variable
              <span><a-icon id="icon" type="caret-up" />
              <a-icon id="icon" type="caret-down"/>
              </span>
            </th>
            <th style="width: 30%" scope="col">Selected
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in datatable" :key="data.id">
            <td>{{ data.id }}</td>
            <td>{{ data.GlobalVariable }}</td>
            <td>
              <!-- <input type="radio" name="radios" id="radio1" /> -->
              <input type="radio" id="one" name="ch" v-model="checkedNames" :value="data"/>
            </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div class="function-cell">
      <div id="list-function">
        <ul class="nav nav-tabs">
          <li class="nav-item d-inline-block text-truncate"
          v-for="item in list_function"
          :key="item.id">
          <a class="nav-link"
          v-on:click="selected_func = item.id"
          v-bind:class="{ active: item.id == selected_func}">{{item.name}}</a>
          </li> 
        </ul>
      </div>
      <div id="func-information-table">
          <div id="table-list">
            <div class="table-row" id="header-row">
              <div class="table-cell header-cell first-cell">
                #
                <span><a-icon id="icon" type="caret-up" />
                <a-icon id="icon" type="caret-down"/>
                </span>
              </div>
              <div class="table-cell header-cell second-cell">
                Local variable
                <span><a-icon id="icon" type="caret-up" />
                <a-icon id="icon" type="caret-down"/>
                </span>
              </div>
              <div class="table-cell header-cell third-cell">
                Selected
              </div>
              
            </div>
            <div class="table-row" v-for="(func, index) in getSelectedFunc" v-bind:key="func.fid" :class="{ even_row: index % 2 == 0}">
              <div class="table-cell first-cell">{{index +1 }}</div>
              <div class="table-cell second-cell">{{func.name}}</div>
              <div class="table-cell third-cell">
                <input type="radio" id="one" name="ch" v-model="checkedNames" :value="data"/>
              </div>
            </div>
          </div>
        
      </div>
    </div>
    <div id="processing-btn">
      <div class="pr-button" @click="routing('save')">
        Next
      </div>
      <div class="pr-button" @click="routing('back')">
        Back
      </div>
    </div>
  </div>
</template>
<script>
export default{
    data() {
        return {
          function_cell_selected: "function",
          list_function:[{name: "Function 1",id:1}],
          function_infor: {1:{
            "name": "Function 1",
            "functions": [
              {
                "fid": 1,
                "name":"Local Variable 1",
              },
              {
                "fid": 2,
                "name":"Local Variable 2",
              },
            ],
          }},
          selected_func: 1,
            datatable: [
                {
                    id: "1",
                    GlobalVariable: "Global Variable 1",
                },
                {
                    id: "2",
                    GlobalVariable: "Global Variable 2",
                },
                {
                    id: "3",
                    GlobalVariable: "Global Variable 3",
                },
                {
                    id: "4",
                    GlobalVariable: "Global Variable 4",
                },
                {
                    id: "5",
                    GlobalVariable: "Global Variable 5",
                },
            ]
        };
        
    },
    computed:{
    getSelectedFunc(){
      if(this.selected_func in this.function_infor){
        return this.function_infor[this.selected_func].functions
      }else{
        return []
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
.row{
    margin-top: 2%;
    padding-right: 10px;
}
table{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

table td,
table th{
    border: 1px solid #ddd;
}
table tr:nth-child(even){
    background-color: #f2f2f2;
}
table tr:hover{
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

#func-information-table{
  border: black solid; 
  padding: 3% 2% 3% 2%;
}

#table-list {
  width: 100%;
  margin: auto;
  font-size: 0.9em;
  height: 300px;
  overflow-y: auto;
  border-radius: 4px;
  border: 2px solid black;
  background: rgb(241, 240, 240);
}

.table-row{
  display: flex;
  height: 50px;
  border: 2px solid #ddd;
}
#header-row{
  background-color: rgb(196, 194, 194);
  font-weight: bold;
}

#table-list span {
  float: right;
  margin: 0 20% 0 0;
  padding: 0;
  font-size: 100%;
}
.even_row{
  background-color: rgb(226, 224, 224);
}
.table-cell{
  padding-top: 10px;
  font-size: 15px;
}
.first-cell{
  flex-basis: 10%;
  padding-left: 5px;
}
.second-cell{
  flex-basis: 60%;
}
.third-cell{
  flex-basis: 30%;
}

/* button */
#processing-btn{
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
.btn{
  margin: 0 3%;
}
</style>