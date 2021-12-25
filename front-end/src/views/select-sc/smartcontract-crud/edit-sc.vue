<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a href="javascript:history.back()" class="link-primary text-decoration-underline"
            >Smart Contract</a
          >
          >
          <a>Edit SC</a>
        </span>
      </div>
      <div class="col-md-7 text-center">
        <h1>Edit the Smart Contract code</h1>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Name</div>
      <div class="col-md-7">
        <input class="form-control" type="text" v-model="nameSc" />
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Smart Contract Type</div>
      <div class="col-md-7">
        <div v-if="isAdmin">
          <select
            class="form-select"
            id="inputGroupSelect01"
            v-model="selectOption"
          >
            <option value="common">Common</option>
            <option value="private">Private</option>
            <option value="pending">Pending</option>
          </select>
        </div>
        <div v-if="!isAdmin">
          <div id="group">
            <div>
              <input
                type="radio"
                id="pending"
                value="pending"
                name="group1"
                 v-model="selectOption"
              />
              <label for="pending">Pending</label>
            </div>
            <div>
              <input
                type="radio"
                id="private"
                value="private"
                name="group1"
                v-model="selectOption"
              />
              <label for="private">Private</label>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Content</div>
      <div class="col-md-7">
        <ace-editor
          v-bind:codeSC="demoEditSC"
          @changeSC="updateContent($event)"
        />
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Description</div>
      <div class="col-md-7">
        <textarea cols="30" rows="5" v-model="descriptionSC"></textarea>
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
        @click="clickHandler('back')"
      >
        Cancel
      </button>
    </div>
  </div>
</template>

<script>
import {
  UpdateSmartContractCode,
  GetSmartContractById,
} from "../../../services/data";
import AceEditor from "../../../components/AceEditor.vue";
export default {
  components: { AceEditor },
  name: "EditSc",

  data() {
    return {
      sc_id: this.$route.params.sc_id,
      nameSc: this.$route.params.name,
      code: this.$route.params.code,
      dataCurrent: {},
      demoEditSC: "test edit sc",
      isAdmin: true,
      descriptionSC: this.$route.params.description,
      selectOption: this.$route.params.type,
    };
  },
  mounted() {
    this.demoEditSC = this.code;
    this.isAdmin =
      JSON.parse(localStorage.getItem("user")).role === "admin" ? true : false;
  },
  methods: {
    async getDataCurrent(sc_id) {
      await GetSmartContractById(sc_id);
    },
    updateContent(value) {
      this.demoEditSC = value;
    },
    async clickHandler(param) {
      if (param == "save") {
        await UpdateSmartContractCode(
          this.sc_id,
          this.nameSc,
          this.demoEditSC,
          this.descriptionSC,
          this.selectOption
        );
        this.$router.push({
          name: "ListSc",
        });
      }
      if (param == "back") {
        this.$router.push(this.$route.params.parent_path);
      }
    },
  },
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