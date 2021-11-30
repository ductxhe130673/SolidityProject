<template>
  <div class="container">
    <div id="dialog">
      <h4>{{ this.dialog.title }}</h4>

      <div id="d-content">
        <input class="form-control" type="file" @change="previewFiles" multiple />
      </div>
      <div id="btn-group">
        <button class="btn btn-outline-primary btn-sm" @click="confirm">
          {{ this.dialog.confirmbtn }}
        </button>
        <button class="btn btn-outline-primary btn-sm" @click="cancel">Cancel</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ["dialog"],
  data() {
    return {
      fileUpload: null,
      content: null,
    };
  },
  methods: {
    handleChange(e) {
      this.fileUpload = e.file;
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
    cancel() {
      this.$emit("cancel");
    },
    confirm() {
      this.convertFileToText();
      this.$emit("confirm");
    },
  },
};
</script>
<style scoped>
#dialog {
  width: 500px;
  height: 300px;

  margin: auto;
  background-color: white;
  border-radius: 5px;
  padding: 15px;
}
#d-content {
  margin-top: 50px;
}
h3 {
  text-align: center;
  padding: 10px;
}
#btn-group {
  width: 24%;
  float: right;
  display: flex;
  justify-content: space-evenly;
  margin: 70px auto;
}
</style>
