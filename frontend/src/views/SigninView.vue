<template>
  <div class="login">
    <h1>Signin Page</h1>
    <div class="section">
      <div class="container">
        <div class="card">
          <div class="card-header">
            <div class="card-header-title">Sign In</div>
          </div>
          <div class="section">
            <div class="card-item">
              <div class="field">
                <p class="control has-icons-left has-icons-right">
                  <input
                    class="input"
                    type="email"
                    placeholder="Email"
                    required
                    v-model="form.email"
                    @blur="validateEmail"
                    id="email-input"
                  />
                  <span class="icon is-small is-left">
                    <font-awesome-icon icon="envelope" />
                  </span>
                  <span class="icon is-small is-right">
                    <font-awesome-icon icon="check" id="check-mark" />
                  </span>
                </p>
                <div v-if="msg.email">{{ msg.email }}</div>
              </div>
              <div class="field">
                <p class="control has-icons-left">
                  <input
                    class="input"
                    type="password"
                    placeholder="Password"
                    required
                    v-model="form.password"
                  />
                  <span class="icon is-small is-left">
                    <font-awesome-icon icon="lock" />
                  </span>
                </p>
              </div>
              <div class="buttons">
                <div class="button is-success" @click="submit">Sign In</div>
                <div class="button is-warning" @click="reset">Reset</div>
                <div v-if="msg.login">{{ msg.login }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        id: null,
        email: "",
        password: "",
        created_on: "",
        last_login: "",
      },
      msg: [],
    };
  },
  methods: {
    validateEmail() {
      const checkEmail = document.getElementById("email-input");
      const checkMark = document.getElementById("check-mark");
      if (
        // eslint-disable-next-line
        !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.form.email)
      ) {
        checkEmail.className = "input is-warning";
        this.msg["email"] = "Please enter a valid email address";
      } else {
        checkEmail.className = "input is-success";
        checkMark.style.color = "green";
        this.msg["email"] = "";
      }
    },
    reset() {
      const checkEmail = document.getElementById("email-input");
      const checkMark = document.getElementById("check-mark");
      checkEmail.className = "input";
      checkMark.style.color = "";
      this.form.email = "";
      this.form.password = "";
      this.msg["email"] = "";
      this.msg["login"] = "";
    },
    submit() {
      if (this.email != "" && this.password != "") {
        this.msg["login"] = "";
        axios
          .post("/signin", this.form)
          .then((res) => {
            this.msg["login"] = "";
            this.msg["login"] = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        this.msg["login"] = "Please enter username/password.";
      }
    },
  },
};
</script>
