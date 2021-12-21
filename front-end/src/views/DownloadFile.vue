<template>
  <div class="container">
    <div id="dialog">
      <h4>{{ this.dialog.title }}</h4>

      <div id="d-content">
        <a class="btn btn-primary btn-sm" href="" download="test.lna"
          >Download lna.prop</a
        >
        <a class="btn btn-primary btn-sm" href="" download="test.lna">Download</a>
        <a class="btn btn-primary btn-sm" href="" download="test.lna">Download</a>

        <!-- <a :href="item.url" v-text="item.label" @click.prevent="downloadItem(item)" />
        <a :href="item.url" v-text="item.label" @click.prevent="downloadItem(item)" />
        <a :href="item.url" v-text="item.label" @click.prevent="downloadItem(item)" /> -->
      </div>
      <div id="btn-group">
        <button class="btn btn-outline-primary btn-sm" @click="cancel">Cancel</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  props: ["dialog"],
  data() {
    return {
      fileUpload: null,
      content: null,
    };
  },
  methods: {
    downloadItem({ url, label }) {
      axios
        .get(url, { responseType: "blob" })
        .then((response) => {
          const blob = new Blob([response.data], { type: "application/pdf" });
          const link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = label;
          link.click();
          URL.revokeObjectURL(link.href);
        })
        .catch(console.error);
    },
    cancel() {
      this.$emit("cancel");
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
h3 {
  text-align: center;
  padding: 10px;
}
#btn-group {
  width: 14%;
  display: flex;
  justify-content: space-evenly;
  margin: 30px auto;
}
a {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
}
</style>
