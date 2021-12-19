<template>
  <div id="ace-editor">
    <!-- <h1>Hello demo {{codeSC}}</h1> -->
    <div class="tool-bar"></div>
    <editor
      v-model="contentSC"
      @init="editorInit"
      lang="solidity"
      theme="chrome"
      width="100%"
      height="100%"
    ></editor>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contentSC: this.$store.state.data.contentFile,
    };
  },
  watch: {
    codeSC: function (newVal, oldVal) {
      console.log(`propchange oldVal:${oldVal}, newVal:${newVal}`);
      this.contentSC = this.codeSC;
    },
    contentSC: function (newVal, oldVal) {
      console.log(`propchange oldVal:${oldVal}, newVal:${newVal}`);
      this.$emit("changeSC", newVal);
    },
  },
  props: ["codeSC"],
  components: {
    editor: require("vue2-ace-editor"),
  },
  methods: {
    editorInit: function () {
      require("brace/ext/language_tools"); //language extension prerequsite...
      require("brace/mode/solidity"); //language
      require("brace/theme/chrome");
    },
    change() {
      console.log("Alo");
    },
  },
};
</script>

<style>
#ace-editor {
  width: 100%;
  height: 300px;
  border: 1px solid #ced4da;
}


</style>
