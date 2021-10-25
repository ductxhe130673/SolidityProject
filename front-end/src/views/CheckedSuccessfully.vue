<template>
  <div class="container-fluid">
    <h1>Generating CPN Model</h1>
    <div class="row">
      <div class="col-3">
        <h5>Smart Contracts</h5>
      </div>
      <div class="col-8">
        <table class="table-header">
            <tr>
              <th>
                #
                <span
                  ><a-icon id="icon" type="caret-up" @click="sort('asId')" />
                  <a-icon id="icon" type="caret-down" @click="sort('deId')" />
                </span>
              </th>
              <th>
                Contract Name<span
                  ><a-icon
                    id="icon"
                    type="caret-up"
                    @click="sort('asName')" /><a-icon
                    id="icon"
                    type="caret-down"
                    @click="sort('deName')"
                /></span>
              </th>
            </tr>
        </table>
        <div class="scroll-table">
        <table >
          <tr v-for="data in datatable" :key="data.id">
            <td>{{ data.id }}</td>
            <td>{{ data.var }}</td>
          </tr>
        </table>
        </div>
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
<script>
export default {
  data() {
    return {
      datatable: [
        { id: "1", var: "GV1" },
        { id: "5", var: "HA5" },
        { id: "3", var: "GV3" },
        { id: "4", var: "EB" },
        { id: "8", var: "BD" },
        { id: "4", var: "UE" },
      ],
    };
  },
  methods: {
    sort(mess) {
      switch (mess) {
        case "asId":
          this.datatable.sort((a, b) => a.id - b.id);
          break;
        case "deId":
          this.datatable.sort((a, b) => b.id - a.id);
          break;
        case "asName":
          this.datatable.sort((a, b) => (a.var < b.var ? 1 : -1));
          break;
        case "deName":
          this.datatable.sort((a, b) => (a.var > b.var ? 1 : -1));
          break;
      }
    },
  },
};
</script>
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
table {
  width: 100%;
  border: 1px solid #ddd;
}
table td,
table th {
  padding: 8px;
}
.scroll-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.scroll-table tr:hover {
  background-color: #ddd;
}

.table-header{
  background-color: #d9edf7;
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  color: black;
  text-indent: inherit;
}
.table-header tr td {
   word-wrap: break-word;
}
span {
  float: right;
  display: block;
}
#icon {
  display: block;
  height: 8px;
}
.scroll-table {
  height: 200px;
  overflow-y: auto;
}
</style>