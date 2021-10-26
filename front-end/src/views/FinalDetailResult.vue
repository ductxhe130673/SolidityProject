<template>
  <div class="container-fluid">
    <h1>Checking Result</h1>
    <div class="textArea">
      <a-textarea
        v-model="value"
        :auto-size="{ minRows: 10, maxRows: 6 }"
        readonly
      />
    </div>

    <div id="action">
      <button type="button" class="btn btn-outline-primary" @click="routing('checkconfig')">
        Checking with the same LTL property and different configuration
      </button>
      <button type="button" class="btn btn-outline-primary" @click="routing('checkproperty')">
        Checking with different LTL property
      </button>
    </div>
    <div id="action">
      <button type="button" class="btn btn-outline-primary" @click="routing('start')">
        Start a new checking session
      </button>
      <button type="button" class="btn btn-outline-primary"  @click="routing('back')">Back</button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      value: "hihi",
    };
  },
  methods:{
    routing(param){
      if(param == "back"){
         this.$router.push({ name: "CheckSmartContractProgress" });
        this.$store.commit("setIndex", 6); 
      }
      else if(param == "checkproperty"){
        this.$router.push({ name: "LTLCheckOption" });
        this.$store.commit("setIndex", 4); 
      }
      else if(param == 'start'){
        this.$router.push({ name: "SelectSmartContract" });
        this.$store.commit("setIndex", 2); 
      }
      else if(param == 'checkconfig'){
        this.$router.push({ name: "" });
        // this.$store.commit("setIndex", ); 
      }
    }
  }
};
</script>

<style scoped>
h1 {
  text-align: center;
  padding: 50px;
}
.textArea {
  margin: auto;
  width: 60%;
}
#action {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 80%;
}
</style>
