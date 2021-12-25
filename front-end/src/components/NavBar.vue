<template>
  <nav class="header">
    <div class="nav__left">
      <div class="name" @click="goHome()">Solidity</div>
    </div>
    <div class="nav__mid">
      <a-steps :current="this.$store.state.data.index - 1" size="small">
        <a-step title="Start" style="cursor: pointer" @click="onChangeIndex(1)" />
        <a-step
          title="Select Smart Contract"
          style="cursor: pointer"
          @click="onChangeIndex(2)"
        />
        <a-step
          title="Select Context"
          style="cursor: pointer"
          @click="onChangeIndex(3)"
        />
        <a-step
          title="Choose Vulnerability"
          style="cursor: pointer"
          @click="onChangeIndex(4)"
        />
        <a-step
          title="Generate SC to CPN"
          style="cursor: pointer"
          @click="onChangeIndex(5)"
        />
        <a-step title="Check the SCs" style="cursor: pointer" @click="onChangeIndex(6)" />
        <a-step title="Finished" style="cursor: pointer" @click="onChangeIndex(7)" />
      </a-steps>
    </div>
    <div class="nav__right">
      <div id="dropdown">
        <div class="icon" title="Manage">
          <i class="material-icons">view_list</i>
        </div>
        <div id="dropdown-content">
          <p @click="goURL('list-sc', 'ListSc')"><a>Smart Contracts</a></p>
          <p @click="goURL('list-context', 'ListContext')"><a>Contexts</a></p>
          <p @click="goURL('list-vul', 'ListVul')"><a>LTL</a></p>
        </div>
      </div>
      <div class="icon" @click="goRoadMap()" title="RoadMap">
        <i class="material-icons">map</i>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data: function () {
    return {
      username: "",
      showDia: false,
    };
  },
  computed: {
    checkUser() {
      return this.$store.state.user.currentUser.id;
    },
    getUserName() {
      return this.$store.state.user.currentUser.name;
    },
    getIndexPage() {
      return this.$store.state.data.index;
    },
  },
  methods: {
    toggleProfile() {
      this.showDia = !this.showDia;
    },
    goHome() {
      this.$store.commit("setIndex", 0);
      this.goURL("/", "Index");
    },
    // goListSC() {
    //   this.goURL("/list-sc", "ListSc");
    // },
    goRoadMap() {
      this.$store.commit("setIndex", 0);
      this.$router.push({ name: "RoadMap" });
    },
    goLogin() {
      this.$store.commit("setIndex", 0);
      this.goURL("/login");
    },
    goURL(url, name) {
      if (this.$route.path != url) {
        this.$store.commit("setIndex", 0);
        this.$router.push({ name: name });
      }
    },
    onChangeIndex(pageNum) {
      if (pageNum === 1) {
        this.$router.push({ name: "ListOfCheckedTransactions" });
        this.$store.commit("setIndex", pageNum);
      }
      if (pageNum === 2) {
        this.$router.push({ name: "SelectSmartContract" });
        this.$store.commit("setIndex", pageNum);
      }
      if (pageNum === 3) {
        this.$router.push({ name: "ContextOfSmartContract" });
        this.$store.commit("setIndex", pageNum);
      }
      if (pageNum === 4) {
        this.$router.push({ name: "LTLCheckOption" });
        this.$store.commit("setIndex", pageNum);
      }
      if (pageNum === 5) {
        this.$router.push({ name: "CheckSmartContract" });
        this.$store.commit("setIndex", pageNum);
      }
      if (pageNum === 6) {
        this.$router.push({ name: "CheckSmartContract" });
        this.$store.commit("setIndex", pageNum);
      }
      if (pageNum === 7) {
        this.$router.push({ name: "checkingresult31" });
        this.$store.commit("setIndex", pageNum);
      }
    },
  },
  // components:{ProDia}
};
</script>

<style scoped>
.road-map {
  width: 1000px;
  height: 50px;
  border: 1px solid;
  position: absolute;
}
.road-map-text {
  width: 100px;
  height: 30px;
  padding-left: 10px;
  background: white;
  position: absolute;
  margin-left: 200px;
  margin-top: -10px;
}
.header {
  height: 70px;
  margin-top: 20px;
}
nav {
  background-color: white;
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: space-between;
  padding: 5px 10px;
  /*     box-shadow: 0px 0px 4px rgb(48, 47, 47); */
}
.nav__left {
  display: flex;
  align-items: center;
  flex-basis: 10%;
  width: 150px;
  height: 70px;
  border: 1px solid black;
}
.nav__left .name {
  flex-basis: 10%;
  margin-left: auto;
  margin-right: auto;
  font-size: 24px;
  cursor: pointer;
  color: black;
  font-weight: bold;
}
.nav__search {
  display: flex;
  align-items: center;
  background-color: #f0f2f5;
  padding: 15px;
  border-radius: 50px;
  height: 40px;
}
.nav__search input {
  outline: none;
  border: none;
  background: transparent;
  padding: 0 10px;
  color: #484849;
}
.nav__mid {
  flex-basis: 80%;
  display: flex;
  align-items: center;
  width: 150px;
  height: 70px;
  border: 1px solid black;
  padding-right: 10px;
  padding-left: 10px;
}
.icon {
  padding: 10px 1.2vw;
  border-radius: 5px;
  cursor: pointer;
  align-items: center;
}
.icon i {
  font-size: 30px;
}
.icon:hover {
  background-color: #e6e6e9;
  transition: ease-in-out 0.1s;
}
.nav__right {
  display: flex;
  align-items: center;
  width: 150px;
  height: 70px;
  border: 1px solid black;
}
.avatar {
  display: flex;
  align-items: center;
  margin-right: 20px;
  border-radius: 50px;
  padding: 5px 10px;
  color: #616264;
}
.avatar:hover {
  background: #c7c7c9;
  transition: ease-in-out 0.1s;
}
.avatar__img {
  height: 30px;
  width: 30px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 5px;
}
.buttons {
  display: flex;
  align-items: center;
}
.buttons i {
  padding: 10px;
  margin: 0 1px;
  border-radius: 50%;
  background: #e4e6eb;
}
.buttons i:hover {
  background: #c7c7c9;
  transition: ease-in-out 0.1s;
}
.material-icons {
  color: #616264;
}
a {
  cursor: pointer;
}
#login-btn {
  border: none;
  border-radius: 5px;
  font-size: 20px;
}
#login-btn:hover {
  color: blue;
  text-decoration: underline;
}
#register-btn {
  font-size: 20px;
  border: none;
  margin-left: 10px;
  margin-right: 30px;
  background-color: #5fb8ee;
  border-radius: 5px;
}
#dropdown-content {
  display: none;
  position: absolute;
  background-color: white;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  padding: 0;
  z-index: 1;
}
#dropdown:hover #dropdown-content {
  display: block;
}
#dropdown-content p {
  width: 100%;
  cursor: pointer;
  margin: 0;
  padding: 8px 16px;
}
#dropdown p:hover {
  background-color: #f9f9f9;
}
@media only screen and (max-width: 720px) {
  .nav__mid {
    display: none;
  }
}
@media only screen and (max-width: 938px) {
  .nav__search {
    border-radius: 50%;
    padding: 10px;
  }
  .nav__search i {
    border-radius: 50%;
  }
  .nav__search input {
    display: none;
  }
}
@media only screen and (max-width: 540px) {
  .avatar {
    display: none;
  }
}
</style>
