<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4">
        <div class="d-flex flex-column align-items-center text-center p-3 py-5">
          <img
            class="rounded-circle mt-5"
            width="150px"
            height="150px"
            src="../assets/avatar.png"
          />
          <h4>{{getUserName}}</h4>
        </div>
      </div>
      <div class="col-md-6">
        <div class="p-3 py-5">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h2 class="text-right">My Profile</h2>
          </div>
          <div class="row mt-2">
            <div class="col-md-6">
              <label class="labels">First Name</label
              ><input
                type="text"
                class="form-control"
                v-model="firstName"
                readonly
              />
            </div>
            <div class="col-md-6">
              <label class="labels">Last Name</label
              ><input
                type="text"
                class="form-control"
                v-model="lastName"
                readonly
              />
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-md-12">
              <label class="labels">Birthday</label
              ><input
                type="text"
                class="form-control"
                v-model="birthday"
                readonly
              />
            </div>
            <div class="col-md-12">
              <label class="labels">Mobile Number</label
              ><input
                type="text"
                class="form-control"
                v-model="mobileNumber"
                readonly
              />
            </div>
            <div class="col-md-12">
              <label class="labels">Address </label
              ><input
                type="text"
                class="form-control"
                v-model="address"
                readonly
              />
            </div>
            <div class="col-md-12">
              <label class="labels">Email </label
              ><input
                type="text"
                class="form-control"
                v-model="email"
                readonly
              />
            </div>
          </div>
          <div class="mt-5 text-center">
            <button class="btn btn-primary" type="button">Save Profile</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { GetAccountById} from "../../src/services/data";
export default {
  created() {
    this.initData();
  },
  data() {
    return {
      firstName: "",
      lastName: "",
      birthday: "",
      mobileNumber: "",
      address: "",
      email: ""
    };
  },
  methods: {
    async initData() {
      const data = await GetAccountById(this.checkUser);
      data.forEach((element) => {
        this.firstName = element.firstname;
        this.lastName = element.lastname;
        this.email = element.email;
        this.mobileNumber = element.phone;
        this.birthday = element.birthDate;
        this.address = element.address;
      });
      console.log(this.checkUser);
    },
    
  },
  computed: {
    checkUser() {
      const userId = localStorage.getItem("user")
        ? JSON.parse(localStorage.getItem("user")).id
        : null;
      return userId;
    },
    getUserName() {
      const username = localStorage.getItem("user")
        ? JSON.parse(localStorage.getItem("user")).username
        : null;
      return username;
    },
  },
};
</script>
<style>
.container-fluid {
  background-color: #f9f9f9;
}

.form-control:focus {
  box-shadow: none;
  border-color: #0d6efd;
}

.labels {
  font-size: 1em;
  letter-spacing: 1px;
  color: rgb(68, 65, 65);
}

</style>