<template>
  <NavComp />
  <div>Test</div>
  <section class="section">
    <body id="body" class="dark-mode">
      <h1>Dark/Light Mode Switcher</h1>

      <button
        type="button"
        name="dark_light"
        @click="toggleDarkLight()"
        title="Toggle dark/light mode"
      >
        🌛
      </button>

      <p>Just press the button above to toggle!</p>
    </body>
  </section>
  <section class="section">
    <MainComp />
  </section>
  <section class="section">
    <div class="container">
      <div class="card">
        <div class="card-image">
          <figure class="image is-4by3">
            <img src="@/assets/images/plane.jpg" alt="Placeholder image" />
          </figure>
        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-left">
              <figure class="image is-48x48">
                <img
                  src="https://bulma.io/images/placeholders/96x96.png"
                  alt="Placeholder image"
                />
              </figure>
            </div>
            <div class="media-content">
              <p class="title is-4">John Smith</p>
              <p class="subtitle is-6">@johnsmith</p>
            </div>
          </div>

          <div class="content">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
            nec iaculis mauris. <a>@bulmaio</a>. <a href="#">#css</a>
            <a href="#">#responsive</a>
            <br />
            <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-8">
        <div class="tile">
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-primary">
              <p class="title">Vertical...</p>
              <p class="subtitle">Top tile</p>
            </article>
            <article class="tile is-child notification is-warning">
              <p class="title">...tiles</p>
              <p class="subtitle">Bottom tile</p>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-info">
              <p class="title">Middle tile</p>
              <p class="subtitle">With an image</p>
              <figure class="image is-4by3">
                <img src="https://bulma.io/images/placeholders/640x480.png" />
              </figure>
            </article>
          </div>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child notification is-danger">
            <p class="title">Wide tile</p>
            <p class="subtitle">Aligned with the right tile</p>
            <div class="content">
              <!-- Content -->
            </div>
          </article>
        </div>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification is-success">
          <div class="content">
            <p class="title">Tall tile</p>
            <p class="subtitle">With even more content</p>
            <div class="content">
              <!-- Content -->
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <div class="container">
    <div class="card">
      <div class="card-content">
        <div class="tile is-ancestor">
          <div class="tile is-vertical is-8">
            <div class="tile">
              <div class="tile is-parent is-vertical">
                <article
                  class="tile is-child notification is-success float-tile"
                  @click="test"
                >
                  <p class="title">Vertical</p>
                  <p class="subtitle">Top tile</p>
                </article>

                <article
                  class="tile is-child notification is-warning float-tile"
                >
                  <p class="title">...tiles</p>
                  <p class="subtitle">Bottom tile</p>
                </article>
              </div>

              <div class="tile is-parent float-tile">
                <article class="tile is-child notification is-info">
                  <p class="title">Middle tile</p>
                  <p class="subtitle">With an image</p>
                  <figure class="image is-4by3">
                    <img src="@/assets/images/beach.jpg" />
                  </figure>
                </article>
              </div>
            </div>

            <div class="tile is-parent float-tile">
              <article class="tile is-child notification is-danger">
                <p class="title">Wide tile</p>
                <p class="subtitle">Aligned with right tile</p>
                <div class="content"></div>
              </article>
            </div>
          </div>

          <div class="tile is-parent float-tile">
            <article class="tile is-child notification is-success">
              <div class="content">
                <p class="title">Tall Tile</p>
                <p class="subtitle">With even more content</p>
                <div class="content"></div>
              </div>
            </article>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MainComp from "@/components/TestComp/MainComp.vue";
import NavComp from "@/components/SharedComp/NavComp.vue";
export default {
  name: "TestView",
  components: {
    MainComp,
    NavComp,
  },
  methods: {
    toggleDarkLight() {
      var body = document.getElementById("body");
      var currentClass = body.className;
      body.className = currentClass == "dark-mode" ? "light-mode" : "dark-mode";
    },
    test() {
      console.log("redirect");
    },
  },
};
</script>

<style lang="scss" scoped>
$dark-color: #111;
$light-color: #eee;

body.dark-mode {
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

body.light-mode {
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

.float-tile {
  cursor: pointer;

  // Animation elements
  // display: block;
  // perspective: 600px;
  // position: relative;
  transition: all 0.1s;
  &:hover {
    transform: scale(1.05, 1.05);
  }
}
</style>
