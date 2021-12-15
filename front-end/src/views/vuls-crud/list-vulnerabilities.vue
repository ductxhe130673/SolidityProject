<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="" class="link-primary text-decoration-underline"
            >LTL</a
          ></span
        >
        >

        <a>List</a>
      </div>
      <div class="col-md-7 text-center">
        <h1>LTL Property Template List</h1>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md">
          <p>Date</p>
          <a-date-picker :default-value="moment('2021/12/01', dateFormat)" />
        </div>
        <div class="col-md"></div>
        <div class="col-md"></div>
        <div class="col-md"></div>
        <div class="col-md">
          <p>Type</p>
          <div class="input-group mb-3">
            <select class="form-select" id="inputGroup" v-model="selected">
              <option value="0">All</option>
              <option value="type0">CSP</option>
              <option value="type1">Vulnerability</option>
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
                
              </th>

              <th style="width: 15%">
                Name<span
                  ><a-icon id="icon" type="caret-up"  @click="sort('upName')"/><a-icon
                    id="icon"
                    type="caret-down"
                     @click="sort('downName')"
                /></span>
              </th>
              <th style="width: 15%">
                Type<span
                  ><a-icon id="icon" type="caret-up"   @click="sort('upType')"/><a-icon
                    id="icon"
                    type="caret-down"  @click="sort('downType')"
                /></span>
              </th>
              <th style="width: 15%">
                Date<span
                  ><a-icon id="icon" type="caret-up"  @click="sort('upDate')" /><a-icon
                    id="icon"
                    type="caret-down"
                     @click="sort('downDate')"
                /></span>
              </th>
              <th style="width: 50%">
                Description<span
                  ><a-icon
                    id="icon"
                    type="caret-up"
                    @click="sort('upDes')" /><a-icon
                    id="icon"
                    type="caret-down"
                    @click="sort('downDes')"
                /></span>
              </th>
            </tr>
          </thead>
          <tr v-for="(data, index) in filterlist" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ data.name }}</td>
            <td>{{ data.template_type }}</td>
            <td>{{ data.createdDate }}</td>
            <td class="align-items">
              {{ data.description }}
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
      <div class="row-end">
        <button
          style="width: 60px"
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
import moment from "moment";
export default {
  data() {
    return {
      selected: "0",
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
          this.filterlist.sort((a, b) =>
            a.createdDate < b.createdDate ? -1 : 1
          );
          break;
        case "downDate":
          this.filterlist.sort((a, b) =>
            a.createdDate > b.createdDate ? -1 : 1
          );
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
      if (
        confirm("Do you want to delete the LTLTemplate out of the system?") ===
        true
      ) {
        this.deleteLtlTemplate(id);
        this.$router.go(0);
      }
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
