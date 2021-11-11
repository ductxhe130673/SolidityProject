<template>
  <div class="container-fluid">
     <div class="row align-items-md-center">
      <div class="col-2 ">
        <span>
          <a href="/" class="link-primary text-decoration-underline">Home</a> >
         <a>Load</a></span
        >
      </div>
      <div class="col-8 text-center"><h1 class="text-center">Choose a new Smart Contract file</h1></div>
    </div>
    <div  class="inputStyle" v-if="step =='initial'">
    <input  type="file" @change="onFileChange" >
    </div>
    <div v-if="step == 'done'"> hi</div>
  </div>
  
 
</template>

<script>
export default {
  data() {
    return{
      smfile: '',
     step : 'initial',
    }
  },
  
  methods: {
    onFileChange() {
      this.smfile = this.$refs.file.files[0];
      this.step = 'done';
    }
  },
};
</script>

<style>
.inputStyle{
margin-left: 25%;
}
</style>