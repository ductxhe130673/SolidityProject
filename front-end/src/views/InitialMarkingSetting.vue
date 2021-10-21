<template>
  <div class="container">
    <h1><b>Configuration</b></h1>

    <div class="row">
      <div class="col-2 left">Number of users</div>
      <div class="col-10 right">
        <input type="text"
          class="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
          placeholder="5"
        />
      </div>
    </div>
    <div class="radioB">
      <div>
        <input id="radio-1" name="radio" type="radio" checked>
        <label for="radio-1" class="radio-label">Fixed</label>
      </div>
      <div>
        <input id="radio-2" name="radio" type="radio">
        <label  for="radio-2" class="radio-label">Random</label>
      </div>

      <div>
        <input id="radio-3" name="radio" type="radio">
        <label for="radio-3" class="radio-label">Map</label>
      </div>
    </div>

    <div class="row">
      <div class="col-2">Balance</div>
      <div class="col-10">
        <input
          type="text"
          class="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
          placeholder="10"
        />
      </div>
    </div>

    <!-- <div class="row">
      <div class="col-2">Sender value</div>
      <div class="col-10">
        <input
          type="text"
          class="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
        />
      </div>
    </div> -->

    <div class="row" id="textbox">
      <div class="col-2">Function parameters</div>
      <div class="col-10 ">
        <textarea class="form-control" aria-label="With textarea"></textarea>
      </div>
    </div>

    <div id="btn-group">
      <button class="btn btn-outline-primary btn-sm" @click="routing('save')">
        Next
      </button>
      <button
        class="btn btn btn-outline-primary btn-sm"
        type="button"
        @click="routing('back')"
      >
        Back
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    routing(param) {
      if (param == "save") {
        this.$router.push({ name: "CheckSmartContract" });
      }
      if (param == "back") {
        this.$router.push({ name: "CSPSettingType" });
      }
    },
  },
};
</script>
<style scoped>
textarea{
  padding-bottom: 15%;
}

h1 {
  padding-top: 35px;
  padding-bottom: 25px;
  text-align: center;
}
.container {
  width: 60%;
}
.left {
  font-size: 20px;
}
.col-2 {
  font-size: 20px;
}
.row {
  margin-top: 30px;
  margin-bottom: 30px;
}

.radioB{
  display: flex;
  margin-left: 15%;
}
label{
  margin: 0.5rem;
}

.text {
  height: 200px;
}
#btn-group {
  width: 100%;
  display: flex;
  margin-left: 4%;
  padding-bottom: 7%;
}
button {
  margin: auto;
  margin-top: 40px;
  cursor: pointer;
  width: 15%;
  height: 2%;
  border: 1px solid #2196f3;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
}
</style>