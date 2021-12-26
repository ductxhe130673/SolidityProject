<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a
            href="javascript:history.back()"
            class="link-primary text-decoration-underline"
            >Context</a
          >
          >
          <a>Edit Context</a></span
        >
      </div>
      <div class="col-md-7 text-center"><h1>Update the Context</h1></div>
    </div>

    <div class="row">
      <div class="col-md-3">Name</div>
      <div class="col-md-7">
        <input class="form-control" type="text" v-model="name" />
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Type</div>
      <div class="col-md-7">
        <select class="form-select" v-model="options">
          <option value="DCR">DCR</option>
          <option value="CPN">CPN</option>
        </select>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Description</div>
      <div class="col-md-7">
        <textarea
          class="form-control"
          type="text"
          v-model="description"
        ></textarea>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Content</div>
      <div class="col-md-7">
        <input
          class="form-control"
          type="file"
          @change="previewFiles"
          multiple
        />
      </div>
    </div>

    <div class="buttonGroup">
      <button
        type="button"
        class="btn btn-outline-primary"
        @click="clickHandler('save')"
      >
        Save
      </button>
      <button
        type="button"
        class="btn btn-outline-primary"
        @click="clickHandler('cancel')"
      >
        Cancel
      </button>
    </div>
  </div>
</template>

<script>
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
      fileUpload: "",
    };
  },
  methods: {
    getDate() {
      this.dateFormat = moment().format("YYYY-MM-DD");
    },
    previewFiles(event) {
      this.fileUpload = event.target.files[0];
    },
    updateContext(data) {
      if(!this.name.trim()){
        alert("Name can not be blank!")
      }else if(!this.description.trim()){
        alert("Description can not be blank!")
      }
      else{
      UpdateContext(
        this.cid,
        this.name,
        this.dateFormat,
        this.options,
        this.description,
        data
      ).then(() => {
        this.$router.push({
          name: "ListContext",
        });
      });
      }
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
        if (this.fileUpload !== "") {
          const reader = new FileReader();
          reader.readAsText(this.fileUpload);
          reader.onload = (e) => {
            this.$store.commit("setContentFile", e.target.result);
            this.updateContext(e.target.result);
          };
        } else {
          this.updateContext(this.content);
        }
      } else if (action == "cancel") {
        this.$router.push({
          name: "ListContext",
        });
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
.container-fluid{
  color: black;
}
.row {
 padding-top: 2%;
  padding-right: 10px;
}

#group {
  display: flex;
  justify-content: space-between;
  width: 70%;
}
label {
  padding-left: 15px;
}

.row>.col-md-3:not(.row:first-of-type >.col-md-3){
  padding-left: 10%;
}

.buttonGroup {
  padding-top: 2%;
  display: flex;
  width: 60%;
  justify-content: space-around;
  margin: 0 auto;
  padding-bottom: 5%;
}
/* textarea */
textarea {
  width: 100%;
  height: 250px;
}
textarea {
  border: 1px solid #ced4da;
}
</style>
