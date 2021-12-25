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
          <a>Add Context</a></span
        >
      </div>
      <div class="col-md-7 text-center"><h1>Create a new Context</h1></div>
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
          <option value="type1">DCR</option>
          <option value="type2">CPN</option>
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
import { CreateContext } from "../../../services/data";
import moment from "moment";

export default {
  data() {
    return {
      options: "",
      name: "",
      description: "",
      content: null,
      fileUpload: null,
      dateFormat: "",
    };
  },
  mounted() {
    this.getDate();
  },

  methods: {
    getDate() {
      this.dateFormat = moment().format("YYYY-MM-DD");
    },
    previewFiles(event) {
      this.fileUpload = event.target.files[0];
    },
    createContext(data) {
      CreateContext(
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
    },
    clickHandler(action) {
      if (action == "save") {
        if (this.fileUpload === "") {
          alert("You have to select file to update!!!");
        }
        if (this.name === "" || this.options === "") {
          alert("Name and Type are must not empty!!!");
        }
        const reader = new FileReader();
        reader.readAsText(this.fileUpload);
        reader.onload = (e) => {
          this.$store.commit("setContentFile", e.target.result);
          this.createContext(e.target.result);
        };
      } else if (action == "cancel") {
        this.$router.push(this.$route.params.parent_path);
      }
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
