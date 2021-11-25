<template>
  <div class="container">
    <div class="row">
      <h2>Upload a new Smart Contract code</h2>
    </div>
    <div class="row">
      <div class="col-3">
        <p>Name</p></div>
      <div class="col-7">
        <input type="text" class="form-control" v-model="nameSc" />
      </div>
    </div>
    <div class="row">
      <div class="col-3">
        <p>Smart Contract Type</p></div>
      <div class="col-7 radioStyle">
        <div class="form-check" v-if="isSuperior">
          <input
            class="form-check-input"
            type="radio"
            name="radiobtn"
            id="common"
            v-model="selectOption"
          />
          <label class="form-check-label" for="common"> Common </label>
        </div>
        <div class="form-check" v-else>
          <input
            class="form-check-input"
            type="radio"
            name="radiobtn"
            id="pending"
            checked
            v-model="selectOption"
          />
          <label class="form-check-label" for="pending"> Pending </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="radiobtn"
            id="private"
            v-model="selectOption"
          />
          <label class="form-check-label" for="private"> Private </label>
        </div>
      </div>
    </div>
    <div class="editor-area">
      <ace-editor
        v-bind:codeSC="demoEditSC"
        @changeSC="updateContent($event)"
      />
    </div>
    <div class="button">
      <button
        type="button"
        class="btn btn-outline-primary"
        @click="routing('save')"
      >
        Save
      </button>
      <button
        type="button"
        class="btn btn-outline-primary"
        @click="routing('cancel')"
      >
        Cancel
      </button>
    </div>
  </div>

</template>

<script>
import AceEditor from "../../../components/AceEditor.vue";
export default {
  data() {
    return {author : 'admin'};
  },
  components: { AceEditor },
  methods: {
    routing(param) {
      if (param == "save") {
        this.$router.push({ name: "SelectSmartContract" });
      }
      if (param == "cancel") {
        this.$router.push({ name: "SelectSmartContract" });
      }
    },
    updateContent(value) {
      this.demoEditSC = value;
    },
    computed: {
      selectOption: {
        get: function () {
          return this.options;
        },
        set: function (value) {
          this.options = value;
        },
      },
      isSuperior() {
        return this.$store.state.user.currentUser.role == "admin";
      },
    },
  },
};
</script>

<style scoped>
.container{
  width: 66%;
}
/* editor area */
.editor-area {
  width: 600px;
  overflow: hidden;
  position: relative;
  margin-left: 12%;
}
p{
 margin-left: 40%;
}

.button {
  width: 70%;
  display: flex;
  justify-content:space-around;
  margin: 0 auto;
}
.radioStyle{
  display: flex;
  justify-content: space-around;
  width: 60%;
}
.row {
  margin: 2%;
}
h2{
  margin-left: 12%;
}


</style>