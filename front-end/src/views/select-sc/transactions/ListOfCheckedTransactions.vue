<template>
  <div id="main">
    <div id="header">
      <h1>Checked Smart Contract List</h1>
    </div>
    <div class="blue">
      <div class="atable">
        <table class="table table-striped table-hover table-sm">
          <thead class="table-inside">
            <tr>
              <th style="width: 10%" scope="col">#</th>
              <th style="width: 30%" scope="col">Checker</th>
              <th style="width: 25%" scope="col">Checked Date</th>
              <th style="width: 35%" scope="col">Number of smart contracts</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in getListTransaction" v-bind:key="index">
              <th scope="row">{{ index + 1 }}</th>
              <td>
                <div v-on:click="set(item.bid)" v-bind:id="item.bid">
                  <router-link
                    :to="{ path: 'checking-result', query: { id: item[0] } }"
                    tag="a"
                    class="lk"
                    >{{ item[1] + " " + item[2] }}</router-link
                  >
                </div>
              </td>
              <td>{{ item[3] }}</td>
              <td>{{ item[4] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div id="processing-btn">
      <div class="pr-button" @click="routing('addsc')">
        Start a new checking session
      </div>
      <div class="pr-button" @click="routing('back')">
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
      info: [],
      id: null,
    };
  },
  methods: {
    routing(param) {
      if (param == "next") {
        this.$router.push({ name: "CheckRentrancy" });
      }
      if (param == "addsc") {
        this.$router.push({ name: "SelectSmartContract" });
        this.$store.commit("setIndex", 2);
      }
      if (param == "back") {
        this.$router.push({ name: "Index" });
        this.$store.commit("setIndex", 0);
      }
    },
    ...mapActions(["getListTran", "setid"]),
    set(data) {
      this.setid(data);
    },
  },
  computed: {
    ...mapGetters(["getListTransaction", "getid"]),
  },
  created() {
    this.getListTran();
  },
};
</script>

<style scoped>
#main {
  padding-bottom: 10%;
  font-family: Arial, Helvetica, sans-serif;
}
#header {
  text-align: center;
  margin-bottom: 2%;
  margin-top: 2%;
}
h1 {
  text-align: center;
  font-size: 35px;
  font-weight: bold;
}
.table-inside {
  background-color: #d9edf7;
  color: #3a7694;
}
.blue {
  border-radius: 10px;
  width: 80%;
  text-align: center;
  margin-left: 10%;
  margin-right: 30%;
  height: 470px;
  color: black;
}
.blue {
  border: 1px solid #d9edf7;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
  margin-top: -40px;
  background: none;
  margin-top: 65px;
  z-index: 2;
  position: relative;
}
.atable {
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
  margin-left: 50px;
  margin-top: 50px;
  margin-right: 50px;
  padding-bottom: 15%;
  border: 1px solid #d9edf7;
  border-radius: 10px;
}
/* button */
#processing-btn{
  width: 60%;
  height: 120px;
  margin-left: 20%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#processing-btn .pr-button {
  cursor: pointer;
  width: 20%;
  height: 30px;
  border: 1px solid #2196f3;
  text-align: center;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  padding-top: 4px;
  border-radius: 4px;
}
#processing-btn .pr-button:hover {
  background-color: #1079cf;
  color: white;
}
.btn{
  margin: 0 3%;
}
a {
  text-decoration: none;
  color: black;
}
a:hover {
  color: red;
  text-decoration: underline red wavy;
}
</style>
