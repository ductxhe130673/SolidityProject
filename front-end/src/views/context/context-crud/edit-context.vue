<template>
  <div id="main">
    <div id="header">Update the Context</div>
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
            <option value="type2">CPN</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="title col-2">Description</div>
        <div class="col-10">
          <textarea class="form-control" type="text" v-model="description"></textarea>
        </div>
      </div>
      <!-- <div class="editor-area">
        <span class="title">Formular</span>
        <EditorSc :code.sync="code" />
      </div> -->
      <div class="row">
        <div class="title col-2">Content</div>
        <div class="col-10">
          <input class="form-control" type="file" @change="previewFiles" multiple />
        </div>
      </div>

      <div id="group-btn">
        <button id="button-add" type="button" @click="clickHandler('save')">Save</button>
        <button id="button-cancel" type="button" @click="clickHandler('cancel')">
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// import EditorSc from "../../../components/TextEditor.vue";
import { GetContextById, UpdateContext } from "../../../services/data";
import moment from "moment";
export default {
  created() {
    this.initData();
    this.getDate();
  },
  data() {
    return {
      cid: this.$route.params.id,
      code: "",
      name: "",
      description: "",
      content: null,
      options: "0",
      dateFormat: "",
    };
  },
  // components: { EditorSc },
  methods: {
    getDate() {
      this.dateFormat = moment().format("YYYY-MM-DD");
    },
    previewFiles(event) {
      this.fileUpload = event.target.files[0];
    },
    convertFileToText() {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.$store.commit("setContentFile", e.target.result);
      };
      this.content = this.$store.state.data.contentFile;
      reader.readAsText(this.fileUpload);
      this.$store.commit("setFileUpload", this.fileUpload);
    },
    async initData() {
      const data = await GetContextById(this.cid);
      this.initModelContext(data);
      this.content = data.content;
      this.name = data.name;
      this.description = data.description;
    },

    async clickHandler(action) {
      if (action == "save") {
        this.convertFileToText();
        await UpdateContext(
          this.cid,
          this.name,
          this.dateFormat,
          this.options,
          this.description,
          this.content
        );

        this.$router.push(this.$route.params.parent_path);
      } else if (action == "cancel") {
        // if (!this.$route.params.parent_path) this.$router.push("/");
        // else this.$router.push(this.$route.params.parent_path);
        this.$router.push(this.$route.params.parent_path);
      }
    },
    initModelContext(modelContext) {
      this.name = modelContext.name;
      this.content = modelContext.content;
      this.description = modelContext.description;
      this.options = modelContext.context_type;
    },
    checkChangeConText() {
      return (
        this.name.trim() === this.name.trim() &&
        this.code.trim() === this.code.trim() &&
        this.description.trim() === this.description.trim()
      );
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
  margin-bottom: 30px;
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
