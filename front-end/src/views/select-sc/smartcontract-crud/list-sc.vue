<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="" class="link-primary text-decoration-underline">Smart Contract</a>
        </span>
      </div>
      <div class="col-md-7 text-center"><h1>Smart Contracts List</h1></div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md">
          
        </div>
        <div class="col-md"></div>
        <div class="col-md"></div>
        <div class="col-md"></div>

        <div class="col-md">
          <p>Type</p>
          <div class="input-group mb-3">
            <select v-if="isAdmin" class="form-select" id="inputGroup" v-model="selected">
              <option value="common">Common</option>
              <option value="private">Private</option>
              <option value="pending">Pending</option>
            </select>
            <select
              v-if="!isAdmin"
              class="form-select"
              id="inputGroup"
              v-model="selected"
            >
              <option value="private">Private</option>
            </select>
          </div>
        </div>
      </div>
      <div class="row">
        <table class="table table-md">
          <thead id="border-top">
            <tr>
              <th style="width: 5%">#</th>
              <th style="width: 15%">
                Name
              </th>
              <th style="width: 15%">
                Type
              </th>
              <th style="width: 15%">
                Date
              </th>
              <th style="width: 25%">

              </th>
            </tr>
          </thead>
          <tr v-for="(item, index) in filterlist" v-bind:key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.type }}</td>
            <td>{{ item.createdDate }}</td>
            <td class="align-items">
              
              <span class="col" id="btn">
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="
                    editSC(item.sid, item.name, item.content, item.description, item.type)
                  "
                >
                  Edit
                </button>
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="deleteSC(item.sid)"
                >
                  Delete
                </button>
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="acceptSC(item.sid)"
                  v-if="isAdmin && selected=='pending'"
                >
                  Accept
                </button>
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="refuseSC(item.sid)"
                  v-if="isAdmin && selected=='pending'"
                >
                  Refuse
                </button></span
              >
            </td>
          </tr>
        </table>
      </div>
      <div class="row-end">
        <button
          style="width: 60px"
          type="button"
          class="btn btn-outline-primary"
          @click="addSmartContract()"
        >
          Add
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import {
  DeleteSmartContracts,
  AcceptPendingSmartContracts,
  RefusePendingSmartContracts,
} from "../../../services/data";
import moment from "moment";
import { mapActions, mapGetters } from "vuex";
import dateFormat from "dateformat";

export default {
  data() {
    return {
      choose_SC: "",
      selected: "pending",
      isAdmin: true,
      filterDate: null,
      formatDate: "yyyy-mm-dd",
    };
  },
  mounted() {
    //this.fetchData();
    this.isAdmin =
      JSON.parse(localStorage.getItem("user")).role === "admin" ? true : false;
    this.checkIsUser();
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

    isSuperior() {
      return this.$store.state.user.currentUser.role == "admin";
    },
  },
  created() {
    this.setListSmartContract();
  },
  methods: {
    sort(param) {
      switch (param) {
        case "upName":
          this.filterlist.sort((a, b) =>
            a.name.toLowerCase() < b.name.toLowerCase() ? -1 : 1
          );
          break;
        case "downName":
          this.filterlist.sort((a, b) =>
            a.name.toLowerCase() > b.name.toLowerCase() ? -1 : 1
          );
          break;
        case "upType":
          this.filterlist.sort((a, b) =>
            a.type.toLowerCase() < b.type.toLowerCase() ? -1 : 1
          );
          break;
        case "downType":
          this.filterlist.sort((a, b) =>
            a.type.toLowerCase() > b.type.toLowerCase() ? -1 : 1
          );
          break;
        case "upDate":
          this.filterlist.sort((a, b) => (a.createdDate < b.createdDate ? -1 : 1));
          break;
        case "downDate":
          this.filterlist.sort((a, b) => (a.createdDate > b.createdDate ? -1 : 1));
          break;
        case "upDes":
          this.filterlist.sort((a, b) =>
            a.description.toLowerCase() < b.description.toLowerCase() ? -1 : 1
          );

          break;
        case "downDes":
          this.filterlist.sort((a, b) =>
            a.description.toLowerCase() > b.description.toLowerCase() ? -1 : 1
          );

          break;
      }
    },
    checkIsUser() {
      if (!this.isAdmin) {
        this.selected = "private";
      }
    },
    onChangeDate(value) {
      const date = dateFormat(value._d, this.formatDate);
      this.filterDate = date;
    },
    async deleteSmartContract(sid) {
      await DeleteSmartContracts(sid);
    },
    async acceptSmartContract(sid) {
      await AcceptPendingSmartContracts(sid);
    },
    async refuseSmartContract(sid) {
      await RefusePendingSmartContracts(sid);
    },
    moment,
    ...mapActions(["setListSmartContract"]),
    // get common contracts
    // async fetchData() {
    //   this.list_smart_contracts.common = await GetCommonSmartContracts();
    //   this.list_smart_contracts.private = await GetPrivateSmartContracts();
    //   this.list_smart_contracts.pending = await GetPendingSmartContracts();
    // },
    inc(value) {
      return value + 1;
    },
    convertDate(value) {
      var date = new Date(value);
      var datestring = "" + date.getDate();
      var monthstring = "" + (date.getMonth() + 1);
      var hourstring = "" + date.getHours();
      var minutestring = "" + date.getMinutes();
      hourstring = hourstring.length == 1 ? "0" + hourstring : hourstring;
      minutestring = minutestring.length == 1 ? "0" + minutestring : minutestring;
      datestring = datestring.length == 1 ? "0" + datestring : datestring;
      monthstring = monthstring.length == 1 ? "0" + monthstring : monthstring;
      return (
        datestring +
        "/" +
        monthstring +
        "/" +
        date.getFullYear() +
        " " +
        hourstring +
        ":" +
        minutestring
      );
    },
    addSmartContract() {
      this.$router.push({
        name: "AddSc",
        params: { options: this.chosen_table, parent_path: "/list-sc" },
      });
    },

    deleteSC(sc_id) {
      if (
        confirm("Do you want to delete the Smart Contract out of the system?") === true
      ) {
        this.deleteSmartContract(sc_id);
        this.$router.go(0);
      }
    },
    acceptSC(sc_id) {
      if (
        confirm(
          "Do you want to change the Smart Contract type from Pending to Common?"
        ) === true
      ) {
        this.acceptSmartContract(sc_id);
        this.$router.go(0);
      }
    },
    refuseSC(sc_id) {
      if (
        confirm(
          "Do you want to change the Smart Contract type from Pending to Private?"
        ) === true
      ) {
        this.refuseSmartContract(sc_id);
        this.$router.go(0);
      }
    },

    editSC(sc_id, sc_name, sc_code, sc_description, sc_type) {
      this.$router.push({
        name: "EditSc",
        params: {
          sc_id: sc_id,
          name: sc_name,
          code: sc_code,
          description: sc_description,
          type: sc_type,
          parent_path: "/list-sc",
        },
      });
    },
  },
};
</script>

<style scoped>
.container-fluid {
  color: black;
}
h1 {
  font-size: 50px;
}
.align-items {
  display: flex;
  align-items: center;
}
.row {
  padding-top: 2%;
  padding-right: 10px;
}
.row-end {
  padding-top: 2%;
  padding-bottom: 5%;
}
button {
  margin-right: 5px;
  margin-top: 5px;
}
table {
  width: 100%;
}

table td,
table th {
  padding-left: 5px;
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
#btn {
  text-align: right;
}
</style>
