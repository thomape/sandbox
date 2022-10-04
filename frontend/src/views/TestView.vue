<template>
  <section class="section" id="top">
    <section class="section">
      <div class="tile is-ancestor">
        <div class="tile is-vertical is-8">
          <div class="tile">
            <!-- Evelyn Tile -->
            <div class="tile is-parent is-vertical">
              <div
                class="tile is-child notification is-primary float-tile"
                @click="show('evelyn')"
              >
                <section>
                  <div class="container">
                    <div class="card">
                      <div class="card-image">
                        <figure class="image is-4by3">
                          <img
                            src="@/assets/images/mustang.jpg"
                            alt="Mustang"
                          />
                        </figure>
                      </div>
                      <div class="card-content">
                        <div class="media">
                          <div class="media-left">
                            <figure class="image is-48x48">
                              <img
                                src="@/assets/images/person3.jpg"
                                alt="Evelyn Stewart"
                              />
                            </figure>
                          </div>
                          <div class="media-content">
                            <p class="title is-4">Evelyn Stewart</p>
                            <p class="subtitle is-6">@evelynstewart</p>
                          </div>
                        </div>

                        <div class="content">
                          Nulla facilisi nullam vehicula ipsum a arcu cursus
                          vitae congue.
                          <a href="#">#mustang</a>
                          <a href="#"> #crazyhorse</a>
                          <br />
                          <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </div>
              <!-- Giraffe tile -->
              <div
                class="tile is-child notification is-warning float-tile"
                @click="show('giraffe')"
              >
                <div class="container">
                  <div class="card">
                    <div class="card-image">
                      <figure class="image is-4by3">
                        <img src="@/assets/images/corsair.jpg" alt="Corsair" />
                      </figure>
                    </div>
                    <div class="card-content">
                      <div class="media">
                        <div class="media-left">
                          <figure class="image is-48x48">
                            <img
                              src="@/assets/images/giraffe.jpg"
                              alt="John Smith"
                            />
                          </figure>
                        </div>
                        <div class="media-content">
                          <p class="title is-4">Frank the Giraffe</p>
                          <p class="subtitle is-6">@frankthetank</p>
                        </div>
                      </div>

                      <div class="content">
                        Egestas diam in arcu cursus euismod quis viverra nibh
                        cras.
                        <a href="#">#gullwing</a>
                        <a href="#"> #gonavy</a>
                        <br />
                        <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- John tile -->
            <div class="tile is-parent">
              <div
                class="tile is-child notification is-info float-tile"
                @click="show('john')"
              >
                <div class="container">
                  <div class="card">
                    <div class="card-image">
                      <figure class="image is-4by3">
                        <img src="@/assets/images/cockpit.jpg" alt="Cockpit" />
                      </figure>
                    </div>
                    <div class="card-content">
                      <div class="media">
                        <div class="media-left">
                          <figure class="image is-48x48">
                            <img
                              src="@/assets/images/person2.jpg"
                              alt="John Smith"
                            />
                          </figure>
                        </div>
                        <div class="media-content">
                          <p class="title is-4">John Smith</p>
                          <p class="subtitle is-6">@johnsmith</p>
                        </div>
                      </div>

                      <div class="content">
                        <p>
                          Lorem ipsum dolor sit amet, consectetur adipiscing
                          elit. Phasellus nec iaculis mauris. Platea dictumst
                          vestibulum rhoncus est pellentesque elit ullamcorper.
                          Fringilla ut morbi tincidunt augue interdum. Quis
                          commodo odio aenean sed adipiscing diam. Fermentum dui
                          faucibus in ornare quam viverra. Cras tincidunt
                          lobortis feugiat vivamus at augue eget.
                        </p>
                        <p>
                          Diam vel quam elementum pulvinar etiam non quam lacus.
                          Mi eget mauris pharetra et ultrices neque ornare
                          aenean euismod. Bibendum at varius vel pharetra vel
                          turpis nunc eget lorem. In cursus turpis massa
                          tincidunt dui ut ornare lectus sit. Ultricies mi quis
                          hendrerit dolor magna eget est lorem. Tincidunt dui ut
                          ornare lectus sit amet. Augue interdum velit euismod
                          in pellentesque massa placerat duis.
                        </p>
                        <a href="#">#buttons</a>
                        <a href="#"> #switches'n'stuff</a>
                        <br />
                        <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Wide Tile -->
          <div class="tile is-parent">
            <router-link
              to="/"
              class="tile is-child notification is-danger float-tile"
            >
              <p class="title">Purus gravida</p>
              <p class="subtitle">
                Diam vel quam elementum pulvinar etiam non quam lacus. Mi eget
                mauris pharetra et ultrices neque ornare aenean euismod.
              </p>
              <div class="content"></div>
            </router-link>
          </div>
        </div>
        <!-- Jane Tile -->
        <div class="tile is-parent">
          <div
            class="tile is-child notification is-success float-tile"
            @click="show('jane')"
          >
            <div class="container">
              <div class="card">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img src="@/assets/images/plane.jpg" alt="Plane" />
                  </figure>
                </div>
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img
                          src="@/assets/images/person1.jpg"
                          alt="Jane Smith"
                        />
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-4">Jane Smith</p>
                      <p class="subtitle is-6">@janesmith</p>
                    </div>
                  </div>

                  <div class="content">
                    <p>
                      Bibendum arcu vitae elementum curabitur vitae nunc sed
                      velit dignissim. Orci sagittis eu volutpat odio facilisis
                      mauris sit. Eget velit aliquet sagittis id consectetur
                      purus ut faucibus pulvinar. Porttitor rhoncus dolor purus
                      non enim. Non nisi est sit amet facilisis magna etiam
                      tempor orci. Morbi tristique senectus et netus et
                      malesuada fames. Elit at imperdiet dui accumsan sit amet
                      nulla. Lobortis feugiat vivamus at augue eget arcu.
                    </p>
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                      sed do eiusmod tempor incididunt ut labore et dolore magna
                      aliqua.Duis aute irure dolor in reprehenderit in voluptate
                      velit esse cillum dolore eu fugiat nulla pariatur.
                      Excepteur sint occaecat cupidatat non proident, sunt in
                      culpa qui officia deserunt mollit anim id est laborum.
                    </p>
                    <p>
                      Commodo elit at imperdiet dui accumsan sit. Interdum velit
                      laoreet id donec. Purus non enim praesent elementum
                      facilisis leo vel fringilla.
                    </p>
                    <a href="#">#radial</a>
                    <a href="#"> #5000hp</a>
                    <a href="#"> #909</a>
                    <br />
                    <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CARD SECTION -->
    <!-- Jane card -->
    <section class="section">
      <section class="section">
        <div class="container" id="jane">
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img src="@/assets/images/plane.jpg" alt="Plane" />
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img src="@/assets/images/person1.jpg" alt="Jane Smith" />
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">Jane Smith</p>
                  <p class="subtitle is-6">@janesmith</p>
                </div>
              </div>

              <div class="content">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
                <a href="#">#radial</a>
                <a href="#"> #5000hp</a>
                <a href="#"> #909</a>
                <br />
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
              </div>
            </div>
          </div>
        </div>
        <!--John card  -->
        <div class="container" id="john" style="display: none">
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img src="@/assets/images/cockpit.jpg" alt="Cockpit" />
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img src="@/assets/images/person2.jpg" alt="John Smith" />
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">John Smith</p>
                  <p class="subtitle is-6">@johnsmith</p>
                </div>
              </div>
              <div class="content">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Phasellus nec iaculis mauris.
                <a href="#">#buttons</a>
                <a href="#"> #switches'n'stuff</a>
                <br />
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
              </div>
            </div>
          </div>
        </div>
        <!-- Evelyn Card -->
        <div class="card" id="evelyn" style="display: none">
          <div class="card-image">
            <figure class="image is-4by3">
              <img src="@/assets/images/mustang.jpg" alt="Mustang" />
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img src="@/assets/images/person3.jpg" alt="Evelyn Stewart" />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">Evelyn Stewart</p>
                <p class="subtitle is-6">@evelynstewart</p>
              </div>
            </div>

            <div class="content">
              Nulla facilisi nullam vehicula ipsum a arcu cursus vitae congue.
              <a href="#">#mustang</a>
              <a href="#"> #crazyhorse</a>
              <br />
              <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
            </div>
          </div>
        </div>
        <!-- Giraffe card -->
        <div class="card" id="giraffe" style="display: none">
          <div class="card-image">
            <figure class="image is-4by3">
              <img src="@/assets/images/corsair.jpg" alt="Corsair" />
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img src="@/assets/images/giraffe.jpg" alt="John Smith" />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">Frank the Giraffe</p>
                <p class="subtitle is-6">@frankthetank</p>
              </div>
            </div>

            <div class="content">
              Egestas diam in arcu cursus euismod quis viverra nibh cras.
              <a href="#">#gullwing</a>
              <a href="#"> #gonavy</a>
              <br />
              <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
            </div>
          </div>
        </div>
      </section>
      <button class="button is-large is-rounded" @click="returnTop">
        <span>
          <font-awesome-icon icon="arrow-up" />
        </span>
      </button>
    </section>

    <TestComp />
  </section>

  <!-- Another tile section -->
  <section class="section">
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

                <div class="tile is-parent">
                  <article
                    class="tile is-child notification is-info float-tile"
                  >
                    <p class="title">Middle tile</p>
                    <p class="subtitle">With an image</p>
                    <figure class="image is-4by3">
                      <img src="@/assets/images/beach.jpg" />
                    </figure>
                  </article>
                </div>
              </div>

              <div class="tile is-parent">
                <article
                  class="tile is-child notification is-danger float-tile"
                >
                  <p class="title">Wide tile</p>
                  <p class="subtitle">Aligned with right tile</p>
                  <div class="content"></div>
                </article>
              </div>
            </div>

            <div class="tile is-parent">
              <article class="tile is-child notification is-success float-tile">
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
    <div class="is-divider"></div>
  </section>
  <TestCaroComp />
</template>

<script>
import TestComp from "@/components/TestComp/TestComp.vue";
import TestCaroComp from "@/components/TestComp/TestCaroComp.vue";

export default {
  name: "TestView",
  components: {
    TestComp,
    TestCaroComp,
  },
  data() {
    return {
      divs: ["jane", "john", "evelyn", "giraffe"],
      visibleId: null,
    };
  },
  methods: {
    test() {
      console.log("redirect");
    },
    show(id) {
      if (this.visibleId !== id) {
        this.visibleId = id;
      }
      this.hide();
    },
    hide() {
      var div, i, id;
      for (i = 0; i < this.divs.length; i++) {
        id = this.divs[i];
        div = document.getElementById(id);
        if (this.visibleId === id) {
          div.style.display = "block";
          div.scrollIntoView({ behavior: "smooth" });
        } else {
          div.style.display = "none";
        }
      }
    },
    returnTop() {
      var top = document.getElementById("top");
      top.scrollIntoView({ behavior: "smooth" });
    },
  },
};
</script>

<style lang="scss" scoped>
.float-tile {
  cursor: pointer;
  transition: all 0.1s;
  &:hover {
    transform: scale(1.02, 1.02);
    box-shadow: 20px 20px 50px gray;
  }
}
</style>
