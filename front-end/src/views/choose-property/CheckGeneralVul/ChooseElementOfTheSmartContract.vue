<template>
  <div>
      <div class="container">
          <div class="header">
              <div class="title">
                  <h1>Select Variables Of Smart Contract</h1>
              </div>
          </div>
          <div class="row">
              
          </div>

        <button @click="routing('next')">Next</button>
        <button @click="routing('back')">Back</button>
      </div>
      
      
  </div>
</template>
<script>
export default {
    methods:{
        routing(param){
            if(param=='next'){
                this.$router.push({name:"Initial"})
            }
            if(param=='back'){
                this.$router.push({name:"LTLCheckOption"})
            }
        }
    }
}
</script>

<style scoped>
.title{
    text-align: center;
}
</style>

<style>

</style>