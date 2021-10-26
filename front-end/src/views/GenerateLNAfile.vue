<template>
        <div class="container-fluid">
        <h1>Generating CPN Model</h1>
        <div class="row">
            <div class="col-3">
                <h5>Smart Contracts</h5>
            </div>
            <div class="col-7">
                <table class="table table-striped" border="2">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Contract Name</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>blind Auction</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>etherLotto</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>...</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-3">
                <h5>Context</h5>
            </div>
            <div class="col-7">
                <div class="input-group input-group-sm mb-3">
                    <input type="text" class="form-control" placeholder="Gaming">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-3">
                <h5>LTL Property</h5>
            </div>
            <div class="col-7">
                <div class="input-group input-group-sm mb-3">
                    <input type="text" placeholder="Interger overflow" class="form-control">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-3">
                <h5>Configuration</h5>
            </div>
            <div class=" col-7">
                <a href="#" class="link" @click="routing('add')">Link to setting configuration</a>
            </div>
        </div>
        <!-- <div class="row">
            <div class="wrapper">
                <h6>The smart contract is generating...</h6>
                <div class="progress" style="height: 40px;">
                    <div class="progress-bar" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
            </div>
        </div> -->

        <div class="contain-process">
            <div id="processing-section">
                <div id="initial" v-if="step == 'initial'"></div>
                <div id="generating" v-show="step == 'generating'">
                <div>The smart contact is generating...</div>
                <div class="progress" id="progress">
                    <div id="progress-bar-gen"
                    class="progress-bar progress-bar-striped bg-warning"
                    role="progressbar"
                    style="width: 0%"></div>                  
                </div>
                </div>

            </div>
        </div>
        <div class="row">
            <div id="action">
                <!-- <button v-if="step == 'initial' || step == 'generating'"
                 class="btn btn-primary-outline" 
                 @click="generate"
                 >
                 Generate
                 </button> -->
                <button class="btn btn-outline-primary">Generate</button>
                <button class="btn btn-outline-primary" @click="routing('back')">Back</button>
            </div>
        </div>

    </div>
</template>
<script>
export default {
    data() {
    return {
      info: [],
      id: null,
    };
  },
  methods: {
      routing(param){
        if (param == "back") {
            this.$router.push({ name: "" });
            this.$store.commit("setIndex", 0); 
        }
        if(param == "add"){
            this.$router.push({name: "InitialMarkingLink"})
        }
      }
  }
}
</script>

<style scoped>
h1 {
    text-align: center;
    padding: 50px;
}

.link {
    text-decoration: underline;
}

h5 {
    text-align: left;
    padding-left: 50px;
}

.row {
    margin-bottom: 50px;
}

.wrapper {
    width: 500px;
    height: 200px;
    border: 1px solid black;
    margin: 50px auto;
    padding: 50px;
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
.table thead tr {
    background-color:darkgrey;
    color:black;
}
table{
    width: 100%;
}
.progress {
    text-align: center;
    border: 1px solid black;
}
.progress-bar{
    width: 50%;
}
#action {
    margin: 0 auto;
    margin-top: 4%;
    display: flex;
    justify-content: space-between;
    width: 25%;
}
</style>