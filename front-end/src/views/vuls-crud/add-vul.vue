<template>
  <div id="main">
    <div id="header">
      Create a new LTL Property Template
    </div>
    <div class="body">
      <div class="row" id="name-section">
        <div class="title col-2">Name</div>
        <div class="col-10"><input class="form-control" type="text" v-model="name" /></div>
      </div>
      <!-- 
      <div class="editor-area">
          <span class="title">Formular</span>
          <div>
            <formular-editor/>
          </div>
        <LTLEditor :code="code" @update="updateCode"/>
      </div> -->
      <div class="row">
        <div class="title col-2">Formula</div>
        <div class="col-10">
          <formular-editor/>
        </div>
      </div>

      <div class="row">
        <div class="title col-2">Description</div>
        <div class="col-10">
          <textarea spellcheck="false" rows="5" class="form-control" type="text" v-model="description"></textarea>
        </div>
      </div>
      
      <div id="group-btn">
          <button id="button-add" type="button" @click="clickHandler('save')">Save</button>
          <button id="button-cancel" type="button" @click="clickHandler('cancel')">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
// import LTLEditor from "../../components/LTLEditor.vue"
import moment from "moment";
import FormularEditor from "../../components/FormularEditor.vue";
import {CreateLTLTemplate} from "../../services/data";

export default {
  components: {
    FormularEditor
  },
  data() {
    return {
      dateFormat : "",
      code: "",
      name: "",
      description: ""
    };
  },
  mounted(){
    this.getDate();
    let el = document.getElementById("textarea-input");
    el.style.height = 180 + 'px';
      
  },
  // components: { LTLEditor },
  methods: {
      getDate(){
        this.dateFormat = moment().format('YYYY-MM-DD');
      },
      updateCode(code){
          this.code = code
      },
    async clickHandler(action){
        if(action == "save"){
        console.log(this.name,this.code,this.description,this.dateFormat)
        this.code = "test"
        await CreateLTLTemplate(this.name, this.description, this.code,this.dateFormat)
        this.$router.push(this.$route.params.parent_path);
        } 
        else if(action == "cancel"){
            this.$router.push(this.$route.params.parent_path);
        }
    }
  },
  computed: {
  }
};
</script>
<style scoped>
#main {
  background-color: rgb(241, 240, 240);
  align-items: center;
  height: 100vh;
  margin: 0;
}
#header{
  text-align: center;
  font-size: 35px;
  font-weight: bold;
  padding-top: 20px;
  margin-bottom: 20px;
}
.body {
  display: flex;
  flex-direction: column;
  width: 700px;
  margin: auto;
}
.title{
    font-size: 18px;
}
#name-section{
    margin-bottom: 30px;
}
textarea{
  height: 250px;
}
/* editor area */
.editor-area {
  width: 100%;
  overflow: hidden;
  position: relative;
  /* left: 40px; */
}
/* button style */
#group-btn{
  width: 100%;
  align-items: center;
  display: flex;
  justify-content: space-evenly;
  margin-top: 30px;
  margin-left: 25px;
}
#group-btn button {
  width: 170px;
  height: 30px;
  color: #0d6efd;
  border: 1px solid;
  border-radius: 4px;
}
#group-btn button:hover {
  opacity: 0.9;
  background-color: #0d6efd;
  color: white;
}
#group-btn button:active {
  cursor: wait;
}
</style>