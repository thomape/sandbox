<template>
  <div>
    <p>{{ msg }}</p>
  </div>

  <div>
    <label>First Name</label>
    <input type="text" v-model="form.first_name" />

    <label>Last Name</label>
    <input type="text" v-model="form.last_name" />

    <label>Email</label>
    <input type="text" v-model="form.email" />

    <button v-on:click="submit()">Submit</button>
    <button v-on:click="remove()">Delete</button>
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
