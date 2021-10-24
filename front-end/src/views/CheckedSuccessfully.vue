<template>
  <div class="container-fluid">
    <h1>Generating CPN Model</h1>
    <div class="row">
      <div class="col-3">
        <h5>Smart Contracts</h5>
      </div>
      <div class="col-8">
        <table class="table table-striped" >
            <tr>
              <th>#</th>
              <th>Contract Name</th>
            </tr>
            <tr>
              <td>1</td>
              <td>cdsvbsk</td>
            </tr>
        </table>
      </div>
    </div>
    <div class="row">
      <div class="col-3">
        <h5>Context</h5>
      </div>
      <div class="col-8">
        <div class="input-group input-group-sm mb-3">
          <input type="text" class="form-control" placeholder="Gaming" />
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-3">
        <h5>LTL Property</h5>
      </div>
      <div class="col-8">
        <div class="input-group input-group-sm mb-3">
          <input
            type="text"
            placeholder="Interger overflow"
            class="form-control"
          />
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-3">
        <h5>Configuration</h5>
      </div>
      <div class="col-8">
        <a href="# " class="link">Link to setting configuration</a>
      </div>
    </div>
    <div class="row">
      <div class="wrapper">
        <h6>The the smart contract is checking ....</h6>
        <div class="progress" style="height: 40px">
          <div
            class="progress-bar"
            role="progressbar"
            style="width: 100%"
            aria-valuenow="100"
            aria-valuemin="0"
            aria-valuemax="100"
          ></div>
        </div>
      </div>
    </div>
    <div class="row">
      <div id="action">
        <button type="button" class="btn btn-outline-primary">Check</button>
        <button type="button" class="btn btn-outline-primary">Back</button>
      </div>
    </div>
  </div>
</template>
<style scoped>
h1 {
  text-align: center;
  padding: 50px;
}

.link {
  text-decoration: underline;
}

h5 {
  text-align: left;
  padding-left: 50px;
}

.row {
  margin-bottom: 50px;
}

.wrapper {
  width: 500px;
  height: 200px;
  border: 1px solid black;
  margin: 50px auto;
  padding: 50px;
}

.progress {
  text-align: center;
  border: 1px solid black;
}

#action {
  margin: 0 auto;
  margin-top: 4%;
  display: flex;
  justify-content: space-between;
  width: 40%;
}
.progress-bar{
  background-color: #73C1D9;
}
th {
  text-indent: inherit;
}
/* .table {
  width: 100%;
}
.table thead tr {
 background-color:darkgray ;
   color: black;
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
} */
</style>