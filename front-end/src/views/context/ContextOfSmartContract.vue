<template>
  <div class="container" id="section">
    <div id="header">Context of the Smart Contract</div>

    <div class="row" id="select">
      <div class="col-2">
        <p>Context of the SCs</p>
      </div>
      <div class="col-10">
        <select
          class="form-select input-sm"
          aria-label="Default select example"
          v-model="selectedContext"
        >
          <option>--- Select Context ---</option>
          <option v-for="c in contexts" :key="c.cid" :value="c">
            {{ c.name }}
          </option>
        </select>
      </div>
    </div>
    <div class="row" id="select">
      <div class="col-2">
        <p>Type</p>
      </div>
      <div class="col-10">
        <input class="form-control" type="text" :value="selectedContext.context_type" />
      </div>
    </div>

    <div class="row" id="description">
      <div class="col-2">
        <p>Description</p>
      </div>
      <div class="col-10">
        <span>There are several options:</span>
        <ul>
          <li v-for="(c, index) in contexts" :key="index">{{ c.description }}</li>
        </ul>
      </div>
    </div>
    <div id="btns">
      <button @click="routing('add')">Next</button>
      <button @click="upLoad()">Upload a Context File</button>
      <button @click="routing('ship')">Skip</button>
      <button @click="routing('back')">Back</button>
    </div>
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirm"
          @confirm="routing('upfile')"
          :dialog="upLoadDialog"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { GetAllcpncontext } from "../../services/data";
import UpLoadFile from "../../components/UpLoadFile.vue";
export default {
  components: {
    confirm: UpLoadFile,
  },
  data() {
    return {
      contexts: [],
      selectedContext: {},
      contextSC: [],
      selectComponents: "",
      selected: "0",
      showConfirmation: false,
      upLoadDialog: {},
    };
  },
  computed: {
    // getShowComponents() {
    //   return this.showComponents;
    // },
    getSelectComponents() {
      return this.selectComponents;
    },
  },

  mounted() {
    this.selectedContext = this.$store.state.data.data.selectedContext;
    this.initData();
  },
  methods: {
    upLoad() {
      this.upLoadDialog = {
        title: "Choose a new Context file",
        confirmbtn: "OK",
      };
      this.showConfirmation = true;
    },
    closeConfirm() {
      this.showConfirmation = false;
    },

    async initData() {
      this.contexts = await GetAllcpncontext();
    },

    cComponents() {
      this.showComponents = false;
    },
    OpenUploadContext() {
      this.selectComponents = "uploadctx";
      this.showComponents = true;
    },
    loadContext() {
      this.showComponents = true;
    },
    routing(param) {
      if (param == "add") {
        this.$store.commit("SetSelectedContext", this.selectedContext);
        this.$router.push({ name: "LTLCheckOption" });
        this.$store.commit("setIndex", 4);
      }
      if (param == "upfile") {
        this.$router.push({ name: "UpLoadContext" });
      }
      if (param == "ship") {
        this.$router.push({ name: "LTLCheckOption" });
        this.$store.commit("setIndex", 4);
      }
      if (param == "back") {
        this.$router.push({ name: "SelectSmartContract" });
        this.$store.commit("setIndex", 2);
      }
    },
  },
};
</script>

<style scoped>
#section {
  width: 70%;
  margin: auto;
}
#header {
  text-align: center;
  font-size: 35px;
  font-weight: bold;
  margin-top: 2%;
  padding-bottom: 2%;
}
#select {
  text-align: center;
}
#select p {
  text-align: left;
  font-size: 18px;
}
#load-btn {
  float: left;
}
#description {
  margin-top: 2%;
}
#description p {
  text-align: left;
  font-size: 18px;
}
#btns {
  text-align: center;
  margin-top: 50px;
  margin-bottom: 50px;
  padding-bottom: 5%;
}
#context-type {
  width: 100%;
  height: 80%;
  border-radius: 3px;
  border: 1px solid black;
}
#btns button {
  margin-left: 40px;
  margin-right: 40px;
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
  background-color: white;
}
#btns button:hover {
  background-color: #1079cf;
  color: white;
}

/* ---- showComponents ---- */
/* #showComponents {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
}
@media screen and (max-width: 800px) {
  #section {
    width: 100%;
  }
} */

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
  margin-top: 180px;
}
</style>
