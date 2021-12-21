<template>
  <div id="addsc">
    <div class="header">
      <div class="title"><h1>Upload a new Smart Contract code</h1></div>
    </div>
    <div class="body">
      <div class="name-area area">
        <h2 class="label">Name</h2>
        <input class="input-name input-type" type="text" v-model="nameSC" />
      </div>
      <div class="type-area area">
        <div class="label">Smart Contract Type</div>
        <div class="option input-type">
          <fieldset id="group1">
            <input
              type="radio"
              v-model="selectOption"
              class="radio"
              name="group1"
              value="common"
              :disabled="!isSuperior"
            />Common
            <input
              type="radio"
              v-model="selectOption"
              class="radio"
              name="group1"
              value="pending"
            />Pending
            <input
              type="radio"
              v-model="selectOption"
              class="radio"
              name="group1"
              value="private"
            />Private
          </fieldset>
        </div>
        <div class="option input-type" v-if="author === 'admin'">
          <select name="" id="type-select">
            <option value="">Private</option>
            <option value="">Common</option>
          </select>
        </div>
      </div>
      <div class="editor-area area">
        <ace-editor v-bind:codeSC="demoEditSC" @changeSC="updateContent($event)" />
      </div>
      <div class="button-area area">
        <div class="button-add-cancell">
          <button id="button-add" type="button" @click="clickHandler('save')">
            Save
          </button>
          <button id="button-cancel" type="button" @click="clickHandler('cancel')">
            Cancel
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import { AddNewSmartContracts } from "../../../services/data";
import AceEditor from "../../../components/AceEditor.vue";
export default {
  data() {
    return {
      selectOption: "",
      demoEditSC: this.$store.state.data.contentFile,
      dateFormat: "",
      nameSC: "",
    };
  },
  components: { AceEditor },
  mounted() {
    this.getData();
    console.log("this.$store.state.data.contentFile", this.$store.state.data.contentFile);
  },
  methods: {
    updateContent(value) {
      this.demoEditSC = value;
    },
    getData() {
      this.dateFormat = moment().format("YYYY-MM-DD");
      this.demoEditSC = this.$store.state.data.contentFile;
    },
    async clickHandler(action) {
      if (action == "save") {
        if (this.nameSc === "" || this.demoEditSC === "" || this.selectOption === "") {
          window.alert("Please input all field");
        } else {
          await AddNewSmartContracts(
            this.hashValue(this.nameSc),
            this.nameSC,
            this.selectOption,
            this.demoEditSC,
            this.dateFormat
          );
          this.$router.push({ name: "SelectSmartContract" });
        }
      } else if (action == "cancel") {
        this.$router.push({ name: "SelectSmartContract" });
      }
    },

    computed: {
      isSuperior() {
        return this.$store.state.user.currentUser.role == "admin";
      },
    },
  },
};
</script>

<style scoped>
#type-select {
  width: 300px;
}
.radio {
  width: 30px;
}
.input-type {
  position: absolute;
  top: 0;
  left: 50%;
}
.area {
  margin-bottom: 30px;
  position: relative;
}
.option div {
  display: flex;
  align-items: center;
}
.option {
  width: 250px;
  display: flex;
  /* background-color: red; */
  justify-content: space-between;
}
/* router style */
a.router-link-active {
  color: white;
  text-decoration: none;
}
.body {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#addsc {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}
/* header style */
.title {
  padding-top: 8%;
  margin-bottom: 5%;
}
.title h1 {
  font-size: 35px;
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif;
}
/* name area */
.name-area,
.type-area {
  width: 500px;
}
.label {
  font-style: normal;
  font-size: 15px;
  font-weight: 100;
  position: relative;
  left: 0;
}
.input-name {
  width: 250px;
  border: 1px solid;
  border-radius: 2px;
  overflow: hidden;
}
/* editor area */
.editor-area {
  width: 600px;
  overflow: hidden;
  position: relative;
  left: 40px;
}
/* button style */
.button-add-cancell button {
  width: 130px;
  height: 28px;
  border: 1px solid #2196f3;
  background-color: white;
  text-align: center;
  color: #2196f3;
  border-radius: 4px;
}
.button-add-cancell button:hover {
  opacity: 0.9;
  background-color: #0d6efd;
  color: white;
  cursor: pointer;
}
.button-add-cancell button:active {
  cursor: wait;
}
#button-add {
  margin-right: 20px;
}
.button-add-cancell {
  position: relative;
  left: 40px;
}
input[type="radio"] {
  transform: scale(1.6);
}
label {
  margin-right: 10px;
}
label:hover {
  cursor: pointer;
}
.common-option,
.private-option {
  border: 1px solid rgb(241, 240, 240);
  border-radius: 15px;
  width: 100px;
}
</style>
