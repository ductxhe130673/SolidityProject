<template>
  <div class="mid">
    <div v-if="index === 0" class="description-start">
      <p>The user clicks on the Check Smart Contract to start a new session.</p>
    </div>
    <div v-if="index === 1" class="description-selectSC">
      <p>
        The user selects Smart Contracts for checking. The user can select one smart
        contract or several smart contracts
      </p>
    </div>
    <div v-if="index === 2" class="description-select-context">
      <p>
        The user selects a context for checking. If the user selects several smart
        contracts in the previous step, the context contains all their functions.
      </p>
    </div>
    <div v-if="index === 3" class="description-choosevul">
      <p>The user selects a Contract-Specifc Property or Vulnerability for checking.</p>
    </div>
    <div v-if="index === 4" class="description-generate">
      <p>
        The system generates a list containing two Helena fles. These fles include the
        model, proposition, and property that need to be checked.
      </p>
    </div>
    <div v-if="index === 5" class="description-checkSC">
      <p>
        The system calls Helena checker tool to check the property or vulnerability that
        generated in the previous step
      </p>
    </div>
    <div v-if="index === 6" class="description-finish">
      <p>
        The result is displayed on the screen for viewing. If there is any
        counter-example, the user can have a look at them in the smart contracts.
      </p>
    </div>
    <a-steps direction="vertical" :current="index">
      <a-step
        title="Start"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(0)"
      />
      <a-step
        title="Select Smart Contract"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(1)"
      />
      <a-step
        title="Select Context"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(2)"
      />
      <a-step
        title="Choose Vulnerability"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(3)"
      />
      <a-step
        title="Generate SC to CPN"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(4)"
      />
      <a-step
        title="Check the SCs"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(5)"
      />
      <a-step
        title="Finished"
        style="cursor: pointer; height: 100px"
        @click="onChangeIndex(6)"
      />
    </a-steps>
  </div>
</template>

<script>
export default {
  data() {
    return {
      index: 0,
    };
  },
  methods: {
    onChangeIndex(idx) {
      this.index = idx;
    },
  },
};
</script>

<style scoped>
.description-start {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 110px;
  left: 20%;
  border-radius: 5px;
}
.description-selectSC {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 210px;
  left: 20%;
  border-radius: 5px;
}
.description-select-context {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 310px;
  left: 20%;
  border-radius: 5px;
}
.description-choosevul {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 410px;
  left: 20%;
  border-radius: 5px;
}
.description-generate {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 510px;
  left: 20%;
  border-radius: 5px;
}
.description-checkSC {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 610px;
  left: 20%;
  border-radius: 5px;
}
.description-finish {
  position: fixed;
  width: 300px;
  height: 100px;
  border: 2px solid gray;
  top: 710px;
  left: 20%;
  border-radius: 5px;
}
.mid {
  position: absolute;
  align-items: center;
  justify-content: center;
  margin-top: 5%;
  margin-left: 45%;
}
a-step {
  height: 100px;
}
</style>
