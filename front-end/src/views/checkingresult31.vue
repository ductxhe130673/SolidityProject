<template>
  <div class="container">
    <div id="header">Checking Result</div>
    <div class="main">
      <div class="content" style="white-space: pre-line">{{ done_result }}</div>
    </div>

    <div class="button">
      <div class="container">
        <div class="row up">
          <div class="col-7">
            <button
              type="button"
              class="btn btn-outline-primary"
              @click="routing('checkIM')"
            >
              Checking with the same LTL properties and different configurations
            </button>
          </div>
          <div class="col-4 right">
            <button
              type="button"
              class="btn btn-outline-primary"
              @click="routing('checkLTL')"
            >
              Checking with different LTL properties
            </button>
          </div>
        </div>

        <div class="row">
          <div class="col-5">
            <button
              type="button"
              class="btn btn-outline-primary"
              @click="routing('checkNew')"
            >
              Start a new checking session
            </button>
          </div>
          <div class="col-6 right">
            <button
              type="button"
              class="btn btn-outline-primary"
              @click="routing('back')"
            >
              Back
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    done_result() {
      return this.$store.getters.Getrs;
    },
  },
  methods: {
    routing(param) {
      if (param == "back") {
        this.$router.push({ name: "CheckSmartContract" });
        this.$store.commit("setIndex", 5);
      }
      if (param == "checkLTL") {
        this.$router.push({ name: "LTLCheckOption" });
        this.$store.commit("setIndex", 4);
      }
      if (param == "checkIM") {
        this.$router.push({ name: "Initial" });
        this.$store.commit("setIndex", 4);
      }
      if (param == "checkNew") {
        this.$store.commit("ResetState");
        this.$router.push({ name: "SelectSmartContract" });
        this.$store.commit("setIndex", 2);
      }
    },
  },
};
</script>

<style>
#header {
  text-align: center;
  font-weight: bolder;
  font-size: 30px;
  margin-bottom: 5%;
  margin-top: 2%;
  color: black;
}

.main {
  display: flex;
  justify-content: center;
}
.content {
  overflow: scroll;
  width: 100%;
  border: 1px solid black;
  height: 300px;
  font-weight: bolder;
  margin-bottom: 3%;
}
.buttonGroup {
  padding-top: 2%;
  display: flex;
  width: 90%;
  justify-content: space-between;
  margin: 0 auto;
}
.buttonGroup1 {
  padding-top: 2%;
  display: flex;
  width: 90%;
  justify-content: space-between;
  margin: 0 auto;
  padding-bottom: 8%;
}
</style>
