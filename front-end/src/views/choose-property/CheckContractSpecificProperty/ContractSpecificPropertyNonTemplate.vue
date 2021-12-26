<template>
  <div>
    <div id="con-setting" class="container">
      <div id="header">Contract-Specifc Property Setting - Non Template</div>
      <div class="row">
        <div class="col-2">Name</div>
        <div class="col-9">
          <input
            type="text"
            class="form-control"
            v-model="template.name"
            placeholder=""
          />
        </div>
      </div>
      <div class="row">
        <div class="col-2">Formula</div>
        <div class="col-9">
          <FormularEditor @changeContent="getData" :ltlcode="template.formula" />
        </div>
      </div>
      <div class="row">
        <div class="col-2">Description</div>
        <div class="col-9">
          <textarea
            name=""
            id=""
            cols="30"
            rows="5"
            v-model="template.description"
            class="form-control"
          >
            Not currentBalance overflow
          </textarea>
        </div>
      </div>
      <div class="row">
        <div class="col-2"></div>
        <div id="btn-group" class="col-9">
          <button class="btn btn-primary-outline btn-sm" @click="routing('save')">
            Next
          </button>
          <button class="btn btn-outline btn-sm" @click="routing('back')">Back</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FormularEditor from "../../../components/LtlEditor.vue";
export default {
  data: function () {
    return {
      template: {
        aid: JSON.parse(localStorage.getItem("user")).id,
        createdDate: "2021-12-27",
        description: "",
        formula: "",
        formula_text: "This is formular text",
        name: "",
        template_type: "type0",
      },
      ltlConfig: {},
    };
  },
  components: {
    FormularEditor,
  },
  mounted() {
    this.template = this.$store.state.data.data.selectedTemplate;
  },
  computed: {
    getFormula() {
      return this.template.formula;
    },
  },
  methods: {
    getData(data) {
      this.template.formula = data;
    },
    setLtlConfig() {
      this.ltlConfig = {
        type: "specific",
        params: {
          name: this.template.name,
          formula: this.template.formula,
        },
      };
    },
    routing(param) {
      if (param == "save") {
        this.setLtlConfig();
        this.$store.commit("SetLtlConfig", this.ltlConfig);
        this.$store.commit("SetSelectedTemplate", this.template);
        this.$router.push({ name: "Initial" });
      }
      if (param == "back") {
        this.$router.push({ name: "CSPSettingType" });
      }
    },
  },
};
</script>

<style scoped>
#con-setting {
  width: 70%;
  color: black;
}
#header {
  margin-top: 2%;
  text-align: center;
  font-size: 35px;
  font-weight: bold;
}
.row {
  margin-top: 20px;
}
.col-2 {
  font-size: 20px;
}
textarea {
  height: auto;
}
#btn-group {
  /* width: 100%; */
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1%;
  margin-bottom: 5%;
  height: 5%;
}
#btn-group button {
  cursor: pointer;
  width: 15%;
  height: 2%;
  border: 1px solid #2196f3;
  text-align: center;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  padding: 4px 3px;
  border-radius: 4px;
  cursor: pointer;
}
#btn-group button:hover {
  background-color: #1079cf;
  color: white;
}
button {
  margin: auto;
}
</style>
