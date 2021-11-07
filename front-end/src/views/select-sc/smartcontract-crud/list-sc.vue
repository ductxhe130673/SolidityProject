<template>
  <div class="container-fluid">
    <!-- btn delete -->
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirm"
          @confirm="deleteSC()"
          :dialog="alertDialog"
        />
      </div>
    </div>
    <!-- btn accept -->
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirm"
          @confirm="acceptSC()"
          :dialog="acceptDialog"
        />
      </div>
    </div>
    <!-- btn refuse  -->
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirm"
          @confirm="refuseSC()"
          :dialog="alertDialog"
        />
      </div>
    </div>
    <div class="row align-items-md-center">
      <div class="col-3 ">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
           <a href="" class="link-primary text-decoration-underline">Smart Contract</a> >
          <a>List</a></span
        >
      </div>
      <div class="col-7 text-center"><h1>Smart Contracts List</h1></div>
    </div>
    <div class="container">
    <div class="row">
      <div class="col">
        <p>Date</p>
        <a-date-picker
          :default-value="moment('01/01/2021', dateFormat)"
          :format="dateFormat"
        />
      </div>
      <div class="col"></div>
      <div class="col"></div>
      <div class="col"></div>

      <div class="col">
        <p>Type</p>
        <div class="input-group mb-3">
          <select class="form-select" id="inputGroup" v-model="selected">
            <option value="common" v-if="isAdmin">Common</option>
            <option value="private">Private</option>
            <option value="pending">Pending</option>
          </select>
        </div>
      </div>
    </div>
    <div class="row">
      <table class="table table-sm">
        <thead>
          <tr>
            <th>
              #
              <span
                ><a-icon id="icon" type="caret-up" />
                <a-icon id="icon" type="caret-down" />
              </span>
            </th>

            <th>
              Name<span
                ><a-icon id="icon" type="caret-up" /><a-icon
                  id="icon"
                  type="caret-down"
              /></span>
            </th>
            <th>
              Type<span
                ><a-icon id="icon" type="caret-up" /><a-icon
                  id="icon"
                  type="caret-down"
              /></span>
            </th>
            <th>
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
        <tr v-for="data in datatable" :key="data.id">
          <td>{{ data.id }}</td>
          <td>{{ data.name }}</td>
          <td>{{ data.type }}</td>
          <td>{{ data.date }}</td>
          <td class="align-items">
             {{ data.description }}
            <span class="col" id="btn"> 
              <button type="button" class="btn btn-outline-primary" @click="editSC()">
                Edit
              </button>
              <button
                type="button"
                class="btn btn-outline-primary"
                @click="deleteSC"
              >
                Delete
              </button>
              <button
                type="button"
                class="btn btn-outline-primary"
                @click="acceptSC()"
                v-if="isAdmin"
              >
                Accept
              </button>
              <button
                type="button"
                class="btn btn-outline-primary"
                @click="refuseSC()"
                v-if="isAdmin"
              >
                Refuse
              </button></span
            >
          </td>
        </tr>
      </table>
    </div>
    <div class="row">
      <button
        style="width: 50px"
        type="button"
        class="btn btn-outline-primary"
        @click="addSmartContract()"
      >
        Add
      </button>
    </div>
  </div>
  </div>
  <!-- 
    <div id="amsb-footer">
      <div id="itb-entries">Show {{ numOfRecod }}/{{ numOfItems }} entries</div>
      <div id="itb-cnpage">
        <i class="material-icons" id="itb-first-page-icon" @click="goPage(1)"
          >first_page</i
        >
        <i
          class="material-icons"
          id="itb-pre-page-icon"
          @click="goPage(pageNum > 1 ? pageNum - 1 : 1)"
          >chevron_left</i
        >
        <div id="itb-cnpage-count">{{ countPageNum }}</div>
        <i
          class="material-icons"
          id="itb-next-page-icon"
          @click="goPage(pageNum < numOfPage ? pageNum + 1 : numOfPage)"
          >chevron_right</i
        >
        <i
          class="material-icons"
          id="itb-last-page-icon"
          @click="goPage(numOfPage)"
          >last_page</i
        >
      </div>
    </div>
   -->
</template>

