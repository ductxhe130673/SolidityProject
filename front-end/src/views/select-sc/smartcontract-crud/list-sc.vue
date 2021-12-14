<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="" class="link-primary text-decoration-underline"
            >Smart Contract</a
          >
          >
          <a>List</a>
        </span>
      </div>
      <div class="col-md-7 text-center"><h1>Smart Contracts List</h1></div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md">
          <p>Date</p>
          <a-date-picker
            :default-value="moment('2021/12/01', dateFormat)"
            @change="onChangeDate"
          />
        </div>
        <div class="col-md"></div>
        <div class="col-md"></div>
        <div class="col-md"></div>

        <div class="col-md">
          <p>Type</p>
          <div class="input-group mb-3">
            <select
              v-if="isAdmin"
              class="form-select"
              id="inputGroup"
              v-model="selected"
            >
              <option value="0">All</option>
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
          <thead>
            <tr>
              <th style="width: 5%">
                #
                <span
                  ><a-icon id="icon" type="caret-up" />
                  <a-icon id="icon" type="caret-down" />
                </span>
              </th>

              <th style="width: 15%">
                Name<span
                  ><a-icon id="icon" type="caret-up" /><a-icon
                    id="icon"
                    type="caret-down"
                /></span>
              </th>
              <th style="width: 15%">
                Type<span
                  ><a-icon id="icon" type="caret-up" /><a-icon
                    id="icon"
                    type="caret-down"
                /></span>
              </th>
              <th style="width: 15%">
                Date<span
                  ><a-icon id="icon" type="caret-up" /><a-icon
                    id="icon"
                    type="caret-down"
                /></span>
              </th>
              <th style="width: 50%">
                Description<span
                  ><a-icon id="icon" type="caret-up" /><a-icon
                    id="icon"
                    type="caret-down"
                /></span>
              </th>
            </tr>
          </thead>
          <tr v-for="(item, index) in filterlist" v-bind:key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.type }}</td>
            <td>{{ item.createdDate }}</td>
            <td class="align-items">
              {{ item.description }}
              <span class="col" id="btn">
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="
                    editSC(
                      item.sid,
                      item.name,
                      item.content,
                      item.description,
                      item.type
                    )
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
                  v-if="isAdmin"
                >
                  Accept
                </button>
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="refuseSC(item.sid)"
                  v-if="isAdmin"
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
  GetCommonSmartContracts,
  GetPendingSmartContracts,
  GetPrivateSmartContracts,
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
      selected: "0",
      isAdmin: true,
      filterDate: null,
    };
  },
  mounted() {
    this.fetchData();
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
    async fetchData() {
      this.list_smart_contracts.common = await GetCommonSmartContracts();
      this.list_smart_contracts.private = await GetPrivateSmartContracts();
      this.list_smart_contracts.pending = await GetPendingSmartContracts();
    },
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
      minutestring =
        minutestring.length == 1 ? "0" + minutestring : minutestring;
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
        confirm(
          "Do you want to delete the Smart Contract out of the system?"
        ) === true
      ) {
        this.deleteSmartContract(sc_id);
        this.$router.go(0);
      }
    },
    acceptSC(sc_id) {
      if (
        confirm(
          "Do you want to change the Smart Contract type from Private to Common?"
        ) === true
      ) {
        this.acceptSmartContract(sc_id);
        this.$router.go(0);
      }
    },
    refuseSC(sc_id) {
      if (
        confirm(
          "Do you want to change the Smart Contract type from Common to Private?"
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
.container-fluid{
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
  margin-top: 2%;
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
