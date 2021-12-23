<template>
  <div class="container">
    <div id="dialog">
      <h4>{{ this.dialog.title }}</h4>
      <div id="d-content">
        <div class="file">
          <a-icon
            type="file"
            style="margin-top: 20px; margin-left: 30px"
            theme="twoTone"
          />
          <h4>HCPN</h4>
        </div>
        <div class="file">
          <a-icon
            type="file"
            style="margin-top: 20px; margin-left: 30px"
            theme="twoTone"
          />
          <h4>Prop</h4>
        </div>
        <div class="file">
          <a-icon
            type="file"
            style="margin-top: 20px; margin-left: 30px"
            theme="twoTone"
          />
          <h4>Context</h4>
        </div>
        <!-- <a class="btn btn-primary btn-sm" @click="downloadItem(1)">Download</a> -->
        <!-- <button type="button" @click="downloadItem(1)">Download blob_hcpn</button> 
        <button type="button" @click="downloadItem(2)">Download blob_prop</button> -->
        <!-- <a :href="item.url" v-text="item.label" @click.prevent="downloadItem(item)" />
        
        <a :href="item.url" v-text="item.label" @click.prevent="downloadItem(item)" /> -->
      </div>
      <div id="processing-btn">
        <button class="btn btn-outline-primary btn-sm" @click="downloadItem()">
          Download
        </button>
        <button class="btn btn-outline-primary btn-sm" @click="cancel">Cancel</button>
      </div>
    </div>
  </div>
</template>
<script>
import { saveAs } from "file-saver";
export default {
  props: ["dialog"],
  data() {
    return {
      content: null,
      dataDownload: null,
    };
  },
  mounted() {
    this.dataDownload = this.$store.state.data.fileToDownload;
    console.log("RES----", this.dataDownload.hcpn)
  },
  methods: {
    
    downloadItem() {
      let blob_hcpn = new Blob([this.dataDownload.hcpn.content], {
        type: "text/plain;charset-urf-8",
      });
      let blob_prop = new Blob([this.dataDownload.prop.content], {
        type: "text/plain;charset-urf-8",
      });
      let blob_context = new Blob([this.dataDownload.context.content], {
        type: "text/plain;charset-urf-8",
      });
      saveAs(blob_hcpn, this.dataDownload.hcpn.name);
      saveAs(blob_prop, this.dataDownload.prop.name);
      saveAs(blob_context, this.dataDownload.context.name);
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
#d-content {
  display: flex;
  flex-direction: column;
}
h3 {
  text-align: center;
  padding: 10px;
}
h4 {
  padding-top: 12px;
  padding-left: 20px;
  color: gray;
}
#processing-btn {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 70%;
}
a {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
}
.file {
  display: flex;
  flex-direction: row;
}
</style>
