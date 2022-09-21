<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
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
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data: function () {
    return {
      isOpen: false,
    };
  },
};
</script>
