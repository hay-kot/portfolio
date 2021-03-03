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
        <li class="checkmark">
          <div class="flex pr-6">
            <div>Mealie</div>
            <p class="ml-auto">
              <a :href="mealieDocs">Docs</a> ·
              <a :href="mealie">Source Code</a>
            </p>
          </div>
          <div class="text-lg text-gray-600">
            a self hosted recipe manager and meal planner with a RestAPI backend
            and a reactive frontend application built in Vue for a pleasant user
            experience for the whole family.
          </div>
        </li>
        <li class="checkmark">
          <div class="flex pr-6">
            <div>Visio2PDF</div>

            <p class="ml-auto">
              <a :href="visio2PDF">Source Code</a>
            </p>
          </div>
          <div class="text-lg text-gray-600">
            A Web App wrapper around the CLI tool for converting Visio documents
            into PDFs with merge, title page, and bookmarks built-in.
          </div>
        </li>
        <li class="checkmark">
          <div>ControlsCoPilot</div>
          <div class="text-lg text-gray-600">
            A line of business application built for Johnson Controls tooling
            for automating daily workflows for system technicians and engineers.
          </div>
        </li>
        <li class="checkmark">
          <div>Quick Zip (Beta)</div>
          <div class="text-lg text-gray-600">
            A CLI interface for creating and scheduling zip file backups of
            system documents
          </div>
        </li>
      </ul>
    </div>
    <!-- end projects -->
  </div>
</template>

<script>
import { projects } from "../globals";
export default {
  data() {
    return {
      mealie: projects.mealie,
      mealieDocs: projects.mealieDocs,
      visio2PDF: projects.visio2PDF,
    };
  },
};
</script>

<style>
</style>