<template>
  <div class="container">
    <div id="dialog">
     
        <h4>{{ this.dialog.title }}</h4>
      
      <div id="d-content">
        <a-upload-dragger
          name="file"
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          @change="handleChange"
        >
          <p class="ant-upload-drag-icon">
            <a-icon type="inbox" />
          </p>
          <p class="ant-upload-text">Click or drag file to upload</p>
        </a-upload-dragger>
      </div>
      <div id="btn-group">
        <button class="btn btn-outline-primary btn-sm" @click="confirm">
          {{ this.dialog.confirmbtn }}
        </button>
        <button class="btn btn-outline-primary btn-sm" @click="cancel">
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ["dialog"],
  data(){
    return{
    fileUp : null
    }
  },
  methods: {
    handleChange(e){
      this.fileUp = e.file;
      console.log('this.fileUp',this.fileUp);
    },
    cancel() {
      this.$emit("cancel");
    },
    confirm() {
      this.$store.commit("setFileUploadSC",this.fileUp)
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
h3 { 
  text-align: center;
  padding: 10px;
}
#btn-group {
  width: 50%;
  float: right;
  display: flex;
  justify-content: space-evenly;
  margin: 30px auto;
}
</style>
