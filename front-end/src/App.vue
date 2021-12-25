<template>
  <div id="app">
    <NavBar v-if="showNavigationBar === 'nav'" />
    <Header v-if="showNavigationBar === 'header'" />
    <HeaderLogin v-if="showNavigationBar === 'headerLogin'" />
    <router-view />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import Header from "./components/Header.vue";
import HeaderLogin from "./components/HeaderLogin.vue";

// @ is an alias to /src
export default {
  components: { NavBar, Header, HeaderLogin },
  data() {
    return {
      sngPage: {
        Register: true,
        Index: true,
        RoadMap: true,
        ListOfCheckedTransactions: true,
        CheckRentrancy: true,
        SelectSmartContract: true,
        Initial: true,
        UpLoadSc: true,
        ContextOfSmartContract: true,
        LoadContext: true,
        UnFolding: true,
        UpLoadContext: true,
        LTLCheckOption: true,
        CSPSettingType: true,
        CSPNonTemplateSetting: true,
        CSPTemplateSetting: true,
        ContractSpecificProperty: true,
        ContractSpecificPropertyNonTemplate: true,
        GenaralVulSetting: true,
        CheckSmartContract: true,
        ListSc: true,
        EditSc: true,
        AddSc: true,
        AddContext: true,
        EditContext: true,
        ListContext: true,
        AddVul: true,
        EditVul: true,
        ListVul: true,
      },
    };
  },
  computed: {
    showNavigationBar() {
      if (this.$route.name in this.sngPage && this.$store.state.data.index === 0) {
        return "header";
      } else if (this.$route.name === "Login") {
        return "headerLogin";
      } else if (this.$route.name === "Profile") {
        return "header";
      } else if (this.$route.name === "Register") {
        return;
      }
      return "nav";
    },
  },
};
</script>

<style>
/* * {
  -webkit-user-select: none;
  -khtml-user-select: none;
  -o-user-select: none;
  user-select: none;
} */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}
</style>