<script>
import {
  GetCommonSmartContracts,
  GetPendingSmartContracts,
  GetPrivateSmartContracts,
  // DeleteSmartContracts,
  AcceptPendingSmartContracts,
} from "../../../services/data";
import moment from "moment";
import ConfirmationDialog from "../../../components/ConfirmationDialog.vue";
export default {
  components: { confirm: ConfirmationDialog },
  data() {
    return {
      datatable: [
        {
          id: "1",
          name: "EtherGame",
          type: "pending",
          date: "20/11/2021",
          description: "This is a smart contract about auction ",
        },
        {
          id: "2",
          name: "AtherGame",
          type: "pending",
          date: "5/11/2021",
          description: "This is a smart contract about auction",
        },
        {
          id: "3",
          name: "CtherGame",
          type: "pending",
          date: "2/11/2021",
          description: "This is a smart contract about auction",
        },
      ],
      dateFormat: "DD/MM/YYYY",
      selected: "pending",
      num_of_record: 7,
      num_of_page: 0,
      pageNum: 1,
      showConfirmation: false,
      alertDialog: {},
      scDelete: null,
      isAdmin : true,
    };
  },
  mounted() {
    this.fetchData();
    // this.list_smart_contracts.common = GetCommonSmartContracts();
    // this.list_smart_contracts.private = GetPrivateSmartContracts();
    // this.list_smart_contracts.pending = GetPendingSmartContracts();
  },
  computed: {
    // GetTableName() {
    //   if (this.chosen_table == "common") {
    //     return "Common Smart Contracts";
    //   }
    //   if (this.chosen_table == "private") {
    //     return "Private Smart Contracts";
    //   }
    //   if (this.chosen_table == "pending") {
    //     return "Pending Smart Contracts";
    //   }
    //   return "Invalid Table";
    // },
    // showAddButton() {
    //   return (
    //     this.chosen_table != "pending" &&
    //     (this.chosen_table != "common" ||
    //       this.$store.state.user.currentUser.role == "admin")
    //   );
    // },
    isSuperior() {
      return this.$store.state.user.currentUser.role == "admin";
    },
    getShowList() {
      let ret = [];
      for (
        let i = 0;
        i < this.list_smart_contracts[this.chosen_table].length;
        i++
      ) {
        if (
          (this.pageNum - 1) * this.num_of_record <= i &&
          this.pageNum * this.num_of_record > i
        ) {
          ret.push(this.list_smart_contracts[this.chosen_table][i]);
        }
      }
      return ret;
    },
    countPageNum() {
      return "" + this.pageNum + "/" + this.numOfPage;
    },
    numOfItems() {
      return this.list_smart_contracts[this.chosen_table].length;
    },
    numOfRecod() {
      if (
        this.list_smart_contracts[this.chosen_table].length <
        this.num_of_record * this.pageNum
      ) {
        return (
          this.list_smart_contracts[this.chosen_table].length -
          this.num_of_record * (this.pageNum - 1)
        );
      }
      return this.num_of_record;
    },
    numOfPage() {
      return Math.ceil(this.numOfItems / this.num_of_record);
    },
  },
  methods: {
    moment,

    // get common contracts
    async fetchData() {
      console.log("Lay Data");
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
    ChooseTable(value) {
      this.chosen_table = value;
      this.fetchData();
    },
    addSmartContract() {
      this.$router.push({
        name: "AddSc",
        params: { options: this.chosen_table, parent_path: "/list-sc" },
      });
    },

    deleteSC() {
      this.alertDialog = {
        title: "Alert",
        message: "Do you want to delete the Smart Contract out of the system?",
        confirmbtn: "Yes",
      };
      this.showConfirmation = true;
    },
    acceptSC() {
      this.alertDialog = {
        title: "Alert",
        message:
          "Do you want to change the Smart Contract type from Private to Common?",
        confirmbtn: "Yes",
      };
      this.showConfirmation = true;
    },
    refuseSC() {
      this.alertDialog = {
        title: "Alert",
        message: "Are you sure to refuse the change from Private to Common?",
        confirmbtn: "Yes",
      };
      this.showConfirmation = true;
    },

    // deleteSC(sc_id, sc_name, option) {
    //   this.deleteDialog = {
    //     title: "Delete Smart Contract",
    //     message:
    //       "Do you sure to delete the Smart Contract out of the system?",
    //     confirmbtn: "Yes",
    //   };
    //   this.showConfirmation = true;
    //   this.scDelete = { sc_id: sc_id, option: option };
    // },
    // cfDeleteSC() {
    //   let sc_id = this.scDelete.sc_id;
    //   let option = this.scDelete.option;
    //   DeleteSmartContracts(sc_id, option);
    //   if (option == "common") {
    //     let list_smart_contracts_afterdelete =
    //       this.list_smart_contracts.common.filter((i) => {
    //         return i.id != sc_id;
    //       });
    //     this.list_smart_contracts.common = list_smart_contracts_afterdelete;
    //   } else if (option == "private") {
    //     let list_smart_contracts_afterdelete =
    //       this.list_smart_contracts.private.filter((i) => {
    //         return i.id != sc_id;
    //       });
    //     this.list_smart_contracts.private = list_smart_contracts_afterdelete;
    //   } else if (option == "pending") {
    //     let list_smart_contracts_afterdelete =
    //       this.list_smart_contracts.pending.filter((i) => {
    //         return i.id != sc_id;
    //       });
    //     this.list_smart_contracts.pending = list_smart_contracts_afterdelete;
    //   }

    //   // this.fetchData();
    //   this.closeConfirm();
    // },

    closeConfirm() {
      this.showConfirmation = false;
    },
    editSC(sc_id, sc_name, sc_code) {
      this.$router.push({
        name: "EditSc",
        params: {
          sc_id: sc_id,
          name: sc_name,
          code: sc_code,
          parent_path: "/list-sc",
        },
      });
    },
    acceptPendingSC(sc_id, sc_name, sc_code) {
      if (
        confirm(
          "Are you sure to accept the pending Smart Contract named: '" +
            sc_name +
            "' ?"
        )
      ) {
        AcceptPendingSmartContracts(sc_id, sc_name, sc_code);

        this.fetchData();
      }
    },
    goPage(value) {
      this.pageNum = value;
    },
  },
  watch: {
    chosen_table: function () {
      this.pageNum = 1;
    },
  },
};
</script>

<style scoped>
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
button {
  margin-right: 5px;
  margin-top: 5px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
table td,
table th {
  padding: 8px;
  border: 1px solid #ddd;
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
#btn{
  text-align: right;
 
}
/* --- box --- */
.chosen_box {
  background-color: #e4ecfa;
}
/* ---- amsb-footer ---- */
#amsb-footer {
  width: 100%;
  height: 50px;
  border-bottom-right-radius: 4px;
  border-bottom-left-radius: 4px;
  display: flex;
}

#itb-entries {
  font-size: 14px;
  margin-top: 10px;
  margin-left: 2%;
}
#itb-cnpage {
  margin-left: auto;
  order: 2;
  margin-top: 10px;
  margin-right: 2%;
  display: flex;
}

#itb-cnpage i {
  margin-top: 1px;
  font-size: 22px;
  color: #636262;
  cursor: pointer;
}
#itb-cnpage i:hover {
  color: #424141;
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