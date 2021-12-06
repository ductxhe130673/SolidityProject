<template>
  <div class="container-fluid">
    <!-- btn delete -->
    <div id="showConfirmation" v-if="showConfirmation">
      <div id="removeSC-holder">
        <confirm @cancel="closeConfirm" @confirm="deleteVul" :dialog="alertDialog" />
      </div>
    </div>

    <div class="row align-items-md-center">
      <div class="col-2">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="" class="link-primary text-decoration-underline">LTL</a></span
        >
      </div>
      <div class="col-8 text-center"><h1>LTL Property Template List</h1></div>
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
              <option value="type0">CSP</option>
              <option value="type1">Vulnerability</option>
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
              <th>
                <span
                  ><a-icon id="icon" type="caret-up" /><a-icon
                    id="icon"
                    type="caret-down"
                /></span>
              </th>
            </tr>
          </thead>
          <tr v-for="(data, index) in filterlist" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ data.name }}</td>
            <td>{{ data.template_type }}</td>
            <td>{{ data.createdDate }}</td>
            <td>{{ data.description }}</td>
            <td class="align-items">
              <span class="col" id="btn">
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="editVul(data.lteid)"
                >
                  Edit
                </button>
                <button
                  type="button"
                  class="btn btn-outline-primary"
                  @click="deleteVul(data.lteid)"
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
          @click="goAdd()"
        >
          Add
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { GetAllltltemplates, DeleteLtlTemplate } from "../../services/data";
import ConfirmationDialog from "../../components/ConfirmationDialog.vue";
import moment from "moment";
export default {
  components: { confirm: ConfirmationDialog },
  data() {
    return {
      dateFormat: "DD/MM/YYYY",
      selected: "0",
      showConfirmation: false,
      alertDialog: {},
      list_vuls: [],
    };
  },
  mounted() {
    this.initData();
  },
  computed: {
    filterlist() {
      const { selected } = this;
      if (selected === "0") return this.list_vuls;
      var items = [];
      this.list_vuls.forEach(function (item) {
        if (item.template_type === selected) {
          items.push(item);
        }
      });
      return items;
    },
  },
  methods: {
    moment,
    async initData() {
      this.list_vuls = await GetAllltltemplates();
    },
    async deleteLtlTemplate(id) {
      await DeleteLtlTemplate(id);
    },
    goAdd() {
      this.$router.push({
        name: "AddVul",
        params: { parent_path: "/list-vul" },
      });
      console.log("list_vuls", this.list_vuls);
    },
    editVul(id) {
      this.$router.push({
        name: "EditVul",
        params: { vul_id: id, parent_path: "/list-vul" },
      });
      this.$store.commit("setIsEditFormula", true);
    },
    deleteVul(id) {
      if (confirm("Do you want to delete the LTLTemplate out of the system?") === true) {
        this.deleteLtlTemplate(id);
        this.$router.go(0);
      }
    },
    closeConfirm() {
      this.showConfirmation = false;
    },
    // async deleteVul(id) {
    //   if (!confirm(`Do you want to delete LTL `)) {
    //     return;
    //   }
    //   const response = await DeleteLtl(id);
    //   if (response.status === 200) {
    //     await this.initData();
    //   }
    //   for (var i = 0; i < this.list_vuls.length; i++) {
    //     if (this.list_vuls[i].id == id) {
    //       this.list_vuls.splice(i, 1);
    //       break;
    //     }
    //   }
    // },
  },
  created() {
    //this.list_vuls = {function to get vulnerabilities from DB}
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
