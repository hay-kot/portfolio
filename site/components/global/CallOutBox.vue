<template>
  <div class="text-white p-1 mb-4 rounded-sm border-l-14" :class="color">
    <div class="pa-1">
      <div class="pt-2 p-1 flex">
        <svg
          v-if="activeType === typeKeys.info"
          class="mb-auto"
          style="width: 32px; height: 32px"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M13,9H11V7H13M13,17H11V11H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"
          />
        </svg>
        <svg
          v-if="activeType === typeKeys.tip"
          style="width: 32px; height: 32px"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M17.66 11.2C17.43 10.9 17.15 10.64 16.89 10.38C16.22 9.78 15.46 9.35 14.82 8.72C13.33 7.26 13 4.85 13.95 3C13 3.23 12.17 3.75 11.46 4.32C8.87 6.4 7.85 10.07 9.07 13.22C9.11 13.32 9.15 13.42 9.15 13.55C9.15 13.77 9 13.97 8.8 14.05C8.57 14.15 8.33 14.09 8.14 13.93C8.08 13.88 8.04 13.83 8 13.76C6.87 12.33 6.69 10.28 7.45 8.64C5.78 10 4.87 12.3 5 14.47C5.06 14.97 5.12 15.47 5.29 15.97C5.43 16.57 5.7 17.17 6 17.7C7.08 19.43 8.95 20.67 10.96 20.92C13.1 21.19 15.39 20.8 17.03 19.32C18.86 17.66 19.5 15 18.56 12.72L18.43 12.46C18.22 12 17.66 11.2 17.66 11.2M14.5 17.5C14.22 17.74 13.76 18 13.4 18.1C12.28 18.5 11.16 17.94 10.5 17.28C11.69 17 12.4 16.12 12.61 15.23C12.78 14.43 12.46 13.77 12.33 13C12.21 12.26 12.23 11.63 12.5 10.94C12.69 11.32 12.89 11.7 13.13 12C13.9 13 15.11 13.44 15.37 14.8C15.41 14.94 15.43 15.08 15.43 15.23C15.46 16.05 15.1 16.95 14.5 17.5H14.5Z"
          />
        </svg>
        <svg
          v-if="activeType === typeKeys.warning"
          style="width: 32px; height: 32px"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M13 14H11V9H13M13 18H11V16H13M1 21H23L12 2L1 21Z"
          />
        </svg>
        <svg
          v-if="activeType === typeKeys.error"
          style="width: 32px; height: 32px"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"
          />
        </svg>
        <h4 class="in-line-title">
          {{ activeTitle }}
        </h4>
      </div>
      <div class="mb-auto wrapper">
        <slot> </slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      default: null,
    },
    info: {
      type: Boolean,
      default: false,
    },
    tip: {
      type: Boolean,
      default: false,
    },
    warning: {
      type: Boolean,
      default: false,
    },
    error: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      typeKeys: {
        info: "Info",
        tip: "Tip",
        warning: "Warning",
        error: "Error",
      },
    };
  },
  computed: {
    activeTitle() {
      return this.title || this.activeType;
    },
    activeType() {
      if (this.tip) {
        return this.typeKeys.tip;
      } else if (this.warning) {
        return this.typeKeys.warning;
      } else if (this.error) {
        return this.typeKeys.error;
      }
      return this.typeKeys.info;
    },
    color() {
      switch (this.activeType) {
        case this.typeKeys.info:
          return "bg-blue-500 border-blue-700";
        case this.typeKeys.tip:
          return "bg-green-700 border-green-900";
        case this.typeKeys.warning:
          return "bg-yellow-500 border-yellow-700";
        case this.typeKeys.error:
          return "bg-red-500 border-red-700";
        default:
          break;
      }
      return;
    },
  },
  methods: {
    titleFactor() {
      return this.activeType;
    },
  },
};
</script>

<style lang="css">
.in-line-title {
  margin-bottom: auto !important;
  margin-top: auto !important;
  padding-left: 0.25rem !important;
}

.wrapper > p {
  margin-bottom: auto !important;
  margin-top: auto !important;
  padding: 1rem !important;
}

.wrapper > * {
  @apply px-2;
}
</style>

