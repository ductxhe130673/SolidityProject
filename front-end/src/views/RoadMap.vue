<template>
  <div class="mid">
  <a-steps direction="vertical" :current="0">
    <a-step title="Start" style="cursor: pointer; height: 100px" @click="onChangeIndex(1)" />
        <a-step
          title="Select Smart Contract"
          style="cursor: pointer; height: 100px"
          @click="onChangeIndex(2)"
        />
        <a-step
          title="Select Context"
          style="cursor: pointer; height: 100px"
          @click="onChangeIndex(3)"
        />
        <a-step
          title="Choose Vulnerability"
          style="cursor: pointer; height: 100px"
          @click="onChangeIndex(4)"
        />
        <a-step
          title="Generate SC to CPN"
          style="cursor: pointer; height: 100px"
          @click="onChangeIndex(5)"
        />
        <a-step title="Check the SCs" style="cursor: pointer; height: 100px" @click="onChangeIndex(6)" />
        <a-step title="Finished" style="cursor: pointer; height: 100px" @click="onChangeIndex(7)" />
  </a-steps>
  </div>
</template>

<script>

export default ({
    data(){
        return {
            
        }
    },
})
</script>

<style scoped>
.mid{
    position: absolute;
    align-items: center;
    justify-content: center;
    margin-top: 5%;
    margin-left: 40%;
}
a-step{
    height: 100px;
}
</style>