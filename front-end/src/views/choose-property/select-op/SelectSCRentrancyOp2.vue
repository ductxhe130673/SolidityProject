<template>
    <div class="container">
        <div class="header">
            <div class="back">
                <a href="/" class="link-primary text-decoration-underline">Back to home</a>
            </div>
            <div class="title">
                <h1>Select smart contracts</h1>
            </div>
        </div>
        <div class="row">
            <table class="table table-striped table-hover table-sm">
                <thead class="table-inside">
                    <tr>
                        <th style="width: 10%" scope="col">#
                            <span>
                                <a-icon id="icon" type="caret-up"/>
                                <a-icon id="icon" type="caret-down"/>
                            </span>
                        </th>
                        <th style="width: 60%" scope="col">Smart Contract name
                            <span>
                                <a-icon id="icon" type="caret-up"/>
                                <a-icon id="icon" type="caret-down"/>
                            </span>
                        </th>
                        <th style="width: 30%" scope="col">Selected
                            <span>
                                <a-icon id="icon" type="caret-up"/>
                                <a-icon id="icon" type="caret-down"/>
                            </span>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="data in datatable" :key="data.id">
                        <td>{{ data.id }}</td>
                        <td>{{ data.SmartContractName }}</td>
                        <td>
                            <input type="radio" id="one" name="ch" v-model="checkedNames" :value="data"/>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div id="processing-btn">
            <div class="pr-button" @click="routing('save')">
                Next
            </div>
            <div class="pr-button" @click="routing('skip')">
                Skip
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
        return{
            datatable: [
                {
                    id: "1",
                    SmartContractName: "Smart Contract 2",
                },
                {
                    id: "2",
                    SmartContractName: "Smart Contract 3",
                },
                {
                    id: "3",
                    SmartContractName: "Smart Contract 4",
                },
            ]
        };
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
.back {
    font-size: 15px;
    margin-top: 15px;
    margin-left: -20%;
}
.row{
    margin-top: 2%;
    padding-right: 10px;
}
table{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: 15px;
}
.table-sm{
    width: 800px;
    margin-left: 20%;
}
table td,
table th{
    border: 1px solid #ddd;
}
table tr:nth-child(odd){
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

/* button */
#processing-btn{
  width: 45%;
  height: 120px;
  margin-left: 27%;
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