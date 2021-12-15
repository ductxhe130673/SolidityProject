<template>
  <div class="container">
    <div class="row">
      <h1 class="text-center">Select smart contracts</h1>
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
              Smart Contract Name<span
                ><a-icon id="icon" type="caret-up" /><a-icon
                  id="icon"
                  type="caret-down"
              /></span>
            </th>
            <th>Select</th>
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
  width: 70%;
  border-collapse: collapse;
  margin: 0 auto;
}

table td,
table th {
  border: 1px solid #ddd;
  padding: 5px;
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
