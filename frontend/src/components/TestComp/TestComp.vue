<template>
  <div>
    <p>{{ msg }}</p>
  </div>

  <div class="container">
    <div class="card">
      <div class="card-header-title">Newsletter Sign Up</div>
      <div class="card-content">
        <label class="label">First Name</label>
        <input class="input is-rounded" type="text" v-model="form.first_name" />

        <label class="label">Last Name</label>
        <input class="input is-rounded" type="text" v-model="form.last_name" />

        <label class="label">Email</label>
        <input class="input is-rounded" type="email" v-model="form.email" />
        <footer class="card-footer">
          <a class="card-footer-item" @click="submit">Sign Up</a>
          <a class="card-footer-item" @click="remove">Delete</a>
          <div>
            <p>{{ msg }}</p>
          </div>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PingPing",
  data() {
    return {
      msg: "",
      form: {
        first_name: "",
        last_name: "",
        email: "",
      },
    };
  },
  methods: {
    getMessage() {
      axios
        .get("/")
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    submit() {
      axios.post("http://127.0.0.1:8000/create-contact", this.form).then(
        function (response) {
          // Handle success
          this.msg = response.data;
        }.bind(this)
      );
    },
    remove() {
      axios.delete("http://127.0.0.1:8000/delete-contact", 21).then(
        function (response) {
          this.msg = response.data;
        }.bind(this)
      );
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style lang="scss" scoped>
.card-footer-item {
  &:hover {
    background-color: rgb(219, 219, 219);
  }
  &:active {
    background-color: rgb(202, 202, 202);
  }
}
.card {
  background-image: url("@/assets/images/news.jpg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}
.card .label {
  color: rgb(105, 105, 133);
}

.card .input {
  opacity: 70%;
  color: black;
}

.card-header-title {
  color: white;
  font-size: 2em;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}

.card-footer-item {
  color: white;
  font-size: 1.5em;
  font-weight: bold;
}
</style>
