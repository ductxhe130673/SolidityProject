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
          <a>Add SC</a>
        </span>
      </div>
      <div class="col-md-7 text-center">
        <h1>Create a new Smart Contract code</h1>
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
          <select class="form-select" id="inputGroupSelect01" v-model="options">
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
                v-model="options"
              />
              <label for="pending">Pending</label>
            </div>
            <div>
              <input
                type="radio"
                id="private"
                value="private"
                name="group1"
                v-model="options"
              />
              <label for="private">Private</label>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">
        <div v-if="isAdmin"></div>
        <div v-if="!isAdmin">Content</div>
      </div>
      <div class="col-md-7">
        <div v-if="isAdmin">
          <ace-editor
            v-bind:codeSC="demoEditSC"
            @changeSC="updateContent($event)"
          />
        </div>
        <div v-if="!isAdmin">
          <ace-editor
            v-bind:codeSC="demoEditSC"
            @changeSC="updateContent($event)"
          />
        </div>
      </div>
    </div>
    <div v-if="!isAdmin">
      <div class="row">
        <div class="col-md-3" id="padding-left">Description</div>
        <div class="col-md-7">
          <textarea
            name=""
            id=""
            cols="30"
            rows="5"
            v-model="description"
          ></textarea>
        </div>
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
import { AddNewSmartContracts } from "../../../services/data";
import moment from "moment";
import AceEditor from "../../../components/AceEditor.vue";
export default {
  components: { AceEditor },
  name: "AddSc",
  data() {
    return {
      dateFormat: "",
      nameSc: "",
      options: "private",
      code: "",
      demoEditSC: "test add sc",
      description: "",
      isAdmin: true,
    };
  },
  mounted() {
    this.getDate();
    this.isAdmin =
      JSON.parse(localStorage.getItem("user")).role === "admin" ? true : false;
  },
  methods: {
    getDate() {
      this.dateFormat = moment().format("YYYY-MM-DD");
    },
    updateContent(value) {
      this.demoEditSC = value;
    },
    async clickHandler(action) {
      if (action == "save") {
        if (this.nameSc === "" || this.options === "") {
          window.alert("Please input all field");
        } else {
          await AddNewSmartContracts(
            this.hashValue(this.nameSc),
            this.nameSc,
            this.options,
            this.demoEditSC,
            this.dateFormat,
            this.description
          );
          this.$router.push(this.$route.params.parent_path);
        }
      } else if (action == "cancel") {
        this.$router.push(this.$route.params.parent_path);
      }
    },
  },
  computed: {
    isSuperior() {
      return this.$store.state.user.currentUser.role == "admin";
    },
  },
};
</script>
<style scoped>
.container-fluid{
  color: black;
}
.row {
  margin-top: 2%;
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
#padding-left{
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
