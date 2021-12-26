<template>
  <div class="container-fluid">
    <div class="row">
      <h1 class="text-center">Generating CPN Model</h1>
    </div>
    <div class="row">
      <div class="col-md-3">Smart Contracts</div>
      <div class="col-md-7">
        <div id="table-list">
          <table class="table table-md">
            <thead>
              <tr>
                <th style="width: 10%">#</th>
                <th>Contract Name</th>
              </tr>
            </thead>
            <tr v-for="(item, index) in filterSC" :key="index">
              <td>{{ index + 1 }}</td>
              <td>{{ item }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Context</div>
      <div class="col-md-7">
        <input
          type="text"
          class="form-control"
          aria-describedby="basic-addon3"
          v-model="this.context"
        />
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">LTL Property</div>
      <div class="col-md-7">
        <input
          v-if="selected_vuls.name"
          type="text"
          class="form-control"
          aria-describedby="basic-addon3"
          v-model="selected_vuls.name"
        />
        <input
          v-else
          type="text"
          class="form-control"
          aria-describedby="basic-addon3"
          v-model="newLtl.params.name"
        />
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Configuration</div>
      <div class="col-md-7">
        <a class="link-primary" @click="navigate('config')">
          Link to setting Configuration</a
        >
      </div>
    </div>

    <div class="contain-process">
      <div id="processing-section">
        <div id="initial" v-if="step == 'initial'"></div>
        <div id="generating" v-show="step == 'generating'">
          <div>The smart contract is generating...</div>
          <div class="progress" id="progress">
            <div
              id="progress-bar-gen"
              class="progress-bar progress-bar-striped bg-warning"
              role="progressbar"
              style="width: 0%"
            ></div>
          </div>
        </div>
        <div id="generated" v-if="step == 'generated'">
          The generating process completed successfully
        </div>
        <div id="checking" v-show="step == 'checking'">
          <div>The smart contract is checking...</div>
          <div class="progress" id="progress">
            <div
              id="progress-bar-check"
              class="progress-bar progress-bar-striped bg-warning"
              role="progressbar"
              style="width: 0%"
            ></div>
          </div>
        </div>
        <div id="checked" v-if="step == 'checked'">
          The checking process completed successfully
        </div>
        <div id="results" v-if="this.results.length > 0 && step == 'finish'">
          <div><h3>Results:</h3></div>
          <div v-for="r in this.results" :key="r">{{ r }}</div>
        </div>
      </div>
    </div>

    <div id="showConfirmation" v-if="showConfirmationDownload">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirmDownload"
          @confirm="routing('uploadfile')"
          :dialog="upLoadDialog"
        />
      </div>
    </div>

    <div id="processing-btn">
      <button
        type="button"
        class="btn btn-outline-primary"
        v-if="step == 'initial' || step == 'generating'"
        @click="generate"
      >
        Generate
      </button>
      <button
        type="button"
        class="btn btn-outline-primary"
        v-if="step == 'check'"
        @click="check"
      >
        Check
      </button>
      <button v-if="step == 'finish'" class="btn btn-primary-outline" id="download">Next</button>
      <button v-if="showDownload" @click="downloadItem()" class="btn btn-primary-outline" id="download">
        Download
      </button>
      <button type="button" class="btn btn-outline-primary" @click="navigate('back')">
        Back
      </button>
    </div>
  </div>
</template>

<script>
import CheckService from "../services/check.service";
import { saveAs } from "file-saver";

// import { GetLtl } from "../services/data";

export default {
  data() {
    return {
      step: "initial",
      list_selected_sc: [],
      selected_vuls: "",
      context: this.$store.state.data.data.selectedContext.name,
      error: true,
      view: "",
      ltlProperty: [],
      results: [],
      showConfirmation: false,
      dialog: {},
      confirmation: "",
      currentSC: null,
      newLtl: this.$store.state.data.data.ltlConfig,
      showConfirmationDownload: false,
      fileDownload: {},
    };
  },

  beforeMount() {
    this.list_selected_sc = this.$store.state.data.data.selectedSc;
    this.selected_vuls = this.$store.state.data.data.selectedTemplate;
    console.log("newLtl", this.newLtl);
  },
  components: {
    // Popup,
  },
  methods: {
    downloadItem() {
      if (this.fileDownload !== {}) {
        let blob_hcpn = new Blob([this.fileDownload.hcpn.content], {
          type: "text/plain;charset-urf-8",
        });
        let blob_prop = new Blob([this.fileDownload.prop.content], {
          type: "text/plain;charset-urf-8",
        });
        let blob_context = new Blob([this.fileDownload.context.content], {
          type: "text/plain;charset-urf-8",
        });
        saveAs(blob_hcpn, this.fileDownload.hcpn.name);
        saveAs(blob_prop, this.fileDownload.prop.name);
        saveAs(blob_context, this.fileDownload.context.name);
      }
    },

    sort(mess) {
      switch (mess) {
        case "asName":
          this.list_selected_sc.sort((a, b) => (a.name < b.name ? 1 : -1));
          break;
        case "deName":
          this.list_selected_sc.sort((a, b) => (a.name > b.name ? 1 : -1));
          break;
      }
    },
    // async fetchLTLProp() {
    //   this.ltlProperty = await GetLtl();
    // },
    navigate(param) {
      if (param == "config") {
        this.$router.push({ name: "InitialMarkingLink" });
      }
      if (param == "back") {
        this.$router.push({ name: "Initial" });
        this.$store.commit("setIndex", 4);
      }
    },
    async callUnfoldingTool() {
      const newVar = this.$store.state.data.data.isVarSelected;
      if (this.newLtl.type !== "general") {
        this.newLtl.params.formula = this.newLtl.params.formula.replaceAll(
          "variable",
          newVar
        );
      }

      const tName = "unfolding";
      const tcontext_PATH_xml = this.$store.state.data.data.selectedContext.content;
      const tltl_PATH_json = JSON.stringify(this.newLtl, 0, 2);
      const initialMarkingInfor = JSON.stringify(
        this.$store.state.data.data.initialMarkingInfor,
        0,
        2
      );
      const res = await CheckService.callUnfoldingTools(
        tName,
        tcontext_PATH_xml,
        tltl_PATH_json,
        initialMarkingInfor
      );
      this.$store.commit("SetDataToDownload", res.data);
      this.fileDownload = res.data;
    },

    async callToolHelena() {
      console.log("Call the helena tool");
      const tName = "helena";
      this.$store.commit("Setrs", "wait a seconds...");
      const res = await CheckService.callHelenaTools(tName);
      if (res.status == 200 && res !== null && res != undefined) {
        const mess = res.data.message;
        console.log(mess);
        this.results.push(mess);
        this.$store.commit("Setrs", mess);
        await CheckService.addNewCheckedBatchSC(
          this.selected_vuls.lteid,
          this.context.cid,
          this.list_selected_sc.length,
          1,
          this.newLtl.params.formula,
          this.results[0]
        );
      } else {
        this.$store.commit("Setrs", "11");
        this.results.push("Can't run HELENA tools");
      }
    },
    async callToolLTL() {
      const tName = "ltl";
      const res = await CheckService.callToolLTL(tName);
      if (res.status == 200 && res !== null && res != undefined) {
        const mess = res.data.message;
        this.results.push(mess);
      } else {
        this.results.push("Can't run LTL tools");
      }
    },
    async checkContext() {
      const toolName = "dcr2cpn";
      const xml = "";
      // console.log(context);
      const res = await CheckService.callDCNTools(toolName, xml);
      console.log(res);
    },
    move(id) {
      //let _this = this;
      var elem = document.getElementById(id);
      var width = elem.offsetWidth;
      if (width >= 0) width = 0;
      var inter = setInterval(() => {
        if (width >= 100) {
          clearInterval(inter);
        } else {
          width++;
          elem.style.width = width + "%";
        }
      }, 10);
    },
    async delay(ms) {
      return await new Promise((resolve) => setTimeout(resolve, ms));
    },
    async generate() {
      console.log("--generating--");
      // await SetDataForCallingTool(this.context, this.selected_vuls);
      this.step = "generating";
      this.move("progress-bar-gen");
      await this.delay(2000);
      this.step = "check";
      this.$store.commit("data/SetProcessView", "check-sc");
      this.$store.commit("setIndex", 6);
      //dcr2cpn
      // await this.checkContext();
      //unfoding
      await this.callUnfoldingTool();
      // await this.callToolLTL();
    },
    async check() {
      this.step = "checking";
      this.move("progress-bar-check");
      await this.delay(2000);
      // if (this.error)
      //  confirm(
      //    "We have discover some counter-examples with the smart contract code. Do you want to look at them?"
      //  );
      this.step = "checked";
      this.step = "finish";
      this.$store.commit("data/SetProcessView", "finish");
      this.callToolHelena();
      await this.delay(2000);
      this.$router.push({ name: "checkingresult31" });
      this.$store.commit("setIndex", 7);
    },
    routing(processview) {
      this.$store.commit("data/SetProcessView", processview);
    },
    addSmartContract() {
      this.$store.commit("data/SetProcessView", "sc-selection");
    },
    inc(value) {
      return value + 1;
    },
    removeSC(sc) {
      this.dialog = {
        title: "Remove Smart Contract",
        message: "Are you sure to remove '" + sc.name + "' ?",
        confirmbtn: "Remove",
      };
      this.confirmation = "removeSC";
      this.currentSC = sc.id;
      this.showConfirmation = true;
    },
    cfRemoveSC(id) {
      for (var i = 0; i < this.list_selected_sc.length; i++) {
        if (this.list_selected_sc[i].id === id) {
          this.list_selected_sc.splice(i, 1);
        }
      }
      this.$cookies.set("_ssc", JSON.stringify(this.list_selected_sc));
      this.closeConfirm();
    },
    editSC(sc_id, sc_name) {
      this.$router.push({
        name: "EditSc",
        params: { sc_id: sc_id, name: sc_name, parent_path: "/process" },
      });
    },
    removeAllSc() {
      if (this.list_selected_sc.length > 0) {
        this.confirmation = "removeAll";
        this.dialog = {
          title: "Remove All",
          message: "Are you sure to remove all selected smart contracts?",
          confirmbtn: "Remove All",
        };
        this.showConfirmation = true;
      }
    },
    cfRemoveAll() {
      this.list_selected_sc = [];
      this.$store.commit("data/SetSelectedSC", this.list_selected_sc);
      this.$cookies.set("_ssc", JSON.stringify(this.list_selected_sc));
      this.closeConfirm();
    },
    closeConfirm() {
      this.showConfirmation = false;
    },
  },
  mounted() {
    this.view = this.$store.getters["data/GetProcessView"];
  },
  computed: {
    filterSC() {
      var listSC = [];
      this.list_selected_sc.forEach(function (item) {
        listSC.push(item.name);
      });
      return listSC;
    },
    done_result() {
      return this.$store.getters.Getrs;
    },
    selectedSc() {
      return this.list_selected_sc;
    },
    isSelectSomeThing() {
      return this.list_selected_sc.length > 0;
    },
    getStep() {
      return this.step;
    },
    showDownload() {
      return this.step != "initial" && this.step != "generating";
    },
  },
};
</script>

<style scoped>
h1 {
  font-weight: bold;
}
.container-fluid {
  color: black;
  background-color: white;
}
.row {
  margin-top: 2%;
  padding-right: 10px;
  margin-bottom: 2%;
}
.col-md-3 {
  padding-left: 13%;
  font-size: 18px;
}
a:hover {
  text-decoration: underline;
}
#table-list {
  width: 100%;
  margin: auto;
  font-size: 0.9em;
  height: 200px;
  overflow-y: auto;
}
/* table */
table {
  width: 100%;
  font-size: 1.1em;
}

