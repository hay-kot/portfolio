<template>
  <div class="overflow-x-hidden">
    <div
      class="projects container-inner mx-auto text-xl border-t border-gray-500 border-b py-16 mb-16 relative"
    >
      <h2 class="font-bold mb-6" id="projects">Project Highlights</h2>

      <div
        class="absolute right-0"
        style="top: 50px; transform: translate(100%) rotate(180deg)"
      >
        <svg width="170px" height="170px">
          <use xlink:href="#dots-triangle" />
        </svg>
      </div>

      <ul class="text-lg sm:text-xl space-y-6">
        <ProjectListItem
          title="Mealie"
          pythonLogo
          vueLogo
          :docs="mealie.docs"
          :source="mealie.sourceCode"
          description="a self hosted recipe manager and meal planner with a RestAPI backend
            and a reactive frontend application built in Vue for a pleasant user
            experience for the whole family."
        />
        <ProjectListItem
          title="ControlsCoPilot"
          pythonLogo
          description="A line of business application built for Johnson Controls tooling
            for automating daily workflows for system technicians and engineers. Includes working 
            with excel, converting and packaging visio files, working with custom file formats,
            and generating custom reports."
        />
        <ProjectListItem
          title="GoGitter"
          goLogo
          :source="goGitter.sourceCode"
          description="A Tiny go application that uses a configuration file and to pull down your
          private and public Github repositories with optional sorting into language type 
          directories and experimental hooks that execute in the repositories local directory"
        />
        <ProjectListItem
          title="Visio2PDF"
          pythonLogo
          vueLogo
          :source="visio2PDF"
          description="A Web App wrapper around the CLI tool for converting Visio documents
            into PDFs with merge, title page, and bookmarks built-in."
        />
      </ul>
    </div>
    <!-- end projects -->
  </div>
</template>

<script>
import ProjectListItem from "./ProjectListItem";
import { projects } from "../globals";
export default {
  components: { ProjectListItem },
  data() {
    return {
      mealie: projects.mealie,
      visio2PDF: projects.visio2PDF,
      quickZipCLI: projects.quickZipCLI,
      goGitter: projects.goGitter,
    };
  },
};
</script>

<style>
</style>