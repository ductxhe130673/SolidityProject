<template>
  <div id="main" class="container">
    <div id="header">
      <h1>Select Smart Contracts</h1>
    </div>

    <div class="row type">
      <div class="col"></div>
      <div class="col"></div>
      <div class="col">
        <div class="input-group mb-3">
          <label class="input-group-text" for="inputGroupSelect01">Type</label>
          <select class="form-select" id="inputGroup" v-model="selected">
            <option value="0">All</option>
            <option value="common">Common</option>
            <option value="private">Private</option>
            <option value="pending">Pending</option>
          </select>
        </div>
      </div>
    </div>
    <table class="table table-striped table-hover table-sm">
      <thead class="table-inside">
        <tr>
          <th style="width: 10%" scope="col">#</th>
          <th style="width: 40%" scope="col">Name</th>
          <th style="width: 30%" scope="col">Type</th>
          <th style="width: 20%" scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in filterlist" v-bind:key="index">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ item.name }}</td>
          <td>{{ item.type }}</td>
          <td>
            <input
              type="checkbox"
              id="one"
              name="ch"
              v-model="checkedNames"
              :value="item"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <div id="action">
      <div id="btn" @click="funtionNext()">Next</div>
      <div id="btn" @click="upLoad">Upload Smart Contract</div>
      <div id="btn" @click="routing('back')">Back</div>
    </div>

    <!-- <popup v-bind:isOpen="isOpen" v-on:clickdahieu="dahieu" /> -->
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirm"
          @confirm="routing('uploadfile')"
          :dialog="upLoadDialog"
        />
      </div>
    </div>
  </div>
</template>

<script>
// import Popup from "./Popup.vue";
import { mapActions, mapGetters } from "vuex";
import UpLoadFile from "../../../components/UpLoadFile.vue";
export default {
  data() {
    return {
      selected: "0",
      isOpen: false,
      info: null,
      checkedNames: [],
      isAdmin: true,
      showConfirmation: false,
      upLoadDialog: {},
    };
  },
  mounted() {
    this.checkedNames = this.$store.state.data.data.selectedSc;
    this.isAdmin =
      JSON.parse(localStorage.getItem("user")).role === "admin" ? true : false;
    this.checkIsUser();
  },
  methods: {
    upLoad() {
      this.upLoadDialog = {
        title: "Choose a new Smart Contract file",
        confirmbtn: "OK",
      };
      this.showConfirmation = true;
    },
    closeConfirm() {
      this.showConfirmation = false;
    },
    routing(param) {
      if (param == "add") {
        this.$store.commit("SetSelectedSC", this.checkedNames);
        this.$router.push({ name: "ContextOfSmartContract" });
        this.$store.commit("setIndex", 3);
      }
      if (param == "back") {
        this.$router.push({ name: "ListOfCheckedTransactions" });
        this.$store.commit("setIndex", 1);
      }
      if (param == "uploadfile") {
        this.$router.push({ name: "UpLoadSc" });
      }
    },
    funtionNext() {
      var checkbox = document.getElementsByName("ch");
      var kt = false;
      for (var i = 0; i < checkbox.length; i++) {
        if (checkbox[i].checked === true) {
          kt = true;
          break;
        }
      }

      if (!kt) {
        alert("Please select a smart contract at least to go to the next step!");
      } else {
        this.routing("add");
      }
    },
    load() {
      this.isOpen = true;
    },
    dahieu() {
      this.isOpen = false;
    },
    ...mapActions(["setListSmartContract"]),
  },
  created() {
    this.setListSmartContract();
  },
  computed: {
    ...mapGetters(["getlistSmartContract"]),
    filterlist() {
      const { selected } = this;
      if (selected === "0") return this.getlistSmartContract;
      var items = [];
      this.getlistSmartContract.forEach(function (item) {
        if (item.type === selected) {
          items.push(item);
        }
      });
      return items;
    },
    // return k;
  },
  components: {
    // Popup,
    confirm: UpLoadFile,
  },
};
</script>

<style scoped>
.main {
  font-family: Arial, Helvetica, sans-serif;
}
#header {
  text-align: center;
  margin-bottom: 7%;
  margin-top: 2%;
}
.table-inside {
  background-color: #d9edf7;
  color: #3a7694;
}
table td,
table th {
  padding: 6px;
}
h1 {
  text-align: center;
  font-size: 35px;
  font-weight: bold;
}

.atable {
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
  margin-top: 40px;
  padding-bottom: 5%;
  border: 1px solid #d9edf7;
  border-radius: 10px;
}
#btn {
  cursor: pointer;
  width: 18%;
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
#btn:hover {
  background-color: #1079cf;
  color: white;
}

#action {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 70%;
}

div#main {
  padding-bottom: 3%;
}

.type {
  margin-top: 50px;
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
</style>
