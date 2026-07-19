import { defineConfig } from "vite";
import { resolve } from "node:path";

export default defineConfig({
    build: {
        manifest: true,
        outDir: resolve(__dirname, "assets/dist"),
        emptyOutDir: true,

        rollupOptions: {
            input: resolve(__dirname, "source/js/main.js"),
        },
    },
});