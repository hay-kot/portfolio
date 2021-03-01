<template>
  <div>
    <div
      class="hero container-inner mx-auto flex flex-col sm:flex-row justify-between py-16"
    >
      <div class="text-4xl font-bold w-full sm:w-3/5 text-center sm:text-left">
        <div class="leading-tight">Portfolio By Hayden</div>
        <div class="text-green-700 leading-tight">Aspiring Developer</div>
      </div>
      <div class="mt-8 sm:mt-0">
        <img
          src="~assets/img/developer.svg"
          alt="hero"
          class="mx-auto sm:mx-0"
        />
      </div>
    </div>
    <!-- end hero -->

    <div class="container-inner mx-auto">
      <p class="text-lg sm:text-xl">
        Welcome to the site! It's currently under contruction so not to be too
        harsh! You can find my
        <a :href="github"> GitHub here</a>. Checkout out my blog for more
        details on what kind of stuff I'm into
      </p>

      <div class="flex justify-between items-center py-6">
        <div class="w-full sm:w-1/2 px-8 py-8 sm:py-0">
          <img src="~assets/img/mind_map.svg" alt="browser" />
        </div>
        <div class="w-1/2 px-8 hidden sm:flex justify-end">
          <img src="~assets/img/web-developer.svg" alt="mobile" />
        </div>
      </div>
    </div>

    <TheProjectSummary />

    <div class="overflow-x-hidden border-gray-200 border-b">
      <div
        class="get-to-know-me container-inner mx-auto text-xl pb-16 relative"
      >
        <h2 class="font-bold mb-6" id="about">Get to know me:</h2>

        <div
          class="absolute left-0"
          style="top: 50px; transform: translateX(-100%)"
        >
          <svg width="170px" height="170px">
            <use xlink:href="#dots-triangle" />
          </svg>
        </div>

        <div
          class="flex flex-col sm:flex-row justify-between items-center mb-16"
        >
          <div>
            <img
              src="~assets/img/avatar.svg"
              alt="avatar"
              class="w-32 h-32 rounded-full mb-8 lg:mb-0"
            />
          </div>
          <div class="flex-1 text-lg sm:text-xl ml-6">
            Hayden is a Building Automation Engineer at Johnson Controls. While
            not a programmer by trade, Hayden spends his free time contributing
            to open source projects and building utility applications to support
            the community.
          </div>
        </div>
      </div>
      <!-- end get-to-know me -->
    </div>
  </div>
</template>

<script>
import TheProjectSummary from "../components/TheProjectSummary";
import AppButton from "../components/AppButton";
export default {
  components: { TheProjectSummary, AppButton },
  data() {
    return {
      github: "https://github.com/hay-kot",
      blog: "https://blog.hay-kot.dev",
    };
  },
};
</script>

<style>
</style>
