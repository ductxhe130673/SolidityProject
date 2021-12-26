<template>
  <div class="popup">
    <div id="icon"><a-icon type="close" @click="cancel" /></div>
    <div class="content-popup">
      <p>
        Under the explosive development of the Internet age, everything is possible in the
        online world from buying, selling, trading to conferences.
      </p>
      <p>
        When you receive an email, word or excel file, it's really just a duplicate. But
        when it comes to assets like money, contracts, intellectual property, stocks,
        bonds, personal information or creative products, things are completely different.
        That is why today we completely rely on intermediaries like banks, governments,
        social media companies or credit card companies etc. to build self-confidence and
        as others. All these intermediaries perform the same functional logic of
        transactions in commerce, from authentication and validation of personal
        information to the creation and deletion of records. However, more and more new
        problems arise: information leaks, these intermediate channels make everything
        time-consuming and slower, etc.
      </p>
      <p>
        Therefore, our team built FOVEMOSO using blockchain technology based on Solidity
        code to solve the above problems. FOVEMOSO requires no human intervention, thus
        ensuring the fastest, safest and most accurate execution.
      </p>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    cancel() {
      this.$emit("cancel");
    },
  },
};
</script>

<style scoped>
.popup {
  width: 50%;
  height: auto;
  margin: auto;
  background-color: white;
  border-radius: 10px;
}
.content-popup {
  padding: 20px;
}
p {
  color: black;
  font-size: 15px;
  text-indent: 30px;
  margin-bottom: 0;
}
#icon {
  text-align: right;
  font-size: 20px;
  margin-right: 15px;
  color: black;
}
</style>
