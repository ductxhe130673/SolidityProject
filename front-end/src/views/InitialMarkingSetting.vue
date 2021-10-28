<template>
  <div class="container">
    <h1><b>Configuration</b></h1>

    <div class="row">
      <div class="col-3 left">Number of users</div>
      <div class="col-7 right">
        <input type="text"
          class="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
          placeholder="5"
        />
      </div>
    </div>
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

    <div class="row">
      <div class="col-3 left">Balance</div>
      <div class="col-7">
        <input
          type="text"
          class="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
          placeholder="10"
        />
      </div>
    </div>

    <!-- <div class="row">
      <div class="col-2">Sender value</div>
      <div class="col-10">
        <input
          type="text"
          class="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
        />
      </div>
    </div> -->
    
    <div class="row" id="textbox">
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
      <div class="col-3 left">Function parameters</div>
      <div class="col-7 ">
        <!-- <textarea class="form-control" aria-label="With textarea">
          
        </textarea> -->
        <textbox class="form-control" aria-label="With textbox">
          <table class="table table-striped" border="2">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Functions</th>
                            <th>Arguments</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Function1</td>
                            <td><a href="#" @click="routing('addsc')">Input Params</a></td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Function2</td>
                            <td><a href="#" @click="routing('addsc')">Input Params</a></td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>Function3</td>
                            <td><a href="#" @click="routing('addsc')">Input Params</a></td>
                        </tr>
                    </tbody>
          </table>
        </textbox>
      </div>
    </div>

    <div id="btn-group">
      <button class="btn btn-outline-primary btn-sm" @click="routing('save')">
        Next
      </button>
      <button
        class="btn btn btn-outline-primary btn-sm"
        type="button"
        @click="routing('back')"
      >
        Back
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    routing(param) {
      if (param == "save") {
        // this.$router.push({ name: "CheckSmartContract" });
        this.$router.push({name: "GenerateLNAfile"});
        // this.$router.push({ name: "CheckSmartContract" });
        this.$store.commit("setIndex", 5);
      }
      if (param == "back") {
        this.$router.push({ name: "CSPSettingType" });
      }
      if(param == "addsc"){
        this.$router.push({name: "ChooseParams"});
        // this.$store.commit("SetIndex",2);
      }
    },
  },
};

// function OpenSC(evt, name) {
//   var i, table, a;
//   table = document.getElementsByClassName("table");
//   for (i = 0; i < table.length; i++) {
//     table[i].style.display = "none";
//   }
//   a = document.getElementsByClassName("a");
//   for (i = 0; i < a.length; i++) {
//     a[i].className = a[i].className.replace(" active", "");
//   }
//   document.getElementById(name).style.display = "block";
//   evt.currentTarget.className += " active";
// }
</script>
<style scoped>
textarea{
  padding-bottom: 15%;
}

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
.col-2 {
  font-size: 20px;
}
.row {
  margin-top: 30px;
  margin-bottom: 30px;
}

.radioB{
  display: flex;
  margin-left: 25%;
}
.nav-tabs{
  margin-left: 30%;
  border-bottom: 0px;
}
.nav-link{
  background-color: darkgray;
  color: black;
}
.nav-item a:hover {
  background-color: white;
}
label{
  margin: 0.5rem;
}

.text {
  height: 200px;
}
.smart_contract_button{
  margin-left: 20%;
}
#btn-group {
  width: 100%;
  display: flex;
  margin-left: 4%;
  padding-bottom: 7%;
}
button {
  margin: auto;
  margin-top: 40px;
  cursor: pointer;
  width: 15%;
  height: 2%;
  border: 1px solid #2196f3;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
}
</style>