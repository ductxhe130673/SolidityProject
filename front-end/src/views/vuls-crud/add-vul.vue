<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
          <a
            href="javascript:history.back()"
            class="link-primary text-decoration-underline"
            >LTL</a
          >
          >
          <a>Add LTL</a>
        </span>
      </div>
      <div class="col-md-7 text-center">
        <h1>Create a new LTL Property Template</h1>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Name</div>
      <div class="col-md-7">
        <input class="form-control" type="text" v-model="name" />
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">Formula</div>
      <div class="col-md-7">
        <FormularEditor @changeContent="updateMessage" />
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">Formula Text</div>
      <div class="col-md-7">
        <textarea
          style="height: 175px"
          spellcheck="false"
          rows="3"
          class="form-control"
          type="text"
          v-model="formulaText"
        ></textarea>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">Description</div>
      <div class="col-md-7">
        <textarea
          spellcheck="false"
          rows="5"
          class="form-control"
          type="text"
          v-model="description"
        ></textarea>
      </div>
    </div>

    <div class="buttonGroup">
      <button type="button" class="btn btn-outline-primary" @click="clickHandler('save')">
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
import moment from "moment";
import FormularEditor from "../../components/FormularEditor.vue";
import { CreateLTLTemplate } from "../../services/data";

export default {
  components: {
    FormularEditor,
  },
  data() {
    return {
      dateFormat: "",
      code: "",
      name: "",
      description: "",
      formulaText: "",
    };
  },
  mounted() {
    this.getDate();
    let el = document.getElementById("textarea-input");
    el.style.height = 180 + "px";
  },
  methods: {
    updateMessage(mes) {
      if (mes.search("property prop: F odp;") >= 0) {
        this.formulaText = "'variable' will occur in some day";
      } else if (mes.search("property prop: G F odp;") >= 0) {
        this.formulaText = "'variable' occurs infinitely often";
      } else if (mes.search("proposition outOfRange:") >= 0) {
        this.formulaText =
          "the case where 'variable' is greater than 2147483647 or less than 0 will never happen";
      }
      this.codeModel = mes;
    },
    getDate() {
      this.dateFormat = moment().format("YYYY-MM-DD");
    },
    async clickHandler(action) {
      if (action == "save") {
        if (this.code === "" || this.name === "") alert("Please input all field!!!");
        await CreateLTLTemplate(
          this.name,
          this.code,
          this.description,
          this.dateFormat,
          this.formulaText
        );
        this.$router.push(this.$route.params.parent_path);
      } else if (action == "cancel") {
        this.$router.push(this.$route.params.parent_path);
      }
    },
  },
  computed: {},
};
</script>
<style scoped>
.container-fluid {
  color: black;
}
.row {
  padding-top: 2%;
  padding-right: 10px;
}
.row > .col-md-3:not(.row:first-of-type > .col-md-3) {
  padding-left: 15%;
}

.buttonGroup {
  padding-top: 2%;
  display: flex;
  width: 60%;
  justify-content: space-around;
  margin: 0 auto;
  padding-bottom: 5%;
}

textarea {
  width: 100%;
  height: 250px;
}
</style>
