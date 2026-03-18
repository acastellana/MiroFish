import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/mirofish/',
  server: {
    port: 9035,
    open: false,
    allowedHosts: ['homebase.tail5e5154.ts.net'],
    proxy: {
      '/api': {
        target: 'http://localhost:9036',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
