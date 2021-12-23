<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4">
        <div class="d-flex flex-column align-items-center text-center p-3 py-5">
          <img
            class="rounded-circle mt-5"
            width="150px"
            src="https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg"
          />
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
                value=""
              />
            </div>
            <div class="col-md-6">
              <label class="labels">Last Name</label
              ><input
                type="text"
                class="form-control"
                value=""
              />
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-md-12">
              <label class="labels">Birthday</label
              ><input
                type="text"
                class="form-control"
                value=""
              />
            </div>
            <div class="col-md-12">
              <label class="labels">Mobile Number</label
              ><input
                type="text"
                class="form-control"
                value=""
              />
            </div>
            <div class="col-md-12">
              <label class="labels">Address </label
              ><input
                type="text"
                class="form-control"
                value=""
              />
            </div>
            <div class="col-md-12">
              <label class="labels">Email </label
              ><input
                type="text"
                class="form-control"
                value=""
              />
            </div>
          </div>
          <div class="mt-5 text-center">
            <button class="btn btn-primary " type="button">
              Save Profile
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.container-fluid {
  background-color: #f9f9f9;
}

.form-control:focus {
  box-shadow: none;
  border-color: #0d6efd;;
}


.labels {
  font-size: 1em;
  letter-spacing: 1px;
  color: rgb(68, 65, 65);

}


</style>