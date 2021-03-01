<template>
  <div class="">
    <div class="text-white px-6 py-2 border-0 rounded-t relative bg-green-700">
      <div class="inline-block align-middle mr-8">
        <b class="capatalize">{{ title }}</b>
      </div>
    </div>
    <div
      class="px-6 pt-2 border-3 rounded-b relative border-b border-l border-r border-green-700"
    >
      <slot> </slot>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    title: String,
  },
};
</script>

<style>
</style>