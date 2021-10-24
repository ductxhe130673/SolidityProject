<template>
    <div class="container">
        <h1><b>Input Parameters</b></h1>

        <div class="row">
            <div class="col-3 left">
                <h5>Sender value</h5>
            </div>
            <div class="col-7 right">
                <input type="text">
                <a><b>To</b></a>
                <input type="text">
            </div>
        </div>
        <div class="TableParam">
        <table class="table table-striped" border="2">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Parameters</th>
                            <th>Range</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Argument1</td>
                            <td>
                                <input type="text">
                                    <a><b>To</b></a>
                                <input type="text">
                            </td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Argument2</td>
                            <td>
                                <input type="text">
                                    <a><b>To</b></a>
                                <input type="text">
                            </td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>...</td>
                        </tr>
                    </tbody>
        </table>
        </div>
    <div id="btn-group">
      <button class="btn btn-outline-primary btn-sm" @click="routing('save')">
        Next
      </button>
      <button
        class="btn btn btn-outline-primary btn-sm"
        type="button"
        @click="routing('back')"
      >
        Back
      </button>
    </div>   
    </div>

</template>
<script>

</script>

<style scoped>
h1{
    text-align: center;
    padding: 50px;
}
h5 {
    text-align: left;
    padding-left: 50px;
}
input{
    width: 40px;
    margin-left: 50px;
}
a{
    margin-left: 50px;
    font-size: 15px;
}
table{
    width: 70%;
    margin-left: 50px;
}
#btn-group {
  width: 80%;
  display: flex;
  margin-top: 5%;
}
.TableParam{
    padding-top: 60px;
}
button {
  margin: auto;
  margin-top: 40px;
  cursor: pointer;
  width: 15%;
  height: 2%;
  border: 1px solid #2196f3;
  color: #2196f3;
  font-size: 13px;
  line-height: 22px;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
.table thead tr {
    background-color:darkgrey;
    color:black;
    /* text-align: left; */
}
</style>