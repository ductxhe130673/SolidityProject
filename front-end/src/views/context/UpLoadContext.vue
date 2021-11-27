<template>
  <div class="container-fluid">
    <div class="row">
      <h1 class="text-center">Upload a new Context file</h1>
    </div>
    <div class="row">
      <div class="col-3">
        <p>Name</p>
      </div>
      <div class="col-7">
        <input class="form-control" type="text" v-model="name" />
      </div>
    </div>
    <div class="row">
      <div class="col-3">
        <p>Type</p>
      </div>
      <div class="col-7">
        <select class="form-select" name="" v-model="type">
          <option value="">DCR</option>
          <option value="">Free-cont</option>
          <option value="">type 3</option>
          <option value="">type 4</option>
        </select>
      </div>
    </div>

    <div class="row">
      <div class="col-3">
        <p>Content</p>
      </div>
      <div class="col-7">
        <input class="form-control" type="text" v-model="file" />
      </div>
    </div>

    <div class="row">
      <div class="col-3">
        <p>Description</p>
      </div>
      <div class="col-7">
        <textarea
          class="form-control"
          name=""
          id=""
          cols="50"
          rows="5"
          v-model="description"
        ></textarea>
      </div>
    </div>

    <div class="button">
      <button type="button" class="btn btn-outline-primary" @click="routing('OK')">
        OK
      </button>
      <button type="button" class="btn btn-outline-primary" @click="routing('cancel')">
        Cancel
      </button>
    </div>
  </div>
</template>

<script>
import { CreateContext } from "../../services/data";
export default {
  data() {
    return {
      name: "",
      description: "",
      type: "",
      file: "",
    };
  },
  mounted() {
    this.file = this.$store.state.data.data.uploadSCFile.name;
  },
  methods: {
    async saveContextFile() {
      await CreateContext(this.name, this.file, this.description, this.type);
    },

    routing(param) {
      if (param == "OK") {
        this.saveContextFile();
        this.$router.push({ name: "ContextOfSmartContract" });
      } else if (param == "cancel") {
        this.$router.push({ name: "ContextOfSmartContract" });
      }
    },
  },
};
</script>

<style scoped>
p {
  text-align: right;
}

.button {
  width: 30%;
  display: flex;
  justify-content: space-between;
  margin: 0 auto;
}
.row {
  margin: 2%;
}
</style>
