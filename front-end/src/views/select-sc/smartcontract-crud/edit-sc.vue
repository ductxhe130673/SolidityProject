<template>
  <div id="editsc">
    <div class="link">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="http://192.168.1.6:8080/list-sc" class="link-primary text-decoration-underline">Smart Contract</a> >
          <a>Edit</a></span>
    </div>
    <div class="header">
      <div class="title"><h1>Edit the Smart Contract code</h1></div>
    </div>
    <div class="body">
      <div class="name-area area">
        <h2 class="label">Name</h2>
        <input class="input-name input-type" type="text" v-model="nameSc" />
      </div>
      <div class="type-area area">
        <div class="label">Smart Contract Type</div>
        <div class="option input-type" v-if="isAdmin">
          <select class="form-select" id="inputGroupSelect01" v-model="selectOption">
            <option value="common">Common</option>
            <option value="private">Private</option>
            <option value="pending">Pending</option>
          </select>
        </div>
<!-- 
        <div class="option input-type" v-if="!isAdmin">
          <div class="common-option" v-if="isSuperior">
            <input
              class="radio"
              id="common"
              value="common"
              type="radio"
              v-model="selectOption"
            />
            <label for="common">Common</label>
          </div>
          <div class="common-option" v-else>
            <input
              class="radio"
              id="common"
              value="pending"
              type="radio"
              v-model="selectOption"
            />
            <label for="common">Pending</label>
          </div>
          <div class="private-option">
            <input
              class="radio"
              id="private"
              value="private"
              type="radio"
              v-model="selectOption"
            />
            <label for="private">Private</label>
          </div>
        </div> -->


      </div>
      <div class="editor-area area">
        <div class="label">Content</div>
        <div class="AceEditor">
        <ace-editor v-bind:codeSC="demoEditSC" @changeSC="updateContent($event)"/>
        </div>
      </div>
      <div class="description">
        <div class="label">Description</div>
        <textarea cols="30" rows="5" v-model="descriptionSC"></textarea>
      </div>
      <div class="button-area area">
        <div class="button-add-cancell">
          <button id="button-add" type="button" @click="clickHandler('save')">Save</button>
          <button id="button-cancel" type="button" @click="clickHandler('back')">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {UpdateSmartContractCode,GetSmartContractCode,GetSmartContractById} from "../../../services/data"
import AceEditor from '../../../components/AceEditor.vue';
export default {
  components: {AceEditor },
  name: "EditSc",

  data() {
    return {
      sc_id : this.$route.params.sc_id,
      nameSc: this.$route.params.name,
      code: GetSmartContractCode(this.$route.params.sc_code),
      dataCurrent : {},
      demoEditSC: "test edit sc",
      isAdmin: true,
      descriptionSC: '',
      selectOption : '',
    };
  },
  mounted(){
      this.demoEditSC = this.code
      // this.dataCurrent = this.getDataCurrent(sc_id);
      console.log('this.dataCurrent',this.code);
  },

  methods:{
     async getDataCurrent(sc_id){
       await GetSmartContractById(sc_id);
    },
    updateContent(value){
      //console.log(value)
      this.demoEditSC = value;
    },
    async clickHandler(param){
      if(param == "save"){
        // UpdateSmartContractCode(this.$route.params.sc_id, this.code)
        // this.$router.push(this.$route.params.parent_path);
        await UpdateSmartContractCode(this.sc_id, this.nameSc,this.demoEditSC, this.descriptionSC, this.selectOption)
        this.$router.push({
          name:"ListSc"
          })
      }
      if(param == "back"){
        this.$router.push(this.$route.params.parent_path);
      }
    },
  }
};
</script>


<style scoped>
#editsc {
  background-color: rgb(241, 240, 240);
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 115vh;
}
#type-select {
  width: 300px;
}
.title{
  padding-top: 8%;
  margin-bottom: 5%;
}
.title h1{
  font-size: 50px;
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
.option {
  width: 350px;
  display: flex;
  justify-content: space-between;
}
.link{
  margin-right: 85%;
  font-size: 15px;
  margin-top: 20px;
}
/* router style */
a.router-link-active {
  color: white;
  text-decoration: none;
}
.body {
  display: flex;
  flex-direction: column;
  /* align-items: center;
  width: 1000px; */
}
/* header style */
/* name area */
.name-area,
.type-area {
  width: 500px;
}
.description{
  display: flex;
  overflow: hidden;
  position: relative;
  margin-bottom: 50px;
}
.label {
  font-style: normal;
  font-size: 20px;
  font-weight: 100;
  position: relative;
  left: 0;
}
.input-name {
  width: 350px;
  border: 1px solid;
  border-radius: 2px;
  overflow: hidden;
}
/* editor area */
.editor-area {
  /* width: 600px; */
  overflow: hidden;
  position: relative;
  display: flex;
  /* left: 40px; */
}
.AceEditor{
  height: 350px;
  margin-left: 185px;
}
/* textarea */
textarea{
  width: 600px;
  height: 250px;
  margin-left: 160px;
}
/* button style */
.button-add-cancell button {
  width: 170px;
  height: 30px;
  color: #0d6efd;
  border: 1px solid;
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
  /* left: 40px; */
  margin-left: 35%;
}
input[type="radio"] {
  transform: scale(1.6);
}
label {
  margin-left: 10px;
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
.common-option:hover,
.private-option:hover {
  background-color: #bcc6d4;
}
</style>