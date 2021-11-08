<template>
    <div id="initial-link">
        <div id="initial-link-header">
            Configuration
        </div>
        <div id="initial-marking-link-input">
            <div id="header-section">
                <div class="multi-cell">
                    Type
                </div>
                <div class="user-cell">
                    User parameters
                </div>
                <div class="function-cell">
                    Function parameters
                </div>
            </div>
            <div id="input-section">
                <div class="multi-cell">
                    <div id="multi-radio-choose">
                        <div class="radio-choose">
                            <input type="radio" name="radio" class="radio-buttons" value="fixed">
                            <span>Fixed</span>
                        </div>
                        <div class="radio-choose">
                            <input type="radio" name="radio" class="radio-buttons" value="random">
                            <span>Random</span>
                        </div>
                        <div class="radio-choose">
                            <input type="radio" name="radio" class="radio-buttons" value="map" checked>
                            <span>Map</span>
                        </div>
                    </div>
                </div>
                <div class="user-cell">
                  <table class="table table-striped" border="2">
                    <thead>
                        <tr>
                            <th>#<span class="material-icons"> swap_vert </span></th>
                            <th>User<span class="material-icons"> swap_vert </span></th>
                            <th>Balance<span class="material-icons"> swap_vert </span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>User 1</td>
                            <td>1</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>User 2</td>
                            <td>3</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>User 3</td>
                            <td>2</td>
                        </tr>
                        <tr>
                            <td>...</td>
                        </tr>
                    </tbody>
                </table>
                </div>
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
                            v-bind:class="{ active: item.id == selected_sc}"
                            >{{ item.name }}</a>
                            </li>
                        </ul>
                    </div>
                    <div id="sm-information-table">
                        <ul class="nav nav-tabs">
                            <li
                            class="nav-item d-inline-block text-truncate"
                            v-for="item in list_function"
                            :key="item.id"                            
                            >
                            <a
                            class="nav-link"
                            v-on:click="selected_sc = item.id"
                            v-bind:class="{ active: item.id == selected_sc}"                
                            >{{ item.name }}</a>
                            </li> 
                        </ul>
                        <div id="fc-information-table">
                            <div id="sender-value-section">
                                <span>Sender value</span>
                                <input type="text" placeholder="2">
                                <span>To</span>
                                <input type="text" placeholder="10">
                            </div>
                            
                        <table class="table table-striped table-hover table-sm" id="table-function">
                            <thead class="table-inside">
                                <tr>
                                    <th>#<span class="material-icons"> swap_vert </span></th>
                                    <th>Argument<span class="material-icons"> swap_vert </span></th>
                                    <th>Value<span class="material-icons"> swap_vert </span></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1</td>
                                    <td>Argument 1</td>
                                    <td>3</td>
                                </tr>
                                <tr>
                                    <td>2</td>
                                    <td>Argument 2</td>
                                    <td>5</td>
                                </tr>
                                <tr>
                                    <td>...</td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </tbody>
                        </table>
                        </div>                    
                    </div>            
                </div>
            </div>
        </div>
        
        <div id="processing-btn">
            <button class="pr-button" @click="routing('back')">Back</button>
        </div>
    </div>

</template>
<script>
export default{
    data(){
        return{
            info: [],
            id: null,
            radio_seleted: "map",
            function_cell_selected: "function",
            list_smart_contract: [{name:"smart I",id:1},{name:"smart II",id:2},{name:"smart III",id:3},{name:"smart IV",id:4}],
            list_function: [{name: "Function 1", id:1},{name: "Function 2",id:2}],
        };
    },
    methods: {
        routing(param){
            if(param == "back"){
                this.$router.push({name: "CheckSmartContract"});
                this.$store.commit("setIndex",0);
            }
        }
    }
}

</script>
<style scoped>
#initial-link{
  height: 100%;
  width: 100%;
  min-width: 900px;
}
#initial-link-header{
  height: 60px;
  padding-top: 10px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}
#initial-marking-link-input{
  width: 60%;
  margin-left: 20%;
  display: flex;
  justify-content: space-between;
}
#header-section{
  flex-basis: 20%;
  font-size: 14px;
}
#input-section{
  flex-basis: 80%;
}
.multi-cell{
  height: 120px;
  margin-top: 120px;
}
.function-cell{
  margin-top: 20px;
}
.user-cell{
    height: 300px;
}
#multi-radio-choose{
  display: flex;
}

.radio-choose{
  flex-basis: 20%;
  height: 20px;
  margin-bottom: 20px;
}

.radio-choose span{
  font-size: 14px;
}

.radio-choose input{
  height: 11px;
}

#fixed-input-form{
  width: 60%;
}

#map-input-form{
  width: 60%;
}

#random-input-form{
  width: 60%;
  display: flex;
  justify-content: space-between;
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
#sm-information-table{
  border: black solid; 
  padding: 3% 2% 3% 2%;
}
#fc-information-table{
  border: black solid; 
  padding: 3% 2% 3% 2%;
}
#sender-value-section{
  margin-top: 10px;
}

#sender-value-section span{
  font-size: 14px;
}
#sender-value-section input{
  width: 80px;
  height: 25px;
  margin-left: 10px;
  margin-right: 10px;
}
#table-function{
    margin-top: 20px;
}

/* Function */
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
  height: 49px;
}
#header-row{
  background-color: rgb(196, 194, 194);
  font-weight: bold;
}

#table-list span {
  float: right;
  margin: 0 20% 0 0;
  padding: 0;
  font-size: 150%;
}
.even_row{
  background-color: rgb(226, 224, 224);
}

.input-param-text{
  color: rgb(42, 42, 214);
  cursor: pointer;
}
.input-param-text:hover{
  color: rgb(78, 78, 243);
}
.table thead tr {
    background-color:darkgrey;
    color:black;
    
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
#processing-btn{
  width: 60%;
  height: 100px;
  margin-left: 30%;
  justify-content: space-between;
  align-items: center;
  margin-top: 100px;
}
#processing-btn .pr-button {
  cursor: pointer;
  width: 20%;
  height: 30px;
  border: 1px solid #2196f3;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  padding-top: 4px;
  border-radius: 4px;
  margin-left: 30%;
}
#processing-btn .pr-button:hover {
  background-color: #176fd4;
  color: white;
}
</style>
