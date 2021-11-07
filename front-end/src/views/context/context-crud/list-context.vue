<template>
  <div class="container-fluid">
    <!-- btn delete -->
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm
          @cancel="closeConfirm"
          @confirm="deleteC()"
          :dialog="alertDialog"
        />
      </div>
    </div>
    <div class="row align-items-md-center">
      <div class="col-2">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="" class="link-primary text-decoration-underline">Context</a>
          > <a>List</a></span
        >
      </div>
      <div class="col-8 text-center"><h1>Context List</h1></div>
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
              <option value="dcr">DCR</option>
              <option value="cpn">CPN</option>
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
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="editContext"
                >
                  Edit
                </button>
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="deleteC"
                >
                  Delete
                </button>
              </span>
            </td>
          </tr>
        </table>
      </div>
      <div class="row">
        <button
          style="width: 50px"
          type="button"
          class="btn btn-outline-primary"
          @click="goAdd"
        >
          Add
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
// import { GetContext, DeleteContext } from "../../../services/data";
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
      selected: "dcr",
      showConfirmation: false,
      alertDialog: {},

      // list_context: [],
    };
  },
  mounted() {
    this.initData();
  },
  methods: {
    moment,
    goAdd() {
      this.$router.push({
        name: "AddContext",
        params: { parent_path: "/list-context" },
      });
    },
    editContext(id) {
      this.$router.push({
        name: "EditContext",
        params: { context_id: id, parent_path: "/list-context" },
      });
    },
    deleteC() {
      this.alertDialog = {
        title: "Alert",
        message: "Do you want to delete the Context out of the system?",
        confirmbtn: "Yes",
      };
      this.showConfirmation = true;
    },
    closeConfirm() {
      this.showConfirmation = false;
    },
    // async deleteContext(id,ct_name) {
    //   if(!confirm(`Do you want to delete context ${ct_name}`)){
    //     return
    //   }
    //   const response = await DeleteContext(id);
    //   if (response.status === 200) {
    //       await this.initData()
    //   }
    // },
    // async initData() {
    //   this.list_context = await GetContext();
    // },
  },
  created() {},
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
#btn {
  text-align: right;
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