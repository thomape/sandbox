<template>
  <div class="animationWrap">
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
  </div>
  <article></article>
</template>

<style lang="scss" scoped>
.circle {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 100%;
  background-color: turquoise;
  animation: move-the-circle 1s infinite;
  transform-origin: center center;
}

@for $num from 1 through 8 {
  .circle:nth-child(#{$num}) {
    left: ($num - 1) * 30px;
    animation-delay: $num * 0.1s;
  }
}

@keyframes move-the-circle {
  0% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
  50% {
    transform: translate(0, 50px) scale(0.4);
    opacity: 0.5;
    background-color: blue;
  }
  100% {
    transform: translate(0, 0) scale(0.8);
    opacity: 1;
    background-color: aquamarine;
  }
}
</style>
