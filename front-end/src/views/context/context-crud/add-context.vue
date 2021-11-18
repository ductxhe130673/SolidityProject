<template>
  <div id="main">
    <div id="header">Create a new Context</div>
    <div class="body">
      <div class="row" id="name-section">
        <div class="title col-2">Name</div>
        <div class="col-10">
          <input class="form-control" type="text" v-model="name" />
        </div>
      </div>

      <div class="row" id="type-section">
        <div class="title col-2">Type</div>
        <div class="col-10">
          <select class="form-select" v-model="options">
            <option value="type1">DCR</option>
            <option value="type2">BPMN</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="title col-2">Description</div>
        <div class="col-10">
          <textarea
            class="form-control"
            type="text"
            v-model="description"
          ></textarea>
        </div>
      </div>
      <!-- <div class="editor-area">
        <span class="title">Formular</span>
        <EditorSc v-model="code" />
      </div> -->
      <div class="row">
        <div class="title col-2">Content</div>
        <div class="col-10">
          <input class="form-control" type="text" v-model="content" />
        </div>
      </div>
      <div id="group-btn">
        <button id="button-add" type="button" @click="clickHandler('save')">
          Save
        </button>
        <button
          id="button-cancel"
          type="button"
          @click="clickHandler('cancel')"
        >
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// import EditorSc from "../../../components/TextEditor.vue";
import { CreateContext } from "../../../services/data";
export default {
  data() {
    return {
      options: "",
      name: "",
      description: "",
      content: "",
    };
  },
  // components: { EditorSc },
  methods: {
    //   async CreateContext(cid) {
    //   await CreateContext(cid);
    // },
    // checkValidateContext() {
    //   if (this.code !== "" && this.name !== "" && this.description !== "") {
    //     return true;
    //   }
    //   return false;
    // },
    async clickHandler(action) {
      if (action == "save") {
        //check validation of field context
        // if (!this.checkValidateContext()) {
        //   alert('You must enter data to field!!!')
        //   return;
        // }
        await CreateContext(
          this.name,
          this.content,
          this.description,
          this.options
        );
        this.$router.push(this.$route.params.parent_path);
      } else if (action == "cancel") {
        this.$router.push(this.$route.params.parent_path);
      }
    },
  },
  computed: {},
};
</script>
<style scoped>
#main {
  background-color: rgb(241, 240, 240);
  align-items: center;
  height: 100vh;
  margin: 0;
}
#header {
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
.title {
  font-size: 18px;
}
#name-section {
  margin-bottom: 20px;
}
#type-section {
  margin-bottom: 20px;
}
textarea {
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
#group-btn {
  width: 100%;
  align-items: center;
  display: flex;
  justify-content: space-evenly;
  margin-top: 25px;
  margin-left: 20px;
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