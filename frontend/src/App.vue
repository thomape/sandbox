<template>
  <NavbarComp />
  <HeroComp />
  <MainComp />
  <FooterComp />
  <!-- <section class="section">
    <div class="container">
      <h3 class="title has-text-centered is-size-4">
        <div class="columns mt-5 is-8 is=variable">
          <div class="column is-4-tablet is-3-desktop">
            <div class="card">
              <div class="card-image has-text-centered px-6">
                <img src="" alt="" />
              </div>
              <div class="card-content">
                <p>hi</p>
                <p class="title is-size-5">Hello, good sir</p>
              </div>
            </div>
          </div>
        </div>
      </h3>
    </div>
  </section> -->
</template>

<script>
import NavbarComp from "./components/NavbarComp.vue";
import HeroComp from "./components/HeroComp.vue";
import MainComp from "./components/MainComp.vue";
import FooterComp from "./components/FooterComp.vue";

export default {
  name: "App",
  components: {
    NavbarComp,
    HeroComp,
    MainComp,
    FooterComp,
  },
};
</script>
