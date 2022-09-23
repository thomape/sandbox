<template>
  <div>
    <p>{{ msg }}</p>
  </div>

  <div class="columns">
    <div class="column">
      <div class="container">
        <div class="card">
          <div class="card-header-title">Newsletter Sign Up</div>
          <div class="card-content">
            <label class="label">First Name</label>
            <input
              class="input is-rounded"
              type="text"
              v-model="form.first_name"
            />

            <label class="label">Last Name</label>
            <input
              class="input is-rounded"
              type="text"
              v-model="form.last_name"
            />

            <label class="label">Email</label>
            <input class="input is-rounded" type="email" v-model="form.email" />

            <section class="section">
              <button class="button" v-on:click="submit()">Submit</button>
              <button class="button" v-on:click="remove()">Delete</button>
            </section>
            <footer class="card-footer">
              <a class="card-footer-item" @click="submit">Sign Up</a>
              <a class="card-footer-item" @click="remove">Delete</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
    <div class="column">
      <div class="container">
        <figure class="image">
          <img src="@/assets/images/news.jpg" />
        </figure>
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
      axios.post("http://127.0.0.1:8000/contact", this.form).then(
        function (response) {
          // Handle success
          this.msg = response.data;
        }.bind(this)
      );
    },
    remove() {
      axios
        .delete("http://127.0.0.1:8000/contact/delete", this.form.first_name)
        .then(
          function (response) {
            this.msg = response.dat;
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
</style>