table td,
table th {
  padding-left: 10px;
}
table td {
  padding: 10px;
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
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  color: #3a7694;
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
.contain-process {
  width: 60%;
  margin: 0 auto;
  padding-bottom: 5%;
}

#processing-btn {
  display: flex;
  width: 50%;
  justify-content: space-between;
  margin: 0 auto;
  padding-bottom: 5%;
}

#download {
  text-align: right;
  padding: 20px;
  height: 60px;
}

#processing-section {
  height: 300px;
  margin: auto;
  border: 1px black solid;
  border-radius: 3px;
  text-align: center;
  background-color: #f5f5f5;
  width: 80%;
}
#generating,
#checking {
  margin: auto;
  margin-top: 60px;
  padding: 0;
  width: 70%;
}
#results {
  margin-left: 40px;
  text-align: left;
  margin-top: 0;
  overflow: scroll;
  height: 79%;
}
#generated,
#checked {
  margin-top: 100px;
}
/*---- showConfirmation */
#showConfirmation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
  z-index: 1;
  align-items: center;
  justify-content: center;
}
#removeSC-holder {
  margin-top: 200px;
}
#removeAll-holder {
  margin-top: 50px;
}
#download {
  border: 1px solid #0d6efd;
  color: #0d6efd;
}
</style>
