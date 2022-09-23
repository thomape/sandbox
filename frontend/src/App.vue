<template>
  <div id="body" class="dark-mode">
    <nav
      class="navbar"
      id="nav-bar"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="@/assets/images/redshift.png" />
        </router-link>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
          @click="isOpen = !isOpen"
          v-bind:class="{ 'is-active': isOpen }"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        id="navbarBasicExample"
        class="navbar-menu"
        v-bind:class="{ 'is-active': isOpen }"
      >
        <div class="navbar-start">
          <router-link to="/store" class="navbar-item">Store</router-link>
          <router-link to="/blog" class="navbar-item">Blog</router-link>
          <router-link to="/about" class="navbar-item">About</router-link>
          <router-link to="/contact" class="navbar-item">Contact</router-link>
          <router-link to="/test" class="navbar-item">Test</router-link>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/signup" class="button is-primary">
                <strong>Sign up</strong>
              </router-link>
              <router-link to="/signin" class="button is-light">
                Sign in
              </router-link>

              <button
                class="button"
                type="button"
                name="dark_light"
                @click="toggleDarkLight()"
                title="Toggle dark/light mode"
              >
                🌛
              </button>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      isOpen: false,
    };
  },
  methods: {
    toggleDarkLight() {
      var body = document.getElementById("body");
      var currentClass = body.className;
      body.className = currentClass == "dark-mode" ? "light-mode" : "dark-mode";
    },
  },
};
</script>

<style lang="scss">
$dark-color: #111;
$light-color: #eee;

div.dark-mode {
  background-color: $dark-color;
  color: $light-color;
  a {
    color: $dark-color;
  }
  button {
    background-color: $light-color;
    color: $dark-color;
  }
}

div.light-mode {
  background-color: $light-color;
  color: $dark-color;
  a {
    color: $dark-color;
  }
  button {
    background-color: $dark-color;
    color: $light-color;
  }
}
</style>
