<template>
  <div class="flex flex-wrap gap-4 justify-center my-5">
    <div
      v-for="(project, title, index) in projects"
      :key="index"
      class="max-w-md py-4 px-8 shadow-lg drop rounded-lg"
    >
      <div class="flex justify-center md:justify-end"></div>
      <div>
        <div class="flex justify-between align-middle">
          <h2 class="text-3xl font-semibold">{{ title }}</h2>
          <img
            alt="place holder"
            class="w-10 h-10 object-cover rounded-full border-indigo-500"
            :src="project.image"
          />
        </div>
        <p class="mt-2">{{ project.description }}</p>
      </div>
      <div class="flex justify-end mt-4 gap-1">
        <a
          v-if="project.docs"
          :href="project.docs"
          target="_blank"
          class="text-xl font-medium"
        >
          Docs ·
        </a>
        <a
          v-if="project.code"
          :href="project.code"
          target="_blank"
          class="text-xl font-medium"
        >
          Code
        </a>
        <p v-else class="text-xl font-medium text-green-700">Closed Source</p>
      </div>

      <div class="relative pt-1">
        <div class="overflow-hidden h-2 mb-2 text-xs flex rounded bg-amber-200">
          <!-- content here -->
          <div
            v-for="(lang, index) in project.languages"
            :key="index"
            :style="`width: ${lang.percentage}%; background-color: ${lang.color};`"
            class="
              shadow-none
              flex flex-col
              text-center
              whitespace-nowrap
              text-white
              justify-center
            "
          />
        </div>
        <div class="flex justify-center gap-2 text-xs">
          <div v-for="(lang, index) in project.languages" :key="index">
            <span class="dot" :style="`background-color: ${lang.color};`" />
            {{ lang.language }}: {{ lang.percentage }}%
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import mealiePNG from "~/assets/img/projects/mealie.png";
import controlsCoPilotPNG from "~/assets/img/projects/controls-co-pilot.png";
import visio2PdfSVG from "~/assets/img/projects/visio-to-pdf.svg";

export default {
  data() {
    return {
      colors: {
        Python: "#3572A5",
        Go: "#00ADD8",
        JavaScript: "#f1e05a",
        HTML: "#e34c26",
        Vue: "#41b883",
        Other: "#808080",
      },
    };
  },
  computed: {
    projects() {
      return {
        Mealie: {
          docs: "https://hay-kot.github.io/mealie/",
          code: "https://github.com/hay-kot/mealie",
          image: mealiePNG,
          languages: this.getLanguages({
            Vue: 318145,
            Python: 270888,
            JavaScript: 69506,
            Makefile: 2606,
            Dockerfile: 2025,
            Jinja: 1836,
            Shell: 1734,
          }),
          description:
            "Mealie is an MIT licensed recipe manager built for self-hosted deployment through Docker. Mealie has been downloaded over 1.5 million times",
        },
        "Controls CoPilot": {
          code: "",
          docs: "",
          image: controlsCoPilotPNG,
          languages: this.getLanguages({
            Python: 3144,
          }),
          description:
            "A line of business application built for Johnson Controls tooling for automating daily workflows for system technicians and engineers.",
        },
        Visio2PDF: {
          code: "https://github.com/hay-kot/Visio2PDF",
          docs: null,
          image: visio2PdfSVG,
          languages: this.getLanguages({
            Python: 16199,
            JavaScript: 14273,
            HTML: 10904,
            CSS: 1167,
            PowerShell: 798,
            Shell: 17,
          }),
          description:
            "A Web App wrapper around the CLI tool for converting Visio documents into PDFs with merge, title page, and bookmarks built-in.",
        },
      };
    },
  },
  methods: {
    getLanguages(allLangs) {
      const totalBytes = Object.values(allLangs).reduce((a, b) => a + b);

      let totalPercent = 0;

      let newValue = Object.entries(allLangs).flatMap(([language, bytes]) => {
        const percentage = Math.round((bytes / totalBytes) * 100);
        if (percentage < 5) return [];

        let color = this.colors.Other;

        if (this.colors.hasOwnProperty(language)) {
          color = this.colors[language];
        }

        totalPercent += percentage;

        return [{ language, percentage, color }];
      });

      if (100 - totalPercent > 0) {
        newValue.push({
          language: "Other",
          percentage: 100 - totalPercent,
          color: this.colors.Other,
        });
      }

      return newValue;
    },
  },
};
</script>

<style>
.dot {
  height: 0.5rem;
  width: 0.5rem;
  border-radius: 50%;
  display: inline-block;
}
</style>