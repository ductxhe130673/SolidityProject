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
          <a>Edit LTL</a>
        </span>
      </div>
      <div class="col-md-7 text-center">
        <h1>Update the LTL Property Template</h1>
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
        <FormularEditor :ltlcode="codeModel" @input="updateMessage" />
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
import { GetLtltemplteById, UpdateLtlTemplate } from "../../services/data";
import FormularEditor from "../../components/FormularEditor.vue";
export default {
  components: {
    FormularEditor,
  },
  data() {
    return {
      id: this.$route.params.vul_id,
      codeModel: "",
      name: "",
      description: "",
      ltl: { name: String, fomular: String, description: String },
      dateFormat: "",
      formulaText: "",
    };
  },
  watch: {
    codeModel: function (newVal) {
      console.log("newVal", newVal);
    },
  },
  mounted() {
    this.initData();
  },
  methods: {
    updateMessage(mes) {
      var mapObj = {
        G: "After an occurrence of",
        F: "at least one occurrence of",
        g: "g",
        f: "f",
      };
      const step1 = mes.replace("=>", "there will be");
      this.formulaText = step1.replace(/G|F/gi, function (matched) {
        return mapObj[matched];
      });
      this.codeModel = mes;
    },
    async initData() {
      const data = await GetLtltemplteById(this.id);
      this.initModelLTL(data);
      this.codeModel = data.formula;
      this.name = data.name;
      this.description = data.description;
      this.dateFormat = data.createdDate;
      this.formulaText = data.formula_text
    },

    async clickHandler(action) {
      if (action == "save") {
        await UpdateLtlTemplate(
          this.id,
          this.name,
          this.description,
          this.codeModel,
          this.dateFormat,
          this.formulaText
        );
        this.$router.push(this.$route.params.parent_path);
        this.$store.commit("setIsEditFormula", false);
      } else if (action == "cancel") {
        this.$store.commit("setIsEditFormula", false);
        if (!this.$route.params.parent_path) this.$router.push("/");
        else this.$router.push(this.$route.params.parent_path);
      }
    },
    initModelLTL(modelLTL) {
      this.ltl.name = modelLTL.name;
      this.ltl.fomular = modelLTL.fomular;
      this.ltl.description = modelLTL.description;
    },
    CheckchangeLTL() {
      return (
        this.ltl.name.trim() === this.name.trim() &&
        this.ltl.fomular.trim() === this.fomular.trim() &&
        this.ltl.description.trim() === this.description.trim()
      );
    },
    changedLTL(value) {
      this.codeModel = value;
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
  margin-top: 2%;
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
