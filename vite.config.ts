import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  base: "/static/",
  build: {
    outDir: "bike_weite/static/assets/bike_weite/",
    manifest: true,
    rollupOptions: {
      input: {
          "main.ts": '/src/main.ts'
        }
      }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
