<template>
  <div class="container">
    <div class="row">
      <h1 class="text-center">Select smart contracts</h1>
    </div>
    <div class="row">
      <table class="table table-sm">
        <thead>
          <tr>
            <th style="width :10%">
              #
            </th>

            <th>
              Smart Contract Name
            </th>
            <th style="width :15%">Select</th>
          </tr>
        </thead>

        <tr v-for="(item, index) in filterlist" :key="item.id">
          <td>{{ index + 1 }}</td>
          <td>{{ item.name }}</td>
          <td>
            <input
              class="form-check-input"
              type="checkbox"
              v-model="checkedNames"
              :value="item"
            />
          </td>
        </tr>
      </table>
  
    </div>
    <div id="action">
      <div
        type="button"
        class="btn btn-outline-primary"
        @click="routing('next')"
      >
        Next
      </div>
      <div
        type="button"
        class="btn btn-outline-primary"
        @click="routing('back')"
      >
        Back
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      checkedNames: [],
    };
  },
  mounted() {
    this.checkedNames = this.$store.state.data.data.selectedSc;
  },

  methods: {
    routing(param) {
      if (param == "back") {
        this.$router.push({ name: "GenaralVulSetting" });
        this.$store.commit("setIndex", 4);
      }
      if (param == "next") {
        this.$store.commit("SetSelectedSC", this.checkedNames);
        this.$router.push({ name: "Initial" });
        this.$store.commit("setIndex", 4);
      }
    },
    ...mapActions(["setListSmartContract"]),
  },
  created() {
    this.setListSmartContract();
  },
  computed: {
    ...mapGetters(["getlistSmartContract"]),
    filterlist() {
      return this.getlistSmartContract;
    },
  },
};
</script>
<style scoped>
h1{
  font-size: 35px;
  font-weight: bold;
}
.row {
  margin-top: 2%;
  padding-right: 10px;
}
/* button */
#action {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 50%;
}
/* table  */
table {
  width: 100%;
  margin: 0 auto;
}

table td,
table th {
  padding: 6px;
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
  color: #3a7694;
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  text-indent: inherit;
}
/* icon */
table span {
  float: right;
  display: block;
}
#icon {
  display: block;
  height: 8px;
}
/* checkbox */
input {
  margin: 7px;
}
</style>
