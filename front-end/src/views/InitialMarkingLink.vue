<template>
    <div class="container">
        <h1><b>Configuration</b></h1>
        <div class="row">
            <div class="col-3 left">Type</div>
            <div class="col 7 right">
                <div class="radioB">
                    <div>
                        <input id="radio-1" name="radio" type="radio" checked>
                        <label for="radio-1" class="radio-label">Fixed</label>
                    </div>
                    <div>
                        <input id="radio-2" name="radio" type="radio">
                        <label  for="radio-2" class="radio-label">Random</label>
                    </div>

                    <div>
                        <input id="radio-3" name="radio" type="radio">
                        <label for="radio-3" class="radio-label">Map</label>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-3 left">User Parameters</div>
            <div class="col-7 right">
                <table class="table table-striped" border="2">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>User</th>
                            <th>Balance</th>
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
        </div>

        <div class="row">
            <div class="col-3 left">Function Parameters</div>
            <div class="col-7 right">
                <ul class="nav nav-tabs">
                <li class="nav-item">
                    <a href="#" class="nav-link" @click="OpenSC(event,'Smart Contract 1')">Smart Contract 1</a>
                </li>

                <li class="nav-item">
                    <a href="#" class="nav-link" @click="OpenSC(event,'Smart Contract 2')">Smart Contract 2</a>
                </li>

                <li class="nav-item">
                    <a href="#" class="nav-link" @click="OpenSC(event,'Smart Contract 3')">Smart Contract 3</a>
                </li>
                </ul>
                <div class="smart">
                   <div class="textbox">
                    <ul class="nav nav-tabs" style="margin-left: 10%">
                        <li class="nav-item">
                            <a class="nav-link">Function 1</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link">Function 2</a>
                        </li>
                    </ul>
                    <div class="function">
                        <div class="atable">
                        <table class="table table-striped table-hover table-sm">
                            <thead class="table-inside">
                                <tr>
                                    <th>#</th>
                                    <th>Argument</th>
                                    <th>Value</th>
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
        </div>

        <div class="action">
            <div id="btn-back" @click="routing('back')">Back</div>
        </div>
    </div>
</template>
<script>
export default{
    data(){
        return{
            info: [],
            id: null,
        };
    },
    methods: {
        routing(param){
            if(param == "back"){
                this.$router.push({name: "GenerateLNAfile"});
                this.$store.commit("setIndex",0);
            }
        }
    }
}

</script>
<style scoped>
h1 {
  padding-top: 35px;
  padding-bottom: 25px;
  text-align: center;
}
.container {
  width: 60%;
}
.left {
  font-size: 20px;
}
.row {
  margin-top: 30px;
  margin-bottom: 30px;
}
.radioB{
  display: flex;
}
label{
  margin: 0.5rem;
}
.table thead tr {
    background-color:darkgrey;
    color:black;
    
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
.smart {
  border: 1px solid #d9edf7;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px,
    rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
  background: none;
  z-index: 2;
  position: relative;
}
.smart {
  border-radius: 10px;
  text-align: center;
  height: 470px;
  color: black;
}
.atable {
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px,
    rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
  margin-left: 50px;
  margin-top: 50px;
  margin-right: 50px;
  padding-bottom: 10%;
  border: 1px solid #d9edf7;
}
.nav-tabs{
  margin-left: 5%;
  border-bottom: 0px;
}
.nav-link{
  background-color: darkgray;
  color: black;
}
.nav-item a:hover {
  background-color: white;
}
.function{
  border: 1px solid #d9edf7;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px,
    rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
  background: none;
  z-index: 2;
  position: relative;
  border-radius: 10px;
  text-align: center;
  height: 350px;
  width: 90%;
  color: black;
  margin-left: 5%;
}
.textbox{
    margin-top: 20px;
}
#btn-back {
  cursor: pointer;
  width: 12%;
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
  margin-left: 40%;
  /* margin-top: 10%; */
}
</style>