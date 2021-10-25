<template>
  <div class="container-fluid">
    <h1>Checking Result</h1>
    <div class="textArea">
      <a-textarea
        v-model="value"
        :auto-size="{ minRows: 10, maxRows: 6 }"
        readonly
      />
    </div>

    <div id="action">
      <button type="button" class="btn btn-outline-primary">
        Checking with the same LTL property and different configuration
      </button>
      <button type="button" class="btn btn-outline-primary">
        Checking with different LTL property
      </button>
    </div>
    <div id="action">
      <button type="button" class="btn btn-outline-primary">
        Start a new checking session
      </button>
      <button type="button" class="btn btn-outline-primary">Back</button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      value: "hihi",
    };
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  padding: 50px;
}
.textArea {
  margin: auto;
  width: 60%;
}
#action {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 80%;
}
</style>
