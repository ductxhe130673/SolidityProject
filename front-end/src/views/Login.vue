<template>
  <div id="body">
    <svg
      width="380px"
      height="500px"
      viewBox="0 0 837 1045"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      xmlns:sketch="http://www.bohemiancoding.com/sketch/ns"
    >
      <g
        id="Page-1"
        stroke="none"
        stroke-width="1"
        fill="none"
        fill-rule="evenodd"
        sketch:type="MSPage"
      >
        <path
          d="M353,9 L626.664028,170 L626.664028,487 L353,642 L79.3359724,487 L79.3359724,170 L353,9 Z"
          id="Polygon-1"
          stroke="#007FB2"
          stroke-width="6"
          sketch:type="MSShapeGroup"
        ></path>
        <path
          d="M78.5,529 L147,569.186414 L147,648.311216 L78.5,687 L10,648.311216 L10,569.186414 L78.5,529 Z"
          id="Polygon-2"
          stroke="#EF4A5B"
          stroke-width="6"
          sketch:type="MSShapeGroup"
        ></path>
        <path
          d="M773,186 L827,217.538705 L827,279.636651 L773,310 L719,279.636651 L719,217.538705 L773,186 Z"
          id="Polygon-3"
          stroke="#795D9C"
          stroke-width="6"
          sketch:type="MSShapeGroup"
        ></path>
        <path
          d="M639,529 L773,607.846761 L773,763.091627 L639,839 L505,763.091627 L505,607.846761 L639,529 Z"
          id="Polygon-4"
          stroke="#F2773F"
          stroke-width="6"
          sketch:type="MSShapeGroup"
        ></path>
        <path
          d="M281,801 L383,861.025276 L383,979.21169 L281,1037 L179,979.21169 L179,861.025276 L281,801 Z"
          id="Polygon-5"
          stroke="#36B455"
          stroke-width="6"
          sketch:type="MSShapeGroup"
        ></path>
      </g>
    </svg>
    <div class="form">
      <label>Username:</label>
      <input type="text" required v-model="username" placeholder="User Name" />

      <label>Password:</label>
      <input type="password" required v-model="password" placeholder="Password" />
      <div v-if="error" class="error">{{ error }}</div>

      <div class="terms">
        <input type="checkbox" v-model="terms" />
        <label>Remember Me</label>
      </div>

      <div class="submit">
        <button @click="login()">Login</button>
      </div>
      <div id="login-with">
        <button class="btn btn-google" type="submit">
          <i class="fab fa-google mr-2"></i> Sign in with Google
        </button>
        <button class="btn btn-facebook" type="submit">
          <i class="fab fa-facebook-f mr-2"></i> Sign in with Facebook
        </button>
      </div>
    </div>
  </div>
</template>

<script>
//import { makeLogin } from "../services/auth";
import { AuthService } from "../services/auth";
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      terms: false,
      error: "",
    };
  },
  mounted() {
    this.$store.commit("setIndex", 0);
  },
  methods: {
    login() {
      if (this.username === "" || this.password === "") {
        alert("You have to fill all");
      } else {
        const response = AuthService.makeLogin({
          username: this.username,
          password: this.password,
        });
        response.then((res) => {
          if (res.status === 200) {
            this.$router.push({
              name: "Index",
            });
          }
        });
      }
    },
  },
};
</script>

<style scoped>
.form {
  max-width: 420px;
  margin: 30px auto;
  background: rgb(241, 240, 240);
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}
label {
  color: rgb(68, 65, 65);
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}
input {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: 1px solid;
  border-color: rgb(163, 161, 161);
  border-radius: 10px;
  color: rgb(126, 126, 126);
}
input[type="checkbox"] {
  display: inline-block;
  width: 16px;
  margin: 0 10px 0 0;
  position: relative;
  top: 2px;
}
button {
  width: 100%;
  background: #0b6dff;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
}
.submit {
  text-align: center;
}
.error {
  color: #ff0062;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
#login-with {
  width: 100%;
  margin-top: 20px;
  padding-top: 20px;
  border-top-style: solid;
  border-top-color: #777;
  border-top-width: 1px;
}
.btn-google {
  color: white;
  background-color: #ea4335;
}
.btn-facebook {
  visibility: hidden;
  color: white;
  background-color: #3b5998;
}
.btn {
  font-size: 80%;
  border-radius: 5rem;
  letter-spacing: 0.1rem;
  font-weight: bold;
  padding: 1rem;
  transition: all 0.2s;
  width: 100%;
}
#body {
  height: 650px;
  width: 100%;
  min-width: 420px;
  background-color: #f9f9f9;
  display: flex;
  align-items: center;
}
svg {
  flex-basis: 50%;
}
.message-box {
  flex-basis: 50%;
  color: rgb(68, 67, 67);
  font-family: Roboto;
  font-weight: 300;
}
.message-box h1 {
  font-size: 60px;
  line-height: 46px;
  margin-bottom: 40px;
}
.message-box p {
  font-size: 16px;
  line-height: 10px;
  margin-bottom: 20px;
}
.buttons-con .action-link-wrap {
  margin-top: 40px;
}
.buttons-con .action-link-wrap a {
  background: #68c950;
  padding: 8px 25px;
  border-radius: 4px;
  color: #fff;
  font-weight: bold;
  font-size: 14px;
  transition: all 0.3s linear;
  cursor: pointer;
  text-decoration: none;
  margin-right: 10px;
}
.buttons-con .action-link-wrap a:hover {
  background: #5a5c6c;
  color: #fff;
}
#Polygon-1,
#Polygon-2,
#Polygon-3,
#Polygon-4,
#Polygon-4,
#Polygon-5 {
  animation: float 1s infinite ease-in-out alternate;
}
#Polygon-6 {
  animation: float 3s infinite ease-in-out alternate;
  animation-delay: 0.8s;
}
#Polygon-2 {
  animation-delay: 0.2s;
}
#Polygon-3 {
  animation-delay: 0.4s;
}
#Polygon-4 {
  animation-delay: 0.6s;
}
#Polygon-5 {
  animation-delay: 0.8s;
}
/* -- current process -- */
#current-process {
  width: 400px;
  height: 60px;
  margin-top: 40px;
  background-image: linear-gradient(to right, #f5f3f3, #d6d4d4);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
#current-process #text-infor {
  padding-left: 25px;
}
#current-process #text-infor p {
  font-size: 13px;
  font-weight: bold;
  margin-bottom: 0px;
  margin-top: 5px;
  color: #918f8f;
}
#current-process #cp-button {
  height: 30px;
  width: 80px;
  border: 1px solid #918f8f;
  border-color: #918f8f;
  color: #918f8f;
  padding: 8px 12px;
  margin-right: 10px;
  cursor: pointer;
}
#current-process #cp-button:hover {
  border-color: #535353;
  color: #535353;
}
/*---- showConfirmation */
#showConfirmation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
  z-index: 1;
  align-items: center;
  justify-content: center;
}
#components-holder {
  width: 50%;
  margin: auto;
  margin-top: 200px;
}
@keyframes float {
  100% {
    transform: translateY(20px);
  }
}
@media only screen and (max-width: 820px) {
  #body {
    flex-direction: column;
  }
  .message-box {
    margin-top: 30px;
  }
}
</style>
